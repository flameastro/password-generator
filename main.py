import secrets


def is_valid(number: int, minimum: int, maximum: int):
    """Returns True if the number is in the correct range between minimum and maximum and False otherwise"""

    return number >= minimum and number <= maximum


def save_passwords(save: bool, password: str):
    """Allow the program to save the generated password if save is True"""

    if save:
        FILE = "passwords.txt"

        with open(FILE, "a+", encoding="utf-8") as f:
            f.write(f"{password}\n\n")


def allowed_characters(numbers: bool = True, special: bool = True):
    """Returns the allowed characters to generate the final password"""

    UPPERCASE = "abcdefghijklmnopqrstuvwxyz"
    LOWERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    SPECIALS = "!@#$%^&*()-_=+?"

    characters = UPPERCASE + LOWERCASE
    if numbers:
        characters += NUMBERS
    if special:
        characters += SPECIALS

    return characters


def generate_encrypt_password(length: int, characters: str):
    """Generate the password with secrets library"""

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    """Execute the all the functions and make it interactive to the user :)"""

    length = int(input("Enter the password length (between 1 and 256): "))

    if is_valid(length, 6, 256):
        numbers = bool(input("Allow numbers? (Type any key and press ENTER for yes, or leave blank): "))
        special = bool(input("Allow special characters? Example: !@#$%^&*()-_=+? (Type any key and press ENTER if yes, or leave blank if no): "))

        characters = allowed_characters(numbers, special)

        quantity = int(input(f"How many passwords do you want to generate with a length of {length} characters? (Between 1 and 100): "))
        if is_valid(quantity, 1, 100):
            save = bool(f"Do you want to save the {quantity} generated passwords to a file named senhas.txt? (Type any key and press ENTER to save, or leave blank if not): ")

            for _ in range(quantity):
                password = generate_encrypt_password(length, characters)
                print(password)

                save_passwords(save, password)
    else:
        print("The password length must be between 6 and 256 characters. Please try again.")

main()
