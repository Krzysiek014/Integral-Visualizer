from Parser.Interfejsy import Wyrazenie, Operator
from Parser.Operacje.Arytmetyczne.WyrazenieAlgebraiczne import WyrazenieAlgebraiczne
from math import isinf
class Dzielenie(WyrazenieAlgebraiczne):
  symbol = '/'
  znaczenieWyrazenia = 1

  def __init__(self, a: Wyrazenie, b: Wyrazenie):
    self.a = a
    self.b = b

  def wykonaj(self, x: float, y: float) -> float:
    m = self.b.wykonaj(x, y)

    if m == 0.0:
      raise ValueError("Dzielenie przez 0")

    return self.a.wykonaj(x, y) / m

class DzielenieOperator(Operator):
  def akceptuje(self, token: str):
    return token == '/'

  def utworz(self, a: Wyrazenie, b: Wyrazenie, token):
    return Dzielenie(a, b)

