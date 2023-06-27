def find_unique_character(text):
    # Create a dictionary to store the count of each character
    character_count = {}

    # Iterate over each word in the text
    for word in text.split():
        # Iterate over each character in the word
        for char in word:
            # Increase the count for the character
            character_count[char] = character_count.get(char, 0) + 1

    # Iterate over each word in the text again
    for word in text.split():
        # Iterate over each character in the word
        for char in word:
            # If the character appears only once, return it
            if character_count[char] == 1:
                return char

    # If there are no unique characters, return None
    return None


# Example usage
input_text = input("Enter the text: ")
result = find_unique_character(input_text)
if result:
    print("The first unique character:", result)
else:
    print("There are no unique characters in the text.")
