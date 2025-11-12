-- a1 애플리케이션용 데이터베이스
CREATE DATABASE a1_db
    WITH OWNER = samuel
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;

-- weather 크롤러용 데이터베이스
CREATE DATABASE crawler_weather_db
    WITH OWNER = samuel
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;

-- 권한 부여 
GRANT ALL PRIVILEGES ON DATABASE a1_db TO samuel;
GRANT ALL PRIVILEGES ON DATABASE crawler_weather_db TO samuel;
