# PYTHON3 FILE

# Import regex lib
import re

# Open file and declare the 2 lists
hand = open('regex_sum_32420.txt')
lst = list()
nums = list()
# Look for numbers in each lines
for line in hand :
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    # Find all data inside each num because there are some
    # num with more than one number and convert it to an int
    # before adding it to a new list
    for data in num :
        data = int(data)
        nums.append(data)
print(sum(nums))
