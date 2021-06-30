from pathlib import Path
folder = Path('Temp')

try:
    with open(folder / "temp.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())
except OSError:
    print('Ошибка доступа к файлу')


try:
    file = open(folder / "temp.txt", "r", encoding="utf-8")
    try:
        while True:
            line = file.readline()
            print(line)
            if not line:
                break
            print(line.rstrip())
    except OSError:
        print("Error IO")
    finally:
        file.close()
except OSError:
    print('Ошибка доступа к файлу')
