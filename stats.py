def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for c in text.lower():
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(chars):
    char_list = []
    for k in chars:
        char_list.append({"char": k, "num" : chars[k]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list