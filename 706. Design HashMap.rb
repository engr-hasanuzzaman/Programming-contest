# https://leetcode.com/problems/design-hashmap/

class MyHashMap

  =begin
      Initialize your data structure here.
  =end
      def initialize()
          @data = []
      end
  
  
  =begin
      value will always be non-negative.
      :type key: Integer
      :type value: Integer
      :rtype: Void
  =end
      def put(key, value)
          @data[key] = value
      end
  
  
  =begin
      Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
      :type key: Integer
      :rtype: Integer
  =end
      def get(key)
          @data[key] || -1
      end
  
  
  =begin
      Removes the mapping of the specified value key if this map contains a mapping for the key
      :type key: Integer
      :rtype: Void
  =end
      def remove(key)
          @data[key] = nil
      end
  
  
  end
  
  # Your MyHashMap object will be instantiated and called as such:
  # obj = MyHashMap.new()
  # obj.put(key, value)
  # param_2 = obj.get(key)
  # obj.remove(key)