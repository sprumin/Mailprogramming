def location_sort(locations):
    for row in locations:
        locations[row].sort()

    return sorted(locations.items())


def main():
    N = int(input())
    locations = dict()

    for _ in range(N):
        x, y = map(int, input().split())

        if locations.get(x):
            locations[x].append(y)
        else:
            locations[x] = [y]

    result = location_sort(locations)

    for key in result:
        for value in key[1]:
            print(key[0], value)


if __name__ == "__main__":
    main()
