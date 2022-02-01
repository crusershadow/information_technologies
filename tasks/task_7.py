
def get_user_num(name):
    try:
        return int(input(f'Enter {name}: '))
    except ValueError:
        return get_user_num(name)


def get_m():
    return get_user_num('m')

def get_n():
    return get_user_num('n')


def calculate_gcd(n, m):
    d = min(n,m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d



if __name__ == '__main__':
    print(calculate_gcd(get_n(), get_m()))
