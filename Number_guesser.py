import random

upper_limit = input("Enter Upper limit ")

if upper_limit.isdigit():
    upper_limit = int(upper_limit)

    if upper_limit <= 0:
        print("Enter number greater than 0")
        quit()
else:
    print("Enter a valid number")
    quit()

random_number = random.randint(0, upper_limit)

guesses=0

while True:
    guesses+=1
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Enter a valid number")
        continue

    if user_guess == random_number:
        print("YAY! you got it right")
        break
    else:
        if user_guess > random_number:
            print("You were above the number")
        else:
            print("You were below the number")

print("You got it in", guesses, "guesses")