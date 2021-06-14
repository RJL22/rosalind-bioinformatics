# Finds the probablility that two organisms will produce an
# organism that expresses the dominant trait.


d = int(input("Enter homozygous dominant count: "))
h = int(input("Enter heterozygous count: "))
r = int(input("Enter homozygous recessive count: "))

t = d + h + r

recessive_probability = (r / t) * ((0.5 * h) + r - 1) / (t - 1)
recessive_probability += (h / t) * ((0.25 * h) + (0.5 * r) - 0.25) / (t - 1)

dominant_probability = 1 - recessive_probability

print(dominant_probability)
