def get_num_words(text):
    text = text.split()
    return len(text)


def map_letters(text):
    text = text.lower()
    letter_count = {}
    for char in text:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count

def sort_on(d):
    return d["num"]

def sort_dict(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list