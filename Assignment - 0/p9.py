user_string = input("Enter a string: ")

cleaned_string = user_string.lower()

reversed_string = cleaned_string[::-1]

if cleaned_string == reversed_string:
    print(f"'{user_string}' is a palindrome!")
else:
    print(f"'{user_string}' is not a palindrome.")
