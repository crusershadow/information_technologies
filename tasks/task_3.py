
def _generate_iter_structure_with_nums(struct, string):
    try:
        return struct(map(int, string.split(',')))
    except ValueError as err:
        print(f'Enter just nums {err}')


def generate_list(nums_string):
    return _generate_iter_structure_with_nums(list, nums_string)


def generate_tuple(nums_string):
    return _generate_iter_structure_with_nums(tuple, nums_string)


def get_user_input():
    return input('Enter nums: ').strip(',')


if __name__ == '__main__':
    user_input = get_user_input()
    print(generate_tuple(user_input))
    print(generate_list(user_input))