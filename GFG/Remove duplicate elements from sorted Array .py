class Solution:	
	def remove_duplicate(self, A, N):
		left = 0
		right = 0
		while right < N:
		    while right < N and A[left] == A[right]:
		        right += 1
		    if right < N:
		        A[left+1] = A[right]
		        left += 1
		return left + 1