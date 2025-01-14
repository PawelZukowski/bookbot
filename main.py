def count_words(s):
    return len(s.split())

def count_characters(s):
    counter = {}
    for char in s.lower():
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_content = f.read()
    word_count = count_words(file_content)
    print(word_count)
    character_count = count_characters(file_content)
    print(character_count)


main()