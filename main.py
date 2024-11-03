#Hangman Game in Python
#English version of the code
#Created by David Ericson
#06/03/2024

import random
import os

#Global variables that will be used in the functions
chances = 6
attempt = ''
remaining = False
used_letters = []
player = ''
p1_score = 0
p2_score = 0
p1_name = ''
p2_name = ''
restart = ''



#------------------------------------------------------



def reset(): #Function used to reset global variables
    global chances
    global attempt
    global remaining
    global used_letters
    global player
    
    chances = 6
    attempt = ''
    remaining = False
    used_letters = []
    player = ''



#------------------------------------------------------



def hangman(chance): #Hangman interface function
    if chance == 6:
        print('  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========')
    elif chance == 5:
        print('  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========')
    elif chance == 4:
        print('  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========')
    elif chance == 3:
        print('  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========')
    elif chance == 2:
        print('  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========')
    elif chance == 1:
        print('  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========')
    else:
        print('  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========')



#------------------------------------------------------



def hidden_word(p): #Hidden word interface function
    discovered = []
    for i in range(len(p)):
        discovered.append('_')
    return discovered



#------------------------------------------------------



def pvp(): #Function - Player vs Player Mode
    global chances
    global attempt
    global remaining
    global used_letters
    global p1_score
    global p2_score
    global player
    global restart
    global p1_name
    global p2_name

    #------------------------------------------------------
    while restart != 'N': #Defines when the function will end

        reset()
        restart = ''

        os.system('cls' if os.name == 'nt' else 'clear')
        print('- Player vs Player Mode -')
        print('-------------------------------')

        if p1_score == 0 and p2_score == 0:
            print('[Rules]: One player will enter a mystery word and the other must guess it. If the player guesses the word,\nhe scores. If he fails, the player who entered the word will score.')
            print('-------------------------------')
            p1_name = str(input('Enter Player 01 Name: '))
            p2_name = str(input('Enter Player 02 Name: '))
        else:
            print(f'[Scoreboard]\n{p1_name}: {p1_score}\n{p2_name}: {p2_score}')
            print('-------------------------------')

        #------------------------------------------------------
        while player != p1_name and player != p2_name:
            player = (input(f'> Which player will be guessing the word this round? [{p1_name}/{p2_name}]: '))
            if player != p1_name and player != p2_name:
                print('Invalid Player!')

        word = str(input('> Enter the word to be guessed (The word will be hidden after being entered): ')).upper() 
        os.system('cls' if os.name == 'nt' else 'clear')
        discovered = hidden_word(word)

        #------------------------------------------------------
        while remaining != True and chances >= 0: #Word guessing part
            remaining = True
            guessed_right = False

            hangman(chances)
            print(f'{discovered}|Used Letters:{used_letters}')


            if chances > 0: #Area to insert characters to guess the hidden word
                while len(attempt) != 1:
                    attempt = str(input('Enter only one letter: ')).upper()
                    for i in range(len(used_letters)): #Checks if the letter in the attempt has been used before
                        if attempt == used_letters[i]:
                            print('Letter already used')
                            attempt = ''


                used_letters.append(attempt) #Adds the attempt to the array of used letters


                for i in range(len(word)): #Checks if the word contains the letter entered in the attempt
                    if word[i] == attempt:
                        discovered[i] = attempt
                        guessed_right = True


            if guessed_right == False: #Removes a chance if the word does not contain the letter entered in the attempt
                chances -= 1


            for i in range(len(discovered)): #Checks if the word has been fully discovered
                if discovered[i] == '_':
                    remaining = False
        

            attempt = ''
            os.system('cls' if os.name == 'nt' else 'clear')

        #------------------------------------------------------
        print('-------------------------------')
        if chances <= 0: #Removes points if the player lost
            hangman(chances)
            if player == 'p1':
                print(f'You lost, the word was {word}. [{p2_name} Received +1 Point]')
                p2_score += 1
            else:
                print(f'You lost, the word was {word}. [{p1_name} Received +1 Point]')
                p1_score += 1

        else: #Adds points if the player won
            hangman(chances)
            print(f'{discovered}')
            print(f'Congratulations, you guessed it! [{player} Received +1 Point]')
            if player == 'p1':
                p1_score += 1
            else:
                p2_score += 1

        #------------------------------------------------------

        while restart != 'Y' and restart != 'N': #Restart or end program
            restart = str(input('Do you want to keep playing? [Y/N]: ')).upper()

            if restart == 'Y' and restart == 'N':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-------------------------------')
            if restart != 'Y' and restart != 'N':
                print('Invalid Operation')



