def count_words(text):
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


def text_contents(path):
    with open(path) as f:
        return f.read()


def sort_on(d):
    return d["num"]

def sort_dict(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    path = "books/frankenstein.txt"
    contents = text_contents(path)
    count = count_words(contents)
    letter_count = map_letters(contents)
    sorted_dict = sort_dict(letter_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in document\n")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



if __name__ == "__main__":
    main()