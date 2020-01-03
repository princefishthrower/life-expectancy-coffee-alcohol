import csv
from collections import defaultdict
from operator import itemgetter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


lDataDicts = []
lDataFiles = ['life-expectancy.csv', 'alcohol.csv', 'coffee.csv', 'suicide.csv', 'happiness.csv']

for sDataFile in lDataFiles:
    with open(sDataFile, mode='r') as oFile:
        oReader = csv.DictReader(oFile)    
        lData = []
        for dLine in oReader:
            lData.append(dLine)
        lDataDicts.append(lData)

d = defaultdict(dict)
for l in (lDataDicts[0], lDataDicts[1], lDataDicts[2], lDataDicts[3], lDataDicts[4]):
    for elem in l:
        d[elem['Country']].update(elem)

lCombinedDictsByCountry = sorted(d.values(), key=itemgetter("Country"))

oDataFrame = pd.DataFrame(lCombinedDictsByCountry)
oDataFrame.dropna(inplace=True) # need countries with all statistics
oDataFrame.reset_index(drop=True, inplace=True)
oDataFrame.LifeExpectancy = oDataFrame.LifeExpectancy.astype(float)
oDataFrame.AlcoholConsumption = oDataFrame.AlcoholConsumption.astype(float)
oDataFrame.CoffeeConsumption = oDataFrame.CoffeeConsumption.astype(float)
oDataFrame.AgeStandardizedRate = oDataFrame.AgeStandardizedRate.astype(float)
oDataFrame.HappinessScore = oDataFrame.HappinessScore.astype(float)



# plot 1 - alcohol vs longevity
fig, ax = plt.subplots()
ax.grid(color='black', linestyle='-', linewidth=1)
ax.scatter(oDataFrame.AlcoholConsumption, oDataFrame.LifeExpectancy, color="black")
for i, sCountry in enumerate(oDataFrame.Country): # add country name to each point
    ax.annotate(sCountry, (oDataFrame.loc[oDataFrame['Country'] == sCountry].AlcoholConsumption*1.005, oDataFrame.loc[oDataFrame['Country'] == sCountry].LifeExpectancy*1.005))
plt.locator_params(axis='x', nbins=15)
plt.locator_params(axis='y', nbins=15)
plt.title("Life Expectancy vs. Alcohol Consumption")
plt.ylabel('Life Expectancy (Years)')
plt.xlabel('Alcohol Consumption (Liters per Capita)')
lFit = np.polyfit(oDataFrame.AlcoholConsumption, oDataFrame.LifeExpectancy, 1)
oFunction = np.poly1d(lFit)
ax.plot(oDataFrame.AlcoholConsumption, oFunction(oDataFrame.AlcoholConsumption),"k-")
# the line equation:
print "y=%.6fx+(%.6f)"%(lFit[0],lFit[1])
plt.show()

# plot 2 coffee consumption vs longevity
fig, ax = plt.subplots()
ax.grid(color='black', linestyle='-', linewidth=1)
ax.scatter(oDataFrame.CoffeeConsumption, oDataFrame.LifeExpectancy, color="black")
for i, sCountry in enumerate(oDataFrame.Country): # add country name to each point
    ax.annotate(sCountry, (oDataFrame.loc[oDataFrame['Country'] == sCountry].CoffeeConsumption*1.005, oDataFrame.loc[oDataFrame['Country'] == sCountry].LifeExpectancy*1.005))
plt.locator_params(axis='x', nbins=15)
plt.locator_params(axis='y', nbins=15)
plt.title("Life Expectancy vs. Coffee Consumption")
plt.ylabel('Life Expectancy (Years)')
plt.xlabel('Coffee Consumption (KG per Capita)')
lFit = np.polyfit(oDataFrame.CoffeeConsumption, oDataFrame.LifeExpectancy, 1)
oFunction = np.poly1d(lFit)
ax.plot(oDataFrame.CoffeeConsumption, oFunction(oDataFrame.CoffeeConsumption),"k-")
# the line equation:
print "y=%.6fx+(%.6f)"%(lFit[0],lFit[1])
plt.show()


# plot 3 suicide vs coffee consumption
fig, ax = plt.subplots()
ax.grid(color='black', linestyle='-', linewidth=1)
ax.scatter(oDataFrame.CoffeeConsumption, oDataFrame.AgeStandardizedRate, color="black")
for i, sCountry in enumerate(oDataFrame.Country): # add country name to each point
    ax.annotate(sCountry, (oDataFrame.loc[oDataFrame['Country'] == sCountry].CoffeeConsumption*1.005, oDataFrame.loc[oDataFrame['Country'] == sCountry].AgeStandardizedRate*1.005))
