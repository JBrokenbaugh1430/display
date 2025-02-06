def sum_odd_and_even(lst):
	
	even = 0
	odd = 0
	for num in lst:
		if num % 2 == 0:
			even += num
		else:
			odd += num
	return [even, odd]

_sum = sum_odd_and_even([-1, -2, -3, -4, -5, -6])
print(_sum)