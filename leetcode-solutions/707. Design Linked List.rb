# https://leetcode.com/problems/design-linked-list/

# Node
class Node
  attr_accessor :next, :val
  
  def initialize(val)
      @val = val
      @next = nil
  end
end

# link list
class MyLinkedList

=begin
  Initialize your data structure here.
=end
  def initialize()
      @head = nil
      @tail = nil
      @size = 0
  end


=begin
  Get the value of the index-th node in the linked list. If the index is invalid, return -1.
  :type index: Integer
  :rtype: Integer
=end
  def get(index)
      node = n_th_node(index)
      
      if node
          node.val
      else
          -1
      end
  end


=begin
  Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
  :type val: Integer
  :rtype: Void
=end
  def add_at_head(val)
      if @head
          n_head = Node.new(val)
          n_head.next = @head
          @head = n_head
      else
          @head = Node.new(val)
          @tail = @head
      end
      
      @size += 1
  end


=begin
  Append a node of value val to the last element of the linked list.
  :type val: Integer
  :rtype: Void
=end
  def add_at_tail(val)
      if @tail
          n_tail = Node.new(val)
          @tail.next = @tail
          @tail = n_tail
      else
          @tail = Node.new(val)
          @head = @tail
      end
      @size += 1
  end


=begin
  Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
  :type index: Integer
  :type val: Integer
  :rtype: Void
=end
  def add_at_index(index, val)   
     return add_at_head(val) if index == 0
     return add_at_tail(val) if index == @size - 1
          
      p_node = n_th_node(index-1) # take nth node
      n_node = p_node.next
      
      new_node = Note.new(val)
      new_node.next = n_node
      p_node.next = new_node
  end


=begin
  Delete the index-th node in the linked list, if the index is valid.
  :type index: Integer
  :rtype: Void
=end
  def delete_at_index(index)
      # handle head & tail        
      if index == 0
          return remove_head
      end
      
      if index == @size - 1
          return remove_tail
      end
      
      # handle other
      p_node = n_th_node(index-1) # take nth node
      n_node = n_th_node(index+1) # take nth node
      p_node.next = n_node
      
      @size -= 1
  end
  
  def n_th_node(index)
      return nil if index >= @size || index < 0
      return @tail if index == @size - 1
      return @head if index == 0
      
      node = @head
      while index > 0
          node = node.next
          index -= 1
      end
  end

  def remove_head
      return unless @head
      @head = @head.next
      @size -= 1
  end
  
  def remove_tail
      return unless @tail
      
      p_node = n_th_node(index-1) # take nth node
      @tail = p_node
      @size -= 1
  end
end
  

# doubly link list
class MyLinkedList

  =begin
      Initialize your data structure here.
  =end
      def initialize()
          @size = 0
          @head = nil
          @tail = nil
          @vals = []
      end
  
  
  =begin
      Get the value of the index-th node in the linked list. If the index is invalid, return -1.
      :type index: Integer
      :rtype: Integer
  =end
      def get(index)
         return -1 if index < 0 || index >= @size
          
          node = get_node(index)
          if node
              node.val
          else
              -1
          end
      end
  
  
  =begin
      Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
      :type val: Integer
      :rtype: Void
  =end
      def add_at_head(val)
          cur_node = Node.new(val)
          cur_node.next = @head
          if @head
              cur_node.next.prev = cur_node
          end
      
          @head = cur_node
          @tail = cur_node unless @tail
          @size += 1
      end
  
  
  =begin
      Append a node of value val to the last element of the linked list.
      :type val: Integer
      :rtype: Void
  =end
      def add_at_tail(val)
          cur_node = Node.new(val)
          
          if @tail
              cur_node.prev = @tail
              @tail.next = cur_node
              @tail = cur_node
          else
              # @head = cur_node
              @head = cur_node
              @tail = cur_node
          end
          
          @size += 1
      end
  
  
  =begin
      Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
      :type index: Integer
      :type val: Integer
      :rtype: Void
  =end
      def add_at_index(index, val)
          return if index > @size || index < 0
          
          cur_node = Node.new(val)
          
          if index == @size
              add_at_tail(val)
          elsif index == 0
              add_at_head(val)
          else
              prev_node = get_node(index)
              
              puts "#{prev_node.val}, #{cur_node.val}"
              
              cur_node.prev = prev_node.prev
              cur_node.next = prev_node
              
              prev_node.prev.next = cur_node if prev_node.prev
              prev_node.prev = cur_node
          
              @size += 1
          end
          
      end
  
  
  =begin
      Delete the index-th node in the linked list, if the index is valid.
      :type index: Integer
      :rtype: Void
  =end
      def delete_at_index(index)
          return if index < 0 || index >= @size
          
          if index == @size -1 
              delete_tail
          elsif index == 0
              delete_head
          else
              cur_node = get_node(index)
              cur_node.prev.next = cur_node.next
              cur_node.next.prev = cur_node.prev
              @size -= 1
          end
      end
  
  
  #  get node from index
      def get_node(index)
          return nil if index < 0 || index >= @size
          
          if index == 0
              @head
          elsif index == @size - 1
              @tail
          else
              cur_node = @head
              while index > 0
                  cur_node = cur_node.next
                  index -= 1
              end
              cur_node
          end
      end
          
  #   remove tail
      def delete_tail
          # if only one node exist
          if @size == 1
              @head = nil
              @tail = nil
          else
              @tail.prev.next = @tail.next
              @tail = @tail.prev
          end
          
          @size -= 1
      end
          
      #   remove head
      def delete_head
          @head = @head.next
          @head.prev = nil
          @size -= 1
      end
  end
  
  class Node
      attr_accessor :val, :next, :prev
      
      def initialize(val)
          self.val = val
          self.next = nil
          self.prev = nil
      end
  end
  
  # Your MyLinkedList object will be instantiated and called as such:
  # obj = MyLinkedList.new()
  # param_1 = obj.get(index)
  # obj.add_at_head(val)
  # obj.add_at_tail(val)
  # obj.add_at_index(index, val)
  # obj.delete_at_index(index)