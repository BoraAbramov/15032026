
'''
1
["apple","banana","kiwi","grape","kiwi"] -> {"apple":5, "banana":6, "kiwi":4, "grape":5 }
'''

def get_len_word(list1: list) -> dict:
    '''

    :param list1: list of words
    :return: dict { <word>: <how many letters (len) > }
    '''
    len_word = dict()
    for word in list1:
        len_word[word] = len(word)
    return len_word

list1 = ["apple","banana","kiwi","grape","kiwi"]

print(get_len_word(list1))

'''
2
grades = {"Tom":80, "Anna":95, "John":70} -> (Anna , 95)
'''
def get_max(dict1: dict) -> tuple:
    '''

    :param dict1: {<name>: <grade> ... }
    :return: (<name>, <grade>) of the max student
    '''
    grade_list = list()
    for key, value in grades.items():
        grade_list.append(value)
    max_grade = max(grade_list)
    return max_grade


grades = {"Tom":80, "Anna":95, "John":70}
print(get_max(grades))



'''
3
count repetition
[4, 2, 1, 2, 3, -1, 3, 2, 2] -> { 1: 1, 2: 4, 3: 2, 4: 1, -1: 1}
'''
def get_count(list1: list) -> dict:
    '''

    :param list1: list of numbers
    :return: dict { <number>: <how many times appear> }
    '''
    pass


list3 = [4, 2, 1, 2, 3, -1, 3, 2, 2]