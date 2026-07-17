while True:
    try:
        num = int(input("Please enter a whole number: "))

        print(f"Success! You entered a valid integer: {num}")
        break
        
    except ValueError:
        print("That is not a valid whole number. Please try again!\n")

print("Thank you for playing!")
