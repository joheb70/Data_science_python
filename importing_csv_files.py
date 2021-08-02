import time
import os
import pandas as pd


while True:
    if os.path.exists("temps_today.csv"):
        data = pd.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("file does not exist")
    
    time.sleep(10)
    







