# Parser
Parser wyrażeń zapisanych w odwrotnej notacji polskiej

```python
from Parser.ParserWyrazen import ParserWyrazen

parser = ParserWyrazen()

try:
  operacja = parser.parsuj("x y + 2 ^ pi * sin")

  print(str(operacja)) # sin(((x + y) ^ (2)) * (pi))
except Exception as e:
  print(f"Błąd parsowania - { str(e) }")
else:
  try:
    wynik = operacja.wykonaj(1, 2)

    print(f"Wynik: { wynik }")
  except Exception as e:
    print(f"Błąd obliczeń - { str(e) }")
```
