#!/usr/bin/env python3

# Simple test for BZST validation
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import validate_bzst

# Test payload
test_payload = {
    "key1": "test1",
    "key2": "test2", 
    "ownvat": "DE123456789",
    "foreignvat": "DE987654321",
    "company": "Test Company",
    "street": "Test Street 1",
    "zip": "12345",
    "town": "Test City",
    "lang": "de"
}

print("Testing BZST validation...")
print("Payload:", test_payload)

try:
    result = validate_bzst.start_validation(test_payload)
    print("Result:", result)
    print("Status messages loaded successfully:", bool(validate_bzst.load_status_messages()))
except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()