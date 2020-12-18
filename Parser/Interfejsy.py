class Wyrazenie:
  znaczenieWyrazenia = 0

  def wykonaj(self, x: float, y: float) -> float:
    pass

class Operator:
  czyDwuargumentowy = True
  
  def akceptuje(self, token: str) -> bool:
    pass

  def utworz(self, a: Wyrazenie, b: Wyrazenie, token: str) -> Wyrazenie:
    pass
