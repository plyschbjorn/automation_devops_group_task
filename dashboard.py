import streamlit as st
import pandas as pd
from get_api import get_weather_data

cities = {
    "Stockholm": {"lat": 59.3293, "lon": 18.0686},
    "Amsterdam": {"lat": 52.3702, "lon": 4.8952},
    "Ankara": {"lat": 39.9334, "lon": 32.8597},
    "Aten": {"lat": 37.9838, "lon": 23.7275},
    "Belgrad": {"lat": 44.7866, "lon": 20.4489},
    "Berlin": {"lat": 52.5200, "lon": 13.4050},
    "Bern": {"lat": 46.9480, "lon": 7.4474},
    "Bratislava": {"lat": 48.1486, "lon": 17.1077},
    "Bryssel": {"lat": 50.8503, "lon": 4.3517},
    "Budapest": {"lat": 47.4979, "lon": 19.0402},
    "Bukarest": {"lat": 44.4268, "lon": 26.1025},
    "Dublin": {"lat": 53.3498, "lon": -6.2603},
    "Helsingfors": {"lat": 60.1699, "lon": 24.9384},
    "Kiev": {"lat": 50.4501, "lon": 30.5234},
    "Köpenhamn": {"lat": 55.6761, "lon": 12.5683},
    "Lissabon": {"lat": 38.7223, "lon": -9.1393},
    "Ljubljana": {"lat": 46.0569, "lon": 14.5058},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Luxemburg": {"lat": 49.6116, "lon": 6.1319},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Minsk": {"lat": 53.9045, "lon": 27.5615},
    "Monaco": {"lat": 43.7384, "lon": 7.4246},
    "Moskva": {"lat": 55.7558, "lon": 37.6173},
    "Oslo": {"lat": 59.9139, "lon": 10.7522},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Podgorica": {"lat": 42.4304, "lon": 19.2594},
    "Prag": {"lat": 50.0755, "lon": 14.4378},
    "Reykjavik": {"lat": 64.1466, "lon": -21.9426},
    "Riga": {"lat": 56.9496, "lon": 24.1052},
    "Rom": {"lat": 41.9028, "lon": 12.4964},
    "San Marino": {"lat": 43.9356, "lon": 12.4473},
    "Sarajevo": {"lat": 43.8563, "lon": 18.4131},
    "Skopje": {"lat": 41.9981, "lon": 21.4254},
    "Sofia": {"lat": 42.6977, "lon": 23.3219},
    "Tallinn": {"lat": 59.4370, "lon": 24.7536},
    "Tirana": {"lat": 41.3275, "lon": 19.8187},
    "Valletta": {"lat": 35.8989, "lon": 14.5146},
    "Vatikanstaten": {"lat": 41.9029, "lon": 12.4534},
    "Vilnius": {"lat": 54.6872, "lon": 25.2797},
    "Warszawa": {"lat": 52.2297, "lon": 21.0122},
    "Wien": {"lat": 48.2082, "lon": 16.3738},
    "Zagreb": {"lat": 45.8150, "lon": 15.9819}
}

st.title("Weather With You - Europe")
st.subheader("Kolla temperaturen dit du vill åka")

cities_list = list(cities.keys())
selected_city_1 = st.selectbox("Välj stad", cities_list, index=0)

selected_city_2 = st.selectbox(
    "Välj ytterligare en stad för jämförelse",
    cities_list,
    index=None,
    placeholder=" "
)

st.subheader(f"Dagliga väderdata för {selected_city_1}")
lat1 = cities[selected_city_1]["lat"]
lon1 = cities[selected_city_1]["lon"]

with st.spinner(f"Hämtar väderdata för {selected_city_1}..."):
    df1 = get_weather_data(lat1, lon1)

st.dataframe(df1.set_index("Datum"), width='stretch')

df1_graph = df1.set_index("Datum")[["Max Temperatur (°C)", "Min Temperatur (°C)"]].rename(columns={
    "Max Temperatur (°C)": f"Max Temp ({selected_city_1})",
    "Min Temperatur (°C)": f"Min Temp ({selected_city_1})"
})

combined_df = df1_graph

if selected_city_2 is not None:
    lat2 = cities[selected_city_2]["lat"]
    lon2 = cities[selected_city_2]["lon"]

    with st.spinner(f"Hämtar väderdata för {selected_city_2}..."):
        df2 = get_weather_data(lat2, lon2)

    st.subheader(f"Dagliga väderdata för {selected_city_2}")
    st.dataframe(df2.set_index("Datum"), width='stretch')

    df2_graph = df2.set_index("Datum")[["Max Temperatur (°C)", "Min Temperatur (°C)"]].rename(columns={
        "Max Temperatur (°C)": f"Max Temp ({selected_city_2})",
        "Min Temperatur (°C)": f"Min Temp ({selected_city_2})"
    })

    combined_df = pd.concat([combined_df, df2_graph], axis=1)

st.subheader("Temperaturjämförelse")
st.line_chart(combined_df)