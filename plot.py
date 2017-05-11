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

# Lese inn data
for i in lines:
    try:
        words = i.split()
        date.append(words[0])
        aar2012.append(float(words[1]))
        aar2013.append(float(words[2]))
        aar2014.append(float(words[3]))
    except:
        print(i)

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
#plt.xlabel("Dato")
plt.ylim(0,1000)
plt.xlim(0,len(date))

early = [106,75,90]
middle = [111,89,95]
late = [119,97,102]

early_val = [aar2012[early[0]],aar2013[early[1]],aar2014[early[2]]]
middle_val = [aar2012[middle[0]],aar2013[middle[1]],aar2014[middle[2]]]
late_val = [aar2012[late[0]],aar2013[late[1]],aar2014[late[2]]]

plt.scatter(early,early_val)
plt.scatter(middle, middle_val)
plt.scatter(late, late_val)

mndSkift = [0,31,61,92,123]
mnd = ["Mai","Juni","Juli","Aug.", "Sep."]
#plt.xticks(mndSkift, mnd)
plt.xticks(mndSkift,"")
#plt.xticklabels(mnd)

for i in range(len(mnd)):
    plt.text(mndSkift[i]+10, -70, mnd[i])

plt.tight_layout()
plt.savefig("plot.png")

