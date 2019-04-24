# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.


def fd(num):
    for i in range(2, num + 1):
        while True:
            if num % i == 0:
                print(i)
                num = num / i
            else:
                break


def main():
    fd(int(input()))


if __name__ == "__main__":
    main()
