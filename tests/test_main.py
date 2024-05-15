import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(2, 3), 5)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_multiply_list_elements(self):
        self.assertEqual(multiply_list_elements([1, 2, 3]), 6)
        self.assertEqual(multiply_list_elements([0, 2, 4]), 0)
        self.assertEqual(multiply_list_elements([-1, 5, 2]), -10)

    def test_check_even_or_odd(self):
        self.assertEqual(check_even_or_odd(2), 'Even')
        self.assertEqual(check_even_or_odd(3), 'Odd')
        self.assertEqual(check_even_or_odd(0), 'Even')

    def test_find_max_in_list(self):
        self.assertEqual(find_max_in_list([1, 3, 5]), 5)
        self.assertEqual(find_max_in_list([-1, -3, -5]), -1)
        self.assertEqual(find_max_in_list([0]), 0)

    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")
        self.assertEqual(reverse_string(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_check_palindrome(self):
        self.assertTrue(check_palindrome("racecar"))
        self.assertTrue(check_palindrome("level"))
        self.assertFalse(check_palindrome("python"))
        self.assertTrue(check_palindrome(""))

    def test_generate_fibonacci_sequence(self):
        self.assertEqual(generate_fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(generate_fibonacci_sequence(1), [0])
        self.assertEqual(generate_fibonacci_sequence(0), [])

    def test_check_prime_number(self):
        self.assertTrue(check_prime_number(2))
        self.assertTrue(check_prime_number(7))
        self.assertFalse(check_prime_number(4))
        self.assertFalse(check_prime_number(1))


if __name__ == '__main__':
    unittest.main()
