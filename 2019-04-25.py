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
