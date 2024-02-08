def main():
    path = "books/frankenstein.txt"
    text = get_text_from_book(path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    letter_list = get_letter_list(char_dict)
    letter_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for letter in letter_list:
        print(f"The '{letter["letter"]}' character was found {letter["num"]} times")
    print("--- End report ---")

def get_text_from_book(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    letters = {}
    for char in text:
        lowered = char.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def get_letter_list(dict):
    letters = []
    for char in dict:
        if char.isalpha():
            letters.append({"letter": char, "num": dict[char]})
    return letters

def sort_on(dict):
    return dict["num"]

main()