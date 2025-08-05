import unittest
from validate_vies import parse_vies_response


class TestValidateVIES(unittest.TestCase):
    def test_parse_response_with_valid_xml(self):
        # Sample XML response data for VIES
        response_data = """
        <env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Header/><env:Body>
         <ns2:checkVatApproxResponse xmlns:ns2="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
           <ns2:countryCode>IT</ns2:countryCode><ns2:vatNumber>01739710307</ns2:vatNumber>
           <ns2:requestDate>2024-02-09+01:00</ns2:requestDate>
           <ns2:valid>false</ns2:valid>
           <ns2:traderName></ns2:traderName>
           <ns2:traderCompanyType>---</ns2:traderCompanyType>
           <ns2:traderAddress></ns2:traderAddress>
           <ns2:requestIdentifier></ns2:requestIdentifier>
         </ns2:checkVatApproxResponse></env:Body></env:Envelope>

        """
        # Faultcode
        # <env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Header/><env:Body>
        #   <env:Fault>
        #     <faultcode>env:Server</faultcode>
        #     <faultstring>MS_UNAVAILABLE</faultstring>
        # </env:Fault></env:Body></env:Envelope>
        expected_result = {
            "traderName": None,
            "traderAddress": None,
            "valid": "false",
            "requestDate": None,  # This will be set to current UTC time in actual code
            "errorcode": "",
        }

        result = parse_vies_response(response_data)
        # Only check keys except requestDate, which is dynamic
        for key in expected_result:
            if key != "requestDate":
                self.assertEqual(result[key], expected_result[key])
            else:
                self.assertIsNotNone(result[key])

    def test_parse_response_with_fault_code(self):
        # Sample XML response data with fault code
        fault_response = """
        <env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Header/><env:Body>
          <env:Fault>
            <faultcode>env:Server</faultcode>
            <faultstring>MS_UNAVAILABLE</faultstring>
          </env:Fault></env:Body></env:Envelope>
        """

        expected_result = {
            "traderName": None,
            "traderAddress": None,
            "valid": None,
            "requestDate": None,  # Will be set to current UTC time in actual code
            "errorcode": "MS_UNAVAILABLE",
        }

        result = parse_vies_response(fault_response)
        for key in expected_result:
            if key != "requestDate":
                self.assertEqual(result[key], expected_result[key])
            else:
                self.assertIsNotNone(result[key])


if __name__ == "__main__":
    unittest.main()
