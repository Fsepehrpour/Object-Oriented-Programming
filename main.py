class Power():
  """ A class that computes a specific power of other numbers.
  in other words, it raises a number by a contant exponent."""

  default_exponent = 2
  def __init__(self, exponent = default_exponent):
    self.exponent = exponent

  def of(self, x):
    return x ** self.exponent

class RealPower(Power):
  """ A subcalss of Power for real numbers."""

def of(self, x):
  if isinstance(self.exponent, int) or x>=0:
    return x ** self.exponent
  raise ValueError(
    "Fractional powers of negative numbers are imaginary" 
  )
