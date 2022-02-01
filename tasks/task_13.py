function = []


def delit(_x, des):
    return _x // des


def minus(_x, v):
    return _x - v


def timofei_function(x):
    var = 0
    for des in (10**i for i in range(0, len(f'{x}'))):
        var += x // des
    return var


def timofei_function_reversed(x):
    numbers = []
    var = None
    for des in (10 ** d for d in range(len(f'{x}')-1, -1, -1)):
        if var is not None:
            numbers.append(var)
            var = x // des - sum(numbers)
        else:
            var = x // des
        x = x - var

    return x


def calculate_task():
    for i in range(1, 10 ** 18):
        if i == timofei_function_reversed(i):
            return i


if __name__ == '__main__':
    # print(timofei_function(983))
    print(timofei_function(600000) / 666666)
    # print(timofei_function_reversed(770637))