#Iterate through, store the most recent 4. Check all unique.
import numpy as np
from collections import Counter
data = (np.loadtxt(fname='aoc_data_06.txt',dtype=str))

def count_distinct_char(num_chars, data):
    for i in range(len(str(data))):
        if len(set(str(data)[i:i+num_chars])) == num_chars:
            print(i + num_chars)
            break   

#Pt 1
print("The start of packet marker begins at character:", count_distinct_char(4,data))

## Pt 2 : Repeat for 14 characters rather than 4
print("The start of message marker begins at character:", count_distinct_char(14,data))
