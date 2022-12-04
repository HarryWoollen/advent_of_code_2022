#Import packages
import numpy as np

#Open data
with open ('aoc_1_data.txt') as f:
    text = f.read()

#Seperate data on new empty lines, this groups each set together. E.g. ('17998\n7761')
line_sep = np.array(text.split('\n\n'))

#Seperate each element in a group by the new lines.
elements_sep = (np.char.split(np.array(line_sep),sep='\n'))

#Set the elements to integers rather than strings
for i in range(len(elements_sep)):
    elements_sep[i] = [int(item) for item in elements_sep[i]]

#Get the sum of each grouping
output = []

for elf in elements_sep:
    output.append(sum(elf))

#Convert to numpy array for easy operations.
output = np.array(output)
#Print answer and elf location
print("The answer to part 1 is,", output.max(), " Which occurs on elf number", output.argmax())

#So the 215th Elf is carrying the most calories, with 67658.

# Pt 2 : Find the top 3 elves carrying the most calories, what is the sum of their total.
#We sort by the summed output, then we reverse the order and return the top 3 elements summed.
print("The answer to part 2 is,", sum(np.sort(output)[::-1][0:3]))

#So the top 3 elves are colectively carrying 200158 calories. 

