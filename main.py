def read_file(path):
    with open(path) as file:
        text = file.read()
    return text

def total_word_count(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def report(word_count, character_count):
    print("---Begin Report---")
    print(f"Total word count: {word_count}")
    for char, count in character_count.items():
        print(f"The '{char}' character appears {count} times.")
    print("---End Report---")

def main():
    text = read_file('books/frankenstein.txt')
    word_count = total_word_count(text)
    character_count = count_characters(text)
    report(word_count, character_count)
    

main()