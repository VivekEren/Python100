import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

print("Let's play rock, paper and scissors")

user_choice = int(input("Choose 0 for rock, 1 for paper and 2 for scissors\n"))

computer_choice = random.randint(0,2)

print("Your Choice:")
print(choice[user_choice])
print("Computer Choice:")
print(choice[computer_choice])

if user_choice == 0 and computer_choice == 1:
    print("You Lost")
elif user_choice == 0 and computer_choice == 2:
    print("You Won")
elif user_choice == 1 and computer_choice == 0:
    print("You Won")
elif user_choice == 1 and computer_choice == 2:
    print("You Lost")
elif user_choice == 2 and computer_choice == 0:
    print("You Lost")
elif user_choice == 2 and computer_choice == 1:
    print("You Won")
else:
    print("It's a draw")

