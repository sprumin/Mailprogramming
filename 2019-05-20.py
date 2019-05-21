# 이진 트리가 주어지면 루트 노드부터 레벨별로 프린트 하시오.
# 프린트 방식은 홀수 레벨은 왼쪽에서 오른쪽으로, 짝수 레벨은 오른쪽에서 왼쪽으로 프린트 하시오. 루트노드는 레벨 1입니다.


def binary_print(binarys):
    result = f"{binarys[0][0]}"

    for i in range(1, len(binarys)):
        result += ", "
        if i % 2 == 0:
            result += ", ".join(binarys[i])
        else:
            result += ", ".join(binarys[i][::-1])

    return result


def main():
    binarys = list()

    while True:
        binary = list(map(str, input().split()))

        if not binary:
            break

        binarys.append(binary)

    print(binary_print(binarys))

if __name__ == "__main__":
    main()
