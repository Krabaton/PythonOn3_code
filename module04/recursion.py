def our_pow(base, exp):
    """
    :param base: основание степени
    :param exp:  степень должна быть больше или равна нулю
    :return: результат base**exp
    """
    # print(base, exp)
    if exp <= 0:
        return 1
    if exp == 1:
        return base
    return base * our_pow(base, exp - 1)


print(__name__)

if __name__ == '__main__':
    print(our_pow(2, 3))
    help(our_pow)
    print(our_pow.__doc__)
    #  2 * 2 * 2
