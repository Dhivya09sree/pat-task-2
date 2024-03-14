def most_frequent_character(input_string):
    char_counts = {} #store the frequency of each character in the input string.
    for char in input_string:
# Updates the count of each character in the dictionary, incrementing by 1 if it exists, otherwise setting it to 1.
     char_counts[char] = char_counts.get(char, 0) + 1
    #Returns the character with the highest frequency based on the values (frequencies) in the dictionary.
    return max(char_counts, key=char_counts.get)

# Test the function
input_string = "malayalam"
#Calls the function with the input string and stores the result (the most frequent character).
most_freq_char = most_frequent_character(input_string)
print("The most frequent character is:", most_freq_char)
