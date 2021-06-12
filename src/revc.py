# Finds the reverse complement strand of a given DNA sequence


sequence = input("Enter DNA sequence: ")
revc_sequence = ""

sequence_length = len(sequence)

for i in range(sequence_length):
	nucleotide = sequence[sequence_length - 1 - i]
	if nucleotide == 'A':
		revc_sequence += 'T'
	elif nucleotide == 'T':
		revc_sequence += 'A'
	elif nucleotide == 'G':
		revc_sequence += 'C'
	elif nucleotide == 'C':
		revc_sequence += 'G'

print(revc_sequence)