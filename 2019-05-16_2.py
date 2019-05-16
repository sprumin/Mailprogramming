def calander(month, day):
    day_of_the_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(months[0:month - 1]) + day - 1

    return day_of_the_week[days % 7]


def main():
    md = list(map(int, input().split()))
    print(calander(md[0], md[1]))


if __name__ == "__main__":
    main()
