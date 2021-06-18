import random
print("*****Welcome to the Snake-Water-Gun Game*****")
print("Your choices- \n 's' for snake\n 'w' for water \n 'g' for gun")
print("important- You have total 10 chances to play the game")

input("Press Enter to start")
print("Lets start the game")


def game1():
    player1 = input("Enter the player name:\n")
    snake = "s"
    water = "w"
    gun = "g"
    you = 0
    comp1 = 0
    r = 0
    yes = "y"
    no = "n"
    while r < 10:


        comp = "computer"
        user = input("Enter your choice from the options 's','w' and 'g':")
        lst = ['s', 'w', 'g']
        comp = random.choice(lst)
        print("opponent(Computer) choice:", comp)
        if user == comp:
            print("It's tie")
            you = you + 0
            comp1 = comp1 + 0

        elif user == "s":
            if comp == "w":
                print(f"You won,{player1}")
                you = you + 1
            else:
                print(f"You lost,{player1}")
                comp1 = comp1 + 1
        elif user == "w":
            if comp == "s":
                print(f"You lost,{player1}")
                comp1 = comp1 + 1
            else :
                print(f"You won,{player1}")
                you = you + 1
        elif user == "g":
            if comp == "s":
                print(f"You won,{player1}")
                you = you + 1
            else:
                print(f"You lost,{player1}")
                comp1 = comp1 + 1
        else:
            print(f"You enter the wrong choice {player1}.Please enter the correct options from s,w,g")
        # to print the total chances left
        left = 9 - r
        print("Your remaining chances are:", left)
        r = r + 1
    print("Game over")
    print(f"{player1},Your score is-", you)
    print("opponent(Computer) score is-", comp1)

    # To print the Total score
    if you == comp1:
        print(f"The game is Tie since the game score is same which is {you}")
    elif you < comp1:
        print(f"You lost the game {player1}, by {comp1 - you} point('s),better luck next time")
    elif you > comp1:
        print(f"You won the game {player1} by {you - comp1} point('s)")

    print("****Why Don't You try again****")

    print("Do you want to play again")

    user2 = input("Enter y for Yes & n for No:")
    if user2 == "y":
        print(f"Welcome Again!! {player1} 'Best of Luck'")

        return game1()
    elif user2 == 'n':
        print("*****Sad to see you go*******")
        print("*****Thank you****")
    else:
        print("you Enter the wrong option ,Go back")
        print(input("enter"))
        return game1()




game1()