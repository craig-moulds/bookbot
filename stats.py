def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_count(text):
    char = text.lower()
    char_counted = {}
    for letter in char:
        if letter in char_counted:
            char_counted[letter] += 1
        else:
            char_counted[letter] = 1
    
    return char_counted

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
