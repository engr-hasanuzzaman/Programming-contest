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
          return if index > @size
          
          cur_node = Node.new(val)
          
          if index == @size
              add_at_tail(val)
          elsif index == 0
              add_at_head(val)
          end
              prev_node = get_node(index-1)
              cur_node.next = prev_node.next
              prev_node.next = cur_node
              @size += 1
          end
          
      end
  
  
  =begin
      Delete the index-th node in the linked list, if the index is valid.
      :type index: Integer
      :rtype: Void
  =end
      def delete_at_index(index)
          return -1 if index < 0 || index >= @size
          
          if index == @size -1 
              delete_tail
          elsif index == 0
              delete_head
          else
              prev_node = get_node(index-1)
              cur_node = prev_node.next
              prev_node.next = cur_node.next
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
          prev_node = get_node(@size-2)
          @tail = prev_node
          @size -= 1
      end
          
      #   remove head
      def delete_head
          @head = @head.next
          @size -= 1
      end
  end
  
  class Node
      attr_accessor :val, :next
      
      def initialize(val)
          self.val = val
          self.next = nil
      end
  end
  
  # Your MyLinkedList object will be instantiated and called as such:
  # obj = MyLinkedList.new()
  # param_1 = obj.get(index)
  # obj.add_at_head(val)
  # obj.add_at_tail(val)
  # obj.add_at_index(index, val)
  # obj.delete_at_index(index)