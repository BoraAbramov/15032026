
def group_numbers(nums: list) -> dict:
    '''

    :param nums: list of numbers
    :return: dictionary with keys:
             "positive", "negative", "zero"
             and lists of numbers for each category
    '''
    num_scale = {"positive": [], "negative": [], "zero": []}
    for x in nums:
        if x > 0:
            num_scale["positive"].append(x)
        elif x == 0:
            num_scale["zero"].append(x)
        else:
            num_scale["negative"].append(x)
    return num_scale


_num = [4, -2, 0, 7, -5, 3]

print(group_numbers(_num))