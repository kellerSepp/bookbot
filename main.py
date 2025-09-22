from stats import count_words
from stats import count_characters
from stats import sort_dictionary_as_list

def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()
    return book_as_string

def main():
    #print("foo")
    book_path = "books/frankenstein.txt"
    book_string = get_book_text(book_path)
    counted_words = count_words(book_string)
    counted_characters = count_characters(book_string)
    #print(counted_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")
    character_count = sort_dictionary_as_list(counted_characters)
    for char_count in character_count:
        print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")
main()