def subtract_strings(str1, str2):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in str1
    for char in str1:
        # Check if the character exists in str2
        if char not in str2:
            # If not, append it to the result string
            result += char

    return result

# Example usage:
str1 = "Abcdef"
str2 = "abcdghi"
result = subtract_strings(str1, str2)
print("Result after subtracting str2 from str1:", result)  
