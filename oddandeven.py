import ast

def sum_odd_and_even(lst):
	
	even = 0
	odd = 0
	for num in lst:
		if num % 2 == 0:
			even += num
		else:
			odd += num
	return [even, odd]

arr = input('Enter an array of numbers.\nThe first element will be the sum of all even numbers, and the second, odd.\n')
arr = ast.literal_eval(arr)
print(sum_odd_and_even(arr))
