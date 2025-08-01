import sys
from stats import get_num_words, get_charater_count, sort_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    num_of_words = get_num_words(contents)
    char_count = get_charater_count(contents)

    # print(f"{num_of_words} words found in the document")
    # print(char_count)
    sorted_list = sort_dictionary(char_count)
    print_report(sorted_list, book_path, num_of_words)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(list, path, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {75767} total words")
    print("--------- Character Count -------")

    for i in range(0, len(list) -1):
        if list[i]['char'].isalpha():
            print(f"{list[i]['char']}: {list[i]['num']}")

    print("============= END ===============")
    
    return


main()