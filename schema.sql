CREATE TABLE sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temp_c REAL,
    ph REAL,
    ammonia_mg_l REAL,
    do_mg_l REAL,
    failure_risk INTEGER
);
