import random

number = random.randint(1, 10)
lives = 3

print("You got 3 lives...")

while True:
    usr_inp = int(input("\nEnter in the number > "))

    if usr_inp == number:
        print("Congrats you won!")
        break
    elif usr_inp > number:
        print("Is less than that...")
        lives -= 1
        print(f"You got {lives} lives")

        if lives == 0:
            print("Gameover...")
            print(f"It was {number}")
            break

    elif usr_inp < number:
        print("Is greater than that...")
        lives -= 1
        print(f"You got {lives} lives")

        if lives == 0:
            print("Gameover...")
            print(f"It was {number}")
            break