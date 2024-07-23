import sys
import os
import re
from collections import Counter
from enum import Enum
from colorama import Fore, Style


class Color(Enum):
    GREY = 0       # Any char not in the wordle
    YELLOW = 1     # Any char which is in the wordle but wrong place
    GREEN = 2      # Any char which is in the wordle and correct place

def guess():
    word = input('Enter next guess e.g. "crane": ').upper()
    if not re.match("^[A-Z]{5}$", word):
        print('Try again, 5-char word only')
        return

    result = input('Enter results e.g. "00120": ')
    if not re.match("^[012]{5}$", result):
        print('Try again, 5-integers only')
        return

    idx = 0
    yellows_tmp = []
    greys_tmp = []
    for ch, r in zip(word, result):

        if Color(int(r)) == Color.GREEN:
            greens[idx] = ch
        elif Color(int(r)) == Color.GREY:
            greys_tmp.append(ch)
        elif Color(int(r)) ==  Color.YELLOW:
            yellows[idx].add(ch)
            yellows_tmp.append(ch)
        else:
            sys.exit(2)
        idx += 1


    # add to greys if they don't exist in the greens
    for g in greys_tmp:
        if g not in greens:
            greys.add(g)
        else:
            junk_greys.add(g)

    update_counter(yellows_tmp)
    suggest()

    print(f'Greys {greys}')
    print(f'Yellows {Style.BRIGHT}{Fore.YELLOW}{yellows}{Fore.BLACK}{Style.NORMAL}')
    print(f'Yellows Counter {Style.BRIGHT}{Fore.YELLOW}{yellows_ctr}{Fore.BLACK}{Style.NORMAL}')
    print(f'Greens {Style.BRIGHT}{Fore.GREEN}{greens}{Fore.BLACK}{Style.NORMAL}')
    print(f'Junk Letter {junk_greys}\n')

def update_counter(yellows_tmp):
    tmp_ctr = Counter(yellows_tmp)
    for letter, count in tmp_ctr.items():
        current = yellows_ctr.get(letter, 0)
        if count > current:
            yellows_ctr[letter] = count

def counter_check(word):
    word_ctr = Counter(word)
    for letter, count in yellows_ctr.items():
        if word_ctr.get(letter, 0) < count:
            return True
    return False

def suggest():
    for word in wl.copy():
        if counter_check(word):
            wl.remove(word)
            continue
        for idx in range(5):
            if (greens[idx] != '_' and word[idx] != greens[idx]) \
                    or (word[idx] in greys | yellows[idx]):
                wl.remove(word)
                break

    print(f'\n\nCHOICES REMAINING = {Fore.RED}{wl}{Fore.BLACK}')

if __name__ == '__main__':

    greens = ['_', '_', '_', '_', '_']
    greys = set()
    yellows = {0: set(),
               1: set(),
               2: set(),
               3: set(),
               4: set()}

    yellows_ctr = Counter()
    junk_greys = set()



    # List of possible words
    wl = []
    path = os.getcwd()
    if not path[path.rfind('\\')+1:] == '02_MISC_II':
        os.chdir('02_MISC_II')
    f = open('word_list.txt', 'r')
    for line in f:
        wl.append(line.upper().rstrip())

    while True:
        guess()
        if len(wl) == 1:
            break

# BUG FIX REQUIRE   ANS=CYNIC  ENTER CIVIL=20020 and deletes CYNIC