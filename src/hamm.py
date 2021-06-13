#Counts the point mutations (hamming distance) between 2 sequences


s = input("Enter first sequence: ")
t = input("Enter second sequence: ")

count = 0


for i in range(len(s)):
	if s[i] != t[i]:
		count += 1

print(count)