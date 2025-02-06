def is_curzon(num):
	if (1 + (2**num)) % (1 + 2*num) == 0:
		return True
	else:
		return False
	
result = int(input("Type a number to see if it's a Curzon number\n"))
print(is_curzon(result))
