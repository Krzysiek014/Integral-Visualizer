from Parser.Wartosci.Zmienna import X, Y
from Parser.Wartosci.Liczba import Liczba, E, PI, FI

from Parser.Operacje.Arytmetyczne.Dodawanie import DodawanieOperator
from Parser.Operacje.Arytmetyczne.Odejmowanie import OdejmowanieOperator
from Parser.Operacje.Arytmetyczne.Mnozenie import MnozenieOperator
from Parser.Operacje.Arytmetyczne.Dzielenie import DzielenieOperator
from Parser.Operacje.Arytmetyczne.Potegowanie import PotegowanieOperator
from Parser.Operacje.Funkcyjne.Logarytm import LogarytmOperator
from Parser.Operacje.Funkcyjne.LogarytmNaturalny import LogarytmNaturalnyOperator
from Parser.Operacje.Funkcyjne.Sinus import SinusOperator
from Parser.Operacje.Funkcyjne.Cosinus import CosinusOperator
from Parser.Operacje.Funkcyjne.Tangens import TangensOperator
from Parser.Operacje.Funkcyjne.Cotangens import CotangensOperator

class ParserWyrazen:
  stale = [PI, E, FI]
  zmienne = [X, Y]
  operatory = [
    DodawanieOperator(),
    OdejmowanieOperator(),
    MnozenieOperator(),
    DzielenieOperator(),
    PotegowanieOperator(),
    SinusOperator(),
    CosinusOperator(),
    TangensOperator(),
    CotangensOperator(),
    LogarytmNaturalnyOperator(),
    LogarytmOperator(),
  ]

  def parsuj(self, wyrazenie: str): 
    stos = []

    for token in wyrazenie.strip().lower().split(" "):
      if self._parsujDzialania(token, stos):
        continue

      if self._parsujZmienne(token, stos):
        continue

      if self._parsujStale(token, stos):
        continue

      self._parsujLiczbe(token, stos)

    if len(stos) > 1:
      raise Exception(f"Niepoprawne wyrażenie za mało operatorów, brakuje { len(stos) - 1 }")

    if len(stos) == 0:
      raise Exception("Puste wyrażenie")
    
    return stos[0]
  
  def _parsujDzialania(self, token: str, stos: list):
    for operator in self.operatory:
      if operator.akceptuje(token):
        iloscArgumentow = 2 if operator.czyDwuargumentowy else 1

        if len(stos) < iloscArgumentow:
          raise Exception(f"Niepoprawne wyrażenie za mało argumentów dla operatora { token } oczekiwano { iloscArgumentow } jest { len(stos) }")

        if operator.czyDwuargumentowy:
          b = stos.pop()
          a = stos.pop()
          stos.append(operator.utworz(a, b, token))
        else:
          a = stos.pop()
          stos.append(operator.utworz(a, a, token))

        return True

    return False

  def _parsujZmienne(self, token: str, stos: list):
    for zmienna in self.zmienne:
      if str(zmienna) == token:
        stos.append(zmienna)
        return True

    return False

  def _parsujStale(self, token: str, stos: list):
    for stala in self.stale:
      if str(stala) == token:
        stos.append(stala)
        return True

    return False

  def _parsujLiczbe(self, token: str, stos: list):
    try:
      stos.append(Liczba(float(token)))
      return True
    except:
      raise Exception(f"Nieznana wartość '{ token }'")
    
    return False
