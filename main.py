import sys
from stats import get_num_words, count_characters, sorted_list

def get_book_text(f):
    with open(f) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    path = sys.argv[1]
    num_words = get_num_words(get_book_text(path))
    dictionary = count_characters(get_book_text((path)))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
   # print(dictionary)
    #print(sorted_list(dictionary))
    for i in sorted_list(dictionary):
       char = i["char"]
       number = i["num"]
       if char[0].isalpha():
        print(f"{char[0]}: {number}")
    #print(sorted_list(dictionary))
    print("============= END ===============")


main()