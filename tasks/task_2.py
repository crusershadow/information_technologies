from math import pi


def get_circle_radius():
    try:
        return float(input('Enter radius: '))
    except ValueError:
        return get_circle_radius()

def calculate_square(circle_radius):
    return 2*pi*circle_radius


if __name__ == '__main__':
    print(calculate_square(get_circle_radius()))