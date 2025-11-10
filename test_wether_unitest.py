import pandas as pd
from unittest.mock import MagicMock
from get_api import get_weather_data

def test_get_weather_data(monkeypatch):
    fake_rain = [10]
    fake_temp_max = [20]
    fake_temp_min = [5]
    
    mock_daily = MagicMock()
    mock_daily.Time.return_value = 0
    mock_daily.TimeEnd.return_value = 86400
    mock_daily.Interval.return_value = 86400

    def fake_variables(fake):
        mock_var = MagicMock()
        if fake == 0:
            mock_var.ValuesAsNumpy.return_value = fake_rain
        elif fake == 1:
            mock_var.ValuesAsNumpy.return_value = fake_temp_max
        elif fake == 2:
            mock_var.ValuesAsNumpy.return_value = fake_temp_min
        return mock_var
    
    mock_daily.Variables.side_effect = fake_variables

    mock_response = MagicMock()
    mock_response.Daily.return_value = mock_daily

    mock_client = MagicMock()
    mock_client.weather_api.return_value = [mock_response]

    monkeypatch.setattr("get_api.openmeteo", mock_client)

    df = get_weather_data(59.3293, 18.0686)  # Stockholm

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