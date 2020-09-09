parrot = "Norwegian Blue"

letter = input("Eneter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")