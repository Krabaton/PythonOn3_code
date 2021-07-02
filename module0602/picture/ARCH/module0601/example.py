from pathlib import Path
import os

cur_path = Path()
print(cur_path.cwd())

folder = cur_path / "bin" / "utils" / "paint.example.jpg"
# print(folder)
# print(cur_path.joinpath("bin", "utils", "paint.example.jpg"))
# print(folder.parts)
# print(folder.name)
# print(folder.parent)
# print(folder.suffix)
# print(folder.suffixes)

# print(os.name)  # posix nt

# list_dir = Path(".")
#
# for el in list_dir.iterdir():
#     if el.is_dir():
#         print(f"{el.name} - это директория")
#     if el.is_file():
#         print(f"{el.name} - это файл")

# not_exist = Path('head.py')
# print(not_exist.exists())

# *.py  **/*.py **/**/*.py

# for el in list_dir.glob("*.py"):
#     print(el)

try:
    tmp = Path("test.txt")
    tmp.unlink()
except FileNotFoundError:
    pass

new_dir = Path("Test")
if not new_dir.exists():
    new_dir.mkdir()

new_dir = Path("Test/temp/asd/baz")
new_dir.mkdir(parents=True, exist_ok=True)
