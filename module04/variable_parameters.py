def first(size, *args):
    print(list(args))
    return size, args


print(first(5, 4, 5, 'Hi'))


def second(size, **kwargs):
    print(kwargs)
    return size, kwargs


print(second(5, a=4, b=5))


def third(size, *args, **kwargs):
    print(list(args))
    print(kwargs)
    return size, len(args), len(kwargs)


print(third(5, 4, 5, 'Hi', a=4, b=5))
