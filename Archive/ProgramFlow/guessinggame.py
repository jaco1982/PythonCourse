import random

highest = 10
answer = random.randint(1,highest)
#print(answer) #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

numofguesses = 1
if guess == answer:
    print("Well done, you guessed it in 1 try!")
else:
    while guess != answer:
        numofguesses += 1
        if guess == 0:
            print("Goodbye")
            break
        elif guess < answer:
            print("Please guess higher")
        elif guess > answer:
            print("Please guess lower")
        guess = int(input())
    print("Well done, you guessed it in {} tries!".format(numofguesses))
    

# else:
#     if guess < answer:
#         print("Please guess higher")
#     else: #Guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
    

