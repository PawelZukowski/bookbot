import sys
from stats import count_words, count_characters




def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content






def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    file_content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    word_count = count_words(file_content)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_counter = count_characters(file_content)
    sorted_character_counter = {k: v for k, v in sorted(character_counter.items(), key=lambda x: x[1], reverse=True) if k.isalpha()}
    for char in sorted_character_counter:
        print(f"{char}: {sorted_character_counter[char]}")





main()



