# 입력 순서 학생 수, 체육복을 잃어버린 학생번호, 여벌 체육복이 있는 학생번호.
# 체육복은 자기 번호 -1 / +1 인 학생들한테만 빌려줄수 있고 인당 여벌 체육복은 1벌씩이라고 가정한다.


def take_a_class(n, lost, reserve):
    students = [i for i in range(1, n + 1)]

    for student in lost:
        if student - 1 in reserve:
            reserve.remove(student - 1)
        elif student + 1 in reserve:
            reserve.remove(student + 1)
        else:
            students.remove(student)

    return len(students)


def main():
    students_count = int(input())
    lost_students = list(map(int, input().split()))
    reserve_students = list(map(int, input().split()))

    print(take_a_class(students_count, lost_students, reserve_students))


if __name__ == "__main__":
    main()
