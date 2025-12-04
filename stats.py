def string_counter(input_string):
    s_count = len(input_string.split())
    return s_count

def count_all_chars(input_string):
    char_set = set()
    for char in input_string:
        char_set.add(char.lower())
    
    char_dic_list = []
    for char in char_set:
        char_dic = {"name": char,"num": 0}
        char_dic_list.append(char_dic)

    for char in input_string:
        for dic in char_dic_list:
            if char.lower() == dic["name"]:
                dic["num"] += 1

    return char_dic_list

def sort_dic(items):
    
    return items.sort(reverse=True, key=lambda x: x["num"])
