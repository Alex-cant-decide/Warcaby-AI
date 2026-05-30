# Projekt SI – Mini Warcaby AI

## Opis problemu

Celem projektu było stworzenie uproszczonej gry w warcaby z przeciwnikiem sterowanym przez sztuczną inteligencję.

## Wybrany algorytm

W projekcie wykorzystano algorytm Minimax z optymalizacją Alpha-Beta Pruning.

## Dlaczego wybrano Minimax

Algorytm Minimax dobrze sprawdza się w grach dwuosobowych o sumie zerowej.
Pozwala analizować możliwe ruchy przeciwnika i wybierać najlepszą strategię.

## Działanie algorytmu

AI generuje wszystkie możliwe ruchy.
Dla każdego ruchu tworzona jest symulacja kolejnych stanów gry.
Algorytm wybiera ruch o najlepszej ocenie.

## Eksperyment

Przetestowano działanie AI dla różnych sytuacji na planszy.
Sprawdzono poprawność:

- ruchów,
- bicia pionków,
- wykrywania zwycięstwa,
- wykrywania remisu.

## Testy

Testy należy odpalać komendą:

```bash
uv run python -m pytest
```

Na ekranie wyskoczy gra, ale w terminalu włączą się testy w Pytest.

## Wyniki

AI poprawnie analizuje ruchy i wybiera najlepsze dostępne decyzje.

## Wnioski

Algorytm Minimax skutecznie działa w grach strategicznych.
Alpha-Beta Pruning znacząco przyspiesza działanie programu.
