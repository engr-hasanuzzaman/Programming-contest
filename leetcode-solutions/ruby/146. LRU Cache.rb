# https://leetcode.com/problems/lru-cache/

class LRUCache
    def initialize(capacity)
        @dict = Hash.new
        @capacity = capacity
        @cur_size = 0
        @d_link = DLink.new
    end

    def get(key)
        return -1 if @cur_size.zero?
        
        node = @dict[key]
        if node
            @dict[key] = @d_link.move_to_tail(node)
            node.val
        else
            -1
        end
    end

    def put(key, value)
        if @dict[key]
            @dict[key].val = value #ensure to update value
            @dict[key] = @d_link.move_to_tail(@dict[key])
        else
            n_node = Node.new(key, value)
            
            if @capacity == @cur_size
                r_node = @d_link.remove
                node = @d_link.add(n_node)
                @dict[key] = node
                @dict.delete(r_node.key)
            else
                node = @d_link.add(n_node)
                @dict[key] = node
                @cur_size += 1
            end
        end
    end

    def to_list
        @d_link.to_list
    end
  end
  
  # dlink list implementaion 
  class Node
      attr_accessor :next, :prev, :val, :key
      
      def initialize(key, val)
          self.next = nil
          self.prev = nil
          self.val = val
          self.key = key
      end
  end
  
# LRU doubley linklist
class DLink
    def initialize
        @head = nil
        @tail = nil
        @length = 0
    end
    
    def add(node)
        # head do not exist
        if !@head
            @head = node
            @tail = node
        else
            @tail.next = node
            @tail.next.prev = @tail
            @tail = @tail.next
        end
        
        @tail
    end
    
    # always remove from head as that is least used     
    def remove
        if @head == @tail
            head = @head
            @head = nil
            return head
        end

        head = @head
        
        @head.next.prev = nil #make prev value of new head null
        @head = @head.next
        
        # return head node
        head
    end
    
    def move_to_tail(node)
    #   puts "move to tail k, v #{node.key}, #{node.val}"
        if node.key == @tail.key
            @tail.val = node.val # ensure update value
            return @tail 
        end
        
        n_node = Node.new(node.key, node.val) #prevent ref overriding
        
        if node.key == @head.key
            @head = @head.next
            @head.prev = nil
        else
            node.prev.next = node.next
            node.next.prev = node.prev
        end
        
        add(n_node)
    end

    def to_list
        list = []
        node = @head
        while node
            list << node.val
            node = node.next
        end

        list
    end
end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value) 

# dl = DLink.new()
# n = Node.new(1, 'v1')
# n2 = Node.new(2, 'v2')
# n3 = Node.new(3, 'v3')
# n4 = Node.new(4, 'v4')

# dl.add(n)
# dl.add(n2)
# dl.add(n3)
# puts "after put 1,2,3 DLink #{dl.to_list}"
# dl.move_to_tail(n)
# puts "after move to tail #{dl.to_list}"
# puts "remove #{dl.remove.val}"
# puts "after move to tail #{dl.to_list}"
# dl.add(n4)
# puts "after move to tail #{dl.to_list}"

# 1st test
cache = LRUCache.new(2)
c.put(1, 'v1')
c.put(2, 'v2')
c.put(3, 'v3')
c.put(4, 'v4')
p "-- #{c.to_list}"
c.get(2)
p "-- #{c.to_list}"

# 2nd test
# cache = LRUCache.new(3)
# cache.put(1, 1);
# cache.put(2, 2);
# cache.put(3, 3);
# cache.put(4, 4);
# puts cache.get(4);   # returns 1
# puts cache.get(3);   # returns 1
# puts cache.get(2);   # returns 1
# puts cache.get(1);   # returns 1
# cache.put(5, 5);
# puts cache.get(1);   # returns 1
# puts cache.get(2);   # returns 1
# puts cache.get(3);   # returns 1
# puts cache.get(4);   # returns 1
# puts cache.get(5);   # returns 1