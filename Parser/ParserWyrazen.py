from Parser.Wartosci.Liczba import Liczba, E, PI
from Parser.Wartosci.Zmienna import Zmienna

from Parser.Operacje.Arytmetyczne.Dodawanie import DodawanieOperator
from Parser.Operacje.Arytmetyczne.Odejmowanie import OdejmowanieOperator
from Parser.Operacje.Arytmetyczne.Mnozenie import MnozenieOperator
from Parser.Operacje.Arytmetyczne.Dzielenie import DzielenieOperator
from Parser.Operacje.Arytmetyczne.Potegowanie import PotegowanieOperator
from Parser.Operacje.Trygonometryczne.Sinus import SinusOperator
from Parser.Operacje.Trygonometryczne.Cosinus import CosinusOperator

class ParserWyrazen:
  operatory = []
  dzialania = [
    DodawanieOperator(),
    OdejmowanieOperator(),
    MnozenieOperator(),
    DzielenieOperator(),
    PotegowanieOperator(),
    SinusOperator(),
    CosinusOperator(),
  ]

  def parsuj(self, wyrazenie: str):
    tokeny = wyrazenie.lower().split(" ")
    stos = []

    for token in tokeny:
      czyOperand = False

      for op in self.dzialania:
        if op.akceptuje(token):
          iloscArgumentow = 2 if op.czyDwuargumentowy else 1

          if len(stos) < iloscArgumentow:
            raise Exception(f"Niepoprawne wyrażenie za mało argumentów dla operatora { token } oczekiwano { iloscArgumentow } jest { len(stos) }")

          czyOperand = True

          if op.czyDwuargumentowy:
            b = stos.pop()
            a = stos.pop()

            stos.append(op.utworz(a, b))
          else:
            a = stos.pop()

            stos.append(op.utworz(a, a))

          break
      
      if not czyOperand:
        if token in ['x', 'y']:
          stos.append(Zmienna(token))
        elif token == 'e':
          stos.append(E)
        elif token == 'pi':
          stos.append(PI)
        else:
          try:
            wartosc = float(token)
            stos.append(Liczba(wartosc))
          except:
            raise Exception(f"Oczekiwano wartości liczbowej spotkano { token }")
        
    if len(stos) > 1:
      raise Exception(f"Niepoprawne wyrażenie za mało operatorów, brakuje { len(stos) - 1 }")

    if len(stos) == 0:
      raise Exception("Puste wyrażenie")
    
    return stos[0]

