def hotel(H, W, N):
    floor = H if (N % H == 0) else N % H
    room = (N // H) if (N % H == 0) else (N // H) + 1

    if room < 10:
        room = f"0{room}"

    return str(floor) + str(room)


def main():
    T = int(input())

    for _ in range(T):
        H, W, N = map(int, input().split())
        print(hotel(H, W, N))


if __name__ == "__main__":
    main()
