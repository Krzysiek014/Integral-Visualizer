# Parser
Parser wyrażeń zapisanych w odwrotnej notacji polskiej

```python
from Parser.ParserWyrazen import ParserWyrazen

parser = ParserWyrazen()

try:
  dzialanie = parser.parsuj("x y + 2 ^ pi * sin 1024 + log2 2 * 1 - 8 *")

  print(str(dzialanie)) # (log2.0(sin((x + y) ^ 2.0 * pi) + 1024.0) * 2.0 - 1.0) * 8.0
except Exception as e:
  print(f"Błąd parsowania - { str(e) }")
else:
  try:
    wynik = dzialanie.wykonaj(1, 2)

    print(f"Wynik: { wynik }") # Wynik: 152.0
  except Exception as e:
    print(f"Błąd obliczeń - { str(e) }")
```
