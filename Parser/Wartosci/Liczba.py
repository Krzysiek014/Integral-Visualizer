from math import pi, e
from Parser.Interfejsy import Operacja

class Liczba(Operacja):
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
