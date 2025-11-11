import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import dashboard
from get_api import get_weather_data


def test_dashboard_has_cities_dict():
    """Kontrollerar att dashboard har en cities-dict med minst ett värde."""
    assert hasattr(dashboard, "cities")
    assert isinstance(dashboard.cities, dict)
    assert len(dashboard.cities) > 0


def test_dashboard_uses_get_api():
    """Kollar att dashboard kan använda get_weather_data och får rätt DataFrame."""
    df = get_weather_data(59.3293, 18.0686)
    assert isinstance(df, pd.DataFrame)
    assert "Datum" in df.columns
    assert len(df) > 0