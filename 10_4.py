from pathlib import Pathsam

print('Enter your name:')
x = input()
path10_4 = Path('guest.txt')
path10_4.write_text(x)