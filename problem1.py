import random

namesList = ["Ahmed", "Adham", "Mohamed", "Mamdouh", "Ali", "Atef"]
emptyNamesList = []

def pickWinner(names):
    if names == 0:
        print("List is empty")
    print(f"Congratulations {random.choice(names)}! You've won!")

pickWinner(namesList)