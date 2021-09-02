i = 0
j = 1

min_ = 0
max_ = 1000 

print("Printing fibonacci numbers from " + str(min_) + " to " + str(max_))

while i < min_:
	temp = j
	j += i
	i = temp

while j < max_:
	print(i)
	temp = j
	j += i
	i = temp