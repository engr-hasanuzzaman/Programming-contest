# https://leetcode.com/problems/lru-cache/

class LRUCache
  # attr_accessor 
=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        @dict = Hash.new
        @capacity = capacity
        @cur_size = 0
        @d_link = DLink.new
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        return -1 if @cur_size.zero?
        
        node = @dict[key]
        if node
            node.val
        else
            -1
        end
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        if @dict[key]
            @dict[key].val = value #ensure to update value
            @d_link.move_to_tail(@dict[key])
        else
            n_node = Node.new(key, value)
            
            if @capacity == @cur_size
                # remove least used item and insert new key to tail
                r_node = @d_link.remove
                node = @d_link.add(value)
                @dict[key] = node
            else
                node = @d_link.add(value)
                @dict[key] = node
            end
        end
    end


end

# dlink list implementaion 
class Node
    attr_accessor :next, :prev, :val, :key
    
    def initialize(val, key)
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
       
        node
    end
    
    # always remove from head as that is least used     
    def remove
        head = @head
        
        @head.next.prev = nil
        @head = @head.next
        
        # return head node
        head
    end
    
    def move_to_tail(node)
        return if node == @tail
        
        if node == @head
            @head = @head.next
            @head.prev = nil
        else
            node.prev.next = node.next
            node.next.prev = node.prev
        end
        
        @tail.next = node
        node.prev = @tail
        @tail = node
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

dl = DLink.new()
n = Node.new(1 , 2)
dl.add(n)
dl.add(Node.new(2, 'k'))
dl.add(Node.new(3, 'k'))
puts "after put 1,2,3 DLink #{dl.to_list}"
dl.move_to_tail(n)
puts "after move to tail #{dl.to_list}"
dl.remove
puts "after remove #{dl.remove}"