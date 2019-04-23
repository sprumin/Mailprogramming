# n 번째 피보나치 수를 구하는 프로그램을 작성하시오.


def fibonacci(n):
    f_list = [0 for i in range(n + 1)]
    f_list[1] = 1

    for i in range(2, n + 1):
        f_list[i] = f_list[i - 1] + f_list[i - 2]

    return f_list[n]


def main():
    print(fibonacci(int(input())))


if __name__ == "__main__":
    main()
