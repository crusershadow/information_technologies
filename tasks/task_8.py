from pprint import pprint


def _get_num_range(num):
    if num < 0:
        return range(-1, num, -1)
    else:
        return range(1, num)


def get_num_dividers(num):
    return [divider for divider in _get_num_range(num) if num % divider == 0]


def get_user_num():
    try:
        return int(input('Enter your num: '))
    except ValueError:
        return get_user_num()


if __name__ == '__main__':
    user_num = get_user_num()
    dividers = get_num_dividers(user_num)
    print(f'All dividers: {dividers}')
