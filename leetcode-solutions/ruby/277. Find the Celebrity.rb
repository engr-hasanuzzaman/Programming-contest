# https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# @param {Integer} person a
# @param {Integer} person b
# @return {Boolean} whether a knows b
# def knows(a, b)

# @param {Integer} n
# @return {Integer}
def find_celebrity(n)
    knows_graph = Array.new(n){Array.new(n){0}}
    n.times do |person|
        if known_to_all?(person, knows_graph, n) && !knowns_anyone?(person, knows_graph, n)
            return person
        end
    end
    # puts "--- #{knows_graph}"
    -1
end

def known_to_all?(target, knows_graph, n)
    n.times do |person|
        next if person == target
        # call API if needed
        if knows_graph[person][target] == 0
            knows_graph[person][target] = knows(person, target)
        end

        if !knows_graph[person][target]
            return false
        end
    end
    
    true
end

def knowns_anyone?(target, knows_graph, n)
    n.times do |person|
        next if person == target
        if knows_graph[target][person] == 0
            knows_graph[target][person] = knows(target, person)
        end

        return true if knows_graph[target][person]
    end
    
    false
end