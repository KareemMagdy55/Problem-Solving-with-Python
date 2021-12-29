txt = input("Please type a word to Reverse it: ")

print(txt[::-1])

if txt[::-1] == txt:

    print("It's a palindrome")

else:

    print("it's not a palindrome")
