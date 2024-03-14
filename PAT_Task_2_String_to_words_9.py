def count_words(string):
    # Split the string into words based on whitespace
    words = string.split()
    # Return the count of words
    return len(words)

# Test the function
input_string = "Hello world"
word_count = count_words(input_string)
print("Number of words:", word_count)
