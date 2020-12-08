from Parser.Interfejsy import *

class Dzielenie(Operacja):
  a: Operacja
  b: Operacja

  def __init__(self, a: Operacja, b: Operacja):
    self.a = a
    self.b = b

  def wykonaj(self, x: float, y: float) -> float:
    return self.a.wykonaj(x, y) / self.b.wykonaj(x, y)

  def __str__(self):
    return f"({ self.a } / { self.b })"

class DzielenieOperator(Operator):
  def akceptuje(self, znak: str):
    return znak == '/'

  def utworz(self, a: Operacja, b: Operacja):
    return Dzielenie(a, b)

