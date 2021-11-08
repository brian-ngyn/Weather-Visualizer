import numpy as np
import matplotlib.pyplot as pyplot
from Chart import Chart
from FileIO import FileIO
from WeatherAnalyzer import WeatherAnalyzer

def main():
    data = FileIO.read_weather("CalgaryWeather.csv")
    num_rows, num_cols = data.shape
    first_year = int(data[0,0])
    last_year = int(data[num_rows-1,0])
    data = WeatherAnalyzer(data)
    degree_sign= u'\N{DEGREE SIGN}'
    loop = True
    print("Welcome to Calgary Weather Analyzer! Please choose an option.")

    while loop == True:
        useroption = int(input("""\n1- Get Minimum Temperature of 1990-2019 \n2- Get Maximum Temperature of 1990-2019 \n3- Get Minimum Temperature of 1990-2019 Anually
4- Get Maximum Temperature of 1990-2019 Anually \n5- Get Average Snowfall between 1990-2019 Anually \n6- Get Average Temperature between 1990-2019 Anuallly
7- LineChart Minimum Temperature of 1990-2019 Anually \n8- LineChart Maximum Temperature of 1990-2019 Anually \n9- BarChart Average Snowfall between 1990-2019 Anually
10- BarChart Average Temperature betweeen 1990-2019 Anually \n11- Exit the program \nPlease choose an option: """))
    
        if useroption == 1:
            print(f"The minimum temperature between {first_year}-{last_year} is {WeatherAnalyzer.getMinTemp(data)}{degree_sign}C")

        elif useroption == 2:
            print(f"The maximum temperature between {first_year}-{last_year} is {WeatherAnalyzer.getMaxTemp(data)}{degree_sign}C")

        elif useroption == 3:
            x = np.array(WeatherAnalyzer.getMinTempAnually(data))
            count = 0
            for row in x:
                print(f"The minimum temperature in the year {int(x[count,0])} is {x[count,1]}{degree_sign}C")
                count +=1

        elif useroption == 4:
            x = np.array(WeatherAnalyzer.getMaxTempAnually(data))
            count = 0
            for row in x:
                print(f"The maximum temperature in the year {int(x[count,0])} is {x[count,1]}{degree_sign}C")
                count +=1

        elif useroption == 5:
            print("The average snowfall anually is: ")
            for row in WeatherAnalyzer.AvgSnowFallAnually(data):
                print(row)

        elif useroption == 6:
            x = np.array(WeatherAnalyzer.getAvgTempAnually(data))
            count = 0
            for row in x:
                print(f"The average temperature in the year {int(x[count,0])} is {x[count,1]}{degree_sign}C")
                count +=1

        elif useroption == 7:
            x = np.array(WeatherAnalyzer.getMinTempAnually(data))
            a = []
            b = []
            count = 0
            for row in x:
                a.append(int(x[count,0]))
                b.append(x[count,1])
                count +=1
            Chart.drawLineChart(a, b, 'Minimum Temperature of 1990-2019 Anually', 'Year', 'Temperature') 

        elif useroption == 8:
            x = np.array(WeatherAnalyzer.getMaxTempAnually(data))
            a = []
            b = []
            count = 0
            for row in x:
                a.append(int(x[count,0]))
                b.append(x[count,1])
                count +=1
            Chart.drawLineChart(a, b, 'Maximum Temperature of 1990-2019 Anually', 'Year', 'Temperature')
    
        elif useroption == 9:
            x = np.array(WeatherAnalyzer.AvgSnowFallAnually(data))
            a = []
            b = []
            count = 0
            for row in x:
                a.append(int(x[count,0]))
                b.append(x[count,1])
                count +=1
            Chart.drawBarChart(a, b, 'Average Snowfall between 1990-2019 Anually', 'Year', 'Snowfall')

        elif useroption == 10:
            x = np.array(WeatherAnalyzer.getAvgTempAnually(data))
            a = []
            b = []
            count = 0
            for row in x:
                a.append(int(x[count,0]))
                b.append(x[count,1])
                count +=1
            Chart.drawBarChart(a, b, 'Average Temperature between 1990-2019 Anually', 'Year', 'Temperature')

        elif useroption == 11:
            break

        else: 
            print("Your option was out of range, please try again")

if __name__ == "__main__":
    main()