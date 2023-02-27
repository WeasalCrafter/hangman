import random
words = ['intention','concept','situation','thanks','orange','perception','negotiation','leadership','memory','location','health','television','explanation','philosophy','president','safety','construction','people','complaint','employer']
selected = random.choice(words)
guessed = []; strikes = 0; win = False
def strike():
    global strikes
    strikes += 1
    if strikes == 1:
        print("STRIKE 1\n +---+\n |   |\n     |\n     |\n     |\n     |")
    elif strikes == 2:
        print("STRIKE 2\n +---+\n |   |\n O   |\n     |\n     |\n     |")
    elif strikes == 3:
        print("STRIKE 3\n +---+\n |   |\n O   |\n |   |\n     |\n     |")
    elif strikes == 4:
        print("STRIKE 4\n +---+\n |   |\n O   |\n/|\  |\n     |\n     |")
    elif strikes == 5:
        print("STRIKE 5\n +---+\n |   |\n O   |\n/|\  |\n/ \  |\n     |")
def progress(word):
    count = 0
    for character in word:
        if character in guessed: print(character + " ", end='') 
        else: print("_ ", end=''); count += 1
    if count > 0: print(" ({:d} LETTERS REMAIN)".format(count)) 
    else: return True
def check(letter, selected):
    letter = letter.lower()
    if letter.isalpha() == True and len(letter) == 1 and letter not in guessed:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") 
        if letter not in selected: strike()
        guessed.append(letter)
        if progress(selected) == True: return True
    else:
        print("ONLY USE ONE UNIQUE LETTER")
        check(input("TRY AGAIN: "), selected)
        return False
print("WELCOME TO HANGMAN")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("FIND THE SECRET WORD BY GUESSING LETTERS")
print('EACH _ REPRESENTS A HIDDEN LETTER') 
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
progress(selected)
while strikes < 6:
    if check(input('GUESS: '), selected) == True: break
if strikes > 5:
    print("GAME OVER")
    print("THE WORD WAS, " + selected.upper())
else:
    print("\nCONGRATULATIONS, YOU WIN!")
print("RE-RUN THE PROGRAM TO PLAY AGAIN!!")

