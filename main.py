import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_string = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {string_counter(book_string)} total words")
    print("--------- Character Count -------")
    book_count = count_all_chars(book_string)
    book_sort = sort_dic(book_count)
    for entry in book_count:
        if entry["name"].isalpha():
            print(f"{entry["name"]}: {entry["num"]}")

main()
