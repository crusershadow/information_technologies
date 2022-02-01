
def get_user_num():
    try:
        return int(input('Enter num: '))
    except ValueError:
        return get_user_num()


def is_even(num: int):
    return num % 2 == 0


def is_odd(num: int):
    return num % 2 != 0


if __name__ == '__main__':
    user_num = get_user_num()
    if is_even(user_num):
        print(f'{user_num} is even')
    else:
        print(f'{user_num} is odd')