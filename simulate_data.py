import pandas as pd
import random
from datetime import datetime, timedelta

data = []
start_time = datetime.now()

for i in range(500):
    temp = round(random.uniform(26, 34), 2)
    ph = round(random.uniform(6.0, 8.0), 2)
    ammonia = round(random.uniform(0.1, 1.0), 2)
    do = round(random.uniform(3.5, 8.0), 2)

    # Label based on unsafe ranges
    risk = 1 if (temp > 32 or ph < 6.5 or ammonia > 0.8 or do < 4) else 0

    data.append([
        start_time + timedelta(minutes=i),
        temp, ph, ammonia, do, risk
    ])

df = pd.DataFrame(data, columns=["timestamp", "temp_c", "ph", "ammonia_mg_l", "do_mg_l", "failure_risk"])
df.to_csv("data/fish_sensor_data.csv", index=False)
