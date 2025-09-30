import unittest
import os
import json
import sys
import settings

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))


class TestConfigJson(unittest.TestCase):
    def setUp(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '../config.json')
        settings.create_config()

    def tearDown(self):
        if os.path.isfile(self.config_path):
            os.remove(self.config_path)

    def test_config_json_exists(self):
        self.assertTrue(os.path.isfile(self.config_path), f"{self.config_path} does not exist.")

    def test_config_json_is_valid_json(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            try:
                _ = json.load(f)
            except Exception as e:
                self.fail(f"config.json is not valid JSON: {e}")

    def test_config_json_has_required_keys(self):
        required_keys = [
            "logfilename",
            "loglevel",
            "delimiter",
            "language",
            "interface"
        ]
        with open(self.config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key in required_keys:
            self.assertIn(key, data, f"Missing required key: {key}")


if __name__ == '__main__':
    unittest.main()
