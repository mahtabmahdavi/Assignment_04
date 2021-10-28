def mul_table(n, m):
    for i in range(n):
        for j in range (m):
            print((i + 1) * (j + 1), end = "\t")
        print()


n = int(input("Enter a number larger than 0: "))
m = int(input("Enter a number larger than 0: "))

mul_table(n, m)


