import random as rd
import time


def number_guessing_game():
    print("Hadej cislo hra")
    print("cislo medzi 1 a 1000")

    number_to_guess = rd.randint(1, 1000)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("tipni si cislo: "))
        except ValueError:
            print("Napis platne cislo")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Moc male cislo, skus znovu.")
        elif guess > number_to_guess:
            print("Moc velke cislo, skus znovu.")
        else:
            guessed = True
            print(f"Super uhadol si cislo: {number_to_guess} na {attempts} pokusy.")


# Start the game
if __name__ == "__main__":
    number_guessing_game()
