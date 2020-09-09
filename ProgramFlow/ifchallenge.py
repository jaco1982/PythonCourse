name = input("What is your name? ")
age = int(input("What is your age? "))

if name:
    if 18 <= age <= 30:
        print("Welcome to your holiday {0}!".format(name))
    else:
        print("You are not the correct age for this. Go away.")
else:
    print("You need to enter your name first!")