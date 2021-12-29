dec = int(input("Input a decimal number : "))
bin = [0] * 8
if 265 > dec > 0:
    for i in range(0, 8):
        if int(dec) % 2 == 0:
            bin[i] = 0
            dec = dec / 2
        else:
            bin[i] = 1
            dec = dec / 2
    print("The binary equivalent is : " + str(bin[7]) + str(bin[6]) + str(bin[5]) + str(bin[4]) + str(bin[3]) + str(
        bin[2]) + str(bin[1]) + str(bin[0]))
elif dec < 0:
    print("Error (number is negative)")
elif dec > 255:
    print("Error (number is not in 8 bits range)")