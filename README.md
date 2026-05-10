# Mini Warcaby AI

Projekt przedstawia uproszczoną wersję gry w warcaby z przeciwnikiem sterowanym przez AI.  
Sztuczna inteligencja wykorzystuje algorytm Minimax wraz z optymalizacją Alpha-Beta Pruning do podejmowania decyzji podczas gry.

## Funkcje

- gra gracz vs AI,
- implementacja algorytmu Minimax,
- Alpha-Beta Pruning dla szybszego przeszukiwania,
- interfejs graficzny oparty o Pygame,
- uproszczone zasady warcabów.

## Technologie

- Python
- Pygame
- Minimax
- Alpha-Beta Pruning

## Instalacja

Najpierw zainstaluj zależności projektu:

```bash
pip install -r requirements.txt
```

lub przy użyciu `uv`:

```bash
uv sync
```

## Uruchomienie projektu

```bash
uv run python app/main.py
```

lub klasycznie:

```bash
python app/main.py
```

## Problemy z Pygame

Jeśli standardowy `pygame` nie działa poprawnie na Twoim systemie, zainstaluj wersję community edition:

```bash
pip install pygame-ce
```

Po instalacji ponownie uruchom projekt.

