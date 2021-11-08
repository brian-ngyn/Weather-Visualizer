import numpy as np
import matplotlib.pyplot as pyplot

class FileIO:
    def read_weather(x):
        filepath = x
        dataTable = np.loadtxt(filepath, delimiter=',', skiprows=1, dtype=np.float)
        return dataTable