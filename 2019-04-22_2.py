# M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
# 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.


def com_square(_min, _max):
    result = list()

    for i in range(_max):
        square = pow(i, 2)

        if square > _max:
            break

        if square >= _min and square <= _max:
            result.append(square)
        else:
            pass

    if result:
        return sum(result), min(result)
    else:
        return -1


def main():
    result = com_square(int(input()), int(input()))

    if result == -1:
        print(result)
    else:
        print(result[0], result[1])


if __name__ == "__main__":
    main()
