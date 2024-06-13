
def read_book(file: str):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def count_words(x: str):
    words = x.split()
    count = len(words)
    return count


def sort_on(dict: dict):
    return dict['count']


def convert_into_list(dict: dict):
    l = []
    for key, value in dict.items():
        char = {"char":key, "count": value}
        l.append(char)
    return l

def count_letters(x: str):
    letter_count = {}
    words = x.split()
    for word in words:
        for letter in word.lower():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    l = convert_into_list(letter_count)
    sorted_dict_list = sorted(l, reverse=True, key=sort_on)
    sorted_letter_count = {}
    for i in sorted_dict_list:
        sorted_letter_count[i["char"]] = i["count"] 
    return sorted_letter_count


def print_report(d: dict):
    for key, value in d.items():
        print(f'The {key} character was found {value} times')


def main():
    book = read_book('books/frankenstein.txt')
    count = count_words(book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{count} words found in the document', '\n')
    sorted_count = count_letters(book)
    print_report(sorted_count)
    print("--- End Report ---")
    

main()

