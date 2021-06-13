# Identifies the highest GC-content of a given database of DNA sequences

lines = []
with open("data.txt") as f:
	lines = f.readlines()

database = {}

currentID = ""
currentSequence = ""

#Highest GC-content percentage and ID
hgcp = 0;
hID = "";

#Current GC-content percentage
cgcp = 0;

for line in lines:
	#Removes newline characters
	appendableLine = line.rstrip("\n")

	#First if statement is for initial entry
	if currentID == "":
		currentID = appendableLine
	elif appendableLine[0] == '>':
		#Check if previous data entry was the highest percentage
		for nucleotide in currentSequence:
			if nucleotide == 'G' or nucleotide == 'C':
				cgcp += 1

		if cgcp / len(currentSequence) > hgcp:
			hgcp = cgcp / len(currentSequence)
			hID = currentID

		cgcp = 0

		database[currentID] = currentSequence
		currentID = appendableLine
		currentSequence = ""
	else:
		currentSequence += appendableLine

#Checks last data entry
for nucleotide in currentSequence:
	if nucleotide == 'G' or nucleotide == 'C':
		cgcp += 1

if cgcp / len(currentSequence) > hgcp:
	hgcp = cgcp / len(currentSequence)
	hID = currentID

#Converting decimal to percentage
hgcp *= 100

print(hID)
print(hgcp)

