# Define a function called match_words that takes a list of words 'words' as input
def match_words(words):
    # Initialize a counter 'ctr' to keep track of matching words
    ctr = 0

    # Iterate through each word in the input list 'words'
    for word in words:
        # Check if the word has a length greater than 1 and its first and last characters are the same
        if len(word) > 1 and word[0] == word[-1]:
            # If the condition is met, increment the counter 'ctr'
            ctr += 1
            print(ctr)

    # Return the final count of matching words
    return ctr

# Call the match_words function with the list ['abc', 'xyz', 'aba', '1221'] as input and print the result
print(match_words(['a', '1221','df','sfsf','648','gsdjgd']))
