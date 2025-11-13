import sys

from stats import get_book_text, get_num_words, get_char_count, sort_dictionary




def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        
        FILEPATH = sys.argv[1]
        file_content = get_book_text(FILEPATH)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {FILEPATH}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(file_content)} total words")
        print("--------- Character Count -------")
        sorted_list_dict = sort_dictionary(get_char_count(file_content))
        for d in sorted_list_dict:
            if d["char"].isalpha():
                print(f"{d["char"]}: {d["num"]}")
        print("============= END ===============")

main()