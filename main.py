import sys

from stats import count_words, get_book_text, get_chars_dict, dict_to_list_chars


def main():
    if (len(sys.argv) <2):
        print(': Usage: python3 main.py <path_to_book>')
        
        sys.exit(1)
    
    path = sys.argv[1]

    text = get_book_text(path)

    num_words = count_words(text)
    dict_characters = get_chars_dict(text)

    list_chars = dict_to_list_chars(dict_characters)

    def sort_on(dict):
        return dict['num']
    
    list_chars.sort(reverse=True,key=sort_on)


    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')

    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')

    print('--------- Character Count -------')

    for item in list_chars:
        print(f'{item['char']}: {item['num']}')

    print('============= END ===============')

main()