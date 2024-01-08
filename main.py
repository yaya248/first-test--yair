# main.py
from tools.numbers.simp import adding, subtracting
from tools.numbers.comp import sum_of_digits, is_palindrome
from tools.col import myzip

# Function to get user input for a number
def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()

# Function to run all functions with user input
def run_all_functions():
    simp_functions_called = False  # Flag to track if a simp function has been called

    def check_simp_functions_called():
        if not simp_functions_called:
            raise Exception("Cannot call functions in comp module before calling at least one function in simp module.")

    num1 = get_user_input()
    num2 = get_user_input()

    result_add = adding(num1, num2)
    result_subtract = subtracting(num1, num2)

    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")

    # Set the flag to indicate that a simp function has been called
    simp_functions_called = True

    num_for_sum_of_digits = get_user_input()
    num_for_is_palindrome = get_user_input()

    # Check if a simp function has been called before calling comp functions
    check_simp_functions_called()

    result_sum_of_digits = sum_of_digits(num_for_sum_of_digits)
    result_is_palindrome = is_palindrome(num_for_is_palindrome)

    print(f"Sum of digits result: {result_sum_of_digits}")
    print(f"Is palindrome result: {result_is_palindrome}")

    # Example usage of myzip with user input
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    print(f"Using myzip with predefined lists: {list(myzip(list1, list2))}")

# Run all functions with user input
run_all_functions()

