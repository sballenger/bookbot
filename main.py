def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_characters = sort_max(each_char_count(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for x in sorted_characters:
        print(f"The '{x[0]}' character was found {x[1]} times")
    print(f"--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def lowercase(text):
    lowercase_string = text.lower()
    return(lowercase_string)

def each_char_count(text):
    char_count = {}
    for char in lowercase(text):
        if char.isalpha() == False:
            continue
        else:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_max(dict):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print (sorted_dict)
    return sorted_dict


def char_count_sorted(key, value):
    sorted
    return sorted

main()