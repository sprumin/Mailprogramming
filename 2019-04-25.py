# 문자열을 입력받아 가장 많이 포함되어있는 알파벳을 출력하시오.
# 여러개일 경우 알파벳 순서대로 출력하시오.

from string import ascii_lowercase

import sys


def alphabet_count(_str):
    _str = _str.replace(" ", "")
    alphabet_list = list(ascii_lowercase)
    result_dict = dict()
    _max = 0

    for alphabet in alphabet_list:
        count = _str.count(alphabet)

        if _max < count:
            _max = count

        try:
            result_dict[count].append(alphabet)
        except:
            result_dict[count] = [alphabet]

    return result_dict[_max]


def main():
    _str = ""
    while True:
        data = sys.stdin.readline()

        if not data:
            break

        _str += data

    print("".join(alphabet_count(_str)))


if __name__ == "__main__":
    main()
