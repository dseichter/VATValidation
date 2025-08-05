import unittest
from unittest.mock import patch, MagicMock
import validate_hmrc

class TestValidateHMRC(unittest.TestCase):
    @patch('validate_hmrc.http')
    def test_start_validation_success(self, mock_http):
        # Mock response for a successful lookup
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = b'{"target": {"name": "Test Company", "address": {"line1": "Street 1", "line2": "Line 2", "postcode": "12345"}}}'
        mock_http.request.return_value = mock_response

        payload = {
            "key1": "k1",
            "key2": "k2",
            "ownvat": "DE123456789",
            "foreignvat": "GB987654321",
            "lang": "en"
        }

        result = validate_hmrc.start_validation(payload)
        self.assertTrue(result["valid"])
        self.assertEqual(result["company"], "Test Company")
        self.assertEqual(result["address"], "Street 1 Line 2")
        self.assertEqual(result["zip"], "12345")
        self.assertEqual(result["type"], "HMRC")
        self.assertEqual(result["key1"], "k1")
        self.assertEqual(result["key2"], "k2")
        self.assertEqual(result["ownvat"], "DE123456789")
        self.assertEqual(result["foreignvat"], "GB987654321")

    @patch('validate_hmrc.http')
    def test_start_validation_error(self, mock_http):
        # Mock response for an error lookup
        mock_response = MagicMock()
        mock_response.status = 404
        mock_response.data = b'{"errorcode": "NOT_FOUND", "message": "NOT_FOUND: VAT number not found"}'
        mock_http.request.return_value = mock_response

        payload = {
            "key1": "k1",
            "key2": "k2",
            "ownvat": "DE123456789",
            "foreignvat": "GB000000000",
            "lang": "en"
        }

        result = validate_hmrc.start_validation(payload)
        self.assertFalse(result["valid"])
        self.assertEqual(result["errorcode"], "NOT_FOUND")
        self.assertIn("not found", result["errorcode_description"].lower())
        self.assertEqual(result["type"], "HMRC")

if __name__ == '__main__':
    unittest.main()