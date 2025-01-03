y = 0
while y==0:
    import random
    matrix = [
        [0, 1, 2],
        [2, 0, 1],
        [1, 2, 0]
    ]
    while True:
        x  = input("Enter Your choice   :  ").lower()
        match x:
            case ("rock"):
                x = 0
                print("You Choose - Rock")
                break
            case ("paper"):
                x = 1
                print("You Choose - Paper")
                break
            case ("scissor"):
                x= 2
                print("You Choose - Scissor")
                break
            case _:
                print("Invlaid Input Please Try Again") 
    random_number = random.randint(0, 2)
    if random_number == 1:
        print("Robot Choose - Paper")
    elif random_number == 2:
        print("Robot Choose - Scissor")
    else :
        print("Robot Choose - Rock")

    win = matrix[x][random_number]
    if win==1:
        print("You Loose The Match and Robot Won THis Match")
    elif win == 2:
        print("You Won The Match and Robot Loose This Match ")
    else:
        print("match is Tie ")
    while True:
        try:
            z = int(input("Can You Play Again This Game \n yes - press 1 \n No - press 2 "))
            match z:
                case 1:
                    print("Okay wait Start Match Again")   
                case 2:
                    print("Okay exiting the match ")
                    y=1
                    break
                case _:
                    print("Please enter valid key only 1 and 2 ")
        except ValueError:
            print("Invalid Input. please Type Integer Value ")
