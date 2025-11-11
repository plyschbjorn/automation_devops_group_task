import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from get_api import get_weather_data



def test_get_weather_data_returns_dataframe():
    """Säkerställ att funktionen returnerar en DataFrame med data."""
    df = get_weather_data(59.3293, 18.0686)  # Koordinater för Stockholm

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_get_weather_data_has_expected_columns():
    """Kontrollerar att kolumnerna finns i rätt format."""
    df = get_weather_data(59.3293, 18.0686)

    expected = [
        "Datum",
        "Nederbörd (mm)",
        "Max Temperatur (°C)",
        "Min Temperatur (°C)"
    ]

    for col in expected:
        assert col in df.columns