import unittest
import defusedxml.minidom as minidom
from validate_bzst import parse_response


class TestValidateBZST(unittest.TestCase):

    def test_parse_response(self):
        # Sample XML response data
        response_data = """
        <response>
            <array>
                <value>
                    <string>key1</string>
                </value>
                <value>
                    <string>value1</string>
                </value>
            </array>
            <array>
                <value>
                    <string>key2</string>
                </value>
                <value>
                    <string>value2</string>
                </value>
            </array>
        </response>
        """

        # Expected result
        expected_result = {
            "key1": "value1",
            "key2": "value2"
        }

        # Call the function
        result = parse_response(response_data)

        # Assert the result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
