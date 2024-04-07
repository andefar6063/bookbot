def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = len(text.split())
    print(f"{word_count} words found in the document")
    char_apperance = character_apperance(text)
    for i in char_apperance:
        print(f"The '{i}' character was found {char_apperance[i]} times")
    print("--- End report ---")


def get_book_text(path):
    print(f"--- Begin report of {path} ---")
    with open(path) as f:
        return f.read()

def character_apperance(text):
    counter = {}
    text = text.lower()
    for i in text:
        if i.isalpha():
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
    return counter

main()
