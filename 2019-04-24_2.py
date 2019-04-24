# 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸없이 주어진다.
# 주어지는 글자들을 세로로 읽은 순서대로 출력하세요.


def col_word(word_list, _max):
    result = ""

    for i in range(_max):
        for j in range(5):
            try:
                result += word_list[j][i]
            except:
                pass

    return result


def main():
    _max = -1
    word_list = list()

    for i in range(5):
        word = input()

        if len(word) > _max:
            _max = len(word)

        word_list.append(word)

    print(col_word(word_list, _max))


if __name__ == "__main__":
    main()
