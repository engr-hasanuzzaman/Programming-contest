# https://leetcode.com/problems/car-pooling/

# solution 1
# create array with max trip length
# if the max visit be very large the array will be very large and solution will not be very efficient
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        visit = [0] * 1001
        
        for t in trips:
            visit[t[1]] += t[0]
            visit[t[2]] -= t[0]

        sum = 0
        for v in visit:
            sum += v
            if sum > capacity:
                return False
        return True

# solution:
# instead of keeping visit info on array, create a tuple for eache visit info
# for each visit, add (start, capacity) & (end, -capacity) and sort the array with first element
# visit each elment and sum the visitors, if any point vigitor number be > capacity return False
# otherwise return True 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        visit = []
        
        for t in trips:
            visit.append((t[1], t[0]))
            visit.append((t[2], -t[0]))
        visit.sort()
        sum = 0
        for v in visit:
            sum += v[1]
            if sum > capacity:
                return False
        return True
