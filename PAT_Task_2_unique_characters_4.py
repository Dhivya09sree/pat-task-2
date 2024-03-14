def count_unique_characters(string):
    # Create an empty set to store unique characters
    unique_characters = set()
    
    # Iterate through each character in the string
    for char in string:
        # Add the character to the set
        unique_characters.add(char)
        print("unique characters:", unique_characters)
    
    # Return the number of unique characters
    return len(unique_characters)

# Test the function
input_string = "malayalam"
unique_count = count_unique_characters(input_string)
print("Number of unique characters:", unique_count)


