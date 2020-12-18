from math import pi, e, sqrt
from Parser.Interfejsy import Wyrazenie

class Liczba(Wyrazenie):
  _wartosc = 0.0
  _str = None

  def __init__(self, wartosc: float, toStr = None):
    self._wartosc = wartosc
    self._str = toStr
  
  def wykonaj(self, x: float, y: float):
    return self._wartosc

  def __str__(self):
    return self._str if self._str != None else str(self._wartosc)

E = Liczba(e, 'e')
PI = Liczba(pi, 'pi')
FI = Liczba((1 + sqrt(5)) / 2, 'fi')
