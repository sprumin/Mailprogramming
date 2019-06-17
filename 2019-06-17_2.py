def top(heights):
    result = list()
    heights.reverse()

    for i in range(len(heights)):
        check = False
        for j in range(i, len(heights)):
            if heights[j] > heights[i]:
                result.insert(0, len(heights) - j)
                check = True
                break

        if not check:
            result.insert(0, 0)

    return result


def main():
    print(top([6, 9, 5, 7, 4]))
    print(top([3, 9, 9, 3, 5, 7, 2]))


if __name__ == "__main__":
    main()
