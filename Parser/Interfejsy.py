class Operacja:
  def wykonaj(self, x: float, y: float) -> float:
    pass

class Operator:
  czyDwuargumentowy = True
  
  def akceptuje(self, znak: str) -> bool:
    pass

  def utworz(self, a: Operacja, b: Operacja) -> Operacja:
    pass
