# PYTHON3 FILE

# Create a new empty list
numlist = list()
while True:
    inp = input('Enter a number or done : ')
    if inp == 'done' : break
    # Convert the value to a float number
    value = float(inp)
    # Add value to the list
    numlist.append(value)
    # Average using built in functions
average = sum(numlist)/len(numlist)
print('Average :', average)
