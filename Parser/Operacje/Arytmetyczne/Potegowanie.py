from Parser.Interfejsy import Wyrazenie, Operator
from Parser.Operacje.Arytmetyczne.WyrazenieAlgebraiczne import WyrazenieAlgebraiczne

class Potegowanie(WyrazenieAlgebraiczne):
  symbol = '^'
  znaczenieWyrazenia = 2

  def __init__(self, a: Wyrazenie, b: Wyrazenie):
    self.a = a
    self.b = b

  def wykonaj(self, x: float, y: float) -> float:
    p = self.a.wykonaj(x, y)

    if p < 0:
      raise ValueError("Potęgowanie liczby ujemnej")

    return p ** self.b.wykonaj(x, y)

class PotegowanieOperator(Operator):
  def akceptuje(self, token: str):
    return token == '^'

  def utworz(self, a: Wyrazenie, b: Wyrazenie, token):
    return Potegowanie(a, b)

