
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
    for key, value in dict1.items():
        if value == max(dict1.values()):
            return (key, value)

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
    dict_count = dict()
    for item in list3:
        _count = list3.count(item)
        dict_count[item] = _count
    return dict_count

import pprint

list3 = [4, 2, 1, 2, 3, -1, 3, 2, 2]
pprint.pprint(get_count(list3))

'''
4
{"apple":5, "banana":6, "kiwi":4} -> {5:"apple", 6:"banana", 4:"kiwi"}
'''
def reverse_dict(dict1: dict) -> dict:
    '''

    :param dict1: {<word>: <number> ... }
    :return: dict { <number>: <word> }
    '''
    reverse_dict = dict()
    for key, value in dict1.items():
        reverse_dict[value] = key
    return reverse_dict

dict4 = {"apple":5, "banana":6, "kiwi":4}
print(reverse_dict(dict4))


'''
5
[1,2,3,4,5,6]
-> {"even":3, "odd":3}
'''
def count_even_odd(nums: list) -> dict:
    '''
    :param nums: list of numbers
    :return: dict {"even": count_even, "odd": count_odd}
    '''
    num_dict = {"even": 0, "odd": 0}
    for _ in list5:
        if _ % 2 == 0:
            num_dict["even"] += 1
        else:
            num_dict["odd"] += 1
    return num_dict


list5 = [1,2,3,4,5,6]
print(count_even_odd(list5))


'''
6
cities = {
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}

-> ["Paris", "Rome", "Madrid", "New York", "London", "Tokyo"]
(sorted by population from small to big)
'''

def get_cities_sorted_by_population(cities: dict) -> list:
    '''

    :param cities: {
        <city_name>: {
            "language": <language>,
            "population": <population>,
            "size": <city_area_km2>,
            "country": <country>
        }
    }

    :return: list of city names sorted by population (small → big)
    '''
    cities2 = dict()
    for key, value in cities.items():
        cities2[key] = value["population"]

    return sorted(cities2, reverse= True)




cities = {
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}

print(get_cities_sorted_by_population(cities))

'''7
["apple","banana","avocado","blueberry","apricot","corn"]

-> {
    "a": ["apple","avocado","apricot"],
    "b": ["banana","blueberry"],
    "c": ["corn"]
}
'''
def group_by_letter(words: list) -> dict:
    '''

    :param words: list of words
    :return: dictionary where:
             key = first letter of the word
             value = list of all words that start with that letter
    '''
    abc_dict = dict()
    for item in list7:
        abc_dict[str(item[0])] = str(item)
    return abc_dict

list7 = ["apple","banana","avocado","blueberry","apricot","corn"]
print(group_by_letter(list7))