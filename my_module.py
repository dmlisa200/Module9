"""
calls the functions from my_definitions.py and provides the dictionary and set lists
"""

import my_definitions


name_dict = {'Sara': 34, 'Janet': 80, 'Daniel' : 65, 'Amy': 55}

name_set = {'Ankeny', 'Johnston', 'Des Moines', 'Grimes', 'Altoona'}


if __name__ == '__main__':
    my_definitions.greeting('Jan')

    my_definitions.message('Lisa Kilmer')

    my_definitions.print_dict(name_dict)

    my_definitions.print_set(name_set)
