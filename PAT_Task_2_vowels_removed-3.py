def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:#iterates the input_string text 
        if char not in vowels:#This condition checks if the current char is not in the vowels string.ture the statement 
            result += char#appends the current char  to the result
    return result

# execute the function
input_string = input()#take input from user 
print("Original string:", input_string)
print("String with vowels removed:", remove_vowels(input_string))

