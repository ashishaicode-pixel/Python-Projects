import random
# !!! There are two option one is for loop and one is while loop if you want to try only copy from line-> 30 to 55!!!
secret_no = random.randint(1, 50)

print("Welcome to the number guessing game. we have a no. that need to be guessed. You have 10 chance.")

print("The secret no is between 1 to 50.")
is_guess_correct = False

for i in range(10, 0, -1):
    print(f"You have {i} attempts left.")
    user = int(input("Enter Your guess (1 to 50):"))
    if secret_no == user:
        print("Congrats Your guess is correct! \n")
        is_guess_correct = True
        break
    elif secret_no < user:
        print("Your guess is wrong! Try lower no.")
    elif secret_no > user:
        print("Your guess is wrong! Try higher no.")

if is_guess_correct == False:
    print("\n\nBad luck! Better luck next time!!")
print(f"The secret no. was {secret_no}. Game Over!!!")


# import random
# secret_no=random.randint(1,50)
# print("Welcome to the number guessing game. we have a no. that need to be guessed. You have 10 chance.")

# print("The secret no is between 1 to 50.")
# num=1
# attempts=10
# while num<=10:
#     print(f"You have {attempts} attempts left.")
#     user=int(input("Enter Your guess (1 to 50):"))
#     if secret_no==user:
#         print("Congrats Your guess is correct! \n")
#         # is_guess_correct=True
#         break
#     elif secret_no<user:
#         print("Your guess is wrong! Try lower no.")
#     elif secret_no>user:
#         print("Your guess is wrong! Try higher no.")
#     num+=1
#     attempts-=1

# if num==11:
#     print("\n\nBad luck! Better luck next time!!")
# print(f"The secret no. was {secret_no}. Game Over!!!")
