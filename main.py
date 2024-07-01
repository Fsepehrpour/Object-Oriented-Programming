class Power():
  """ A class that computes a specific power of other numbers.
  in other words, it raises a number by a constant exponent."""

  def __init__(self, exponent):
    self.exponent = exponent

  def of(self, x):
    return x ** self.exponent

class RealPower(Power):
  """ A subclass of Power for real numbers."""

def of(self, x):
  if isinstance(self.exponent, int) or x>=0:
    return x ** self.exponent
  raise ValueError(
    "Fractional powers of negative numbers are imaginary" 
  )

square = Power(2)
root = Power(0.5)
print("square: ", square)
print("square.of(3) =", square.of(3))
print("root.of(3) =", root.of(3))
print("root.of(-3) =", root.of(-3))
real_root = RealPower(0.5)
print("real_root.of(3) =", real_root.of(3))
print("real_root.of(-3) =", real_root.of(-3))
