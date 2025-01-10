def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    list_of_dict = convert_list(num_characters)
    list_of_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frakenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for char_dict in list_of_dict:
        print(f"The '{char_dict["char"]}' character was found {char_dict["num"]} times" )
    print("--- End report ---")
   

def convert_list(num_characters):
    chars_list = []
    for char, count in num_characters.items():
        if char.isalpha():
            new_dict = {
                "char": char,
                "num": count
            } 
            chars_list.append(new_dict)
    return chars_list

def sort_on(dict):
    return dict["num"]


def get_num_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()