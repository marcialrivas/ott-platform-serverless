import unittest
from main.lambda_get_movie_handler import lambda_handler

class lambda_handler_test(unittest.TestCase):
    def setUp(self):
        print("setUp...")

    def tearDown(self):
        print("tearDown...")

    def test_Returns_Request(self):
        victim = lambda_handler()
        result = victim.handle(None, None)
        self.assertEqual(result, "Hello World", 'Expected other value...')