#------------------------------------------------------



def pvm(): #Function - Player vs Machine Mode
    global chances
    global attempt
    global remaining
    global used_letters
    global restart
    global p1_score


    while restart != 'N': #Defines when the function will end
        reset()
        
        word_list = ["house", "car", "flower", "cat", "dog", "table", "chair", "window", "door", "book", "pen", "pencil", "paper", "bag", "shoe", "sun", "moon", "star", "cloud", "river", "sea", "fish", "bird", "phone", "computer", "keyboard", "mouse", "shirt", "bicycle", "ball", "key", "knife", "fork", "spoon", "plate", "cup", "horse", "pineapple", "milk", "friend"]
        os.system('cls' if os.name == 'nt' else 'clear')
        print('- Player vs Machine Mode -')
        print('-------------------------------')

        if restart != 'Y':
            print('[Rules]: Try to guess as many words as possible to accumulate points. If you make a single mistake, you lose!')
            print('-------------------------------')
            a = str(input('Press any button to start the game...'))

        restart = ''

        os.system('cls' if os.name == 'nt' else 'clear')

        word = (word_list[random.randint(0,39)]).upper()
        discovered = hidden_word(word)

        #------------------------------------------------------
        while remaining != True and chances >= 0: #Word guessing part
            remaining = True
            guessed_right = False

            hangman(chances)
            print(f'{discovered}\nUsed Letters:{used_letters}|Score: {p1_score}')


            if chances > 0: #Area to insert characters to guess the hidden word
                while len(attempt) != 1:
                    attempt = str(input('Enter only one letter: ')).upper()
                    for i in range(len(used_letters)):
                        if attempt == used_letters[i]:
                            print('Letter already used')
                            attempt = ''


                used_letters.append(attempt) #Adds the attempt to the array of used letters


                for i in range(len(word)): #Checks if the word contains the letter entered in the attempt
                    if word[i] == attempt:
                        discovered[i] = attempt
                        guessed_right = True


            if guessed_right == False: #Removes a chance if the word does not contain the letter entered in the attempt
                chances -= 1


            for i in range(len(discovered)): #Checks if the word has been fully discovered
                if discovered[i] == '_':
                    remaining = False
        
            attempt = ''
            os.system('cls' if os.name == 'nt' else 'clear')

        #------------------------------------------------------

        print('-------------------------------')
        if chances <= 0:
            hangman(chances)
            print(f'You lost, the word was [{word}] | Your final score was {p1_score} points.')
            p1_score = 0

        else:
            hangman(chances)
            print(f'{discovered}')
            p1_score += 1
            print(f'Congratulations, you guessed it and received +1 point!!! [Total: {p1_score}]')


#------------------------------------------------------

        while restart != 'Y' and restart != 'N': #Restart or end program
            restart = str(input('Do you want to keep playing? [Y/N]: ')).upper()

            if restart == 'Y' and restart == 'N':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('-------------------------------')
            if restart != 'Y' and restart != 'N':
                print('Invalid Operation')



#------------------------------------------------------



def main(): #Main function to select game mode
    print('-------------------------------')
    print('- Hangman Game -')
    print('-------------------------------')
    mode = str(input('If you wish to exit type [Exit] | Which game mode do you want to play?[[Player vs Player][Player vs Machine]]: ')).lower() #Mode selection
    while mode != 'exit':

        if mode == 'player vs player' or mode == 'pvp':
            print('-------------------------------')
            mode = 'exit'
            pvp()

        elif mode == 'player vs machine' or mode == 'pvm':
            print('-------------------------------')
            mode = 'exit'
            pvm()

        else:
            print('Invalid option, please try again.')
            print('-------------------------------')

            mode = str(input('If you wish to exit type [Exit] | Which game mode do you want to play?[Player vs Player][Player vs Machine]: ')).lower()

main() #Starts the main function
print('-------------------------------')
print('Program Terminated....')