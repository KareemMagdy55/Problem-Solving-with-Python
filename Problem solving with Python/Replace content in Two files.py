def files_replace(file1, file2):
    file1 = open(file1, "r+")
    file2 = open(file2, "r+")
    y = file2.read()
    x = file1.read()

    with open("file1.txt", "a") as file1:
        file1.truncate(0)
        file1.write(y)

    with open("file1.txt", "r") as file1:
        print(file1.read())

    with open("file2.txt", "a") as file2:
        file2.truncate(0)
        file2.write(x)

    with open("file2.txt", "r") as file2:
        print(file2.read())

    file1.close()
    file2.close()


files_replace("hello1.txt", "hello2.txt")
