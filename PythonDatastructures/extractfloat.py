# PYTHON3 FILE
# This version is the non-harcoded version of the 1st assignment
# of the Python Datastructures course

text = "X-DSPAM-Confidence:      0.8475"
num = None
i = 0
for charact in text :
    i = i + 1
    if charact in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'] :
        num = charact
        break
print(text[i-1:])