plt.locator_params(axis='x', nbins=15)
plt.locator_params(axis='y', nbins=15)
plt.title("Suicide Rate vs. Coffee Consumption")
plt.ylabel('Suicide Rate (Years)')
plt.xlabel('Coffee Consumption (KG per Capita)')
lFit = np.polyfit(oDataFrame.CoffeeConsumption, oDataFrame.AgeStandardizedRate, 1)
oFunction = np.poly1d(lFit)
ax.plot(oDataFrame.CoffeeConsumption, oFunction(oDataFrame.CoffeeConsumption),"k-")
# the line equation:
print "y=%.6fx+(%.6f)"%(lFit[0],lFit[1])
plt.show()

# plot 4 happiness vs coffee consumption
fig, ax = plt.subplots()
ax.grid(color='black', linestyle='-', linewidth=1)
ax.scatter(oDataFrame.CoffeeConsumption, oDataFrame.HappinessScore, color="black")
for i, sCountry in enumerate(oDataFrame.Country): # add country name to each point
    ax.annotate(sCountry, (oDataFrame.loc[oDataFrame['Country'] == sCountry].CoffeeConsumption*1.005, oDataFrame.loc[oDataFrame['Country'] == sCountry].HappinessScore*1.005))
plt.locator_params(axis='x', nbins=15)
plt.locator_params(axis='y', nbins=15)
plt.title("Relative Happiness Score vs. Coffee Consumption")
plt.ylabel('Relative Happiness Score')
plt.xlabel('Coffee Consumption (KG per Capita)')
lFit = np.polyfit(oDataFrame.CoffeeConsumption, oDataFrame.HappinessScore, 1)
oFunction = np.poly1d(lFit)
ax.plot(oDataFrame.CoffeeConsumption, oFunction(oDataFrame.CoffeeConsumption),"k-")
# the line equation:
print "y=%.6fx+(%.6f)"%(lFit[0],lFit[1])
plt.show()

# plot 5 happiness vs suicide rate
fig, ax = plt.subplots()
ax.grid(color='black', linestyle='-', linewidth=1)
ax.scatter(oDataFrame.HappinessScore, oDataFrame.AgeStandardizedRate, color="black")
for i, sCountry in enumerate(oDataFrame.Country): # add country name to each point
    ax.annotate(sCountry, (oDataFrame.loc[oDataFrame['Country'] == sCountry].HappinessScore*1.005, oDataFrame.loc[oDataFrame['Country'] == sCountry].AgeStandardizedRate*1.005))
plt.locator_params(axis='x', nbins=15)
plt.locator_params(axis='y', nbins=15)
plt.title("Suicide Rate vs. Relative Happiness Score")
plt.ylabel('Suicide Rate')
plt.xlabel('Relative Happiness Score')
lFit = np.polyfit(oDataFrame.HappinessScore, oDataFrame.AgeStandardizedRate, 1)
oFunction = np.poly1d(lFit)
ax.plot(oDataFrame.HappinessScore, oFunction(oDataFrame.HappinessScore),"k-")
# the line equation:
print "y=%.6fx+(%.6f)"%(lFit[0],lFit[1])
plt.show()


# plot 4 - coffee + alcohol vs longevity 3d plot
ax = plt.axes(projection='3d')
plt.hold(True) # both surface and scatter here

# Data for three-dimensional scattered points
zdata = oDataFrame.LifeExpectancy
xdata = oDataFrame.AlcoholConsumption
ydata = oDataFrame.CoffeeConsumption
ax.plot_trisurf(xdata, ydata, zdata, cmap=cm.jet, linewidth=0)
ax.scatter3D(xdata, ydata, zdata, c='black')
for i, sCountry in enumerate(oDataFrame.Country): # add country name to each point
    ax.text(oDataFrame.iloc[i].AlcoholConsumption*1.005, oDataFrame.iloc[i].CoffeeConsumption*1.005, oDataFrame.iloc[i].LifeExpectancy*1.005, sCountry, None)
    
plt.title("Life Expectancy as a function of Coffee & Alcohol Consumption")
ax.set_xlabel('Alcohol Consumption (Liters per Capita)')
ax.set_ylabel('Coffee Consumption (KG per Capita)')
ax.set_zlabel('Life Expectancy (Years)')
plt.show()



