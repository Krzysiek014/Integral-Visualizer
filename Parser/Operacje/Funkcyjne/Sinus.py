from math import sin
from Parser.Interfejsy import Wyrazenie, Operator

class Sinus(Wyrazenie):
  a: Wyrazenie

  def __init__(self, a: Wyrazenie):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return sin(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"sin({ self.a })"

class SinusOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, token: str):
    return token == 'sin'

  def utworz(self, a: Wyrazenie, b, token):
    return Sinus(a)

