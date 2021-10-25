"""
Lab 7 Question 2. -- Practice good coding etiquette here also.

Write a guessing game for a user. This program should initially generate a random 
number between 1 and 100. 
It should then repeatedly ask the user to guess the random number. 
Each time the user enters a guess the program should tell them that their guess was too 
high, too low or correct. 
When the user finally guesses the correct number the program should tell the user how 
many guesses they made before arriving at the correct number. 

Your program should make use of the following methods:
    
    
• generateRandomNumber. This function will generate a random number 
between 0, 100 and return the result.

• askUser. This function will ask the user to enter a guess and will return the 
result.

• checkGuess. This function will take in the users guess and the random 
number as parameters and will return True if the user entered the correct 
value and False otherwise. 


Program has generated a random number:
Please enter your guess: 50
Too high
Please enter your guess: 25
Too low
Please enter your guess: 38
Correct. You made a total of 3 guesses. 
"""




import random


def generate_random_number() : 
    
    return random.randint(0, 100)



def ask_user() :
    
    user_int = int(input("Guess the number: "))
    return user_int
    


def check_guess(ans , user_guess) :
    
    if user_guess > ans :
        
        print("Incorrect guess (Too high), try again")
        
        return True
    
    elif user_guess < ans :
        
        print("Incorrect guess (Too low), try again")
        
        return True
    
    else :
        
        print("Correct!!")
        
        return False


def guessing_game():

    game_running = True
    num_guesses = int(0)
    
    ans = generate_random_number()
    print(ans)

    print("Program has generated a random number:")
    
    while game_running is True :
        
        user_guess = ask_user()
        
        game_running = check_guess(ans, user_guess) 
        num_guesses += 1
            
        
    
    print("Total number of guesses:" , num_guesses)
    
guessing_game()