import unittest
import functions


class TestisIsEvenMethods(unittest.TestCase):
    def test_honest(self):
        self.assertTrue(functions.is_even(10), "10 should be even")

    def test_odd(self):
        self.assertFalse(functions.is_even(9), "9 should not be even")

    def test_exception(self):
        with self.assertRaises(TypeError):
            functions.is_even("9")


class TestIsOddMethods(unittest.TestCase):
    def test_honest(self):
        self.assertFalse(functions.is_odd(10), "10 should be even")

    def test_odd(self):
        self.assertTrue(functions.is_odd(9), "9 should not be even")

    def test_exception(self):
        with self.assertRaises(TypeError):
            functions.is_odd("9")


class TestCustomMaxMethods(unittest.TestCase):
    def test_ten(self):
        self.assertEqual(functions.custom_max(1, 10), 10, "should be 10")

    def test_hundred(self):
        self.assertEqual(functions.custom_max(10, 100), 100,  "should be 100")

    def test_exception(self):
        with self.assertRaises(TypeError):
            functions.custom_max("9", 10)


class TestMultiplyMethods(unittest.TestCase):
    def test_list(self):
        example_list = list(range(1, 10))
        self.assertEqual(functions.multiply(*example_list), 362880, "should be 362880")

    def test_base(self):
        example_list = list(range(1, 10))
        self.assertEqual(functions.multiply(*example_list, 2), 725760,  "should be 725760")

    def test_zero(self):
        self.assertEqual(functions.multiply(0), 0,  "should be 0")


class TestReverseMethods(unittest.TestCase):
    def test_list(self):
        self.assertEqual(functions.reverse("QWERqwer123!@#"), "#@!321rewqREWQ", "should be #@!321rewqREWQ!@#")

    def test_empty(self):
        self.assertEqual(functions.reverse(""), "", "should be \"\"")

    def test_exception(self):
        with self.assertRaises(TypeError):
            functions.reverse(1)


class TestUpperCountMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(functions.upper_count("QWER qwer 123 !@#"), 4, "should be 4")

    def test_empty(self):
        self.assertEqual(functions.upper_count(""), 0, "should be 0")

    def test_zero(self):
        self.assertEqual(functions.upper_count("fgfg ffgd g fdgfg fdg"), 0, "should be 0")

    def test_all(self):
        self.assertEqual(functions.upper_count("ABCDE"), 5, "should be 5")

    def test_exception(self):
        with self.assertRaises(TypeError):
            functions.upper_count(1)


class TestUniqueMethods(unittest.TestCase):
    def test_list(self):
        self.assertEqual(functions.unique([2, 2, 1, 5, 5, 2, 7]), [1, 2, 5, 7], "should be [1, 2, 5, 7]")

    def test_empty(self):
        self.assertEqual(functions.unique([]), [], "should be []")

    def test_same(self):
        self.assertEqual(functions.unique([1, 2, 5, 7]), [1, 2, 5, 7], "should be [1, 2, 5, 7]")

    def test_exception(self):
        with self.assertRaises(TypeError):
            functions.unique(1)


class TestIsPangramMethods(unittest.TestCase):
    def test_alph(self):
        self.assertTrue(functions.is_pangram("The five boxing wizards jump quickly!@#"))

    def test_no_alph(self):
        self.assertFalse(functions.is_pangram("1234567890!@#$%^&*()"))

    def test_empty(self):
        self.assertFalse(functions.is_pangram(""))

    def test_exception(self):
        with self.assertRaises(AttributeError):
            functions.is_pangram(1)
