option = None

while option != 0:
    print("Please choose your option from the below:")
    print("1. learn Java")
    print("2. learn Python")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")
    print("6. Exit")
    option = int(input())

    if option == 1:
        print("You have selected to learn Java")
    elif option == 2:
        print("You have selected to learn Python")
    elif option == 3:
        print("You have selected to go swimming")
    elif option == 4:
        print("You have selected to have dinner")
    elif option == 5:
        print("You have selected to go to bed")
    elif option == 6:
        print("Thank you, have a good day")
else:
    print("Invalid choice")