num_of_options = 9

for i in range(1, num_of_options+1):
    print("{0} - Select menu option {0}".format(i))
print("0 - Exit")

while True:
    selection = input("Please select a valid menu option: ")
    if selection.isnumeric():
        if int(selection) in range(1, num_of_options+1):
            print("You have selected option {}".format(selection))
        elif int(selection) == 0:
            break
        else:
            print("You have not made a valid selection")
    else:
        print("You have not made a valid selection")
