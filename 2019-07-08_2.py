def alpha_centauri(x, y):
    num = y - x
    k = 1
    p = 1

    while num > 0:
        num -= k
        k += 1

        if num >= p:
            num -= p
            p += 1

    return k + p - 2


def main():
    T = int(input())

    for _ in range(T):
        x, y = map(int, input().split())
        print(alpha_centauri(x, y))


if __name__ == "__main__":
    main()
