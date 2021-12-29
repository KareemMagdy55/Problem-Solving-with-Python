n = int(input("Input the number of terms : "))
d = 3
sum2 = 0
for i in range(0, n):
    sum1 = (-1 / d) + (1 / (d + 2))
    sum2 = sum1 + sum2
    d = d + 4

print((1 + sum2)*4)
