"""Moduł do inżynierii cech i wskaźników technicznych."""

import pandas as pd
import ta


def build_features(data: pd.DataFrame) -> pd.DataFrame:
    """Tworzy zestaw cech na podstawie surowych danych rynkowych."""
    df = data.copy()
    df["return"] = df["Close"].pct_change()
    df["ma_10"] = ta.trend.sma_indicator(df["Close"], window=10)
    df["ma_50"] = ta.trend.sma_indicator(df["Close"], window=50)
    df["rsi"] = ta.momentum.rsi(df["Close"], window=14)
    macd = ta.trend.MACD(df["Close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["volume_mean"] = df["Volume"].rolling(window=20).mean()
    df["volatility"] = df["return"].rolling(window=20).std()
    df = df.dropna()
    return df
