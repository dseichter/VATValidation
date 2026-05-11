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

import argparse
import sys
import json
import helper
import batch
import single
import settings

import logging_config  # Setup the logging  # noqa: F401
import logging

logger = logging.getLogger(__name__)


# Initialize the settings
settings.create_config()

# Create the parser with an extended description or epilog
parser = argparse.ArgumentParser(
    description=helper.NAME + " CLI" + " - " + helper.VERSION,
    epilog="""
For more information, visit our GitHub repository: https://github.com/dseichter/VATValidation
License: GPL 3.0 - see LICENSE file at the root of the repository for details.

Modes:
  Batch mode: Use --input and --output to validate a list of VAT numbers from a file
  Single mode: Use --ownvat, --vat, --company, --street, --zip, --town for single validation
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

# Add the version argument
parser.add_argument("--version", action="version", version=helper.VERSION)

# Batch mode arguments
parser.add_argument(
    "--input", type=str, help="Input filename for VAT numbers (batch mode).", required=False
)

parser.add_argument(
    "--output", type=str, help="Output filename for validation results (batch mode).", required=False
)

# Optional delimiter override for CSV files
parser.add_argument(
    "--delimiter",
    type=str,
    help="Optional CSV delimiter (single character) to use for this run. MUST be quoted, e.g. '--delimiter '\";\"'' to pass a semicolon.",
    required=False,
)

# Single validation mode arguments
parser.add_argument(
    "--ownvat", type=str, help="Own VAT number (single mode).", required=False
)

parser.add_argument(
    "--vat", type=str, help="VAT number to validate (single mode).", required=False
)

parser.add_argument(
    "--company", type=str, help="Company name (single mode).", required=False
)

parser.add_argument(
    "--street", type=str, help="Street address (single mode).", required=False
)

parser.add_argument(
    "--zip", type=str, help="ZIP/postal code (single mode).", required=False
)

parser.add_argument(
    "--town", type=str, help="Town/city (single mode).", required=False
)

# Common arguments
parser.add_argument(
    "--interface",
    type=str,
    help="Overwrite the interface to be used during validation. Accepted values are: bzst,vies",
    required=False,
)

parser.add_argument(
    "--proxy-mode",
    type=str,
    choices=["system", "manual", "none"],
    help="Proxy mode for network requests.",
    required=False,
)

parser.add_argument(
    "--proxy-url",
    type=str,
    help="Manual proxy URL, e.g. http://proxy.example.com:8080",
    required=False,
)

parser.add_argument(
    "--proxy-username",
    type=str,
    help="Username for manual proxy authentication.",
    required=False,
)

parser.add_argument(
    "--proxy-password",
    type=str,
    help="Password for manual proxy authentication.",
    required=False,
)

parser.add_argument(
    "--ignore-validation-errors",
    action="store_true",
    help="Return exit code 0 even if validation fails. Useful for integration into other applications.",
    required=False,
)

# Check if no arguments were passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Parse the arguments
args = parser.parse_args()

# Determine which mode to use
batch_mode = bool(getattr(args, 'input', None) and getattr(args, 'output', None))
single_mode = bool(getattr(args, 'ownvat', None) or getattr(args, 'vat', None))

if not batch_mode and not single_mode:
    print("Error: You must provide either batch mode (--input and --output) or single mode (--ownvat and --vat) parameters.")
    print("")
    parser.print_help(sys.stderr)
    sys.exit(1)

if batch_mode and single_mode:
    print("Error: Cannot use both batch mode and single mode simultaneously.")
    sys.exit(1)

# Common settings
interface_type = settings.load_value_from_json_file("interface")
if getattr(args, 'interface', None):
    val = args.interface
    if val not in ("bzst", "vies"):
        print("Interface must be either 'bzst' or 'vies'.")
        sys.exit(2)
    else:
        interface_type = val

if getattr(args, 'proxy_mode', None):
    settings.save_config("proxy_mode", args.proxy_mode)
if getattr(args, 'proxy_url', None) is not None:
    settings.save_config("proxy_url", args.proxy_url)
if getattr(args, 'proxy_username', None) is not None:
    settings.save_config("proxy_username", args.proxy_username)
if getattr(args, 'proxy_password', None) is not None:
    settings.save_config("proxy_password", args.proxy_password)

# Batch mode processing
if batch_mode:
    delimiter_char = None

    # If delimiter provided, accept either a single character or a quoted/escaped value
    if getattr(args, 'delimiter', None):
        val = args.delimiter
        # If the user provided a plain single character, accept it directly
        if len(val) == 1:
            delimiter_char = val
        else:
            # Otherwise accept a quoted value like '";"' or '"\\t"'
            if len(val) >= 3 and val[0] in ('"', "'") and val[-1] == val[0]:
                inner = val[1:-1]
                try:
                    inner_decoded = inner.encode('utf-8').decode('unicode_escape')
                except Exception:
                    inner_decoded = inner
                if len(inner_decoded) != 1:
                    print("Delimiter must be a single character (after unquoting/escape processing).")
                    sys.exit(2)
                delimiter_char = inner_decoded
            else:
                print("Delimiter must be a single character. For special characters, quote and/or escape them, e.g. --delimiter ';' or --delimiter '\\t'.")
                sys.exit(2)

    print(f"Start batch validation with input file: {args.input} and output file: {args.output} using {interface_type} interface.")
    response = batch.validatebatch(
        inputfile=args.input,
        outputfile=args.output,
        lang="en",
        type=interface_type,
        delimiter=delimiter_char,
    )

    match response:
        case 0:
            print("Validation successful")
            exit(0)
        case 127:
            print("Unsupported file format")
            exit(127 if not args.ignore_validation_errors else 0)
        case _:
            print("Validation failed: " + str(response))
            exit(0 if args.ignore_validation_errors else 1)

# Single mode processing
elif single_mode:
    # Validate required fields for single mode
    required_fields = ["ownvat", "vat", "company", "street", "zip", "town"]
    missing_fields = [field for field in required_fields if not getattr(args, field, None)]
    
    if missing_fields:
        print(f"Error: Missing required fields for single validation mode: {', '.join(missing_fields)}")
        sys.exit(1)

    print(f"Start single validation for VAT: {args.vat} using {interface_type} interface.")
    
    response = single.validatesingle(
        key1="",
        key2="",
        ownvat=args.ownvat,
        foreignvat=args.vat,
        company=args.company,
        street=args.street,
        zip=args.zip,
        town=args.town,
        type=interface_type,
        lang="en"
    )

    # Parse and output the response
    try:
        if isinstance(response, dict):
            body = response.get("body", "{}")
            if isinstance(body, str):
                result = json.loads(body)
            else:
                result = body
        else:
            result = response

        print(json.dumps(result, indent=2))
        
        # Check status code for exit code
        status_code = response.get("statusCode", 200) if isinstance(response, dict) else 200
        if status_code == 200:
            exit(0)
        else:
            exit(0 if args.ignore_validation_errors else 1)
    except Exception as e:
        logger.error(f"Error processing response: {e}")
        print(f"Error processing response: {e}")
        print(json.dumps(response, indent=2, default=str))
        exit(0 if args.ignore_validation_errors else 1)

