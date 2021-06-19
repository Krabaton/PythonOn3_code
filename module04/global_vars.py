count: int = 0


def foo():
    global count
    count += 1


def baz():
    global count
    count += 1


baz()
foo()
print(count)
