import random

current_number = random.randrange(100, 999, 1)
guess_number = 0
print(current_number)
while True:
    guess_number = int(input("input an number:"))
    if current_number != guess_number:
        if current_number > guess_number:
            print("error number and more bigger")
        elif current_number < guess_number:
            print("error number and more smaller")
    elif current_number == guess_number:
        print("you got it!!")
        break
