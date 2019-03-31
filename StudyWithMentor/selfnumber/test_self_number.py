import unittest


class SelfNumberTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2, 1+1)


if __name__ == '__main__':
    unittest.main()
