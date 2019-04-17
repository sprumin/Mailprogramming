"""
    "./" 과 "../" 이 포함된 파일 경로를 "./"과 "../" 이 없는 유닉스 파일 경로로 바꾸시오.
    "./" 는 현재의 위치를 뜻하고, "../" 는 상위 디렉토리를 뜻합니다.
    input : "/usr/bin/../" output: "/usr/"
"""


def file_path(path):
    s_path = path.split("/")
    path_list = [".", ".."]
    result = "/"

    for row in s_path[1:-1]:
        if row not in path_list:
            result += row + "/"
        elif row == path_list[1]:
            temp = "/"

            for add in result.split("/")[1:-2]:
                temp += add + "/"

            result = temp

    return result


def main():
    path = input()
    print(file_path(path))


if __name__ == "__main__":
    main()
