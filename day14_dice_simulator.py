import random

while True:
    choice = input("Roll the dice? (yes/no): ").lower()

    if choice == "yes":
        dice = random.randint(1, 6)
        print("You got:", dice)
    elif choice == "no":
        print("Game ended 🎲")
        break
    else:
        print("Invalid input")
