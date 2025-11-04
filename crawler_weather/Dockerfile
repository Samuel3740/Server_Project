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

# 앱 소스는 로컬에서 바인드 마운트할 예정이므로 비워둠
# COPY . .

# 임시: 컨테이너가 바로 종료되지 않도록 무한 대기 상태로 유지
# 추후 main.py가 준비되면 CMD를 ["python","main.py"]로 변경
CMD ["tail", "-f", "/dev/null"]
