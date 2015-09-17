#100% solution to Tape Equilibrium problem on Codility.com#
####TIME COMPLEXITY: O(n) SPACE COMPLEXITY: O(1)###
########################################

def solution(A):
	sumTotal = 0
	minDiff = 0
	for i in xrange(len(A)):
		sumTotal += A[i]
		minDiff += abs(A[i]) #guarantees that this number is larger than any in the array
		
	sumLeft = 0
	
	for i in xrange(len(A)-1):
	    sumLeft += A[i] 
	    sumTotal -= A[i]
	    minDiff = min(minDiff,abs(sumTotal - sumLeft)) 
	    
	return minDiff
	
	
