
# Complete the flippingBits function below.
def flippingBits(n)
  max = 4294967295
  return max if n.zero?

  max ^ n  
end


