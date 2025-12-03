def get_book_text(file_path):
    with open(file_path, encoding='utf-8-sig') as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def get_chars_dict(text):
    words = text.split()

    dict_characters = {}

    for word in words:
        chars = list(word)
        lower_chars = [item.lower() for item in chars]

        for char in lower_chars:
            if (char in dict_characters):
                dict_characters[char] += 1
            else:
                dict_characters[char] = 1

    return dict_characters