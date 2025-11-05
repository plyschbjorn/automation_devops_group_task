# Weather With You - Dashboard

Detta är en dashboard byggd med Streamlit som hämtar och visualiserar 7-dagars väderprognoser. Data hämtas i realtid från [Open-Meteo API](https://open-meteo.com/).

## Funktioner

* **Val av Stad:** Välj en stad från en lista över europeiska huvudstäder.
* **Jämförelse:** Välj en andra stad för att jämföra väderprognoserna.
* **Datavisualisering:**
    * Varje vald stad visar en tabell med prognos för "Datum", "Max Temperatur (°C)", "Min Temperatur (°C)" och "Nederbörd (mm)".
    * En graf plottar max- och mintemperatur för de valda städerna för enkel jämförelse.
* **Caching:** API-anrop cachas lokalt i en timme för att snabba upp laddningstider och minska API-användning.

## Installation

För att köra detta projekt lokalt behöver du ha [**uv**](https://github.com/astral-sh/uv) och Python installerat.

#### 1. Klona projektet

Klona först ner detta repository till din lokala dator:
```
cd <mapp-namn>
git clone <URL-till-github-repo>
```

#### 2. Skapa och aktivera en virtuell miljö (med uv)
Det rekommenderas starkt att köra projektet i en virtuell miljö.

##### Skapa miljön (med uv):

```bash
uv venv
```
##### Aktivera miljön:

* På macOS/Linux:

```bash
source .venv/bin/activate
```

* På Windows git bash:

```bash
source .venv\Scripts\activate
```

#### 3. Installera beroenden (med uv)
När din virtuella miljö är aktiv, installera alla paket som krävs från requirements.txt-filen:

```bash
uv pip install -r requirements.txt
```

### Så här kör du appen
När installationen är klar, kör följande kommando i din terminal:

```bash
streamlit run dashboard.py
```
##### Streamlit kommer automatiskt att öppna din webbläsare och visa din dashboard.