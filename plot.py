#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
#import seaborn
#seaborn.set(style='ticks')

#plt.style.use('ggplot')

SIZE = 14
MEDIUM_SIZE = 16
BIGGER_SIZE = 18

plt.rc('font', size=SIZE)                # controls default text sizes
plt.rc('axes', titlesize=SIZE)           # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZE)          # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZE)          # fontsize of the tick labels
plt.rc('legend', fontsize=SIZE)          # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

myfile = open("data.txt","r")
lines = myfile.readlines()
myfile.close()

date = []
aar2012 = []
aar2013 = []
aar2014 = []

for i in lines:
    try:
        words = i.split()
        date.append(words[0])
        aar2012.append(float(words[1]))
        aar2013.append(float(words[2]))
        aar2014.append(float(words[3]))
    except:
        print(i)

print(date)


x = np.arange(len(date))

linestyle = ["-","--","-.",":"]
k = 0
plt.plot(x,aar2012, label = "2012", ls = linestyle[k], color = "black")
k += 1
plt.plot(x,aar2013, label = "2013", ls = linestyle[k], color = "black")
k += 1
plt.plot(x,aar2014, label = "2014", ls = linestyle[k], color = "black")

plt.legend()
plt.ylabel("Akkumulerte døgngrader")
plt.xlabel("Dato")
plt.ylim(0,1000)

plt.show()

bw = True
col = ["#a6611a", "#dfc27d", "#80cdc1", "#018571"]
linestyle = ["-","-","-","-"]
if bw:
    col = ["black","black","black","black"]



m = 0
navn = ["TA", "TP", "EA", "MS"]
aar = ["2012","2013","2014"]
multe = ["102","306","Fjellgull","Fjordgull"]
xakse = ["Early","Middle","Late","Early","Middle","Late","Early","Middle","Late"]



