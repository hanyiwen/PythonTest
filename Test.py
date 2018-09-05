from functools import reduce


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3,
                '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


b = list(map(char2num, '1467'))
a = str2int('123567')

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

nums = ['flower', 'flow', 'flight']
for i in zip(*nums):
    print(i)

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(map(lambda x_y: x_y[0] * x_y[1], [(1, 2), (3, 4)])))

print("debug")
