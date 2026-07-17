file_name = input("Enter the name of the file (e.g., sample.txt): ")

try:
    with open(file_name, 'r') as file:
        word_count = 0
        
        for line in file:
            words = line.split()
            word_count += len(words)
            
    print(f"The file '{file_name}' contains {word_count} words.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' could not be found.")
