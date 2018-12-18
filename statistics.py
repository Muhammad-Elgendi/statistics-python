import pandas
import math
import matplotlib.pyplot as pl
import numpy as np

def getMean(data):
    sum = 0
    for i in range(data.size):
        sum+= data[i]    
    return sum/data.size

def getRange(data):
    return data.max() - data.min()

def getMedian(data):
    isEven = data.size % 2  == 0
    if(isEven):
        index1 = data.size /2 -1
        index2 = data.size /2
        return (data[index1]+data[index2])/2   
    else:
        return data[round(data.size/2) -1]
    
def getMode(data):
    maxValue = 0
    maxCount = 0
    for i in range(data.size):
        count = 0
        for j in range(data.size):        
            if (data[j] == data[i]):
                count+=1        
        if (count > maxCount):
            maxCount = count
            maxValue = data[i]
    return  maxValue

def getIQR(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    return q3 -q1


def getVariance(data):
    mean = getMean(data)
    sum = 0
    for i in range(data.size):
        sum+= (data[i] - mean)**2    
    return sum/(data.size -1)

def getStandardDeviation(data):
    return math.sqrt(getVariance(data))


dataFrame = pandas.read_csv('simpleDataSet.csv')
# print(dataFrame.head(5))
# print(dataFrame['asviSrc'][0])
# i =dataFrame['asviSrc']
# print(type(i))
# print(dataFrame['asviSrc'].size)
dataFrame.sort_values(by=['asviSrc'])
data = dataFrame['asviSrc']

print('mean',getMean(data))
print('range',getRange(data))
print('variance',getVariance(data))
print('median',getMedian(data))
print('mode',getMode(data))
print('IQR',getIQR(data))
print('standard deviation',getStandardDeviation(data))

hist = dataFrame.hist()
pl.savefig("histogram.png")