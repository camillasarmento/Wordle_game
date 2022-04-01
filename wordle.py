import random
import sys
from termcolor import colored

WORD_LENGTH = 5

def print_menu():
    print("Let's play!:")
    print("Type a 5 letter word and hit enter!\n")
        
def get_words():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return words

print_menu()
WORD_LIST = get_words()

play_again = ""
while play_again != "q":
    word = random.choice(WORD_LIST)

    attempt = 1
    while attempt in range(1,7):
        guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        if len(guess) != WORD_LENGTH:
            print(f"'{guess}' is not a {WORD_LENGTH} letter word, please try again.")
            continue
        
        if guess not in WORD_LIST:
            print(f"'{guess}' is not on the list of words, please try again.")
            continue
                        
        for i in range(min(len(guess), WORD_LENGTH)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'),end="")
            else:
                print(guess[i], end="")
                
        print()
        
        if guess == word:
            print(colored(f"Congrats!!! you got in {attempt}", 'red'))
            break
        elif attempt == 6:
            print (f"Sorry the Wordle was..{word}")
            
        attempt += 1

    play_again = input("Want to play again? Type q to exit.")
print('Bye!')