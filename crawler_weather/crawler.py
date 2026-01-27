import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.weather.go.kr/w/weather/land/city-obs.do"


def crawl_weather():
    """
    기상청 도시별 관측 페이지를 크롤링하여
    도시, 기온, 습도, 수집 시각을 담은 딕셔너리 리스트를 반환합니다.
    """
    res = requests.get(URL, timeout=10)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.select_one("table.table-col")
    if table is None:
        raise RuntimeError("기상청 페이지 구조가 변경되어 table.table-col을 찾을 수 없습니다.")

    results = []

    for row in table.select("tbody tr"):
        cols = [td.text.strip() for td in row.select("td")]

        # 컬럼 수가 예상보다 적으면 스킵
        if len(cols) < 8:
            continue

        city = cols[0]
        temp = float(cols[5]) if cols[5] != "-" else None
        humidity = int(cols[7]) if cols[7] != "-" else None

        results.append(
            {
                "city": city,
                "temperature": temp,
                "humidity": humidity,
                "observed_at": datetime.now(),
            }
        )

    return results

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
