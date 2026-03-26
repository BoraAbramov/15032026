
def get_average_grade(grades: dict) -> float:
    '''

    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    sum = 0
    avg = 0
    for k, v in grades.items():
        sum += v
    avg = sum / len(grades)
    return avg


grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}


print(get_average_grade(grades))