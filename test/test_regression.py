import unittest
import validate_workflow


class TestVATValidationRegression(unittest.TestCase):
    """
    Regression tests using real API calls.
    These tests verify that validation behavior remains consistent.
    Run with: python -m unittest test.test_regression
    """

    def test_vies_valid_german_vat(self):
        """Test valid German VAT via VIES"""
        payload = {
            "key1": "test1",
            "key2": "test2",
            "ownvat": "DE123456789",
            "foreignvat": "DE811128135",  # Known valid German VAT
            "company": "",
            "street": "",
            "zip": "",
            "town": "",
            "type": "vies",
            "lang": "en"
        }
        result = validate_workflow.start_workflow(payload)
        
        self.assertEqual(result["type"], "vies")
        self.assertIn("valid", result)
        self.assertIn("errorcode", result)
        self.assertEqual(result["foreignvat"], "DE811128135")

    def test_hmrc_valid_uk_vat(self):
        """Test valid UK VAT via HMRC"""
        payload = {
            "key1": "test1",
            "key2": "test2",
            "ownvat": "DE123456789",
            "foreignvat": "GB333289454",  # Known valid UK VAT
            "company": "",
            "street": "",
            "zip": "",
            "town": "",
            "type": "vies",
            "lang": "en"
        }
        result = validate_workflow.start_workflow(payload)
        
        self.assertEqual(result["type"], "HMRC")
        self.assertIn("valid", result)
        self.assertEqual(result["foreignvat"], "GB333289454")

    def test_swiss_vat_detection(self):
        """Test Swiss VAT auto-detection"""
        payload = {
            "key1": "test1",
            "key2": "test2",
            "ownvat": "DE123456789",
            "foreignvat": "CHE-109.740.084",
            "company": "",
            "street": "",
            "zip": "",
            "town": "",
            "type": "vies",
            "lang": "en"
        }
        result = validate_workflow.start_workflow(payload)
        
        self.assertEqual(result["type"], "swiss")
        self.assertIn("valid", result)

    def test_bzst_routing(self):
        """Test BZST interface selection"""
        payload = {
            "key1": "test1",
            "key2": "test2",
            "ownvat": "DE123456789",
            "foreignvat": "DE811128135",
            "company": "",
            "street": "",
            "zip": "",
            "town": "",
            "type": "bzst",
            "lang": "en"
        }
        result = validate_workflow.start_workflow(payload)
        
        self.assertEqual(result["type"], "bzst")
        self.assertIn("valid", result)

    def test_invalid_vat_format(self):
        """Test invalid VAT format handling"""
        payload = {
            "key1": "test1",
            "key2": "test2",
            "ownvat": "DE123456789",
            "foreignvat": "INVALID123",
            "company": "",
            "street": "",
            "zip": "",
            "town": "",
            "type": "vies",
            "lang": "en"
        }
        result = validate_workflow.start_workflow(payload)
        
        self.assertIn("valid", result)
        self.assertIn("errorcode", result)

    def test_result_structure(self):
        """Test that result structure is consistent"""
        payload = {
            "key1": "test1",
            "key2": "test2",
            "ownvat": "DE123456789",
            "foreignvat": "DE811128135",
            "company": "",
            "street": "",
            "zip": "",
            "town": "",
            "type": "vies",
            "lang": "en"
        }
        result = validate_workflow.start_workflow(payload)
        
        # Verify all expected keys exist
        required_keys = ["key1", "key2", "ownvat", "foreignvat", "type", 
                        "valid", "errorcode", "timestamp"]
        for key in required_keys:
            self.assertIn(key, result, f"Missing key: {key}")


if __name__ == '__main__':
    unittest.main()
