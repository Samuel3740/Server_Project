# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# URL = "https://www.weather.go.kr/w/weather/land/city-obs.do"

# def crawl_weather():
#     res = requests.get(URL, timeout=10)
#     res.raise_for_status()

#     soup = BeautifulSoup(res.text, "html.parser")
#     table = soup.select_one("table.table-col")

#     results = []

#     for row in table.select("tbody tr"):
#         cols = [td.text.strip() for td in row.select("td")]

#         if len(cols) < 8:
#             continue

#         city = cols[0]
#         temp = float(cols[5]) if cols[5] != "-" else None
#         humidity = int(cols[7]) if cols[7] != "-" else None

#         results.append({
#             "city": city,
#             "temperature": temp,
#             "humidity": humidity,
#             "observed_at": datetime.now()
#         })

#     return results
