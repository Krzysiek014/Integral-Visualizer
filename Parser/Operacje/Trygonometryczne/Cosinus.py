from math import cos
from Parser.Interfejsy import *

class Cosinus(Operacja):
  a: Operacja

  def __init__(self, a: Operacja):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return cos(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"cos({ self.a })"

class CosinusOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, znak: str):
    return znak == 'cos'

  def utworz(self, a: Operacja, b):
    return Cosinus(a)
