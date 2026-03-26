
def group_words_by_length(fruits: list) -> dict:
    '''

    :param words: list of words
    :return: dict { <length>: [list of words with that length] }
    '''
    sorted_by_len = dict()
    for x in fruits:
        sorted_by_len.setdefault(len(x),[])
        sorted_by_len[len(x)].append(x)
    return sorted_by_len




fruits = ["apple","banana","kiwi","grape","melon","pear"]

#{
#    5: ["apple","grape","melon"],
#    6: ["banana"],
#    4: ["kiwi","pear"]
#}


print(group_words_by_length(fruits))
