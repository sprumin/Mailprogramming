# 사람들의 몸무게와 구명보트의 몸무게 한계치가 주어졌을때 사람들을 옮기기위해 몇대의 보트가 필요한지 구하시오.


def solution(people, limit):
    people.sort(reverse=True)
    boats = 0
    temp_limit = limit

    while len(people) > 0:
        if temp_limit - people[0] >= 0:
            temp_limit -= people[0]
            people.remove(people[0])

            if temp_limit in people:
                people.remove(temp_limit)
                boats += 1
            else:
                for p in people:
                    if temp_limit - p >= 0:
                        temp_limit -= p
                        people.remove(p)
                boats += 1

            temp_limit = limit

    return boats


def main():
    solution1 = [70, 50, 80, 50]
    solution2 = [70, 80, 50]
    limit = 100

    print(solution(solution1, limit))
    print(solution(solution2, limit))


if __name__ == "__main__":
    main()
