from pathlib import Path
import sys

p = Path(sys.argv[1])


def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            print(f"This is folder - {el.name}")
        else:
            print(f"This is file - {el.name}")


def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir():
            parse_folder_recursion(element)
        else:
            print(f"This is file - {element}")


parse_folder_recursion(p)
