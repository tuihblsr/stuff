import random
import os

hangman = [
    r'''
    ===        10 guesses
    ''',
    r'''
     | 
     |         9 guesses
     |
    ==='
    ''',
    r'''
+----+
     | 
     |         8 guesses
     |
    ===
    ''',
    r'''
+----+
0    | 
     |         7 guesses
     |
    ===
    ''',
    r'''
+----+
0    | 
|    |         6 guesses
     |
    ===
    ''',
    r'''
+----+
 0   | 
/|   |         5 guesses
     |
    ===
    ''',
    r'''
+----+
 0   | 
/|\  |         4 guesses
     |
    ===
    ''',
    r'''
+----+
 0   | 
/|\  |         3 guesses
/    |
    ===
    ''',
    r'''
+----+
 0   | 
/|\  |         2 guesses
/ \  |
    ===
    ''',
    r'''
+----+
[0]  | 
/|\  |         1 guesses
/ \  |
    ===
    '''
]
guesses = 10
guess = ''
words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()
secret_word = ''
correct_letters = []
done = False

def chooseWord():
    global secret_word
    secret_word = random.choice(words)

def checkIfUWin():
    count = 0
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            count += 1
    if count == len(secret_word):
        return 'Win'
    else:
        return 'No'

def checkGuess():
    global done
    global guesses
    if len(guess) != 1:
        print('Only 1 letter')
    elif guess.isalpha() == False:
        print('Only letters')
    elif guesses < 1:
        print('Out of guesses')
        done = True
    elif guess in secret_word:
        correct_letters.append(str(guess))
        guesses -= 1
        if checkIfUWin() == 'Win':
            print('You won!')
            done = True
    else:
        guesses -= 1
        print('Letter is not in word')
def main():
    global guess
    chooseWord()
    while not done:
        os.system('clear')
        display = ''
        for i in range(len(secret_word)):
            if secret_word[i] in correct_letters:
                display = display + secret_word[i]
            else:
                display = display + '*'
        print(display)
        # print('Guesses left: ' + str(guesses))
        if guesses == 10:
            print(hangman[0])
        elif guesses == 9:
            print(hangman[1])
        elif guesses == 8:
            print(hangman[2])
        elif guesses == 7:
            print(hangman[3])
        elif guesses == 6:
            print(hangman[4])
        elif guesses == 5:
            print(hangman[5])
        elif guesses == 4:
            print(hangman[6])
        elif guesses == 3:
            print(hangman[7])
        elif guesses == 2:
            print(hangman[8])
        elif guesses == 1:
            print(hangman[9])
        elif guesses == 0:
            print(secret_word)
        
        guess = input("Guess a letter: ").lower().strip()
        checkGuess()

main()

# for i in hangman:
#     print(i)
