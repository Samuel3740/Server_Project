import os

import psycopg2
from dotenv import load_dotenv


# 로컬 실행 시 .env를 읽어오고, Docker 환경에서는 docker-compose의 환경변수를 사용합니다.
load_dotenv()


def get_connection():
    """
    환경 변수에 설정된 PostgreSQL 정보로 커넥션을 생성합니다.

    필요한 환경변수:
      - POSTGRES_HOST
      - POSTGRES_DB
      - POSTGRES_USER
      - POSTGRES_PASSWORD
    """
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=5432,
    )

