import time
import random

while True:
    sleep_duration = random.uniform(2, 5)
    print('hey')
    time.sleep(sleep_duration)
    print(f'sleeping for {sleep_duration}')
    print('how are you')