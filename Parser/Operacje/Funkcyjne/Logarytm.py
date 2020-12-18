import re
from math import log
from Parser.Interfejsy import Wyrazenie, Operator

class Logarytm(Wyrazenie):
  a: Wyrazenie
  p: float

  def __init__(self, a: Wyrazenie, p: float):
    self.a = a
    self.p = p

  def wykonaj(self, x: float, y: float) -> float:
    return log(self.a.wykonaj(x, y), self.p)
  
  def __str__(self):
    return f"log{ self.p }({ self.a })"

class LogarytmOperator(Operator):
  czyDwuargumentowy = False

  def akceptuje(self, token: str):
    return bool(re.match("^log(\\d*(\\.\\d*)?)$", token))

  def utworz(self, a: Wyrazenie, b, token: str):
    return Logarytm(a, float(re.match("^log(\\d*(\\.\\d*)?)$", token)[1]))
