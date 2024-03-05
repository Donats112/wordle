import sys
import random
from rich import print



"""
looks for all the words in certain file
"""
def read_all_words():

    all_words = []
    if len(sys.argv) > 1:
        word_len = sys.argv[1]

        if word_len == str(5):
            with open("collections/5.txt") as words:
                all_words=words.read().split("\n")
        elif word_len == str(6):
            with open("collections/6.txt") as words:
                all_words = words.read().split("\n")
                
        elif word_len == str(7):
            with open("collections/7.txt") as words:
                all_words = words.read().split("\n")
                
        elif word_len == str(8):
            with open("collections/8.txt") as words:
                all_words = words.read().split("\n")
                
        else:
            raise ValueError("kys")
    else:
        raise ValueError("kys")

    return all_words

"""
selects single random word
"""
def select_random_word(all_words):

    word = random.choice(all_words)

    return word


"""
prompts the user for input
"""
def get_guess(word):

    if len(word)==5:
        guess = input("Guess the word with 5 letters: ")
    elif len(word)==6:
        guess = input("Guess the word with 6 letters: ")
    elif len(word)==7:
        guess = input("Guess the word with 7 letters: ")
    elif len(word)==8:
        guess = input("Guess the word with 8 letters: ")


    return guess


"""
iterates over word and checks for correct/wrong letters
"""
def check_guess(guess, word):
    # string for color-coding the word user enters
    # example: RRGYRY (R - red, G - green, Y - yellow)
    colorized_guess = "" * len(word)


    # loops through both letters and indices in word
    for position, letter in enumerate(guess):
        if letter in word:
            if guess[position] == word[position]:
                colorized_guess+="G"
            else:
                colorized_guess+="Y"
        else:
            colorized_guess+="R"

    return colorized_guess 


"""
prints out the word in correct colors
"""
def print_word(colorized_guess, guess, guesses=0):

    colors = {
        "G": "green",
        "Y": "yellow",
        "R": "red"
    }
    print("Guesses :" + str(guesses))

    guesss = ""
    n=0
    for letter in colorized_guess:
        color = colors.get(letter)
        guesss+=(f"[{color}]{guess[n]}[/{color}]")
        n+=1
    print(guesss)

    return guesss


"""
main logic
"""
def main():
    try:
        all_words = read_all_words()
        word = select_random_word(all_words)
    except Exception as e:
        print(e)

    print("[green]This is WORDLE[/green]")

    # for counting user inputs
    guesses = 0 

    guess = ""

    # repeats prompting until user guess the word or no more available guesses
    while guess != word: 
        guess = get_guess(word)

        # repeats prompting for input when word is too short or too long
        while len(guess) != len(word):
            print("Wrong length!")
            guess = get_guess(word)

        # next guess
        guesses += 1 

        colorized_guess = check_guess(guess, word)

        # prints colorized word
        print_word(colorized_guess, guess, guesses)

        if guesses >= 5:
            print("No luck today!")
            print("The word was "+ word)
            break
    else:
        # VICTORY!
        print("You guessed the word!")



if __name__ == "__main__":
    main()