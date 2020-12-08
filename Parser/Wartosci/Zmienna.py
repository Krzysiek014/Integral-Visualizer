from Parser.Interfejsy import Operacja

class Zmienna(Operacja):
  czyX = True
  nazwa = ''

  def __init__(self, nazwa: str):
    self.czyX = nazwa == 'x'
    self.nazwa = nazwa
  
  def wykonaj(self, x: float, y: float):
    return x if self.czyX else y
  
  def __str__(self):
    return self.nazwa

X = Zmienna('x')
Y = Zmienna('y')
