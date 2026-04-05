password = input("Enter your password: ")

length = len(password)

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password 💪")
elif length >= 6:
    print("Medium Password 🙂")
else:
    print("Weak Password 😢")
