def caesar_cypher():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    word = input('please input a word : ').lower().replace(" ", "")
    choice = input('if you wanna decrypt the word enter (D) \nif you wanna encrypt the word enter (E)'
                   ' \nif you wanna both enter (B) \n: ').lower()

    def caesar_cypher_encrypt():
        for char in word:
            if char.isalpha():
                if char != 'z':
                    x = ord(char) - ord('a')
                    # because ord('a') = 97 and ord(char) - ord('a') will get the char index in alphabet lists

                    print(alphabet[x + 1], end="")  # adding one to get the next char to print it

                else:
                    print('a', end="")

            else:
                print(char, end="")

    def caesar_cypher_decrypt():
        for char in word:
            if char.isalpha():
                if char != 'a':
                    x = ord(char) - ord('a')
                    # because ord('a') = 97 and ord(char) - ord('a') will get the char index in alphabet lists

                    print(alphabet[x - 1], end="")  # adding one to get the next char to print it

                else:
                    print('z', end="")
            else:
                print(char, end="")

    if choice == 'd':
        print('Decryption for the word is : ', end='')
        caesar_cypher_decrypt()
    elif choice == 'e':
        print('Encryption for the word is : ', end='')
        caesar_cypher_encrypt()
    elif choice == 'b':
        print('Decryption for the word is : ', end='')
        caesar_cypher_decrypt()
        print('\nEncryption for the word is : ', end='')
        caesar_cypher_encrypt()
    else:
        caesar_cypher()


caesar_cypher()
