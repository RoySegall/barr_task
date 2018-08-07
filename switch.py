def recurse_switcher(base_string, alternatives, new_strings, char_position):
    """
    Getting a base string and switch any letter with the alternatives char.

    :param base_string:
        The base string we need to handle.
    :param alternatives:
        A dictionary with alternatives. Each key represents a letter and the values are alternatives we need to append.
    :param new_strings:
        A list of strings.
    :param char_position:
        The potions of the current char we need to handle.
    """

    if char_position == len(base_string):
        return

    if base_string[char_position] not in alternatives.keys():
        return recurse_switcher(base_string, alternatives, new_strings, char_position + 1)

    # Go over the alternatives of the char.
    original_char = base_string[char_position]

    for new_char in alternatives[original_char]:

        if char_position == 0:
            # Append the rest of the string to the char.
            new_string = str(new_char) + string[char_position + 1:]
            massage_new_string(new_string=new_string, alternatives=alternatives, new_strings=new_strings)

            # Append the char which exists in the original string.
            string_with_original = str(original_char) + string[char_position + 1:]
            if string_with_original not in new_strings:
                new_strings.append(string_with_original)

        if not(char_position == 0) and not char_position == len(base_string):
            # Append the previous chars of the string and rest chars of the string.
            new_string = string[:char_position] + str(new_char) + string[char_position + 1:]
            massage_new_string(new_string=new_string, alternatives=alternatives, new_strings=new_strings)

            # Append the char which exists in the original string.
            string_with_original = string[:char_position] + str(original_char) + string[char_position + 1:]
            if string_with_original not in new_strings:
                new_strings.append(string_with_original)

        if char_position == len(base_string):
            # Append all the chard ahead of the string.
            new_string = str(original_char) + string[char_position + 1:]
            massage_new_string(new_string=new_string, alternatives=alternatives, new_strings=new_strings)

            string_with_original = str(new_char) + string[char_position + 1:]
            if string_with_original not in new_strings:
                new_strings.append(string_with_original)

    # Call the next char in line.
    recurse_switcher(base_string, alternatives, new_strings, char_position + 1)


def massage_new_string(new_string, alternatives, new_strings):
    """
    Go over the new string we created and replace the chars with their replacements.

    :param new_string:
        The new string we appended.
    :param alternatives:
        The alternatives dictionary.
    :param new_strings:
        The strings lists which get the strings.
    :return:
    """
    for char in new_string:

        if char not in alternatives.keys():
            continue

        for replace in alternatives[char]:
            string_to_append = new_string.replace(char, str(replace))

            if string_to_append not in new_strings:
                new_strings.append(new_string.replace(char, str(replace)))

    if new_string not in new_strings:
        new_strings.append(new_string)


# Set the chars and their other representations.
options = {
    "a": ["A", 4],
    "l": ["l", "!", 1],
    "o": ["O", 0],
    "s": ["$", "S"]
}

# Define the string which we need to filter.
string = "loads"

# Available alternatives.
strings = []

# Go over the original string and start to build the strings.
recurse_switcher(base_string=string, alternatives=options, new_strings=strings, char_position=0)
print("The total options number is: " + str(len(strings)) + "\n")
# print(strings)
