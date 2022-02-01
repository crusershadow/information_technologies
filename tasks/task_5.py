def get_triangle_base():
    try:
        return int(input(f'Base of triangle: '))
    except ValueError:
        return get_triangle_base()


def get_triangle_height():
    try:
        return int(input('Height of triangle: '))
    except ValueError:
        return get_triangle_height()


def get_triangle_square(base: int, height:int):
    return 0.5 * base * height


if __name__ == '__main__':
    t_base = get_triangle_base()
    t_height = get_triangle_height()
    print(get_triangle_square(base=t_base, height=t_height))
