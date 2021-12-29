a = [0] * 50

for i in range(0, 50, 1):
    a[i] = int(input())
for i in range(0, 50, 2):
    x = a[i]
    y = a[i + 1]
    a[i] = y
    a[i + 1] = x
    print(a[i + 1])
    print(a[i])

