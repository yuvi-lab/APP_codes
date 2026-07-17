char = input("Enter a single character: ")

if len(char) == 1 and char.isalpha():
    
    lower_char = char.lower()
    
    if lower_char in ('a', 'e', 'i', 'o', 'u'):
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
        
else:
    print("Invalid input! Please enter a single alphabetic letter.")
