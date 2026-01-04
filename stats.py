def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = {}
    for char in text.lower():
        if char not in characters: 
            characters[char] = 1
            continue
        characters[char] += 1
    list_characters = []
    for char in characters:
        if not char.isalpha(): continue
        dict = {"char": char, "num": characters[char]}
        list_characters.append(dict)
    list_characters.sort(reverse=True, key=sort_on)
    return list_characters
def sort_on(characters):
    return characters["num"]