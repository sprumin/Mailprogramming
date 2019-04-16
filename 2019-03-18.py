"""
정렬(sort)된 정수 배열과 정수 n이 주어지면, 배열안에 n이 있는지 체크하시오. 시간복잡도를 최대한 최적화하시오.
"""


def find_num(_list, num):
    if num in _list:
        return True
    else:
        return False


def main():
    _list = list(map(int, input().split()))
    num = int(input())
    print(find_num(_list, num))


if __name__ == "__main__":
    main()
