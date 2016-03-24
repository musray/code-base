!# python3
# toCapital.py
# This script has 2 main parts of function:
# First part: 
# Inside the first "with" clause. This part function open the text file, read all line in that file, and trun every single word in that line into capital word. Finally put all processed results into varaible "newLines".
# Second Part;
# Inside the second with clause. This part will write all lines in the varabile "newLine" to a new file.

newLines = []
with open('strings.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        capLine = []
        for word in line.split(' '):
            capWord = word[0].upper() + word[1:].lower()
            capLine.append(capWord)

        newLines.append(' '.join(capLine))

with open('newStrings.txt', 'w') as f:
    for newLine in newLines:
        f.write(newLine) 
