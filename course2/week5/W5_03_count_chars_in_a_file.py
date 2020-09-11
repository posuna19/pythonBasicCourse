def character_frequency(filename):
    """Counts the frequency of each character in a the given file"""

    try:
        file = open(filename)

    except OSError:
        return None

    # Now we process the file
    characters = {}
    for line in file:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    file.close()

    return characters

print(character_frequency("W5_03_chars.txt2"))