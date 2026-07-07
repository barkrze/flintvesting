# Projekt: Strategie inwestycyjne z ML

## Cele projektu

Celem projektu jest implementacja i analiza strategii inwestycyjnych z wykorzystaniem metod uczenia maszynowego oraz uczenia wzmocnionego.

Modele obejmują:
- regresję logistyczną
- Random Forest
- XGBoost
- LSTM
- Deep Q-Network (RL DQN)

## Struktura katalogów

- `src/` – kod źródłowy projektu
  - `src/data/` – wczytywanie i przygotowanie danych
  - `src/features/` – inżynieria cech i wskaźników technicznych
  - `src/models/` – trening i predykcja modeli
  - `src/backtest/` – symulacja strategii i ocena wyników
  - `src/utils/` – narzędzia pomocnicze
- `notebooks/` – notatniki analityczne i eksperymenty
- `tests/` – testy jednostkowe
- `requirements.txt` – zależności Python

## Środowisko Python

1. Zainstaluj Python 3.11 lub nowszy.
2. Utwórz i aktywuj środowisko wirtualne:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

## Uruchamianie

Przykładowo, aby uruchomić pipeline przetwarzania danych i modelowania:

```bash
python src/main.py
```

## Dalsze kroki

- uzupełnienie modułów danych i cech
- opracowanie backtestingu
- implementacja modeli ML i RL
- walidacja na instrumentach i kosztach transakcyjnych
