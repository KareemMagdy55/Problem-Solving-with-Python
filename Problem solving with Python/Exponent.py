number = int(input("Please enter the number : "))
exponent = int(input("Please enter the exponent : "))
result = 1
for i in range(0, exponent):
    result = number * result

print("the result is : ", result)
