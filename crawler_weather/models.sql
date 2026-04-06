CREATE TABLE IF NOT EXISTS city_weather (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    temperature REAL,
    humidity INTEGER,
    observed_at TIMESTAMP NOT NULL
);

