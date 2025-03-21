



# def main():
#     path = "books/frankenstein.txt"
#     contents = text_contents(path)
#     count = count_words(contents)
#     letter_count = map_letters(contents)
#     sorted_dict = sort_dict(letter_count)
#     print("--- Begin report of books/frankenstein.txt ---")
#     print(f"{count} words found in document\n")
#     for item in sorted_dict:
#         if item["char"].isalpha():
#             print(f"The '{item['char']}' character was found {item['num']} times")

#     print("--- End report ---")
from stats import get_num_words, map_letters, sort_dict
import sys



def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    text = get_book_text(sys.argv[1])
    wc = get_num_words(text)
    count = map_letters(text)
    sorted_dict = sort_dict(count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    

if __name__ == "__main__":
    main()