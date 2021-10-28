n = int(input("Enter a number larger than or equal to 0: "))

f0 = 0
f1 = 1

fibo = []

if n == 0:
    fibo.append(f0)

elif n == 1:
    fibo.append(f0)
    fibo.append(f1)

elif n > 1:
    fibo.append(f0)
    fibo.append(f1)
    counter = 2

    while counter <= n:
        fn = f0 + f1
        fibo.append(fn)

        f0 = f1
        f1 = fn
        counter += 1

print("Fibonacci sequence:")
for i in range(len(fibo)):
    print(fibo[i])

