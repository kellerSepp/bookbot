import sys
from stats import count_words
from stats import count_characters
from stats import sort_dictionary_as_list

def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()
    return book_as_string

def main():
    try:
        script_name = sys.argv[0]
        book_path = sys.argv[1]
        book_string = get_book_text(book_path)
        counted_words = count_words(book_string)
        counted_characters = count_characters(book_string)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {counted_words} total words")
        print("--------- Character Count -------")
        character_count = sort_dictionary_as_list(counted_characters)
        for char_count in character_count:
            print(f"{char_count["char"]}: {char_count["num"]}")
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
main()