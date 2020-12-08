from math import sin
from Parser.Interfejsy import *

class Sinus(Operacja):
  a: Operacja

  def __init__(self, a: Operacja):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return sin(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"sin({ self.a })"

class SinusOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, znak: str):
    return znak == 'sin'

  def utworz(self, a: Operacja, b):
    return Sinus(a)

