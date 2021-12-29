start = int(input("input start : "))
end = int(input("input end : "))
lst = []

for i in range(start, end + 1):
    if i % 9 == 0 and i % 4 != 0:
        lst.append(i)

for i in range(0, len(lst)):
    print(lst[i], end=",")
