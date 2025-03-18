import sys
from stats import get_num_words
from stats import get_characters
from stats import sort_characters

exception = False
try:
    book = sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    exception = True
    sys.exit(1)

def main(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_characters(book_path)
    for character, count in sorted_characters:
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")
    

main(sys.argv[1])