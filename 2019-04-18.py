# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.


def group_word(word):
    check = list()

    for i in range(0, len(word)):
        if i == 0:
            check.append(word[i])
        else:
            if word[i] in check:
                if word[i] != word[i - 1]:
                    return False
            else:
                check.append(word[i])

    return True


def main():
    t = int(input())
    count = 0

    for i in range(t):
        if group_word(input()):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
