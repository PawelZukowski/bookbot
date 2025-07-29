def count_words(s):
    words = s.split()
    num_words = len(words)
    return num_words





def count_characters(s):
    s = s.lower()
    counter = {}

    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter
