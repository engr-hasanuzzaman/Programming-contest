# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        target_color = image[sr][sc]
        visited = [[False]*len(image[0]) for _ in range(len(image))]
        image[sr][sc] = newColor
        visited[sr][sc] = True
        s = [[sr, sc]]
        max_row = len(image)
        max_col = len(image[0])
        # left, right, top, down
        neighbours = [[0, -1],[0, 1], [-1, 0], [1, 0]]
        while s:
            r, c = s.pop()
            for p in neighbours:
                n_row = r + p[0] 
                n_col = c + p[1]
                if n_row >= 0 and n_row < max_row and n_col >= 0 and n_col < max_col and image[n_row][n_col] == target_color and visited[n_row][n_col] == False:
                    image[n_row][n_col] = newColor
                    visited[n_row][n_col] = True
                    s.append([n_row, n_col])
        
        return image
