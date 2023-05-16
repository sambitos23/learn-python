import os
import time

REPEAT_INTERVAL = 10

while True:
    command = "say \'Hello Sambit, Drink Water\'; notify-send \"Drink Water\""
    os.system(command)
    time.sleep(REPEAT_INTERVAL)
