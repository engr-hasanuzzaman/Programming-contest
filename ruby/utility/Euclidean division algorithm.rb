def divide(n, d)
  return 'Division by Zero' if d.zero?
  
  if d < 0 
    q, r = divide(n, -d)
    return -q, r
  end 
  
  if n < 0
    q, r = divide(-n, d)
    
    if r == 0
      return -q, 0 
    else
      return -q - 1, d - r
    end 
  end
  
  q, r = 0, n
  while(r >= d)
   r = r -d
   q += 1
  end 
   
  return q, r 
end
