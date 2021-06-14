# Translates a RNA sequence into a chain of amino acids


#Read in data for rna codon table
lines = []
with open("../res/rna-codon-table.txt") as f:
	lines = f.readlines()

codon_table = {}

for l in lines:
	line = l.rstrip('\n')
	codon_table[line[0:3]] = line[4:]

#Get RNA sequence input
sequence = ""
with open("/PATH/TO/FILE") as file:
	sequence = file.read()

#Convert RNA sequence to chain of amino acids
chain = ""
for i in range(int(len(sequence) / 3) - 1):
	chain += codon_table[sequence[(i * 3):((i * 3) + 3)]]

print(chain)
