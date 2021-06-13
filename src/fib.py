# Given an original pair of rabbits that give birth to a litter of size k, find
# the total number of rabbits pairs (assuming no rabbits die)

n = int(input("Enter n (generation number): "))
k = int(input("Enter k (litter size): "))

sequence = [1, 1, int(k) + 1]

while len(sequence) < int(n):
	sequence.append((k * sequence[len(sequence) - 2]) + sequence[len(sequence) - 1])

print(sequence[n - 1])