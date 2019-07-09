def kaing_calander(M, N, x, y):
    count = 1
    year = [1, 1]

    while year != [M, N]:
        if year[0] < M:
            year[0] = year[0] + 1
        else:
            year[0] = 1

        if year[1] < N:
            year[1] = year[1] + 1
        else:
            year[1] = 1

        count += 1

        if year == [x, y]:
            break

    if year != [x, y]:
        count = -1

    return count


def main():
    T = int(input())

    for _ in range(T):
        M, N, x, y = map(int, input().split())
        print(kaing_calander(M, N, x, y))


if __name__ == "__main__":
    main()
