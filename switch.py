import redis 
import subprocess
import time

rdev = redis.Redis(
    host="127.0.0.1",
    port="6379",
    password="",
    decode_responses=True
)

previous_state = None

while True:
    try:
        current_state = rdev.get("switch")
            
        if current_state != previous_state:
            print(f"Switch state changed: {previous_state} to {current_state}")

            if current_state == "on":
                print("Switch is on................................................................")
                subprocess.run("/bin/bash video -k && chvt 7", shell=True)
                # subprocess.run("su - sotpurk -c 'export DISPLAY=:0 && cd /home/sotpurk/airport-node/ && node index.js' &", shell=True)
                subprocess.run("su - sotpurk -c 'export DISPLAY=:0 && /bin/bash /home/sotpurk/airport-node/startindex.sh'" , shell=True)

            else:
                print("Switch is off................................................................................")
                subprocess.run("su - sotpurk -c 'export DISPLAY=:0 && pkill -f chromium && pkill -f chromium'", shell=True)
                subprocess.run("chvt 1 && /bin/bash video -s", shell=True)
            previous_state = current_state

        time.sleep(1)  

    except Exception as e:
        print("Error:", e)
