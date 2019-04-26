# 이 프린터는 규칙이 있습니다.
# 가장 앞에있는 문서의 중요도를 체크하고 프린터 큐 안에 더 높은 중요도를 가진 문서가 있는지 체크합니다
# 없다면 문서를 출력하고 있다면 해당 문서를 큐 가장 뒤쪽으로 옮깁니다.
# 문서갯수, 찾고자하는 문서의 위치, 각 문서의 중요도를 입력받아 찾고자하는 문서가 몇번째로 출력되는지 출력하시오.


def printer_queue(doc_count, doc_index, docs):
    doc_check = ["True" if i == doc_index else "False" for i in range(len(docs))]
    count = 0

    while True:
        if docs[0] == max(docs):
            count += 1

            if doc_check[0] == "True":
                return count

            docs.remove(docs[0])
            doc_check.remove(doc_check[0])
        else:
            temp_num = docs[0]
            temp_check = doc_check[0]

            docs.remove(docs[0])
            doc_check.remove(doc_check[0])

            docs.append(temp_num)
            doc_check.append(temp_check)


def main():
    num = int(input())

    for _ in range(num):
        doc_count, doc_index = map(int, input().split())
        docs = list(map(int, input().split()))

        print(printer_queue(doc_count, doc_index, docs))


if __name__ == "__main__":
    main()
