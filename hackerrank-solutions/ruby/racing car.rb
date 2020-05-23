require 'pry'

def minimumMovement(obstacleLanes)
  current_track = 2
  i = 0
  jump = 0
  while i < obstacleLanes.size
    # binding.pry
    # road clear
    if current_track != obstacleLanes[i]
      i += 1
      next
    end

    passing_track = []
    has_jump = false
    new_index = j
    loop_end = true
    for j in i...obstacleLanes.size
      # binding.pry
      has_jump = true
      if passing_track.size < 2 || passing_track.include?(obstacleLanes[j])
        unless passing_track.include?(obstacleLanes[j])
          passing_track << obstacleLanes[j]
        end
      else
        current_track = obstacleLanes[j]
        new_index = j
        loop_end = false
        break
      end
      new_index = j
    end

    jump += 1 if has_jump
    i = new_index
    break if loop_end
  end

  jump
end
#       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]  
input = [2, 1, 3, 2]#[1, 1, 2, 2, 3, 1, 2, 3, 2, 3, 2, 1, 3, 3, 2, 1, 1, 3, 3, 3, 3, 1, 1, 2, 2, 3, 2, 1, 3, 3, 3, 1]
puts "input size is #{input.size}"
puts minimumMovement(input)