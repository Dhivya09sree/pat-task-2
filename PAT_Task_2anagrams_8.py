def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

def test_anagram():
    string1 = "listen"
    string2 = "silent"
    if are_anagrams(string1, string2):
        print("The strings are anagrams of each other.")
    else:
        print("The strings are not anagrams of each other.")

# Call the testing function directly
test_anagram()

