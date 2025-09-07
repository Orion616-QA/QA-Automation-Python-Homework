import unittest
from lesson_09.homeworks import (
    sum_of_numbers,
    calculate_two_numbers,
    string_reverse,
    longer_word_in_list,
    find_substring,
)


class TestSumOfNumbers(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(sum_of_numbers("10,20,30"), 60)
        self.assertEqual(sum_of_numbers("5"), 5)
        self.assertEqual(sum_of_numbers("1,2,3,4,50"), 60)

    def test_invalid_numbers(self):
        self.assertEqual(sum_of_numbers("qwerty1,2,3"), "Не можу це зробити")
        self.assertEqual(sum_of_numbers("abc"), "Не можу це зробити")


class TestCalculateTwoNumbers(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(calculate_two_numbers(1, 2), 3)
        self.assertEqual(calculate_two_numbers("3", "7"), 10)
        self.assertEqual(calculate_two_numbers("-5", 5), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_two_numbers("a", "2")


class TestStringReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(string_reverse("hello"), "olleh")
        self.assertEqual(string_reverse("12345"), "54321")
        self.assertEqual(string_reverse("a"), "a")
        self.assertEqual(string_reverse(""), "")


class TestLongerWordInList(unittest.TestCase):
    def test_longest_word(self):
        self.assertEqual(longer_word_in_list(["cat", "dog", "elephant"]), "elephant")
        self.assertEqual(longer_word_in_list(["123", "12345"]), "12345")

    def test_single_word(self):
        self.assertEqual(longer_word_in_list(["hello"]), "hello")

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            longer_word_in_list([])


class TestFindSubstring(unittest.TestCase):
    def test_found(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("12345", "23"), 1)

    def test_not_found(self):
        self.assertEqual(find_substring("The quick brown fox", "cat"), -1)
        self.assertEqual(find_substring("12345", "67"), -1)


if __name__ == "__main__":
    unittest.main()