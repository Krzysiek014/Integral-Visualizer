from math import cos
from Parser.Interfejsy import Wyrazenie, Operator

class Cosinus(Wyrazenie):
  a: Wyrazenie

  def __init__(self, a: Wyrazenie):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return cos(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"cos({ self.a })"

class CosinusOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, token: str):
    return token == 'cos'

  def utworz(self, a: Wyrazenie, b, token):
    return Cosinus(a)
