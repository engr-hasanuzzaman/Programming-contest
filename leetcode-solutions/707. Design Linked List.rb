# https://leetcode.com/problems/design-linked-list/

# Node
class Node
  @attr_accessor :next, :val
  
  def initialize(val)
      self.val = val
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
      return -1 if index >= @size || index < 0
      return @tail.val if index == @size -1
      return @head.val if index == 0
      
      node = @head
      while index > 0
          node = node.next
      end
      
      node.val
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
          @head  @tail
      end
  end


=begin
  Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
  :type index: Integer
  :type val: Integer
  :rtype: Void
=end
  def add_at_index(index, val)
      
  end


=begin
  Delete the index-th node in the linked list, if the index is valid.
  :type index: Integer
  :rtype: Void
=end
  def delete_at_index(index)
      
  end


end
  

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList.new()
# param_1 = obj.get(index)
# obj.add_at_head(val)
# obj.add_at_tail(val)
# obj.add_at_index(index, val)
# obj.delete_at_index(index)