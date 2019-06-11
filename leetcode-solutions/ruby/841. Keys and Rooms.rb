# https://leetcode.com/problems/keys-and-rooms/

# @param {Integer[][]} rooms
# @return {Boolean}
def can_visit_all_rooms(rooms)
  visited = []
  rooms.size.times { visited << [] }
  r_visit = []
  
  dfs(rooms, visited, r_visit)
  
  rooms.size.times do |i|
      return false unless r_visit[i]
  end
  
  true
end

def dfs(rooms, visited, r_visit)
  stack = rooms.first
  stack.each {|j| visited[0][j] = true }
  r_visit[0] = true
  
  until stack.empty?
      i = stack.pop
      r_visit[i] = true
      
      rooms[i].size.times do |j|
          if valid?(i, j, visited)
              stack << rooms[i][j]
              visited[i][j] = true
          end
      end
  end
end

def valid?(i, j, visited)
  !visited[i][j]
end