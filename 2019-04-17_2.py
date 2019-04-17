"""
한 쌍의 괄호 기호로 된 "()" 문자열을 VPS 라고하는데. 문자열을 입력받아 VPS 인지 아닌지 판단하여 YES/NO 로 출력하시오.
"(())()" 는 YES 이지만 "(()))" 는 NO 이다.
"""

"""
이것도 잘돌아가는데...쩝... 백준한테 입구컷당함
def vps(_str):
    if _str[0] == ")":
        print("NO")

    if _str.count("(") == _str.count(")"):
        print("YES")
    else:
        print("NO")


def main():
    num = int(input())

    for i in range(num):
        vps(input())
"""


def vps(_str):
    _list = list()
    check = 1

    if _str[0] == ")":
        check = 0
    else:
        for char in _str:
            if char == "(":
                _list.append(char)
            elif char == ")":
                if len(_list) == 0:
                    check = 0
                    break
                else:
                    _list.pop()

        if len(_list) != 0:
            check = 0

    if check == 0:
        print("NO")
    else:
        print("YES")


def main():
    num = int(input())

    for i in range(num):
        vps(input())


if __name__ == "__main__":
    main()
