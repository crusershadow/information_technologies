from functools import partial


def _filter_value(min_value, max_value, num):
    return min_value <= num < max_value


def get_elems_count_by_filter(l: list, _min, _max):
    filter_value = partial(_filter_value, _min, _max)
    return len(tuple(filter(filter_value, l)))


if __name__ == '__main__':
    elems_count = get_elems_count_by_filter([1, 24, 5, 45, 46], 20, 46)
    print(f'Filtered elements count: {elems_count}')
