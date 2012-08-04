# Matthias Pall Gissurarson 26. jul 2012
# Finding positive natural numbers such that when their last digit is put in front, they are equal to double the original number

# We know that the numbers that have this property also satisfy the equation 19x = (x mod 10)*(10^(floor(log10(x))+1) -1)
# We have 2x = (x mod 10)*(10^(floor(log10(x))) + (x - (x mod 10))/10 (This right part here is merely putting the last digit in front)
# <=> 2x - x/10 =  (x mod 10)*(10^(floor(log10(x))) - (x mod 10) /10 
# <=> 19x/10 = (x mod 10)*((10^(floor(log10(x))) - 1/10) <=> 19x =(x mod 10)*(10^(floor(log10(x))+1) -1) 
# x mod 10 is the last digit of the number, and the (10^(floor(log10(x))+1) -1) is just a number of nines equal to the number of digits 
# in the number so the reason goes that to be a candidate, 19 must be a prime factor in the 9 possibilities for each of the last 
# numbers that can appear in each digit count. We simply find those numbers, divide by 19, and thus we have a candidate x. To then 
# verify x, we check if its last digit is indeed the one we used in the possibility. If it is, we have found a number, if it isn't, we 
# discard it and move on.

import sys

# Note: does not account for leading 0's. That is: it finds the numbers, 
# but they will appear incorrect as they do not have the needed leading zero
x = 1 #We know that 0 is a solution, but as it is not positive, we disregard that.
numLength = 1
def nNines(n):
	return ''.join(['9' for i in range(n)])

maxLength = len(str(sys.maxint)) #We can't do better unless we use gmpy2 or something similar
print "Maximum numberlength on system: %d" % maxLength #We can't find that many numbers, because we are limited by the max size of our integers
#maxLength = len(str(2**31)) #32 bit system check
while numLength <= maxLength: 
	nN = int(nNines(numLength))
	for i in range(1,10): #We skip zero, as we know that it is only a factor in the solution x = 0.
		if (i*nN)%19 is 0: #19 is a primenumber, and if this i*nN does not contain 19 as a primefactor, 19x cannot be i*nN. If it is a primefactor, we have a possible candidate.
			if ((i*nN)/19)%10 is i: #It is only a right number if it satisfies the property that the last digit is indeed what we used in the multiplication.
				x = (i*nN)/19
				print x
	numLength = numLength +1



	