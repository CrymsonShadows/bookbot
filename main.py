def main():
    text = get_text_from_book("books/frankenstein.txt")
    num_words = get_num_words(text)
    # print(file_contents)
    print(f"The number of words in frankenstein is {num_words}!")

def get_text_from_book(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

main()