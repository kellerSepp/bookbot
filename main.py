from stats import count_words

def get_book_text(filepath):
    book_as_string = ""
    with open(filepath) as f:
        book_as_string = f.read()
    return book_as_string

def main():
    #print("foo")
    book_path = "books/frankenstein.txt"
    count = count_words(get_book_text(book_path))
    print(f"Found {count} total words")

main()