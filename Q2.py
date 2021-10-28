def print_func(n, m):
    for i in range(n):
        for j in range (m):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("#", end = "")
                else:
                    print("*", end = "")

            else:
                if j % 2 == 0:
                    print("*", end = "")
                else:
                    print("#", end = "")
        print()


n = int(input("Enter a number larger than 0: "))
m = int(input("Enter a number larger than 0: "))

print_func(n, m)