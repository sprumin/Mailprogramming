# 가운데 글자 가져오기
# 길이가 짝수라면 가운데 두글자를 가져오면 됨


def word_center(word):
    if len(word) == 1:
        return word
    elif len(word) % 2 == 0:
        return word[int(len(word) / 2) - 1:int(len(word) / 2) + 1]
    else:
        return word[int(len(word) / 2)]


def main():
    print(word_center(input()))


if __name__ == "__main__":
    main()
