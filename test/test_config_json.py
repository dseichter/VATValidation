import unittest
import os
import json
import sys
import tempfile
import settings

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))


class TestConfigJson(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self._old_configfile = settings.CONFIGFILE
        self.config_path = os.path.join(self.temp_dir.name, 'config.json')
        settings.CONFIGFILE = self.config_path
        settings.create_config()

    def tearDown(self):
        settings.CONFIGFILE = self._old_configfile
        self.temp_dir.cleanup()

    def test_config_json_exists(self):
        self.assertTrue(os.path.isfile(self.config_path), f"{self.config_path} does not exist.")

    def test_config_json_is_valid_json(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            try:
                _ = json.load(f)
            except Exception as e:
                self.fail(f"config.json is not valid JSON: {e}")

    def test_config_json_has_required_keys(self):
        required_keys = [
            "logfilename",
            "loglevel",
            "delimiter",
            "language",
            "interface",
            "proxy_mode",
            "proxy_url",
            "proxy_username",
            "proxy_password"
        ]
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key in required_keys:
            self.assertIn(key, data, f"Missing required key: {key}")


if __name__ == '__main__':
    unittest.main()
