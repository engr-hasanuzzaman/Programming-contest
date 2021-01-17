
'''
problem:
Given an image of size n*m, location of a pixel in the screen i,e(sr, cc) and 
color newColor, your task is to replace color of the given pixel and 
all adjacent(excluding diagonally adjacent) same colored pixels with the given color newColor.
'''
# solve using BFS
from collections import deque

class Solution:
	def floodFill(self, images, sr, sc, newColor):
	    row_size = len(images)
	    if row_size == 0:
	        return
	    col_size = len(images[0])
	    visited = [[False] * col_size for _ in range(row_size)]
	    target_color = images[sr][sc]
	    visited[sr][sc] = True
	   
	    images[sr][sc] = newColor
	    q = deque([(sr, sc)])
	    while q:
	        c_size = len(q)
	        for _ in range(c_size):
	            i, j = q.pop()
	            # left     
	            if j > 0 and not visited[i][j-1] and images[i][j-1] == target_color:
	                deque.appendleft(q, (i, j-1))
	                visited[i][j-1] = True
	                images[i][j-1] = newColor
	            # right
	            if j+1 < col_size and not visited[i][j+1] and images[i][j+1] == target_color :
	                deque.appendleft(q, (i, j+1))
	                visited[i][j+1] = True    
	                images[i][j+1] = newColor
	           
	            # top
	            if i > 0 and not visited[i-1][j] and images[i-1][j] == target_color:
	                deque.appendleft(q, (i-1, j))
	                visited[i-1][j] = True
	                images[i-1][j] = newColor
	            # bottom
	            if i+1 < row_size and not visited[i+1][j] and images[i+1][j] == target_color:
	                deque.appendleft(q, (i+1, j))
	                visited[i+1][j] = True
	                images[i+1][j] = newColor
		return images