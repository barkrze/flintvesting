"""Główny skrypt uruchamiający pipeline projektu."""

from src.data.load_data import load_market_data
from src.features.feature_engineering import build_features
from src.models.train import train_models
from src.backtest.backtest import run_backtest


def main() -> None:
    print("Start projektu: strategie inwestycyjne z ML")

    data = load_market_data()
    features = build_features(data)
    models = train_models(features)
    run_backtest(models, features)


if __name__ == "__main__":
    main()
