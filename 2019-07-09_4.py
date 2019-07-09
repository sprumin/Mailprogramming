def sosu(M, N):
    result = list()

    for i in range(M, N + 1):
        temp = list()

        for j in range(1, i + 1):
            if i % j == 0:
                temp.append(j)

        if len(temp) == 2:
            result.append(i)

    if result:
        return sum(result), min(result)
    else:
        return -1


def main():
    M = int(input())
    N = int(input())

    result = sosu(M, N)

    if result == -1:
        print(-1)
    else:
        print(result[0])
        print(result[1])

if __name__ == "__main__":
    main()
