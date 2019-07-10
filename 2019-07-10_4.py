def old_sort(users):
    return sorted(users.items())


def main():
    N = int(input())
    users = dict()

    for _ in range(N):
        old, user = input().split()
        old = int(old)

        if users.get(old):
            users[old].append(user)
        else:
            users[old] = [user]

    result = old_sort(users)

    for key in result:
        for value in key[1]:
            print(key[0], value)


if __name__ == "__main__":
    main()
