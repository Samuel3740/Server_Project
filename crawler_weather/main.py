# from crawler import crawl_weather
# from db import get_connection

# def main():
#     conn = get_connection()
#     cur = conn.cursor()

#     # 테이블 생성
#     with open("models.sql", "r", encoding="utf-8") as f:
#         cur.execute(f.read())
#         conn.commit()

#     data = crawl_weather()

#     insert_sql = """
#         INSERT INTO city_weather
#         (city, temperature, humidity, observed_at)
#         VALUES (%s, %s, %s, %s)
#     """

#     for d in data:
#         cur.execute(insert_sql, (
#             d["city"],
#             d["temperature"],
#             d["humidity"],
#             d["observed_at"]
#         ))

#     conn.commit()
#     cur.close()
#     conn.close()

#     print(f"[OK] {len(data)} rows inserted into crawler_weather_db")

# if __name__ == "__main__":
#     main()
