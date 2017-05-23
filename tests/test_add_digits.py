from unittest import TestCase


class TestAdd_digits(TestCase):
    def test_add_digits(self):
        try:
            from build import add_digits
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, add_digits, None)
        self.assertRaises(ValueError, add_digits, -1)
        self.assertEqual(add_digits(0), 0)
        self.assertEqual(add_digits(9), 9)
        self.assertEqual(add_digits(138), 3)
        self.assertEqual(add_digits(65536), 7)
