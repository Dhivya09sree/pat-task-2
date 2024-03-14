def count_vowels(text):
    # Convert the input text to lowercase for case insensitivity
    text = text.lower()
    
    # Count occurrences of each vowel using list comprehension
    count_a = text.count('a')
    count_e = text.count('e')
    count_i = text.count('i')
    count_o = text.count('o')
    count_u = text.count('u')
    
    # Calculate total number of vowels
    total_vowels = count_a + count_e + count_i + count_o + count_u
    
    return total_vowels, count_a, count_e, count_i, count_o, count_u

# Input string
input_string = "GUVI GEEKS NETWORK PRIVATE LIMITED"

# Count vowels
total_vowels, count_a, count_e, count_i, count_o, count_u = count_vowels(input_string)

# Display results
print("Total number of vowels:", total_vowels)
print("Number of 'A':", count_a)
print("Number of 'E':", count_e)
print("Number of 'I':", count_i)
print("Number of 'O':", count_o)
print("Number of 'U':", count_u)
