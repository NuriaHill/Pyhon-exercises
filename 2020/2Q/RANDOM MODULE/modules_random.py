#Random module
""" the project starts by importing the randome module For example, to generate a random between 1 and 10 (inclusive) and store it in a variable named num, use this line of code:"""
import random
num = random.randint(1, 10)
""" The project also has a variable called money that starts at 100. This represents your current amount of money. In every game of chance you will be able to bet money
the value of money should change depending if you lose or win the game"""
import random

money = 100
#1Create function that simulates flipping a coin
def coin_flip(guess, bet):  
  #Will randomly get 1 or 2. Will associate 1 to heads and 2 to tails.
  flip = random.randint(1,2)
  if flip == 1: 
    print("the coin toss result was heads")
  if flip == 2: 
    print("the coin toss result was tails")
  if (flip==1) and (guess.lower()== "heads"):
    print("your guess is right! You won "+ str(bet) + " Euros")
    return +bet 
  elif (flip==2) and (guess.lower()== "tails"):
    print("your guess is right! You won "+ str(bet) + " Euros")
    return +bet 
  else :
    print ("Sorry, try again, you lost " + str(bet) + " Euros")
    return -bet
  
#Call your game of chance functions here

coin_flip ("heads", 50)