# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue

  =begin
      Initialize your data structure here. Set the size of the queue to be k.
      :type k: Integer
  =end
      def initialize(k)
          @length = k
          @q = []
          @head = -1
          @rear = -1
      end
  
  
  =begin
      Insert an element into the circular queue. Return true if the operation is successful.
      :type value: Integer
      :rtype: Boolean
  =end
      def en_queue(value)
          return false if is_full
          puts "-- old rear #{@rear}"
          @rear = (@rear + 1) % (@length)
          @q[@rear] = value
          
          if @head == -1
              @head += 1
          end
          # puts "new rear #{@rear}, #{@head}"
          true
      end
  
  
  =begin
      Delete an element from the circular queue. Return true if the operation is successful.
      :rtype: Boolean
  =end
      def de_queue()
  #         queue empty
          return false if @head == -1
         
          if @head == @rear
              @head = -1
              @rear = -1
          else
              @head = (@head + 1) % (@length)
          end
          
          true
      end
  
  
  =begin
      Get the front item from the queue.
      :rtype: Integer
  =end
      def front()
          return -1 if @head == -1
          
          @q[@head]
      end
  
  
  =begin
      Get the last item from the queue.
      :rtype: Integer
  =end
      def rear()
          return -1 if @rear == -1
          
          @q[@rear]
      end
  
  
  =begin
      Checks whether the circular queue is empty or not.
      :rtype: Boolean
  =end
      def is_empty()
          @head == -1 && @rear == -1 && @length > 0
      end
  
  
  =begin
      Checks whether the circular queue is full or not.
      :rtype: Boolean
  =end
      def is_full()
          return false if is_empty
          return true if @length == 0
          
          # puts "r #{@rear}, h #{@head}, l #{@length}"
          # ((@rear + 1) % @length == @head) means if next element after rear is
          # head then stack is full
          (@rear == @length - 1 && @head == 0) || (@rear == @head - 1)
      end
  
  
  end
  
  # Your MyCircularQueue object will be instantiated and called as such:
  # obj = MyCircularQueue.new(k)
  # param_1 = obj.en_queue(value)
  # param_2 = obj.de_queue()
  # param_3 = obj.front()
  # param_4 = obj.rear()
  # param_5 = obj.is_empty()
  # param_6 = obj.is_full()