# Kristen Valadez
# Assignment 6 CISW 24
# 10/05/2025
import sys
lets_play = input('Would you like to play a game? (y/n/q): ')


if lets_play == 'n' : 
    print ('Thank you for playing. Good bye.')
    # you will need to import sys at the top of your file
    sys.exit() 

while True: 
    game_choice = input('''
Choose a game or quit: 
1) Bagels
2) Rock, Paper, Scissors
3) The Game 21
q) to quit 
                        
Enter your choice: ''')

    
    if game_choice.lower() == 'q': 
        print('Thank you for playing. Good bye.')
        sys.exit() 
    if game_choice == '1': 
    # we are only printing a message 
    # but we could call the game file or function from here 
        print ('You chose bagels! Have a nice game.')
    elif game_choice == '2': 
        print ('You chose Rock, Paper, Scissors! Have a nice game.')
    elif game_choice == '3': 
        print ('You chose The Game 21! Have a nice game.')
    else: 
        print ('Please enter one of listed options.')

