import random
number = random.randint(1, 50)
while True:
    guess = int(input("Guess the number (between 1 and 50):"))
    if guess < number:
        print("Too low!")
    elif  guess > number:   
        print("Too high!") 
    else:
        print("You are win 👍😃", number)
        break   