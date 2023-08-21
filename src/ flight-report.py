import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrame = {
            'altitude': [0, 40, 50 ,60],
            'temperature': [30, 40, 50 ,60],
            'battery-voltage': [30, 40, 50 ,60],
            'air-pressure': [30, 40, 50 ,60],
            'gps-altitude': [30, 40, 50 ,60],
            'gps-latitude': [30, 40, 50 ,60],
            'gps-longitude': [30, 40, 50 ,60],
            'humidity': [30, 40, 50 ,60],
            'time': [1, 2, 3 ,4]
        }

df = pd.DataFrame(dataFrame, columns=['a', 'b', 'c', 'd'])

f = open('Dados_1h24.txt')

for line in f:
    if '| A:' in line:
        altitude = line.split(' ')[2].strip().replace('A:','')
        print(altitude)



# print("Line graph: ")
# plt.plot(df["time"], df["altitude"])
# plt.show()



