def main():
    
    getCorrectAnswerWithRecursion(5)
    getCorrectAnswerWithWhileLoop(5)


def getCorrectAnswerWithRecursion(number):

    answer = input('enter a number: ')
    if number == int(answer):
            print('Correct you win!')
            return
    else:
         getCorrectAnswerWithRecursion(number)




def getCorrectAnswerWithWhileLoop(number):
    number = 5
    print('Guess a number between 1 and 10.  You have unlimited guesses.')
    
    while True:

        answer = input('enter a number: ')
        print(answer)

        if number == int(answer):
            print('Correct you win!')
            return
            

         
main()    
