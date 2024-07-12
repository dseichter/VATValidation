import argparse
import sys
import helper
import batch

# Create the parser with an extended description or epilog
parser = argparse.ArgumentParser(
    description=helper.NAME + " CLI" + " - " + helper.VERSION,
    epilog="For more information, visit our GitHub repository: https://github.com/dseichter/VATValidation\r\n\n"
    "License: GPL 3.0 - see LICENSE file at the root of the repository for details.",
)

# Add the version argument
parser.add_argument("--version", action="version", version=helper.VERSION)

# Add the input file argument
parser.add_argument(
    "--input", type=str, help="Input filename for VAT numbers.", required=True
)

# Add the output file argument
parser.add_argument(
    "--output", type=str, help="Output filename for validation results.", required=True
)

# Check if no arguments were passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Parse the arguments
args = parser.parse_args()

# You can now use args.input and args.output for further processing
print(
    "Start batch validation with input file: "
    + args.input
    + " and output file: "
    + args.output
)
response = batch.validatebatch(inputfile=args.input, outputfile=args.output, iscli=True)

match response:
    case 0:
        print("Validation successful")
        exit(0)
    case 127:
        print("Unsupported file format")
        exit(127)
    case True:
        print("Validation successful")
        exit(0)
    case _:
        print("Validation failed: " + str(response))
        exit(1)
