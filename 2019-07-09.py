def snail(A, B, V):
    return (V - B - 1) // (A - B) + 1


def main():
    A, B, V = map(int, input().split())
    print(snail(A, B, V))


if __name__ == "__main__":
    main()
