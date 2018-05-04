
time24 = range(1, 25) # from 1 to 24 hour
load = [40, 75, 50, 40, 0, 2, 0, 20, 30, 25, 20, 50, # load of grid every hour
        60, 55, 120, 115, 145, 245, 330, 340, 560, 555, 300, 215] # in kW

# time splited by the electricity factory
peak = [10, 11, 12, 13, 14, 18, 19, 20] # peak time in a day
flat = [7, 8, 9, 15, 16, 17, 21, 22] # flat time in a day
valley = [23, 24, 1, 2, 3, 4, 5, 6] # vally time in a day

# 
avgPeak = sum([load[i-1] for i in peak]) / 8
avgFlat = sum([load[i-1] for i in flat]) / 8
avgValley = sum([load[i-1] for i in valley]) / 8

totalLoad = avgPeak + avgFlat + avgValley
totalCar = 996

peakCarNum = avgPeak / totalLoad * totalCar
flatCarNum = avgFlat / totalLoad * totalCar
valleyCarNum = avgValley / totalLoad * totalCar

def fitness(number):
    return sum(number)
