from collections import deque

def read_file():
    file = open("input.in", 'r')

    #read first line
    L, R, C = [int(n) for n in file.readline().split(" ")]
    # print("-----L, R, C is ", L, R, C)
    input = []
    for _ in range(L):
        for _ in range(R):
            input.append(file.readline())
        # skip new line
        file.readline()
    # print("---the input data is ", input)
    return input, R, C

def escape_dungeon(input, R, C):
    # find the start
    s_row, s_col = -1, -1
    for row in range(R):
        for col in range(C):
            if input[row][col] == 'S':
                s_row, s_col = row, col
                break
        if s_row != -1:
            break
    
    # no starting point
    if s_col == -1:
        return False
    
    #bfs for visiting neighbors
    queue = deque([])
    visited = [[False] * C for _ in range(R)]
    queue.append((s_row, s_col))
    visited[s_row][s_col] = True
    
    while queue:
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()

            # right
            n_row, n_col = r, c + 1
            # out of boundary 
            if n_row < 0 or n_col < 0 or n_row >= R or n_col >= C:
                continue

            # block or already visited
            if input[n_row][n_col] != '.' or visited[n_row][n_col]:
                continue
            
            # keep on queue
            if input[n_row][n_col] == 'E':
                return True
            
            queue.append((n_row, n_col))
    return False

input, R, C = read_file()
assert escape_dungeon(input, R, C) == False