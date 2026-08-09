import secrets


# Todo: add just one function called is_valid_number, that verify if the input number is correct

def is_valid_lenght(length: int):
    return length >= 6 and length <= 256


def is_valid_quantity(quantity: int):
    return quantity >= 1 and quantity <= 100


def save_passwords(password):
    FILE = "passwords.txt"

    with open(FILE, "a+", encoding="utf-8") as f:
        f.write(f"{password}\n\n")


def allowed_characters(numbers: bool = True, special: bool = True):
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
    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password



def main():
    length = int(input("Enter the password length (between 1 and 256): "))

    if is_valid_lenght(length):
        numbers = bool(input("Allow numbers? (Type any key and press ENTER for yes, or leave blank): "))
        special = bool(input("Allow special characters? Example: !@#$%^&*()-_=+? (Type any key and press ENTER if yes, or leave blank if no): "))

        characters = allowed_characters(numbers, special)

        quantity = int(input(f"How many passwords do you want to generate with a length of {length} characters? (Between 1 and 100): "))
        if is_valid_quantity(quantity):
            save = bool(f"Do you want to save the {quantity} generated passwords to a file named senhas.txt? (Type any key and press ENTER to save, or leave blank if not): ")

            for _ in range(quantity):
                password = generate_encrypt_password(length, characters)
                print(password)

                if save:
                    save_passwords(password)
    else:
        print("The password length must be between 6 and 256 characters. Please try again.")


main()
