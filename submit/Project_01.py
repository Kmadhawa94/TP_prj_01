# import random module since we need to randomize the numbers generated
import random

# headline quote
print("="*25)
print("  Gambling With Python  ")
print("="*25)

try:
    def dice_simulation():
        """
        To roll the dices for a player and count the total score of each player
        :return: score of the player
        """

        # defining 3 unique dices
        dice_1 = [1, 2, 3, 4, 5, 6]
        dice_2 = ["CMB", "TYK", "NY", "LON", "SYN"]
        dice_3 = [True, False, True, False, True, False]

        # defining 3 lists to store the outcomes of 3 dices.
        out_dice_1 = []
        out_dice_2 = []
        out_dice_3 = []

        # number of attempts for a player
        attempts = 0
        # asking the player to go forward
        prompt = "y"

        # apply while loop to roll the 3 dices until all 3 chances are utilized.
        while attempts < 3:
            print("Attempt", (attempts+1))
            prompt = input("Roll the dice? [y/n]: ")
            if prompt == "y":

                # roll the first dice to get a number
                out_dice_1.append(random.choice(dice_1))
                # roll the second dice to get a city
                out_dice_2.append(random.choice(dice_2))
                # roll the first dice to check the number is positive or negative
                out_dice_3.append(random.choice(dice_3))
                # count the attempts
                attempts = attempts + 1
            else:
                break
        # apply higher order function to make a nested list
        player_output = list(zip(out_dice_1, out_dice_2, out_dice_3))
        print("Outcomes: ",player_output)

        # initial player score value
        player_score = 0
        # apply for loop to check the number is positive or negative
        for i in range(len(player_output)):
            if player_output[i][2]:
                player_score = player_score + player_output[i][0]
            else:
                player_score = player_score - player_output[i][0]

        print("Your score is: ", player_score)
        # function return the player score
        return player_score


    if __name__ == '__main__':
        # creating a list to store the player names
        players_list = []
        # creating a list to store the player names and their scores
        all_details = []
        # creating a list to store the scores
        score_list = []

        print("Welcome to the game!!!")
        # starting the game for 3 players
        for y in range(0, 3):

            # append player names to player_list
            players_list.append(input("Enter your name: "))
            print("Hello, " + players_list[y] + ", the game is about to start!!!!:\n>>> ")

            # calling the dice simulation function and store the value as score
            score = dice_simulation()

            # append player names and their scores to all_player list
            all_details.append([players_list[y], score])

            # append each player score to a separate list
            score_list.append(score)
            print("-------------------------------------------------------------------------------")

        # finding the maximum score among three players
        max_score = sorted(list(set(score_list)))[2]
        # selecting the winner by the maximum score
        for player, scores in sorted(all_details):
            if scores == max_score:
                print("Congratulations!!!" + player + " Wins")

except:
    print("invalied Entry")





