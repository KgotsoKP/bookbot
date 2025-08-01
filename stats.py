from audioop import reverse


def get_num_words(book_text):
    result = book_text.split()
    return len(result)


def get_charater_count(book_text):
    char_count = {}

    for word in book_text:
        transformed = word.lower()

        if transformed in char_count:
            char_count[transformed] += 1
        else:
            char_count[transformed] = 1

    return char_count

def sort_on(items):
    return items["char"]

def sort_dictionary(char_dict):

    dict_list = []
    # new_dict = char_dict.sort(key=char_dict)

    for key in char_dict:
        nd = {}
        nd['char'] = key
        nd['num'] = char_dict[key]
        dict_list.append(nd)

    dict_list.sort(key=sort_on)

    return dict_list


        
        