x = int(input("Please Enter a Number :  "))
print("Factors of the number are :")
for i in range(1, x + 1):
    if x % i == 0:
        print(i)
