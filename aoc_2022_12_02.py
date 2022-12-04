#Instructions : https://adventofcode.com/2022/day/2
#Key - A : Rock (opponent), B: Paper (opponent), C: Scissors (opponent)
# X : Rock, Y : Paper, Z : Scissors
# Points - Rock (1), Scissors (2), Paper (3), Loss (0), Draw (3), Win (6)
#Using the stratergy provided in 'aoc_2_data.txt' determine your score. 

#Import packages
import numpy as np

#Open data
with open ('aoc_data_02.txt') as f:
    text = f.read()

data = (np.loadtxt(fname='aoc_data_02.txt',dtype=str))

#Define rock paper scissors function
def rock_paper_scissors(round_tuple, player_1, player_2):
    """
    A game of rock paper scissors where you input each round as a tuple (e.g. ['Rock', 'Paper'])
    Outputs the scores from each round based on the players inputs.
    """
    score_dict = {
    'Rock' : 1,
    'Paper' : 2,
    'Scissors' : 3,
    }

    loses_to = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock",
    }
    
    for i in round_tuple:
#Add scores for each input
        player_1.append(score_dict[i[0]])
        player_2.append(score_dict[i[1]])
        
#Add scores for outcome
        if i[1] == loses_to[i[0]]:
            player_2.append(6)

        elif i[0] == loses_to[i[1]]:
            player_1.append(6)
        else:
            player_1.append(3)
            player_2.append(3)

    return(player_1, player_2)

# We want to create tuples based on " " seperator.

#Seperate data on new empty lines, this groups each set together. E.g. ('17998\n7761')
line_sep = np.array(text.split('\n\n'))

#Split each elements up in a round to be individual elements
round_split = (np.char.split(np.array(line_sep),sep='\n'))
#Create the object as an array
round_split = (np.array(round_split[0]))

## For Part 1: 

# Replace all letters with 'Rock', 'Paper', 'Scissors'
round_split_replace = ([s.replace("A","Rock").replace("B", "Paper").replace("C", "Scissors").replace("X","Rock").replace("Y", "Paper").replace("Z", "Scissors") for s in round_split])
#Seperate each element
round_tuple = (np.char.split(round_split_replace, sep = ' '))


### Pt 2 : X, Y , Z now means Lose, Draw, Win. 

#Only rename A, B and C
round_split_pt2_replace = ([s.replace("A","Rock").replace("B", "Paper").replace("C", "Scissors") for s in round_split])
round_tuple_pt2 = (np.char.split(round_split_pt2_replace, sep = ' '))

#Code to map players twos input 'X', 'Y', 'Z' to lose, draw, win. 
for i in round_tuple_pt2:
    # Replace all Ys with the same element
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

#Run part 1
player_1, player_2 = rock_paper_scissors(round_tuple=round_tuple, player_1=player_1, player_2=player_2)

print("For Part 1, Players 1 score is:", sum(player_1), ", My score is:", sum(player_2))

#Run part 2
player_1 = []
player_2 = []

player_1, player_2 = rock_paper_scissors(round_tuple=round_tuple_pt2, player_1=player_1, player_2=player_2)

print("For Part 2, Players 1 score is:", sum(player_1), ", My score is:", sum(player_2))
