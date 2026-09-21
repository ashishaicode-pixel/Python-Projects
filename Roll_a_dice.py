import random
print("Wellcom to the game of Roll a Dice ->")
while True:
    user = input("Press 'Enter' to continue or 'q' to Quit:")
    user = user.strip()
    if user == 'q':
        print("Thank You, Well Played Bye!!!")
        break
    elif user == '':
        number = random.randint(1, 6)
        print(f"Your no. is {number}")
    else:
        print("Invalid Input!!!")

print("GAME OVER")
