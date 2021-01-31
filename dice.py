import random
import statistics
import plotly.figure_factory as pf

diceSum = []

for i in range(1,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceSum.append(dice1 + dice2)

mean = sum(diceSum) / len(diceSum)
print(mean)

median = statistics.median(diceSum)
print(median)

mode = statistics.mode(diceSum)
print(mode)

standardDeviation = statistics.stdev(diceSum)
print(standardDeviation)

fig = pf.create_distplot([diceSum], ['Result'], show_hist = False)
fig.show()


firstsdStart, firstsdEnd  = mean - standardDeviation, mean + standardDeviation
secondsdStart, secondsdEnd = mean - (2 * standardDeviation), mean + (2 * standardDeviation)
thirdsdStart, thirdsdEnd = mean - (3 * standardDeviation), mean + (3 * standardDeviation)


list_of_data_within_1_standardDeviation = [result for result in diceSum if result > firstsdStart and result < firstsdEnd]

list_of_data_within_2_standardDeviation = [result for result in diceSum if result > secondsdStart and result < secondsdEnd]

list_of_data_within_3_standardDeviation = [result for result in diceSum if result > thirdsdStart and result < thirdsdEnd]

per = format(len(list_of_data_within_1_standardDeviation) * 100 / len(diceSum))
print(per)

per2 = format(len(list_of_data_within_2_standardDeviation) * 100 / len(diceSum))
print(per2)

per3 = format(len(list_of_data_within_3_standardDeviation) * 100 / len(diceSum))
print(per3)