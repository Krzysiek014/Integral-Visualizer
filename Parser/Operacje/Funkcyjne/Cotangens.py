from math import tan
from Parser.Interfejsy import Wyrazenie, Operator

class Tangens(Wyrazenie):
  a: Wyrazenie

  def __init__(self, a: Wyrazenie):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return tan(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"tg({ self.a })"

class TangensOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, token: str):
    return token == 'tg'

  def utworz(self, a: Wyrazenie, b, token):
    return Tangens(a)
