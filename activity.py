def find_first_repeating_character(s):
    char_count = {}  # Dictionary to store character counts
    
    for char in s:
        if char in char_count:
            # Character is repeating, print it along with memory address
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1
    
    # No repeating character found
    return None

# Example usage
input_string = "hello"
result = find_first_repeating_character(input_string)
if result:
    print(f"Found: {result}")
else:
    print("No repeating character found.")
