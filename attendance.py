medical = input("Did the student have any medical problems lately? Y or N: ")

if(medical == 'N' or medical == 'n'):
    print("The student is allowed")

elif(medical == 'Y' or medical == 'y'):
    attend = int(input("Enter the attendance score of the student: "))
    if(attend >= 75):
        print("The student is allowed")
    
    else:
        print("The student is not allowed")

else:
    print("What?")