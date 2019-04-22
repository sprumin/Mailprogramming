# 정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오.
# 단, 시간복잡도는 O(n) 이여야 합니다.

# O(n) 포기 ㅈㅈ

from itertools import combinations


def _combination(numbers):
    c_nums = list()
    max_num = sum(numbers)

    for i in range(1, len(numbers) + 1):
        for num_tup in list(combinations(numbers, i)):
            c_nums.append(sum(num_tup))

    for i in range(1, max_num + 1):
        if i not in c_nums:
            return i
            break


def main():
    numbers = list(map(int, input().split()))

    print(_combination(numbers))


if __name__ == "__main__":
    main()
