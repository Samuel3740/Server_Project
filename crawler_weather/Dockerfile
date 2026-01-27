FROM python:3.11-slim

WORKDIR /app

# psycopg2-binary 설치를 위한 시스템 패키지
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드는 docker-compose에서 바인드 마운트하므로 여기서는 복사하지 않습니다.

# 컨테이너가 시작되면 main.py를 실행하여 한 번 크롤링 후 종료
CMD ["python", "main.py"]
