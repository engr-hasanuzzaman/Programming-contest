class Solution:
	def stockBuySell(self, A, n):
		#code here
		start_day = 0
		ans = []
		current_price = A[0]
		for i in range(1,n):
		    if A[i] <= current_price:
		        if start_day != i - 1 and i - 1 > start_day:
		            ans.append([start_day, i-1])
		        start_day = i 
		    current_price = A[i]
		if start_day < n - 1:
		    ans.append([start_day, n - 1])
		return ans