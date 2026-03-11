#Hangman Game
import random

words = ("apple","orange","banana","coconut","pineapple")

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" O ",
                  "   ",
                  "   "),
               2:(" O ",
                  " | ",
                  "   "),
               3:(" O ",
                  "/| ",
                  "   "),
               4:(" O ",
                  "/|\\"
                  "   "),
               5:(" O ",
                  "/|\\",
                  "/  "),
               6:(" O ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_guesses):
    print("*"*6)
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*"*6)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] *len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    while is_running == True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue

        if guess in guessed_letter:
            print(f"{guess} is alredy in guessed letter")
            continue


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        
        else:
            wrong_guesses += 1

        if"_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win")
            is_running = False
        
        if wrong_guesses == 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose")
            is_running = False


if __name__ == "__main__":
    main()
for line in hangman_art[0]:
    print(line)
