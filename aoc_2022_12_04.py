#Instructions : https://adventofcode.com/2022/day/4

#Import packages
import numpy as np
# Open data
data = (np.loadtxt(fname='aoc_data_04.txt',dtype=str))

#Create np.aranges for each elfs cover
elf_1_cover = []
elf_2_cover = []

for i in data:
    #Elf 1
    elf_1_cover.append(set(np.arange(start = (int(str(i.split(',')[0]).split('-')[0])), stop = (int(str(i.split(',')[0]).split('-')[1])+1))))
    #Elf 2:
    elf_2_cover.append(set(np.arange(start = (int(str(i.split(',')[1]).split('-')[0])), stop = (int(str(i.split(',')[1]).split('-')[1])+1))))

#Check if there is a union between the covers
overlap_true = []

for j in range(len(elf_1_cover)):
    overlap = []
    overlap.append([(elf_1_cover[j].union(elf_2_cover[j]) == elf_1_cover[j]),(elf_2_cover[j].union(elf_1_cover[j]) == elf_2_cover[j])])
    overlap_true.append(np.array(overlap).any(axis=1))

#Sum how many times there was a overlap
print(sum(overlap_true)[0])

#Pt 2: How many total overlaps (pt 1 was complete overlaps) occur. 
overlap_len = []
for k in range(len(elf_1_cover)):
    overlap_len.append(len((elf_1_cover[k]) & (elf_2_cover[k])))

#Count how many times the overlap length was 0 and then subtract that from total length
print(len(elf_1_cover) - overlap_len.count(0))