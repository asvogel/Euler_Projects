import math
##### Project Euler Problem 1:
def multiples(cap, *factors):
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
##### Project Euler Problem 2:
def fibs(cap,*factors):
	# Each new term in the Fibonacci sequence is generated by
		# adding the previous two terms. By considering the terms 
		# in the Fibonacci sequence whose values do not exceed four 
		# million, find the sum of the even-valued terms.
	# Method: create list of all fibonacci terms that are divisible by
		# any of the factors. Delete duplicates. Find sum.
	fib_nums = [2,1]
	mylist = [2]
	i = 1
	while fib_nums[1] < cap:
		fib_nums = [(fib_nums[1]+fib_nums[0]), fib_nums[0]]
		print(fib_nums)
		for num in factors:
			if (fib_nums[1]%num == 0):
				mylist.append(fib_nums[1])
	mylist = list(dict.fromkeys(mylist))
	out = sum(mylist)
	return out
##### Project Euler Problem 3:
def largest_prime(cap):
	# What is the largest prime factor of the number 600851475143 ?
	# Method: Use Sieve of Atkin to find all primes less than sqrt(num)
		# Find largest one that is a factor
	primes = sieve_of_atkin(cap)
	primes.sort(reverse=True)
	for num in primes:
		if (cap%num == 0):
			return num
	return 0
def sieve_of_atkin(ceiling):	
	#cap = int(math.sqrt(ceiling))+1
	cap = ceiling
	# We know 2 and 3 are prime.
	primes = [2,3]
	# Initialize the sieve with FALSE
	sieve = [False] * (cap+1)
	# sieve[n]=True if one of the following:
		# (a) n = (4*x*x)+(y*y) has an odd num of solutions
			# e.g. an odd number of (x,y) pairs exist that satisfy
			# n%12 = 1 or 5
		# (b) n = (3*x*x)+(y*y) has an odd num of solutions & n%12 = 7
		# (c) n = (3*x*x)-(y*y) has an odd num of solutions, x>y, 
			# and n%12=11
	x = 1
	while (x*x < cap):
		y = 1
		while (y*y < cap):
			# Part (a)
			n = (4*x*x)+(y*y)
			if (n <= cap and (n%12==1 or n%12==5)):
				sieve[n] ^= True
			# Part (b)
			n = (3*x*x)+(y*y)
			if (n <= cap and (n%12==7)):
				sieve[n] ^= True		
			# Part (c)
			n = (3*x*x)-(y*y)
			if (n <= cap and (n%12==11) and x>y):
				sieve[n] ^= True		
			y = y+1
		x = x+1
	# Remove all multiples of squares
	r = 5
	while (r*r<cap):
		if (sieve[r]):
			for i in range(r*r, cap, r*r):
				sieve[i]=False
		r=r+1
	for a in range(5, cap):
		if (sieve[a]):
			primes.append(a)
	return primes
##### Project Euler Problem 4:
def palind(dig):	
	# A palindromic number reads the same both ways. The largest
		# palindrome made from the product of two 2-digit numbers 
		# is 9009 = 91 × 99.
		# Find the largest palindrome made from the product of 
			# two 3-digit numbers.
	# Method: Try all products of three digit numbers. Check if 
		# palindrome. Find max. Not the most elegant.
	arr = []
	for i in range(10**(dig-1),10**dig):
		for n in range(9*10**(dig-1),10**dig):
			num = i*n
			if str(num) == str(num)[::-1]:
				arr.append(num)
			else:
				pass
	
	return(arr[-1])
##### Project Euler Problem 5:
def mult(num):
	# 2520 is the smallest number that can be divided by each of the
		# numbers from 1 to 10 without any remainder. What is the
		# smallest positive number that is evenly divisible by all
		# of the numbers from 1 to 20?
	# Method: Check all numbers from 999**2  down to see if it is 
		# divisible by 11-20
	i = 1
	out = 0
	while out < 1:
		for k in range(int(num/2)+1,num+1):
			if ((i*num)%k == 0 and out != -1):
				out = i*num
				print(out)
			else:
				out = -1
		if (out == -1):
			out = 0
			i = i+1
	return out
