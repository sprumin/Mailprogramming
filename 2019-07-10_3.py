def word_sort(words):
    for row in words:
        words[row].sort()

    return sorted(words.items())


def main():
    N = int(input())
    words = dict()
    valid = list()

    for _ in range(N):
        word = input()

        if word not in valid:
            if words.get(len(word)):
                words[len(word)].append(word)
            else:
                words[len(word)] = [word]

            valid.append(word)

    result = word_sort(words)

    for key in result:
        for value in key[1]:
            print(value)


if __name__ == "__main__":
    main()
