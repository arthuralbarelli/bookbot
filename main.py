from stats import get_num_words, get_num_chars, sort_by_num
import sys


def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        num_words = get_num_words(file_content)
        ordered_chars = sort_by_num(get_num_chars(file_content))
        alpha_chars = [alpha_char for alpha_char in ordered_chars if alpha_char["char"].isalpha()]
        print("=========== BOOKBOT ============")
        print(f"Analyzing book found at {path[1:]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in alpha_chars:
            print(f"{char['char']}: {char['num']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    get_book_text(sys.argv[1])


main()