##### Project Euler Problem 6:
def sq_diff(length):
	# The sum of the squares of the first ten natural numbers is,
		# 12+22+...+102=385
	# The square of the sum of the first ten natural numbers is,
		# (1+2+...+10)2=552=3025
	# Hence the difference between the sum of the squares of the 
		# first ten natural numbers and the square of the sum is 
		# 3025−385=2640
	# Find the difference between the sum of the squares of the
		# first one hundred natural numbers and the square of the sum.
	# Method: (a+b)^2 - (a^2+b^2) is 2ab. Iterate through all of them.

	mylist = range(1, length+1)
	result = 0
	i = 0
	for num in mylist[i:]:
		for num2 in mylist[(i+1):]:
			result += 2*num*num2
		i += 1
	return result
#### Project Euler Problem 7:
def nth_prime(n):
	# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
		# we can see that the 6th prime is 13.
		# What is the 10 001st prime number?
	# Method: Find a bunch of primes. Return the 10001st.
	mylist = []
	i=10
	while len(mylist)<n:
		mylist = sieve_of_atkin(10*i*n)
		i = i*10
	return mylist[n-1]
##### Project Euler Problem 8:
def AdjNums(dig):
	# The four adjacent digits in the 1000-digit number that have 
		# the greatest product are 9 × 9 × 8 × 9 = 5832.
	# Find the thirteen adjacent digits in the 1000-digit number
		#that have the greatest product. What is the value of
		# this product?
	# Method: Go number by number and calculate it. 
	big_num = '731671765313306249192251196744265747423553491'\
		'9493496983520312774506326239578318016984801869478851843'\
		'8586156078911294949545950173795833195285320880551112540'\
		'6987471585238630507156932909632952274430435576689664895'\
		'0445244523161731856403098711121722383113622298934233803'\
		'0813533627661428280644448664523874930358907296290491560'\
		'4407723907138105158593079608667017242712188399879790879'\
		'2274921901699720888093776657273330010533678812202354218'\
		'0975125454059475224352584907711670556013604839586446706'\
		'3244157221553975369781797784617406495514929086256932197'\
		'8468622482839722413756570560574902614079729686524145351'\
		'0047482166370484403199890008895243450658541227588666881'\
		'1642717147992444292823086346567481391912316282458617866'\
		'4583591245665294765456828489128831426076900422421902267'\
		'1055626321111109370544217506941658960408071984038509624'\
		'5544436298123098787992724428490918884580156166097919133'\
		'8754992005240636899125607176060588611646710940507754100'\
		'2256983155200055935729725716362695618826704282524836008'\
		'23257530420752963450'
	i = 0
	biggest = 0
	big = 1
	while i < (len(big_num)-(dig+1)):
		for j in range(0, dig):
			big = big*int(big_num[i+j])
		if (big > biggest):
			biggest = big
		i = i+1
		big = 1
	return biggest
##### Project Euler Problem 9:
def PythTriplet(val):
	# A Pythagorean triplet is a set of three natural numbers,
		# a < b < c, for which,
		# a2 + b2 = c2
		# For example, 32 + 42 = 9 + 16 = 25 = 52.
	# There exists exactly one Pythagorean triplet for which 
		# a + b + c = 1000. Find the product abc.
	# a^2 + b^2 = c^2 and a+b+c=1000
	# Method: Find all perfect squares < 1000. Find all combinations of
		# a + b + c = 1000. Find which one is a pythagorean triplet.

	unsquared = []
	perfect_squares = []
	out = []
	for j in range(1, val):
		unsquared.append(j)
		perf_squares.append(j*j)
	
	return(out)

a = PythTriplet(1000)
print(a)
print(a[0]*a[1]*a[2])

