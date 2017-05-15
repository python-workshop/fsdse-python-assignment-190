from unittest import TestCase


class TestBuild(TestCase):
    #check if input is 0 output must 0
    #check if input is none should give false
    #input any number divisible 9 should give output 9
    #check by higher number should give one digit

    def test_check_if_input_is_0_output_must_0(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import error")

        result = build(0)
        self.assertEqual(0,result)

    def test_check_if_input_is_none_give_false(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import error")

        result = build(None)
        self.assertEqual(False, result)

    def test_check_if_input_is_none_give_false(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import error")

        result = build(12890)
        self.assertEqual(True, result)