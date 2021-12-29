x = input()
digit = 0
letter = 0
for ch in x:
    if ch.isdigit():
        digit = digit + 1
    elif ch.isalpha():
        letter = letter + 1
print("Letters:", letter)
print("Digits:", digit)
