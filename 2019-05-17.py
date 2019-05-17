import string


def over_index(list_len, find_text, n):
    if list_len - find_text - n > 0:
        return find_text + n
    else:
        return abs(list_len - find_text - n + 1)


def cyzer_pwd(s, n):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    result = ""

    for text in s:
        if text == " ":
            result += text
        elif text in lowers:
            indexs = over_index(len(lowers) - 1, lowers.find(text), n)
            result += lowers[indexs]
        else:
            indexs = over_index(len(uppers) - 1, uppers.find(text), n)
            result += uppers[indexs]

    return result


def main():
    s = input()
    n = int(input())

    print(cyzer_pwd(s, n))


if __name__ == "__main__":
    main()
