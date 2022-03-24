import random

row = 5
col = 10
digit = 3

for x in range(1, row*col+1):
	num = random.randint(1,pow(10, digit) - 1)
	cell = "%" + str(digit) + "d "
	print(cell % num, end="")
	if x % col == 0:
		print()
