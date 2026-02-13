import unittest
from unittest.mock import patch, MagicMock
import validate_swiss


class TestValidateSwiss(unittest.TestCase):
    @patch('validate_swiss.http')
    def test_start_validation_success(self, mock_http):
        # Mock response for a successful validation
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = b'''<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
  <s:Body>
    <ValidateVatNumberResponse xmlns="http://www.uid.admin.ch/xmlns/uid-wse">
      <ValidateVatNumberResult>true</ValidateVatNumberResult>
    </ValidateVatNumberResponse>
  </s:Body>
</s:Envelope>'''
        mock_http.request.return_value = mock_response

        payload = {
            "key1": "k1",
            "key2": "k2",
            "ownvat": "DE123456789",
            "foreignvat": "CHE-109.740.084",
            "lang": "en"
        }

        result = validate_swiss.start_validation(payload)
        self.assertTrue(result["valid"])
        self.assertEqual(result["errorcode"], "VALID")
        self.assertEqual(result["type"], "swiss")
        self.assertEqual(result["key1"], "k1")
        self.assertEqual(result["key2"], "k2")

    @patch('validate_swiss.http')
    def test_start_validation_invalid(self, mock_http):
        # Mock response for an invalid VAT number
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = b'''<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
  <s:Body>
    <ValidateVatNumberResponse xmlns="http://www.uid.admin.ch/xmlns/uid-wse">
      <ValidateVatNumberResult>false</ValidateVatNumberResult>
    </ValidateVatNumberResponse>
  </s:Body>
</s:Envelope>'''
        mock_http.request.return_value = mock_response

        payload = {
            "key1": "k1",
            "key2": "k2",
            "ownvat": "DE123456789",
            "foreignvat": "CHE-000.000.000",
            "lang": "en"
        }

        result = validate_swiss.start_validation(payload)
        self.assertFalse(result["valid"])
        self.assertEqual(result["errorcode"], "INVALID")
        self.assertEqual(result["type"], "swiss")

    @patch('validate_swiss.http')
    def test_start_validation_adds_mwst_suffix(self, mock_http):
        # Test that MWST suffix is added automatically
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = b'''<?xml version="1.0"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
  <s:Body>
    <ValidateVatNumberResponse xmlns="http://www.uid.admin.ch/xmlns/uid-wse">
      <ValidateVatNumberResult>true</ValidateVatNumberResult>
    </ValidateVatNumberResponse>
  </s:Body>
</s:Envelope>'''
        mock_http.request.return_value = mock_response

        payload = {
            "key1": "k1",
            "key2": "k2",
            "ownvat": "DE123456789",
            "foreignvat": "CHE-109.740.084",
            "lang": "en"
        }

        validate_swiss.start_validation(payload)
        
        # Check that the request was made with MWST suffix
        call_args = mock_http.request.call_args
        request_body = call_args[1]['body'].decode('utf-8')
        self.assertIn('CHE-109.740.084 MWST', request_body)

    @patch('validate_swiss.http')
    def test_start_validation_error(self, mock_http):
        # Mock response for an error
        mock_response = MagicMock()
        mock_response.status = 500
        mock_response.data = b'Internal Server Error'
        mock_http.request.return_value = mock_response

        payload = {
            "key1": "k1",
            "key2": "k2",
            "ownvat": "DE123456789",
            "foreignvat": "CHE-109.740.084",
            "lang": "en"
        }

        result = validate_swiss.start_validation(payload)
        self.assertFalse(result["valid"])
        self.assertEqual(result["errorcode"], "HTTP_500")
        self.assertEqual(result["type"], "swiss")


if __name__ == '__main__':
    unittest.main()
