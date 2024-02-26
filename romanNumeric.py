from itertools import pairwise, groupby
import math
import json
import os

rom = {
    'I': 1, 'V': 5,
    'X': 10, 'L': 50,
    'C': 100, 'D': 500,
    'M': 1000, "H": 5000, "хуй": 887
}
rom = dict(sorted(rom.items(), key=lambda c: c[1]))

# division = 2
# for (k1, v1), (k2, v2) in pairwise(rom.items()):
#     division = max(division, math.ceil(v2 / v1 / 2))
division = 3


# old code
def croman(number):
    total = []
    for i in range(len(str(number))):

        thenum = number % 10 ** (i + 1) - number % 10 ** i
        temp = 'I' * thenum
        for k in range(1, 7):
            num2 = list(rom.items())[k][1]
            char2 = list(rom.items())[k][0]
            num1 = list(rom.items())[k - 1][1]
            char1 = list(rom.items())[k - 1][0]
            if temp.count(char1) >= num2 // num1:
                temp = temp.replace(char1 * (num2 // num1), char2)
        # print(temp, " tempold")
        for k in range(0, 5):
            char = list(rom.items())[k][0]
            temps = 0
            if temp.count(char) >= 4:
                for j in range(7):
                    temps += temp.count(list(rom.items())[j][0]) * list(rom.items())[j][1]
                min_ = float('inf')
                for j in range(6, -1, -1):
                    if min_ > list(rom.items())[j][1] - temps and list(rom.items())[j][1] > temps:
                        nchar = list(rom.items())[j][0]
                        min_ = list(rom.items())[j][1] - temps
                temp = char + nchar or ''
                break
        # print(temp, i, '3')
        total.append(temp)
    return ''.join(total[::-1])


# new code - better functionality
def arabic_to_roman(number):
    roman_keys = tuple(rom)
    t = len(roman_keys) - 1
    temp = []
    digit = number
    while digit > 0 and t >= 0:
        k = roman_keys[t]
        v = rom[k]
        if v <= digit:
            temp.extend([k] * (digit // v))
            digit %= v
        t -= 1
    st_index = 0
    print(temp)
    for char, char_count in ((label, sum(1 for _ in group)) for label, group in groupby(temp)):
        diff = 0
        if char_count > division:
            _min = char_count * rom[char]
            if flag := (st_index > 0):
                _min2 = char_count * rom[char] + rom[temp[st_index - 1]]
                temps2 = _min2
            temps = _min
            temp_reduced = temp[:st_index]
            temp_reduced_n = temp[st_index + char_count:]
            nchar: str = ''
            nchar2: str = ''
            for _key, value in reversed(rom.items()):
                if _min > (value - temps) and value > temps:
                    nchar = _key
                    _min = (value - temps)
                if flag and (_min2 > (value - temps2) and value > temps2):
                    nchar2 = _key
                    _min2 = (value - temps2)
            diff = len(temp)
            if nchar:
                temp = temp_reduced + ([char] * (_min // rom[char]) + [nchar]) + temp_reduced_n
            if nchar2:
                temp2 = temp_reduced[:-1] + ([char] * (_min2 // rom[char]) + [nchar2]) + temp_reduced_n
                temp = min(temp, temp2, key=len)
            diff -= len(temp)
        st_index += char_count - diff
    return ''.join(temp)


def carab(numro):
    num = 0
    numro = list(numro)
    while numro:
        if len(numro) > 1 and rom[numro[0]] < rom[numro[1]]:
            num += rom[numro.pop(1)] - rom[numro.pop(0)]
        else:
            num += rom[numro.pop(0)]
    return num


def main():
    global rom
    print(f"""Римские цифры - {rom}        
    1. Перевести число в Римское
    2. Перевести Римское число в арабское
    3. Импорт правил из Roman_ruleSet.json
    4. Выход""")
    while True:
        try:
            match input():
                case "1":
                    num = int(input("Введи число: "))
                    print(arabic_to_roman(num))
                case "2":
                    num = input("Введи римское число: ")
                    print(carab(num))
                case "3":
                    if "Roman_ruleSet.json" not in os.listdir():
                        with open("Roman_ruleSet.json", "a") as f:
                            json.dump(rom, f)
                    with open("Roman_ruleSet.json") as f:
                        rom = json.load(f)
                    print(rom)
                case "4":
                    break
                case _:
                    print("Не верная опция.")
        except Exception:
            print("Ошибка")


if __name__ == '__main__':
    main()
