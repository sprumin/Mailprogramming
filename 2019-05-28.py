def skill_tree(skill, skill_trees):
    result = 0

    for row in skill_trees:
        temp = skill
        valid = True

        for char in row:
            if char in temp:
                if char == temp[0]:
                    temp = temp[1: len(temp)]
                else:
                    valid = False

        if valid:
            result += 1

    return result


def main():
    skill_tree(input(), list(map(str, input())))


if __name__ == "__main__":
    main()
