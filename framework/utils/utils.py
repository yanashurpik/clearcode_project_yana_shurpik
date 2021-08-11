import random
from string import ascii_letters


def get_value_by_key(key, structure, is_list=False):
    res = []

    def search(key, structure):
        if isinstance(structure, dict):
            for i, j in structure.items():
                if i == key:
                    res.append(j)
                if isinstance(j, dict) or isinstance(j, list):
                    search(key, j)
        if isinstance(structure, list):
            for i in structure:
                if i == key:
                    res.append(i)
                if isinstance(i, dict) or isinstance(i, list):
                    search(key, i)

    search(key, structure)
    if is_list:
        return res
    try:
        return res[0]
    except IndexError:
        return None


def get_random_string():
    random_string = ''
    for _ in range(random.randint(6, 12)):
        random_string += random.choice(ascii_letters)
    return random_string
