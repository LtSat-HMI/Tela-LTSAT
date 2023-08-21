import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrame = {
            'altitude': [30, 40, 50 ,60],
            'time': [1, 2, 3 ,4]
        }

df = pd.DataFrame(dataFrame)

print("Line graph: ")
plt.plot(df["time"], df["altitude"])
plt.show()



