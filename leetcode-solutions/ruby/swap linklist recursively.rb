class Node
  attr_accessor :next, :val
  def initialize(val)
    self.next = nil
    self.val = val
  end
end

def print_link_list(head)
  node = head
  while node
    print "#{node.val} -> " 
    node = node.next
  end
end

# swap tow node
def swap_pairs(head)
  return head unless head && head.next
  # store node temp     
  t_h = head
  t_nn = head.next.next
  
  # swap node
  head = head.next
  head.next = t_h
  head.next.next = swap_pairs(t_nn)
  head
end

head = Node.new(1)
head.next = Node.new(2)
head.next.next = Node.new(3)
head.next.next.next = Node.new(4)

puts "--befor swaping link list is "
print_link_list(head)
puts ""
puts "--after swaping link list is "
head = swap_pairs(head)
print_link_list(head) # 2 -> 1 -> 4 -> 3.
puts head.next.next.inspect
puts ""