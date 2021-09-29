import unittest
import  sys

class TestCase(unittest.TestCase):
    @unittest.skip('demonstrating sipping')
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"), 'requires Windows')
    def test_windows_support(self):
        pass

    @unittest.expectedFailure
    def test_format(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()