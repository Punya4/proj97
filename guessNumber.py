import random 
chance =0
number= random.randint(0,9)
print("   Number Guessing game ")
print("Guess a number between 0 - 9 ")
while chance< 5:
    guess=int(input("Enter a random number between 0 - 9 : "))
    if (guess==number):
        print("Congrats you Won")
        break
    elif (guess<number):
        print("The number is wrong but ur guess is grater then ",guess,)
    else:
        print("The number is wrong but ur guess is smaller then ",guess)
    chance=chance+1
    print("chances left :",5-chance)
        
if not (chance<5):
    print("You Lose")
    print("The Number Is : ",number)