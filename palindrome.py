# reverse_string.py

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

if user_input == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
