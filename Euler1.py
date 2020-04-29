import math

import sys

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)



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
def PythTriplet(PERIMETER):
	# A Pythagorean triplet is a set of three natural numbers,
		# a < b < c, for which,
		# a2 + b2 = c2
		# For example, 32 + 42 = 9 + 16 = 25 = 52.
	# There exists exactly one Pythagorean triplet for which 
		# a + b + c = 1000. Find the product abc.
	# a^2 + b^2 = c^2 and a+b+c=1000
	# Method: Find all perfect squares < 1000. Find all combinations of
		# a + b + c = 1000. Find which one is a pythagorean triplet.
	for a in range(1, PERIMETER + 1):
		for b in range(a+1, PERIMETER + 1):
			c = PERIMETER - a - b
			if (a * a + b * b == c * c):
				# It is now implied that b < c, because we have a > 0
				return str(a * b * c)
##### Project Euler Problem 10:
def sumPrimes(PERIMETER):
	# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	# Find the sum of all the primes below two million.
	return sum(sieve_of_atkin(PERIMETER))

##### Project Euler Problem 11:
	# What is the greatest product of four adjacent numbers in the 
		#same direction (up, down, left, right, or diagonally) 
		# in the 20×20 grid?
def int_form(str_grid):
	# Turn the grid of strings into integers
	# Split each line by spaces. Iterate through and create a 
		# new array of ints
	lines = []
	for line in str_grid:
		split_line = line.split()
		new_line = []
		for elem in split_line:
			num = int(elem)
			new_line.append(num)
		lines.append(new_line)
	return lines

def product(valx,valy,dx,dy,CONSEC,grid):
	# Find the product of CONSEC number adjacent values in grid
		# based on dx and dy
	output = 1
	for i in range(CONSEC):
		output *= grid[valy + dy*i][valx + dx*i]
	return output

def highest(input_grid, NUMBERS):
	
	# String grid to int grid
	GRID = int_form(input_grid)
	ans = -1
	width = len(GRID[0])
	height = len(GRID)
	
	# Find each product	
	for y in range(height):
		for x in range(width):
			if x + NUMBERS <= width:
				ans = max(product(x,y,1,0,NUMBERS,GRID),ans)
			if y + NUMBERS <= height:
				ans = max(product(x,y,0,1,NUMBERS,GRID),ans)
			if x + NUMBERS <= width and y + NUMBERS <= height:
				ans = max(product(x,y,1,1,NUMBERS,GRID),ans)
			if x + NUMBERS >= -1 and y + NUMBERS <= height:
				ans = max(product(x,y,-1,1,NUMBERS,GRID),ans)
	return ans

string_grid = ['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08',\
		'49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00',\
		'81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65',\
		'52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91',\
		'22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',\
		'24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',\
		'32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',\
		'67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',\
		'24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',\
		'21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',\
		'78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',\
		'16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',\
		'86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',\
		'19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',\
		'04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',\
		'88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',\
		'04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36',\
		'20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16',\
		'20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54',\
		'01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48']		

##### Project Euler Problem 12:
def triangle_number(n):
	# Finds the ith triangle number (defined as 1+2+...+i)
	if n==1:
		tri = 1
	else:
		#tri = triangle_number(n-1)+n
		tri = n*(n+1)/2
	return tri
def factors(NUMBER):
	# creates list of all factors of a number
	mylist = []
	for f in range(1,math.floor(NUMBER/2)):
		if NUMBER%f == 0:
			mylist.append(f)
			mylist.append(int(NUMBER/f))
	mylist = list(dict.fromkeys(mylist))	
	mylist.sort()
	return mylist
def divisible_number(FACTORS):
	# The sequence of triangle numbers is generated by adding the
		#natural numbers. So the 7th triangle number would be:
		# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
		# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
	# Let us list the factors of the first seven triangle numbers:
		# 1: 1
		# 3: 1,3
		# 6: 1,2,3,6
		# 10: 1,2,5,10
		# 15: 1,3,5,15
		# 21: 1,3,7,21
		# 28: 1,2,4,7,14,28
	# We can see that 28 is the first triangle number to have 
		# over five divisors.
	# What is the value of the first triangle number to have over 
		#five hundred divisors?
	NUMBER_OF_FACTORS = 0
	i = 12300
	# i = 0
	while NUMBER_OF_FACTORS <= FACTORS:
		i += 1
		NUMBER_OF_FACTORS = len(factors(triangle_number(i)))
		print(i)
		print(triangle_number(i))
		print(NUMBER_OF_FACTORS,'\n')
	return triangle_number(i)

if __name__ == "__main__":
	with recursionlimit(1000000):
		print(divisible_number(500))
