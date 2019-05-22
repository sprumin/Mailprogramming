# 1 / 리스트 arr 에 있는 자연수들 중 divisor 로 나누어떨어지는 자연수들만 리스트에담아 오름차순으로 정렬 후 반환하세요.
def divide(arr, divisor):
    if [num for num in arr if num % divisor == 0]:
        return sorted([num for num in arr if num % divisor == 0])
    else:
        return [-1]

# 2 / "수박수박수박수.." 와 같은 규칙을 가진 길이가 n인 문자열을 완성하세요. ex) 길이가 3이면 "수박수" 4면 "수박수박" 을 리턴하면됩니다.
def water_melon(n):
    result = ""

    for i in range(1, n + 1):
        if i % 2 == 0:
            result += "박"
        else:
            result += "수"

    return result

# 3 / 문자열 내림차순으로 배치하기. s는 영문 대소문자로만 구성되어있으면 대문자는 소문자보다 작은것으로 간주됩니다
def desc_str(s):
    return "".join(sorted(s, reverse=True))

# 4 / 이상한 문자 만들기. 문자열 s 는 여러개의 단어로 이루어져있습니다. 각 단어의 짝수 인덱스는 대문자로 홀수 인덱스는 소문자로 변환하여 문자열s를 출력하세요.
def unusual_str(s):
    result = ""
    
    for row in s.split(" "):
        for i in range(len(row)):
            if i % 2 == 0:
                result += row[i].upper()
            else:
                result += row[i].lower()
    
        result += " "
    
    return result[:len(result) - 1]