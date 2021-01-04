ef merge_two_lists(l1, l2)
    if l1 == nil
      return l2
    elsif l2 == nil
      return l1
    end
    if l1.val > l2.val
      root = l2
      l2 = l2.next
    else
      root = l1
      l1 = l1.next
    end
  
    current = root
    while l1 && l2
      if l1.val > l2.val
        current.next = l2
        current = current.next
        l2 = l2.next
      else
         current.next = l1
         current = current.next
         l1 = l1.next
      end
    end
  if l1
    current.next = l1
  else
    current.next = l2
  end
  
  root
end