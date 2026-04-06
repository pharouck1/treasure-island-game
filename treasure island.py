print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
question_1 = input("Do you wish to find the treasure? Y or N: ").upper()
if question_1 == "Y":
    way = input("Which way is lead to treasure island? L for left or R for right: ").upper()
    if way == "L":
        print("ohh There is a big river here!")
        question_2 = input("Are you going to wait for boat or you will swim? Y for swim or N for wait:  ").upper()
        if question_2 == "N":
            print("waiting...\nThere are three doors in front of you")
            question_3 = input("which door do you choose? B for Blue_Door R for Red_Door or Y for Yellow_Door: ").upper()
            if question_3 == "Y":
                print("Congratulation! You found the treasure!")
            elif question_3 == "B":
                print("You have been killed and eaten by the beast\nGame over!")
            elif question_3 == "R":
                print("You have been burnt by fire\nGame over!")
            else:
                print("Game over!")
        else:
            print("Attacked by trout\nGame over!")
    else:
        print("Fallen into a hole\nGame over!")
else:
    print("Maybe next time")
    exit()



