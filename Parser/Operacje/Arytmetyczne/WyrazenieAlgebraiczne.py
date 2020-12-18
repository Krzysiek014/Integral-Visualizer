from Parser.Interfejsy import Wyrazenie

class WyrazenieAlgebraiczne(Wyrazenie):
  symbol: str
  a: Wyrazenie
  b: Wyrazenie

  def __str__(self):
    _a = f"({self.a})" if self.a.znaczenieWyrazenia < 0 and self.znaczenieWyrazenia > 0 else f"{self.a}"
    _b = f"({self.b})" if self.b.znaczenieWyrazenia < 0 and self.znaczenieWyrazenia > 0 else f"{self.b}"

    return f"{_a} {self.symbol} {_b}"
