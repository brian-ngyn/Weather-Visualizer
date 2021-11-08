import numpy as np
import matplotlib.pyplot as pyplot

class WeatherAnalyzer:
    def __init__(self, temperatureData):
        self.temperatureData = np.array(temperatureData)

    def getMinTemp(self):
        y = []
        num_rows, num_cols = self.temperatureData.shape
        for count in range(0,num_rows):
            y.append(self.temperatureData[count,3])
        return np.min(y)

    def getMinTempAnually(self):
        num_rows, num_cols = self.temperatureData.shape
        first_year = int(self.temperatureData[0,0])
        last_year = int(self.temperatureData[num_rows-1,0])
        count = 0
        counter = 0
        x = []
        for s in range (first_year, last_year+1):
            y = []
            while (count < num_rows) and (self.temperatureData[count,0] == first_year + counter):
                y.append(self.temperatureData[count,3])
                count +=1
            combinedlist = ([int(self.temperatureData[count-1,0]), np.min(y)])
            x.append(combinedlist)
            counter +=1
        return x

    def getMaxTemp(self):
        y = []
        num_rows, num_cols = self.temperatureData.shape
        for count in range(0,num_rows):
            y.append(self.temperatureData[count,2])
        return np.max(y)

    def getMaxTempAnually(self):
        num_rows, num_cols = self.temperatureData.shape
        first_year = int(self.temperatureData[0,0])
        last_year = int(self.temperatureData[num_rows-1,0])
        count = 0
        counter = 0
        x = []
        for s in range (first_year, last_year+1):
            y = []
            while (count < num_rows) and (self.temperatureData[count,0] == first_year + counter):
                y.append(self.temperatureData[count,2])
                count +=1
            combinedlist = ([int(self.temperatureData[count-1,0]), np.max(y)])
            x.append(combinedlist)
            counter +=1
        return x

    def AvgSnowFallAnually(self):
        num_rows, num_cols = self.temperatureData.shape
        first_year = int(self.temperatureData[0,0])
        last_year = int(self.temperatureData[num_rows-1,0])
        count = 0
        counter = 0
        x = []
        for s in range (first_year, last_year+1):
            y = []
            while (count < num_rows) and (self.temperatureData[count,0] == first_year + counter):
                y.append(self.temperatureData[count,4])
                count +=1
            combinedlist = ([int(self.temperatureData[count-1,0]), np.average(y)])
            x.append(combinedlist)
            counter +=1
        return x

    def getAvgTempAnually(self):
        num_rows, num_cols = self.temperatureData.shape
        first_year = int(self.temperatureData[0,0])
        last_year = int(self.temperatureData[num_rows-1,0])
        count = 0
        counter = 0
        x = []
        for s in range (first_year, last_year+1):
            y = []
            while (count < num_rows) and (self.temperatureData[count,0] == first_year + counter):
                y.append(self.temperatureData[count,2])
                y.append(self.temperatureData[count,3])
                count +=1
            combinedlist = ([int(self.temperatureData[count-1,0]), np.average(y)])
            x.append(combinedlist)
            counter +=1
        return x