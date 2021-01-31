import random
import statistics
import pandas as pd
import csv
import plotly.figure_factory as pf

df = pd.read_csv('data.csv')

height = df['Height(Inches)'].to_list()
weight = df['Weight(Pounds)'].to_list()

heightMean = statistics.mean(height)
weightMean = statistics.mean(weight)

heightMedian = statistics.median(height)
weightMedian = statistics.median(weight)

heightMode = statistics.mode(height)
weightMode = statistics.mode(weight)

heightstd = statistics.stdev(height)
weightstd = statistics.stdev(weight)

#height

heightfirstsdStart, heightfirstsdEnd  = heightMean - heightstd, heightMean + heightstd
heightsecondsdStart, heightsecondsdEnd = heightMean - (2 * heightstd),  heightMean + (2 * heightstd)
heightthirdsdStart, heightthirdsdEnd = heightMean - (3 * heightstd), heightMean + (3 * heightstd)

data_of_1_height = [result for result in height if result > heightfirstsdStart and result < heightfirstsdEnd]

data_of_2_height = [result for result in height if result > heightsecondsdStart and result < heightsecondsdEnd]

data_of_3_height = [result for result in height if result > heightthirdsdStart and result < heightthirdsdEnd]

per1 = format(len(data_of_1_height) * 100 / len(height))
print(per1)

per2 = format(len(data_of_2_height) * 100 / len(height))
print(per2)

per3 = format(len(data_of_3_height) * 100 / len(height))
print(per3)


#weight

weightfirstsdStart, weightfirstsdEnd  = weightMean - weightstd, weightMean + weightstd
weightsecondsdStart, weightsecondsdEnd  = weightMean - (2 * weightstd), weightMean + (2 *weightstd)
weightthirdsdStart, weightthirdsdEnd  = weightMean - (3 * weightstd), weightMean + (3 *weightstd)


data_of_1_weight = [result for result in weight if result > weightfirstsdStart and result < weightfirstsdEnd]

data_of_2_weight = [result for result in weight if result > weightsecondsdStart and result < weightsecondsdEnd]

data_of_3_weight = [result for result in weight if result > weightthirdsdStart and result < weightthirdsdEnd]

per1 = format(len(data_of_1_weight) * 100 / len(weight))
print(per1)

per2 = format(len(data_of_2_weight) * 100 / len(weight))
print(per2)

per3 = format(len(data_of_3_weight) * 100 / len(weight))
print(per3)