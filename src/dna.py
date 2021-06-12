#Counts the number of each specific nucleotides in a given DNA sequence.
#Outputs in the order of adenine, cytosine, guanine, and thymine.

sequence = input("Enter DNA sequence: ")

a = 0;
c = 0;
g = 0;
t = 0;


for i in range(len(sequence)):
	if sequence[i] == 'A':
		a += 1;
	if sequence[i] == 'C':
		c += 1
	if sequence[i] == 'G':
		g += 1
	if sequence[i] == 'T':
		t += 1

print(str(a) + " " + str(c) + " " + str(g) + " " + str(t))