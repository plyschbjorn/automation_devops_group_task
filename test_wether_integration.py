import pandas as pd
from get_api import get_weather_data

def test_get_weather_data_real_api():
    df = get_weather_data(59.3293, 18.0686) #Stockholm
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    expected_cols = [
        "Datum",
        "Nederbörd (mm)",
        "Max Temperatur (°C)",
        "Min Temperatur (°C)"
    ]

    for col in expected_cols:
        assert col in df.columns