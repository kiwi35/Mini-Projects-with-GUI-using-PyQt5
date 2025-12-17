import random as rnd
import sys
letter = []
cho = ''
lives = 1
is_running = True

def hangman(lives):
    hang = {
        1: "  \n  \n  ",
        2: " O \n   \n   ",
        3: " O \n | \n   ",
        4: " O \n/| \n   ",
        5: " O \n/|\\ \n   ",
        6: " O \n/|\\ \n/ \\ ",
        7:"You Lose, hehehe ;)"
    }

    print(hang[lives])

def choose():
    global cho
    cho = (rnd.choice(["ATMOSPHERE", "PHONE", "WATER", "NAMASTE", 'CLOCK', "ORANGE", "APPLE"]))
    return cho
def display(letter):
    for let in cho:
        if let in letter:
            print(let, end=' ')
        else:
            print('_', end=' ')
    print()
def inputt():
    global letter
    l = input("Enter a letter: ").upper()
    comparee(l, cho)
def comparee(l,cho):
    global lives
    global letter
    global is_running
    if l in cho:
        print("The word is present in the alphabet.")
        letter.append(l)
        display(letter)
        hangman(lives)
    else:
        print("The word is not present in the alphabet.")
        lives += 1
        display(letter)
        hangman(lives)
    if lives > 6:
        print(f"Game Over. The word was: {cho}")
        is_running = False
        sys.exit(1)


    if set(cho).issubset(set(letter)):
        print(f"Congratulations! You guessed the word: {cho}")
        is_running = False





def playing():
    global lives, letter, is_running
    choose()
    display(letter)
    lives = 1
    letter = []
    is_running = True
    while is_running == True and lives <= 6:
        inputt()
    if is_running == False:
        print(f"Game Over. The word was: {cho}")



if __name__ == '__main__':
    playing()









