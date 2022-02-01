N = 2
M = 4
Y = 2


def get_all_nums_by_task_condition(n, m, y):
    return [x for x in range(0, m) if x * n % m == y]


if __name__ == '__main__':
    numbers = get_all_nums_by_task_condition(N, M, Y)
    print(numbers)
