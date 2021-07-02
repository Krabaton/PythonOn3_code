import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print('Не передано имя файла для прочтения')
    quit()

try:
    inf = open(sys.argv[1], "r", encoding="utf-8")
    try:
        line = inf.readline()
        count = 0
        while count < NUM_LINES and line != "":
            line = line.rstrip()
            count += 1
            print(line)
            line = inf.readline()
    except OSError:
        print('Ошибка чтения файла')
    finally:
        inf.close()
except OSError:
    print('Ошибка доступа к файлу')