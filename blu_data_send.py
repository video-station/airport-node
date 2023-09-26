import pandas as pd
import json
import redis

rdev = redis.Redis(
    host="127.0.0.1",
    port=6379,
    password=""
)

excel_file = 'data\\media.xlsx'  
df = pd.read_excel(excel_file)

df['path'] = 'downloads' + df['path']
data = df.to_dict(orient='records')
#folder = "/downloads"

json_data = json.dumps(data)

try:
    rdev.set("content", json_data)
    print(f"JSON data sent to Redis key 'content' successfully.")
except Exception as e:
    print(f"Failed to send data to Redis: {str(e)}")
