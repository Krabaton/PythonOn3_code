import time
from multiprocessing import Manager, Process


def factorize_number(number, dict):
    result_number = []
    for i in range(1, number + 1):
        if number % i == 0:
            result_number.append(i)
    dict[number] = result_number


def factorize(numbers, m):
    processes = []
    for number in numbers:
        pr = Process(target=factorize_number, args=(number, m))
        pr.start()
        processes.append(pr)
    for p in processes:
        p.join()
    return m


if __name__ == '__main__':
    with Manager() as manager:
        start = time.time()
        m = manager.dict()
        result = factorize((128, 255, 99999, 10651060), m)
        end = time.time() - start
        print(end)
        a = result[128]
        b = result[255]
        c = result[99999]
        d = result[10651060]
        assert a == [1, 2, 4, 8, 16, 32, 64, 128]
        assert b == [1, 3, 5, 15, 17, 51, 85, 255]
        assert c == [1, 3, 9, 41, 123, 271,
                     369, 813, 2439, 11111, 33333, 99999]
        assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                     380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
