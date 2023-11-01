print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_option = input(
    "You are at a crossroad. Where do you want to go? Type 'left' or 'right' \n"
).lower()
if first_option == "left":
    second_option = input(
        "You have reached a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across the lake. \n"
    ).lower()
    if second_option == "wait":
        third_option = input(
            "You arrived at the island. There are three doors. Type 'red' to choose the red one, 'yellow' to choose the yellow one or 'blue' to choose the blue one. \n'"
        ).lower()
        if third_option == "yellow":
            print("You found a room full of treasure! You win!")
        elif third_option == "blue":
            print("You entered a room full of beasts! Game over.")
        elif third_option == "red":
            print(
                "The room is pitch black. You fall into a bottomless pit. Game over."
            )
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You were attacked the lochness monster. Game over.")
else:
    print("You got lost in the woods. Game over.")
