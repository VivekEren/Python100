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

walk_direction = input('Choose a direction in which you are walking, type "left" if you want to go left type "right" if you want to go right\n')

walk_direction = walk_direction.lower()

if walk_direction == "right":
  print("You fell from cliff. Game Over.")
else:
  swim_or_boat = input('You encountered a sea. Do you want to wait for a boat or you want to swim, type "wait" to wait for a boat and type "swim" to swim\n')
  swim_or_boat = swim_or_boat.lower()
  if swim_or_boat == "swim":
    print("You encountered sharks. Game Over")
  else:
    door = input('There are doors of three colors, choose one of them. Type "Red" for red door, "yellow" for yellow door and type "blue" for blue door\n')
    door = door.lower()
    if door == "red":
      print("You entered a room of fire. Game Over.")
    elif door=="blue":
      print("You enetered a rood of tigers. Game Over")
    else:
      print("You entered a room of people. You Win.")
