import sys
import os
os.system('clear')

answer = 'basil'

def main():
    #print('Welcome to hangman')
    guesses = 0
    max_guesses= 5
    print_hangman(0)
    while guesses < max_guesses:
        print('')
        print('Please guess the name of the biggest asshole at THG, you have ' + str(max_guesses - guesses) + ' guesses remaining ')
        guess = input(':')
        if guess == answer:
            guesses = max_guesses
            print('')
            print('Correct, '+ answer + ' is an asshole. You Win!')
            sys.exit(0)
        else:
            guesses = guesses + 1  
            print_hangman(guesses)

    print('')
    print('Too Many Guesses, You Lose!')          
    

def print_hangman(number):
    
    body_parts = build_body_parts(number)
    
    os.system('clear')
    print('      ')   
    print('      ')
    print('_____') 
    print('|    |')
    print('|',body_parts[0])
    print('|',body_parts[1] + body_parts[2])
    print('|',body_parts[3])
    print('|',body_parts[4])
    print('|'),
    print('|______')
        
    return

def build_body_parts(number):
    body_parts = ["   O","  /-","\ ","   |","  / \ "] 
    parts = []
    i = 0
        
    while i < len(body_parts):  
        if i < int(number): 
            parts.append(body_parts[i])
        else:
            parts.append("")
        i = i + 1
                
    return parts     

                 
main()    
