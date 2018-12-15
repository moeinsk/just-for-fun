import random
import sys

javab = True

while javab:
    soal = input("beyne 1 ta 5 ye adad bezan :(baraye khoroj enter bezan:")

    answer = random.randint(1,5)

    if soal == "":
        sys.exit()
    elif answer== 1 :
        print("its good")
    elif answer == 2:
        print("not bad")
    elif answer== 3 :
        print("you have problem")
    elif answer == 4 :
        print("cangrogelation")
    elif answer == 5 :
        print("Fuk you")                        
