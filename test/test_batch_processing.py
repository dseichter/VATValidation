import unittest
from unittest.mock import patch
import tempfile
import os
import batch


class TestValidateBatch(unittest.TestCase):
    @patch('batch.processcsv', return_value=0)
    @patch('batch.processxlsx', return_value=0)
    @patch('batch.processjson', return_value=0)
    def test_validatebatch_csv(self, mock_json, mock_xlsx, mock_csv):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp:
            tmp.write("key1,key2,ownvat,foreignvat,company,street,zip,town\n")
            tmp.flush()
            result = batch.validatebatch(tmp.name)
            self.assertEqual(result, 0)
            mock_csv.assert_called_once()
        os.remove(tmp.name)

    @patch('batch.processcsv', return_value=0)
    @patch('batch.processxlsx', return_value=0)
    @patch('batch.processjson', return_value=0)
    def test_validatebatch_xlsx(self, mock_json, mock_xlsx, mock_csv):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xlsx', delete=False) as tmp:
            tmp.write("dummy")  # content doesn't matter, function is mocked
            tmp.flush()
            result = batch.validatebatch(tmp.name)
            self.assertEqual(result, 0)
            mock_xlsx.assert_called_once()
        os.remove(tmp.name)

    @patch('batch.processcsv', return_value=0)
    @patch('batch.processxlsx', return_value=0)
    @patch('batch.processjson', return_value=0)
    def test_validatebatch_json(self, mock_json, mock_xlsx, mock_csv):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            tmp.write("{}")
            tmp.flush()
            result = batch.validatebatch(tmp.name)
            self.assertEqual(result, 0)
            mock_json.assert_called_once()
        os.remove(tmp.name)

    def test_validatebatch_unsupported(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
            tmp.write("unsupported")
            tmp.flush()
            result = batch.validatebatch(tmp.name)
            self.assertEqual(result, 127)
        os.remove(tmp.name)


if __name__ == '__main__':
    unittest.main()
