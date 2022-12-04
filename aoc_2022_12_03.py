#Instructions : https://adventofcode.com/2022/day/3

#Import packages
import numpy as np

#Open data
with open ('aoc_data_03.txt') as f:
    text = f.read()

#Seperate data on new empty lines, this groups each set together. E.g. ('17998\n7761')
line_sep = np.array(text.split('\n\n'))

#Seperate each element in a group by the new lines.
elements_sep = (np.char.split(np.array(line_sep),sep='\n'))
elements_sep = np.array(elements_sep)[0]

# First backpack contains 42 elements, so needs to be split in half (21 elements each)
common_element = []
for i in elements_sep:
    first_half = i[0:len(i)//2]
    second_half = i[len(i)//2:]
    common_element.append(list(set(first_half).intersection(second_half)))
    #print(np.intersect1d(first_half, second_half))

priorities = []

for i in range(len(common_element)):    
    if common_element[i][0].isupper():
        priorities.append(ord(common_element[i][0])-38)
    else:
        priorities.append(ord(common_element[i][0])-96)

print("The sum of all priorities for elements that occur in both compartments is :", sum(priorities))

# Pt 2: Now each grouping is every 3 lines and we find the common element that occurs once in those 3 lines. 

#Split the array into every 3 sections (There are 300 lines so 100 even sections)
group_backpack = np.split(np.array(elements_sep),100)

group_code = []

for i in group_backpack:
    group_code.append(list(set(i[0]).intersection(set(i[1])).intersection(i[2])))

priorities_group = []

for i in range(len(group_code)):    
    if group_code[i][0].isupper():
        priorities_group.append(ord(group_code[i][0])-38)
    else:
        priorities_group.append(ord(group_code[i][0])-96)

print("The sum of all priorities for elements that occur in all 3 backpacks per group is :", sum(priorities_group))