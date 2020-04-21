def multiples(cap, *factors):
	# Project Euler Problem 1:
	# If we list all the natural numbers below 10 that are multiples 
		# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples
		# is 23. Find the sum of all the multiples of 3 or 5 below 1000.
	# Method: create list of all multiples of user supplied factors 
		# less than the user supplied cap. Delete duplicates and sum.

	mylist = []
	for x in range(cap+1):
		for num in factors:
			if num*x < cap:
				mylist.append(num*x)
	mylist = list(dict.fromkeys(mylist))
	out = sum(mylist)
	return out

print(multiples(1000,3,5))
