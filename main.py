import secrets


def encrypt_password(length: int = 64, numbers: bool = True, special: bool = True):
    if length < 6 or length > 256:
        return "The password length must be between 6 and 256 characters. Please try again."

    UPPERCASE = "abcdefghijklmnopqrstuvwxyz"
    LOWERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    SPECIALS = "!@#$%^&*()-_=+?"

    characters = UPPERCASE + LOWERCASE
    if numbers:
        characters += NUMBERS
    if special:
        characters += SPECIALS

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password

FILE = "passwords.txt"
length = int(input("Enter the password length (between 1 and 256): "))
numbers = bool(input("Allow numbers? (Type any key and press ENTER for yes, or leave blank)"))
special = bool(input("Allow special characters? Example: !@#$%^&*()-_=+? (Type any key and press ENTER if yes, or leave blank if no)"))
quantity = int(input(f"How many passwords do you want to generate with a length of {length} characters? (Between 1 and 100):"))

if quantity >= 1 and quantity <= 100:
    save = bool(f"Do you want to save the {quantity} generated passwords to a file named senhas.txt? (Type any key and press ENTER to save, or leave blank if not):")

    for _ in range(quantity):
        password = encrypt_password(length, numbers, special)
        print(password)

        if save:
            with open(FILE, "a+", encoding="utf-8") as f:
                f.write(f"{password}\n\n")
