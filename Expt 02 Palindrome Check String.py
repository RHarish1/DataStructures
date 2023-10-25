input_str = input("Enter a string: ")

def is_palindrome(input_str):
    input_str = input_str.lower()
    input_str = input_str.replace(" ", "")
    length = len(input_str)
    for i in range(length // 2):
        if input_str[i] != input_str[length - i - 1]:
            return False
    return True

if is_palindrome(input_str):
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
