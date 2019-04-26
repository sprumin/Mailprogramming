# 3개의 컵이있고 1번쨰 컵에 공이 들어가있다.
# x, y를 m번 입력받아 x, y의 서로 위치를 바꾸었을때 최종적으로 공이 들어있는 컵의 번호를 출력하시오.


def find_ball(m):
    cups = [1, 0, 0]

    for i in range(m):
        cup_x, cup_y = input().split()
        cup_x, cup_y = int(cup_x), int(cup_y)

        cups[cup_x - 1], cups[cup_y - 1] = cups[cup_y - 1], cups[cup_x - 1]

    return cups.index(1) + 1


def main():
    print(find_ball(int(input())))


if __name__ == "__main__":
    main()
