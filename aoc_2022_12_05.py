#Instructions : https://adventofcode.com/2022/day/5

#Import packages
import numpy as np
import re

#Def function
def grab_item(amount, col_start, col_end,current_state, part_no):
    #Elements 'grabbed' by claw
    inital_col = current_state[:,col_start - 1]

    grabbed = list(filter(None, np.char.strip(inital_col)))[0:amount]
    #Reverse the order as the bottom items get placed first
    if part_no == 1:
        grabbed = list(reversed(grabbed))

    #update inital_col to remove the elements taken
    taken_col_no_null = (list(filter(None, np.char.strip(inital_col)))[amount:])
    #Fill taken col with NA
    length_null_taken = len(extended_matrix) - (len(taken_col_no_null))
    nulls_for_taken = list(np.full((1,length_null_taken), ' ', dtype = str))
    update_taken =  (list(nulls_for_taken[0]) + list(taken_col_no_null))
    #Replace column
    current_state[:, col_start -1] = update_taken

    #Column after elements have been added to new col
    drop = (grabbed + list(current_state[:,col_end - 1]))

    #Remove the nulls to get it in order
    drop_no_null = (list(filter(None, np.char.strip(drop))))

    #Add in the nulls again at the end (make it the same shape as extended matrix)
    length_null = len(extended_matrix) - len(drop_no_null)

    nulls = list(np.full((1,length_null), ' ', dtype = str))
    new_col = (list(nulls[0]) + list(drop_no_null))

    #Replace old col current_state[:,col_end - 1] with new_col
    current_state[:, col_end -1] = new_col

    return(current_state)

# Open data

with open ('aoc_data_05.txt') as f:
    txt = f.read()

#Split the text into the inital state and instructions
initial_state, instructions = (txt.split("move", 1))
#Get each line as a seperate row
initial_state = initial_state.split("\n") 

#Get each entry as a seperate element
instructions = (instructions.split("\n"))
#Seperate at the words "move", "to", and "from", keeping only the numbers. 
for i in range(len(instructions)):
    instructions[i] = (re.split(r"move|to|from", string = instructions[i]))

#Remove all the empty strings
for j in range(len(instructions)):
    instructions[j] = (list(filter(None, instructions[j])))

#I need to get these 'column' into a np array. Is it possible to split a text file into columns?

#This gives us rows not columns

# 1st element : 1
# 2nd element : 5
# 3rd element : 9
# 4th element : 13
# nth element : 4n - 3

rows = [[] for _ in range(8)]

for i in range(8):
    for j in range(10):
        rows[i].append(initial_state[i][4*j - 3])

matrix = (np.stack((np.array(rows[0][1:]),np.array(rows[1][1:]), np.array(rows[2][1:]),np.array(rows[3][1:]),np.array(rows[4][1:]), np.array(rows[5][1:]), np.array(rows[6][1:]), np.array(rows[7][1:])),axis=0))

#Select the column and the height
#matrix[:,col_no-1][height-1]

#We want to convert the instructions into integers

for i in range(len(instructions)):
    instructions[i] = [int(item) for item in instructions[i]]

#We need to add some extra height to the array
empty_array = (np.full((50,9), ' ', dtype = str))

extended_matrix = (np.array(list(empty_array) + list(matrix)))

#Create initial state
current_state_pt1 = extended_matrix.copy()


for i in instructions:
    amount, col_start, col_end = i
    current_state_pt1 = grab_item(amount=amount, col_start=col_start, col_end=col_end, current_state=current_state_pt1, part_no = 1)

#Seperate out each colum, drop the empty strings, find the top value
#print(list(filter(None, current_state[:,0].strip())))

print("Part 1 State : ", current_state_pt1)

for i in range(9):
    print("Part 1 top items : ", list(filter(None, np.char.strip(current_state_pt1[:,i])))[0])

## PT2 : The crane can now pick up multiple items at the same time
#I.e. you don't need to reverse the order

current_state_pt2 = extended_matrix.copy()

for i in instructions:
    amount, col_start, col_end = i
    current_state_pt2 = grab_item(amount=amount, col_start=col_start, col_end=col_end, current_state=current_state_pt2, part_no = 2)

print("Part 2 State : ", current_state_pt2)

for i in range(9):
    print("Part 2 top items : ", list(filter(None, np.char.strip(current_state_pt2[:,i])))[0])