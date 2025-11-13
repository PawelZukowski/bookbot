def get_book_text(filepath):
    with open(filepath, mode="r") as f:
        file_content = f.read()
    
    return file_content


def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    counter = {}
    text = text.lower()
    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter


def sort_dictionary(d):
    list_dict = [{"char": key, "num": value} for key, value in d.items()]
    return sorted(list_dict, reverse=True, key=lambda d: d["num"])
