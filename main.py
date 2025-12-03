

from stats import count_words, get_book_text, get_chars_dict


def main():
    text = get_book_text('books/frankenstein.txt', )

    num_words = count_words(text)


    dict_characters = get_chars_dict(text)

    print(f'Found {num_words} total words')
    print(dict_characters)

main()