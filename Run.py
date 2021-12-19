from datetime import datetime
import os
import shutil
import sys

SYMBOLS = {
    '0': ( 28,  34,  65,  65,  65,  34,  28),
    '1': ( 16,  48,  80,  16,  16,  16, 124),
    '2': ( 62,  65,   1,  62,  64,  64, 127),
    '3': ( 62,  65,   1,  62,   1,  65,  62),
    '4': ( 64,  66,  66,  66, 127,   2,   2),
    '5': (127,  64,  64, 126,   1,  65,  62),
    '6': ( 62,  65,  64, 126,  65,  65,  62),
    '7': (127,  66,   4,   8,  16,  16,  16),
    '8': ( 62,  65,  65,  62,  65,  65,  62),
    '9': ( 62,  65,  65,  63,   1,  65,  62),
    ':': (  0,  28,  28,   0,  28,  28,   0)
}

WIDTH, HEIGHT = shutil.get_terminal_size()


def show(time, date):
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    print('\n' * (HEIGHT // 2 - 4))
    for row in range(7):
        print(' ' * (WIDTH // 2 - 35), end='')
        for ch in time:
            for i in range(6, -1, -1):
                if SYMBOLS[ch][row] & (2**i):
                    print('#', end='')
                else:
                    print(' ', end='')
            print('  ', end='')
        print()
    print('\n\n', ' ' * (WIDTH // 2 - len(date) // 2), date)


old_time = ''
while True:
    time = datetime.now().strftime('%H:%M:%S')
    date = datetime.now().strftime('%A %d %B, %Y')
    if time != old_time:
        show(time, date)
    old_time = time
