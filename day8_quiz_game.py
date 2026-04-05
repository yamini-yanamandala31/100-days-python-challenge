score = 0

print("Welcome to Quiz Game!")

q1 = input("1. What is the capital of India? ")
if q1.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

q2 = input("2. 5 + 3 = ? ")
if q2 == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

q3 = input("3. Python is a (language/game)? ")
if q3.lower() == "language":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour Score:", score, "/ 3")
