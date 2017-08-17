# PYTHON3 FILE
# This version is the harcoded version of the 1st assignment
# of the Python Datastructures course

text = "X-DSPAM-Confidence:      0.8475"
colon = text.find(':')
text = text[colon +1:]
text = text.lstrip()
text = float(text)
print(text)
