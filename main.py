def main():
    line_break = "===================="
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    print(f"Total word count: {word_count} \n")
    
    char_count = character_count(text)
    
    sorted_list = sort_char_count(char_count)
    for i in sorted_list:
        print(f"The '{i['char']}' character was found {i['num']} times.")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
        words = text.split()
        return len(words)

def character_count(text):
    lowered_text = text.lower()
    char_dict = {}
    for c in lowered_text:
        if c not in char_dict and c.isalpha():
            char_dict[c] = 1
        else:
            if c.isalpha() == False:
                continue
            char_dict[c] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_char_count(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()