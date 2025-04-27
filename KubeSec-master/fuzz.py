# Worked and tested on by group members

import logging
import random
import sys
import os

# Since scanner.py is in the same directory as this script, we can import it directly.
# This worked locally, trying a different option to get the action working
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import scanner

# Set up logging for all fuzzed functions
logging.basicConfig(filename='fuzz_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Provide collection of odd/unusual inputs to fuzz the scanner functions with
fuzz_inputs = [
    None, # None input
    "", # Empty string
    "    ", # Whitespace string that may trip up some functions
    "admin", # Username that should be reserved only for admin and not general users
    "password123", # Common password that shouldn't be used by anyone
    "api_key", # Basic api key name that shouldn't be allowed
    "!!invalid!!", # Invalid characters in input that shoudl be rejected
    "super$ecret", # Contains basic word obfuscation that should be rejected
    "root", # Root is something that shouldn't be used in usernames/passwords
    123, # Integer input that may not behave in some functions
    123.45, # Float input that may not behave in some functions
    float('nan'), # NaN input that may break some functions depending on how its handled
    float('inf'), # Infinity input that may break some functions depending on how its handled
    [], # Empty list input that may break some functions either from input or from being blank
    {}, # Empty dict input that may break some functions either from input or from being blank
    set(), # Empty set input that may break some functions either from input or from being blank
    {"key": "value"}, # Dict input that may break some functions
    [1, 2, 3], # List input that may break some functions
    (1, 2, 3), # Tuple input that may break some functions
    set([1, 2, 3]), # Set input that may break some functions
    lambda x: x, # Lambda function input that may break some functions
    b"binary", # Binary input that may break some functions
    b"bytes", # Bytes input that may break some functions
    True, # Boolean input that may break some functions
    False, # Boolean input that may break some functions
    object(), # Object input that may break some functions either from input or from being blank
]

def fuzz_function(func, func_name):
    logging.info(f"=== Starting fuzzing for {func_name} ===")
    for idx, input_val in enumerate(fuzz_inputs):
        try:
            result = func(input_val)
            logging.info(f"Test {idx}: Input={repr(input_val)} Output={repr(result)}")
        except Exception as e:
            logging.error(f"Test {idx}: Input={repr(input_val)} raised an exception: {e}")
    logging.info(f"=== Finished fuzzing for {func_name} ===\n")

def main():
    fuzz_function(scanner.isValidUserName, "isValidUserMame")
    fuzz_function(scanner.isValidPasswordName, "isValidPasswordName")
    fuzz_function(scanner.isValidKey, "isValidKey")
    fuzz_function(scanner.checkIfValidKeyValue, "checkIfValidKeyValue")
    fuzz_function(scanner.checkIfValidSecret, "checkIfValidSecret")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        import sys
        sys.exit(1)
