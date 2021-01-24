print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure island")
print("Your mission is to find the treasure")
direction=input("You are at the cross road.Where you want to go? Type 'left' or 'right'.")
if direction.lower()=="left":
    swim_wait=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat.Type 'swim'to swim across.")
    if swim_wait=="wait":
        door=input("Which door ? Type Red,Blue or Yellow.")
        if door.lower()=="yellow":
            print("You win!")
        elif door.lower()=="red":
            print("Burned by fire. Game over!")
        elif door.lower()=="blue":
            print("Eaten by beasts. Game over!")
        else:
            print("Game over!")
    else:
        print("Attacked by trout. Game over!")
else:
    print("You fell into a hole. Game over!")