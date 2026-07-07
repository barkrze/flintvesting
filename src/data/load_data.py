"""Moduł odpowiedzialny za wczytywanie danych finansowych."""

import pandas as pd
import yfinance as yf


def load_market_data(symbol: str = "AAPL", period: str = "5y") -> pd.DataFrame:
    """Wczytuje dane historyczne dla wybranego instrumentu."""
    data = yf.download(symbol, period=period, auto_adjust=True)
    data = data.dropna()
    return data
