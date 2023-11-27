from pathlib import Path

try:
    print('Enter your name:')
    x = input()
    path10_4 = Path('guest.txt')
    path10_4.write_text(x)
except Path.error as Error:
    print(Error)