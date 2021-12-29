a = [0] * 100
x = [0] * 100

for i in range(0, 100):
    a[i] = int(input(" input a number : "))
n = 0
for i in range(99, 0, -1):
    x[i] = a[n]
    n = n + 1
for i in range(0, 100):
    print(x[i])
