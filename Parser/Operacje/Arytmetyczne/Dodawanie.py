from Parser.Interfejsy import Wyrazenie, Operator
from Parser.Operacje.Arytmetyczne.WyrazenieAlgebraiczne import WyrazenieAlgebraiczne

class Dodawanie(WyrazenieAlgebraiczne):
  symbol = '+'
  znaczenieWyrazenia = -1

  def __init__(self, a: Wyrazenie, b: Wyrazenie):
    self.a = a
    self.b = b

  def wykonaj(self, x: float, y: float) -> float:
    return self.a.wykonaj(x, y) + self.b.wykonaj(x, y)

class DodawanieOperator(Operator):
  def akceptuje(self, token: str):
    return token == '+'

  def utworz(self, a: Wyrazenie, b: Wyrazenie, token):
    return Dodawanie(a, b)

