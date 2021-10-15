from pathlib import Path

path_text = Path('Test/my_txt_file.txt')
path_text.write_text('Test dfhfdhf\nSdff')
path_text.write_text('AAAaaaa')
print(path_text.read_text())

path_bytes = Path('Test/my_bin_file.bin')
path_bytes.write_bytes(b'Test dfhfdhf\nSdff')
path_bytes.write_bytes(b'AAAaaaa')
print(path_bytes.read_bytes())