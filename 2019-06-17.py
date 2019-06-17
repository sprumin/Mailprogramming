# 4의 거듭제곱


def pow_four(num):
    if num < 16:
        return False

    while True:
        num = int(num / 4)

        if num == 4:
            return True
        elif num < 16 or num % 4 != 0:
            return False


def main():
    print(pow_four(int(input())))


if __name__ == "__main__":
    main()
