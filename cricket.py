
def main():
    from random import randint

    print("****************************************************WELCOME TO CRICMANIA***********************"
          "********************")
    name = input("\nEnter player name: ").capitalize()

    toss = ["h", "t"]
    run = [1, 2, 3, 4, 6, 0]
    num_of_players = 1
    x = num_of_players
    wickets = 0
    score = 0
    player_score = 0
    computer_score = 0
    again = "y"
    check = "n"

    while True:
        try:
            print("\nWho will call the toss ? ", name, "(1) Computer 2 (2), Quit (q): ")
            turn = input("\nWho will call the toss?")
            if turn not in ("1", "2", "q"):
                raise ValueError
        except ValueError:
            print("Press valid key")
        else:
            break
    if turn == "q":
        exit()
    elif turn == "1":
        print("\n",name, " please call the toss")
        while True:
            try:
                toss_player1 = input("\nHead (h), Tails (t), Quit (q): ").lower()
                if toss_player1 not in ("h", "t", "q"):
                    raise ValueError
            except ValueError:
                print("Press valid key")
            else:
                break
        if toss_player1 == "q":
            exit()
        flip = toss[randint(0,1)]
        print("\n                                           Player call:", toss_player1)
        print("\n                                                  Toss: ", flip)

        if toss_player1 == flip:
            print("Player won the toss")
            first = "player1"
            second = "computer"
            if first == "player1":

                while wickets < num_of_players:
                    while True:
                        try:
                            player_hit = int(input("Play the shot: (1,2,3,4,6,0): "))
                            if player_hit not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break
                    computer_guess = int(run[randint(0, 5)])
                    print("you hit: ", player_hit)
                    print("Computer guess: ", computer_guess)
                    if player_hit == computer_guess:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        player_score = player_score + player_hit
                        print("\nScore: ", player_score)

            print("*********************************************End of first half: Final score: ", player_score)

            print("Need ", (player_score + 1), " runs to win")

            print("Lets play second innings")
            print("Need ", (player_score + 1), " runs to win")
            print("Computer will bat now")
            if second == "computer":
                wickets = 0
                num_of_players = x
                while wickets < num_of_players:

                    computer_hit = int(run[randint(0, 5)])
                    while True:
                        try:
                            player_guess = int(input("Guess the shot: (1,2,3,4,6,0): "))
                            if player_guess not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break

                    print("Your guess: ", player_guess)
                    print("Computer hits: ", computer_hit)
                    if player_guess == computer_hit:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        computer_score = computer_score + computer_hit
                        if computer_score > player_score:
                            print("******************************************************Computer wins")
                            print("*******************************************************Game over")
                            break
                        else:
                            print("Score: ", computer_score, " Need", ((player_score + 1) - computer_score), " runs to win")
            print("Game over")
            if computer_score > player_score:
                print("******************************************************************Computer wins")
            elif computer_score < player_score:
                print("*****************************************************************",name, " wins")
            elif computer_score == player_score:
                print("********************************************************************Match draw")
            main()

        else:
            print("Computer won the toss")
            first = "computer"
            second = "player"
            if first == "computer":
                while wickets < num_of_players:
                    computer_hit = int(run[randint(0, 5)])
                    while True:
                        try:
                            player_guess = int(input("Guess the shot: (1,2,3,4,6,0): "))
                            if player_guess not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break
                    print(" Computer hits: ", computer_hit)
                    print("you guess: ", player_guess)

                    if computer_hit == player_guess:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        computer_score = computer_score + computer_hit
                        print("Score: ", computer_score)
            print("*******************************************End of first half: Final score: ", computer_score)

            print("                                                  Need ", (computer_score + 1), " runs to win")

            print("Lets play second innings")
            print("Need ", (computer_score + 1), " runs to win")
            print("Player will bat now")
            if second == "player":
                wickets = 0
                num_of_players = x
                while wickets < num_of_players:

                    computer_guess = int(run[randint(0, 5)])
                    while True:
                        try:
                            player_hit = int(input("Play the shot: (1,2,3,4,6,0): "))
                            if player_hit not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break
                    print("You hit: ", player_hit )
                    print(" Computer guess: ", computer_guess)
                    if player_hit == computer_guess:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        player_score = player_score + player_hit
                        if player_score > computer_score:
                            print("*****************************************************************",name, " wins")
                            print("********************************************************Game over")
                            break
                        else:
                            print("Score: ", player_score, " Need", ((computer_score + 1) - player_score), " runs to win")
            print("Game over")
            if computer_score > player_score:
                print("********************************************************************Computer wins")
            elif computer_score < player_score:
                print("*****************************************************************",name, " wins")
            elif computer_score == player_score:
                print("*********************************************************************Match Draw")
            main()
    elif turn == "2":
        print("Computer calls the toss")
        flip = toss[randint(0, 1)]
        toss_computer = toss[randint(0, 1)]
        print("\n                                            Computer call: ", toss_computer)
        print("\n                                            Toss: ", flip)

        if toss_computer == flip:
            print("Computer won the toss")
            first = "computer"
            second = "player"
            if first == "computer":
                while wickets < num_of_players:
                    computer_hit = int(run[randint(0, 5)])
                    while True:
                        try:
                            player_guess = int(input("Guess the shot: (1,2,3,4,6,0): "))
                            if player_guess not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break
                    print(" Computer hits: ", computer_hit)
                    print("you guess: ", player_guess)

                    if computer_hit == player_guess:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        computer_score = computer_score + computer_hit
                        print("Score: ", computer_score)
            print("*******************************************End of first half: Final score: ", computer_score)

            print("                                                  Need ", (computer_score + 1), " runs to win")

            print("Lets play second innings")
            print("Need ", (computer_score + 1), " runs to win")
            print("Player will bat now")
            if second == "player":
                wickets = 0
                num_of_players = x
                while wickets < num_of_players:

                    computer_guess = int(run[randint(0, 5)])
                    while True:
                        try:
                            player_hit = int(input("Play the shot: (1,2,3,4,6,0): "))
                            if player_hit not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break

                    print("You hit: ", player_hit )
                    print(" Computer guess: ", computer_guess)
                    if player_hit == computer_guess:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        player_score = player_score + player_hit
                        if player_score > computer_score:
                            print("*****************************************************************",name, " wins")
                            print("**********************************************************Game over")
                            break
                        else:
                            print("Score: ", player_score, " Need", ((computer_score + 1) - player_score), " runs to win")
            print("Game over")
            if computer_score > player_score:
                print("**********************************************************************Computer wins")
            elif computer_score < player_score:
                print("*****************************************************************",name, " wins")
            elif computer_score == player_score:
                print("************************************************************************Match draw")
            main()

        else:
            print("Player won the toss")
            first = "player1"
            second = "computer"
            if first == "player1":

                while wickets < num_of_players:
                    computer_guess = int(run[randint(0, 5)])
                    while True:
                        try:
                            player_hit = int(input("Play the shot: (1,2,3,4,6,0): "))
                            if player_hit not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break
                    print("you hit: ", player_hit)
                    print(" Computer guess: ", computer_guess)
                    if player_hit == computer_guess:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ",(num_of_players-wickets), "  wickets remaining ")

                    else:
                        player_score = player_score + player_hit
                        print("Score: ", player_score)

            print("*********************************************End of first half: Final score: ", player_score)

            print("Need ", (player_score + 1), " runs to win")

            print("Lets play second innings")
            print("Need ", (player_score + 1), " runs to win")
            print("Computer will bat now")
            if second == "computer":
                wickets = 0
                num_of_players = x
                while wickets < num_of_players:

                    computer_hit = int(run[randint(0, 5)])

                    while True:
                        try:
                            player_guess = int(input("Guess the shot: (1,2,3,4,6,0): "))
                            if player_guess not in (1,2,3,4,6,0):
                                raise ValueError
                        except ValueError:
                            print("Play valid shot")
                        else:
                            break
                    print("Your guess: ", player_guess)
                    print(" Computer hits: ", computer_hit)

                    if player_guess == computer_hit:
                        wickets = wickets + 1
                        print("That's a wicket !!!!! ", (num_of_players - wickets), "  wickets remaining ")

                    else:
                        computer_score = computer_score + computer_hit
                        if computer_score > player_score:
                            print("****************************************************Computer wins")
                            print("****************************************************Game over")
                            break

                        else:
                                print("Score: ", computer_score, " Need", ((player_score +1 ) - computer_score), " runs to win")
                print("Game over")
                if computer_score > player_score:
                    print("****************************************************************Computer wins")
                elif computer_score < player_score:
                    print("*****************************************************************",name, " wins")
                elif computer_score == player_score:
                    print("******************************************************************Match draw")
                main()

play = input(" Play: y or n: ")
if play == "y":
    computer_score = 0
    player_score = 0
    wickets = 0
    main()

else:
    exit()





