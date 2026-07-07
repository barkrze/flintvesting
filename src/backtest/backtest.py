"""Moduł do prostego backtestingu strategii inwestycyjnych."""

import pandas as pd


def run_backtest(models: dict, data: pd.DataFrame) -> None:
    """Uruchamia przykładowy backtest dla wytrenowanych modeli."""
    features = ["return", "ma_10", "ma_50", "rsi", "macd", "macd_signal", "volume_mean", "volatility"]
    X = data[features]

    for name, model in models.items():
        data[f"pred_{name}"] = model.predict(X)

    print("Backtest zakończony. Modele wygenerowały sygnały.")
