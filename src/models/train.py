"""Moduł do trenowania prostych modeli ML."""

from typing import Dict
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def train_models(data: pd.DataFrame) -> Dict[str, object]:
    """Trenuje przykładowe modele na przygotowanych cechach."""
    features = ["return", "ma_10", "ma_50", "rsi", "macd", "macd_signal", "volume_mean", "volatility"]
    target = (data["return"] > 0).astype(int)

    X = data[features]
    y = target

    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "xgboost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42),
    }

    for model in models.values():
        model.fit(X, y)

    return models
