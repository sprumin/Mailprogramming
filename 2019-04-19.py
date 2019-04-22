# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.


def peoples(floor, room):
    apart = [list() for i in range(floor + 1)]
    apart[0] = [i for i in range(1, room + 1)]

    for i in range(1, floor + 1):
        for j in range(room):
            count = 0
            for k in range(j + 1):
                count += apart[i - 1][k]

            apart[i].append(count)

    print(apart[floor][room - 1])


def main():
    t = int(input())

    for i in range(t):
        floor = int(input())
        room = int(input())

        peoples(floor, room)


if __name__ == "__main__":
    main()
