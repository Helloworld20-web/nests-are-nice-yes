print("Please type in a character")
letterordigit = input()

if(letterordigit >= "A" and letterordigit <= "Z" or letterordigit >= "a" and letterordigit <= "z"):
    print("Your character is a letter")

elif(letterordigit >= "0" and letterordigit <= "9"):
    print("Your character is a digit")

else:
    print("Your character", letterordigit, " is a special character")