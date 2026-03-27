# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from urllib.parse import urlparse, urlunparse, quote

import urllib3

import settings

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = urllib3.util.Timeout(connect=5.0, read=10.0)
EMPTY_VALUE = ""

VALIDATION_ENDPOINTS = {
    "vies": "https://ec.europa.eu/taxation_customs/vies/services/checkVatService",
    "hmrc": "https://api.service.hmrc.gov.uk/organisations/vat/check-vat-number/lookup/",
    "bzst": "https://api.evatr.vies.bzst.de/app/v1/abfrage",
    "swiss": "https://www.uid-wse.admin.ch/V5.0/PublicServices.svc",
}


def _safe_setting(key):
    value = settings.load_value_from_json_file(key)
    return value if isinstance(value, str) else EMPTY_VALUE


def get_proxy_settings():
    return {
        "proxy_mode": (_safe_setting("proxy_mode") or "none").lower(),
        "proxy_url": _safe_setting("proxy_url").strip(),
        "proxy_username": _safe_setting("proxy_username"),
        "proxy_password": _safe_setting("proxy_password"),
    }


def build_proxy_url(proxy_url, username=EMPTY_VALUE, secret=EMPTY_VALUE):
    if not proxy_url:
        return EMPTY_VALUE

    parsed = urlparse(proxy_url)
    if not parsed.scheme or not parsed.netloc:
        return EMPTY_VALUE

    if not username:
        return proxy_url

    host = parsed.hostname or ""
    port = f":{parsed.port}" if parsed.port else ""
    auth = quote(username, safe="")
    if secret:
        auth = f"{auth}:{quote(secret, safe='')}"
    netloc = f"{auth}@{host}{port}"
    return urlunparse((parsed.scheme, netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))


def _get_system_proxy(url):
    return urllib3.util.proxy.getproxies().get(urlparse(url).scheme, "")


def resolve_proxy_url(url):
    proxy_settings = get_proxy_settings()
    proxy_mode = proxy_settings["proxy_mode"]
    if proxy_mode == "manual":
        return build_proxy_url(
            proxy_settings["proxy_url"],
            proxy_settings["proxy_username"],
            proxy_settings["proxy_password"],
        )
    if proxy_mode == "none":
        return ""
    return _get_system_proxy(url)


def create_http_client(url):
    proxy_url = resolve_proxy_url(url)
    if proxy_url:
        logger.debug("Using proxy for %s via %s", url, proxy_url)
        return urllib3.ProxyManager(proxy_url, timeout=DEFAULT_TIMEOUT)
    return urllib3.PoolManager(timeout=DEFAULT_TIMEOUT)


def request(method, url, **kwargs):
    http = create_http_client(url)
    return http.request(method, url, **kwargs)


def test_validation_endpoints():
    results = []
    for name, url in VALIDATION_ENDPOINTS.items():
        try:
            response = request("HEAD", url, preload_content=False, redirect=False)
            status = response.status
            response.release_conn()
            if status == 405:
                response = request("GET", url, preload_content=False, redirect=False)
                status = response.status
                response.release_conn()
            results.append(
                {
                    "name": name,
                    "url": url,
                    "ok": True,
                    "status": status,
                    "message": "Host reachable",
                }
            )
        except Exception as exc:
            logger.error("Proxy test failed for %s: %s", url, exc)
            results.append(
                {
                    "name": name,
                    "url": url,
                    "ok": False,
                    "status": None,
                    "message": str(exc),
                }
            )
    return results