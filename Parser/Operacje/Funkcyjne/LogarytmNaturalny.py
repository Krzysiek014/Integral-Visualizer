from math import log
from Parser.Interfejsy import Wyrazenie, Operator

class LogarytmNaturalny(Wyrazenie):
  a: Wyrazenie

  def __init__(self, a: Wyrazenie):
    self.a = a

  def wykonaj(self, x: float, y: float) -> float:
    return log(self.a.wykonaj(x, y))
  
  def __str__(self):
    return f"ln({ self.a })"

class LogarytmNaturalnyOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, token: str):
    return token == 'ln'

  def utworz(self, a: Wyrazenie, b, token: str):
    if token == 'ln':
      return LogarytmNaturalny(a)

