WORDS = {"pair" : 4, "hear" : 4, "chear" : 5,}


def main():
    print("welcome to spelling bee!")
    print("your letters are: a i p c r h g")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word:  ")

        
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! you scored {points} points.")

    print("that the game!")


main()