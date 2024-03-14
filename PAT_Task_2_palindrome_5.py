def palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Initialize a variable to store the result
    is_palindrome = True
    
    # Iterate over half of the string using a for loop
    for i in range(len(s) // 2):
        # Check if characters from the beginning and end match
        if s[i] != s[-i - 1]:
            # If characters don't match, set the result to False
            is_palindrome = False
            # Break out of the loop since we don't need to check further
            break
    
    return is_palindrome

# Test the function
test_string = "malayalam"
result = palindrome(test_string)
if result:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
