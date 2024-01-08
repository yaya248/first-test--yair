# comp.py

def sum_of_digits(number):
    """Function to calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(abs(number)))

def is_palindrome(number):
    """Function to check if a number is a palindrome."""
    str_number = str(abs(number))
    return str_number == str_number[::-1]
