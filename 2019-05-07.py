# 주어진 정수를 2진법으로 나타내었을때 1의 갯수를 리턴하시오.


def count_one(num):
    return str(bin(num)).count("1")


def main():
    print(count_one(int(input())))


if __name__ == "__main__":
    main()
