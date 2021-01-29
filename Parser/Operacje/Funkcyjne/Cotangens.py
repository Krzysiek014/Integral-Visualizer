from math import tan
from Parser.Interfejsy import Wyrazenie, Operator

class Tangens(Wyrazenie):
  a: Wyrazenie

  def __init__(self, a: Wyrazenie):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return 1 / tan(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"ctg({ self.a })"

class TangensOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, token: str):
    return token == 'ctg'

  def utworz(self, a: Wyrazenie, b, token):
    return Tangens(a)
