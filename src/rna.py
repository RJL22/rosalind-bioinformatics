#Converts DNA sequence into RNA sequence

dna_sequence = input("Enter DNA sequence: ")

rna_sequence = ""


for i in range(len(dna_sequence)):
	if dna_sequence[i] == 'T':
		rna_sequence += 'U'
	else:
		rna_sequence += dna_sequence[i]

print(rna_sequence)