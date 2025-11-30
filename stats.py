def get_num_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_list(dict):
    sorted = list()
    for i in dict:
        sorted.append({"char": [i], "num": dict[i]})
    sorted.sort(reverse=True,key=sort_on)
    return sorted

def sort_on(items):
    return items["num"]