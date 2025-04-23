from collections import defaultdict


def words_count(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words


def characters_count(filepath):
    alphabet = defaultdict(int)
    with open(filepath) as file:
        file_contents = file.read().lower()
        for ch in file_contents:
            if ch.isalpha() and 'a' <= ch <= 'z':
                alphabet[ch] += 1
    return alphabet


def sorted_list_of_dicts(freq_dict):

    items = [{"char": k, "num": v} for k, v in freq_dict.items()]

    def sort_on(d):
        return d["num"]

    items.sort(reverse=True, key=sort_on)

    return items
