def _pow(n):
    for i in range(n + 1):
        num = pow(i, 2)
        
        if num == n:
            return pow(i + 1, 2)
        elif num > n:
            return - 1


def main():
 	print(_pow(int(input())))


if __name__ == "__main__":
	main()