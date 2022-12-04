#Instructions : https://adventofcode.com/2022/day/2
#Key - A : Rock (opponent), B: Paper (opponent), C: Scissors (opponent)
# X : Rock, Y : Paper, Z : Scissors
# Points - Rock (1), Scissors (2), Paper (3), Loss (0), Draw (3), Win (6)
#Using the stratergy provided in 'aoc_2_data.txt' determine your score. 

#Import packages
import numpy as np

#Open data
with open ('aoc_2_data.txt') as f:
    text = f.read()


def rock_paper_scissors(round_tuple, player_1, player_2):
    """
    A game of rock paper scissors where you input each round as a tuple (e.g. ['Rock', 'Paper'])
    Outputs the scores from each round based on the players inputs.
    """
    for i in round_tuple:
#Add scores for each input
        if i[0] == 'Rock':
            player_1.append(1)
        elif i[0] == 'Paper':
            player_1.append(2)
        elif i[0] == 'Scissors':
            player_1.append(3)

        if i[1] == 'Rock':
            player_2.append(1)
        elif i[1] == 'Paper':
            player_2.append(2)
        elif i[1] == 'Scissors':
            player_2.append(3)

#Add scores for outcome
#Draw
        if i[0] == i[1]:
            player_1.append(3)
            player_2.append(3)

    #Player 1 plays rock
        elif i[0] == 'Rock':
            if i[1] == 'Scissors':
                player_1.append(6)
            else:
                player_2.append(6)

    #Player 1 plays scissors
        elif i[0] == 'Scissors':
            if i[1] == 'Paper':
                player_1.append(6)
            else:
                player_2.append(6)

    #Player 1 plays paper
        elif i[0] == 'Paper':
            if i[1] == 'Rock':
                player_1.append(6)
            else:
                player_2.append(6)

    return(player_1, player_2)

# We want to create tuples based on " " seperator.

#Seperate data on new empty lines, this groups each set together. E.g. ('17998\n7761')
line_sep = np.array(text.split('\n\n'))

#Split each elements up in a round to be individual elements
round_split = (np.char.split(np.array(line_sep),sep='\n'))
#Create the object as an array
round_split = (np.array(round_split[0]))

# Replace letters with 'Rock', 'Paper', 'Scissors'
# Mainly wanted player 1 and 2 to have the same coding to use ==. 
round_split_replace = ([s.replace("A","Rock").replace("B", "Paper").replace("C", "Scissors").replace("X","Rock").replace("Y", "Paper").replace("Z", "Scissors") for s in round_split])
#Seperate each element
round_tuple = (np.char.split(round_split_replace, sep = ' '))


# Could do one pass through to determine the score for each player based on what they played
# And then a second passthrough based on if they won. 

player_1 = []
player_2 = []

player_1, player_2 = rock_paper_scissors(round_tuple=round_tuple, player_1=player_1, player_2=player_2)

print("Players 1 score is:", sum(player_1), "My score is:", sum(player_2))



### Pt 2 : X, Y , Z now means Lose, Draw, Win. 



# Replace all Ys with the same element

round_split_pt2_replace = ([s.replace("A","Rock").replace("B", "Paper").replace("C", "Scissors") for s in round_split])
round_tuple_pt2 = (np.char.split(round_split_pt2_replace, sep = ' '))

#Code to map players twos input 'X', 'Y', 'Z' to lose, draw, win. 
for i in round_tuple_pt2:
    if i[1] == 'Y':
        i[1] = i[0]

    elif i[1] == 'X':
        if i[0] == 'Rock':
            i[1] = 'Scissors'
        elif i[0] == 'Scissors':
            i[1] = 'Paper'
        else:
            i[1] = 'Rock'
    
    elif i[1] == 'Z':
        if i[0] == 'Rock':
            i[1] = 'Paper'
        elif i[0] == 'Scissors':
            i[1] = 'Rock'
        else:
            i[1] = 'Scissors'

player_1 = []
player_2 = []

player_1, player_2 = rock_paper_scissors(round_tuple=round_tuple_pt2, player_1=player_1, player_2=player_2)

print("Players 1 score is:", sum(player_1), "My score is:", sum(player_2))
