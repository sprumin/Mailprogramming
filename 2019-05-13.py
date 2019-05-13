# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.


def find_num(num_list, commands):
    result = list()

    for command in commands:
        start = command[0] - 1
        end = command[1]
        find = command[2] - 1

        slice_list = sorted(num_list[start:end])

        result.append(slice_list[find])

    return result


def main():
    num_list = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(find_num(num_list, commands))


if __name__ == "__main__":
    main()
