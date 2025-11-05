import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"

def get_weather_data(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["rain_sum", "temperature_2m_max", "temperature_2m_min"],
        "timezone": "Europe/Stockholm",
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()

    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        ),
        "rain_sum": daily.Variables(0).ValuesAsNumpy(),
        "temperature_2m_max": daily.Variables(1).ValuesAsNumpy(),
        "temperature_2m_min": daily.Variables(2).ValuesAsNumpy()
    }

    df = pd.DataFrame(daily_data)

    df["date"] = (
        df["date"]
        .dt.tz_convert("Europe/Stockholm")
        .dt.normalize()
        .dt.strftime("%Y-%m-%d")
    )
    df = df.round({
    "temperature_2m_max": 1,
    "temperature_2m_min": 1,
    "rain_sum": 1
}).rename(columns={
    "date": "Datum",
    "rain_sum": "Nederbörd (mm)",
    "temperature_2m_max": "Max Temperatur (°C)",
    "temperature_2m_min": "Min Temperatur (°C)"
})
    return df