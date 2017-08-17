# PYTHON3 FILE

largest = None
smallest = None

while True:
    num = input("Enter a number :")
    try :
        num = int(num)
        if smallest == None :
            smallest = num
        if largest == None :
            largest = num
        if num > largest :
            largest = num
        if num < smallest :
            smallest = num
    except :
        if num == "done" :
            break
        else :
            print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
