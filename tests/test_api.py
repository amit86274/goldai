
import unittest

class TestAPI(unittest.TestCase):
    def test_health(self):
        self.assertIsNotNone("ok")
