lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("input element: "))
    lst.append(ele)

x = (len(lst) - 7)
for i in range(0, len(lst)):
    if i < x+1:
        del lst[i + 1]
print(lst)
