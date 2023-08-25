import random
import string

# SETTINGS FOR THE PASSWORD GENERATOR
length_of_word = 0
has_numbers = True
has_special_characters = False

# CONSTANTS FOR THE PASSWORD
CHARACTERS = string.ascii_letters
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation


# SETTING THE USER PREFERENCES FOR THE SETTING
def set_settings():
    global length_of_word
    global has_numbers
    global has_special_characters

    while True:
        length_of_word = str(input("Enter the length for your password (or press enter for a random one (6 - 256)): "))

        if length_of_word == "":
            length_of_word = random.randrange(6, 257)
        else:
            try:
                length_of_word = int(length_of_word)
            except:
                print("ERROR! Please try again and enter a number, not a character.")
                continue

        break

    while True:
        has_numbers = input("Would you like to include numbers in your password (y/n)? ").lower()
        if has_numbers != "y" and has_numbers != "n":
            print("ERROR! Please try again and type in either,'y' or 'n for 'yes' or 'no'")
            continue

        has_numbers = True if has_numbers == "y" else False
        break

    while True:
        has_special_characters = input("Would you like to include special characters in your password (y/n)? ").lower()
        if has_special_characters != "y" and has_special_characters != "n":
            print("ERROR! Please try again and type in either, 'y' or 'n' for 'yes' or 'no'")
            continue

        has_special_characters = True if has_special_characters == "y" else False
        break


# GENERATING THE ACTUAL PASSWORD
def generate_password():
    password = ""

    for i in range(0, length_of_word):

        if has_numbers and has_special_characters:
            option = random.randrange(0, 3)
        elif has_numbers or has_special_characters:
            option = random.randrange(0, 2)
        else:
            option = 0

        if option == 0:
            random_char = random.randrange(0, len(CHARACTERS) - 1)
            password += CHARACTERS[random_char]

        elif option == 1:
            if has_numbers:
                random_char = random.randrange(0, len(NUMBERS) - 1)
                password += str(NUMBERS[random_char])
            else:
                random_char = random.randrange(0, len(SPECIAL_CHARACTERS) - 1)
                password += str(SPECIAL_CHARACTERS[random_char])

        elif option == 2 and has_special_characters:
            random_char = random.randrange(0, len(SPECIAL_CHARACTERS) - 1)
            password += SPECIAL_CHARACTERS[random_char]

    return password


# THE MAIN METHOD FOR RUNNING EVERYTHING
def main():
    print("Welcome to the password generator! To generator a password, please fill out the following settings.")
    while(True):
        set_settings()
        while(True):
            print("Here is your password:", generate_password(), end="\n\n")

            prompt = input("Would you like to generate another password (y/n)? ")
            if prompt.lower() == "y":
                prompt = input("Would you like to do it with the same settings (y/n)? ")
                if prompt.lower() == "y":
                    continue

                break
            else:
                print("Thanks for using the password generator!")
                exit()
main()
