def sortedInsert(head, data)
  # no dead 
  return DoublyLinkedListNode.new(data) unless head

  node = head
  while node.next && data > node.data 
      node = node.next
  end

  n_node = DoublyLinkedListNode.new(data)
  if node == head
      n_node.next = node
      node.prev = n_node
      return n_node
  elsif node.data >= data
      n_node.prev = node.prev
      n_node.next = node
      node.prev = n_node
      n_node.prev.next = n_node if n_node.prev
  else 
    n_node.prev = node
    node.next = n_node
  end

  return head
end