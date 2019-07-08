def break_even_point(A, B, C):
    return (A // (C - B)) + 1 if B < C else -1


def main():
    A, B, C = map(int, input().split())

    print(break_even_point(A, B, C))


if __name__ == "__main__":
    main()
