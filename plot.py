#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

#import seaborn
#seaborn.set(style='ticks')

#plt.style.use('ggplot')
#print(plt.style.available)
#plt.style.use('grayscale')

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


myfile = open(sys.argv[1],"r")
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

bw = True
col = ["#a6611a", "#dfc27d", "#80cdc1", "#018571"]
linestyle = ["-","-","-","-"]
if bw:
    col = ["black","black","black","black"]
    linestyle = ["-","--","-.",":"]
#linestyle = ["-","--","-.",":"]

k = 0
linje1 = plt.plot(x,aar2012, label = "2012", ls = linestyle[k], color = col[k])
k += 1
linje2 = plt.plot(x,aar2013, label = "2013", ls = linestyle[k], color = col[k])
k += 1
linje3 = plt.plot(x,aar2014, label = "2014", ls = linestyle[k], color = col[k])


plot_lines = [linje1, linje2, linje3]
#second_legend = 
#plt.legend()
#handles=[linje1, linje2, linje3], loc = 1)
#plt.gca().add_artist(second_legend)

#plt.ylabel("Akkumulerte døgngrader")
if sys.argv[1] == "data.txt":
    early = [106,75,90]
    middle = [111,89,95]
    late = [119,97,102]

    early_val = [aar2012[early[0]],aar2013[early[1]],aar2014[early[2]]]
    middle_val = [aar2012[middle[0]],aar2013[middle[1]],aar2014[middle[2]]]
    late_val = [aar2012[late[0]],aar2013[late[1]],aar2014[late[2]]]

    punkt1 = plt.scatter(early,early_val, c="black", label = "Early")
    punkt2 = plt.scatter(middle, middle_val, c = "black", marker = "v", label = "Middle")
    punkt3 = plt.scatter(late, late_val, c = "black", marker = "D", label = "Late")

    first_legend = plt.legend(handles=[punkt1, punkt2, punkt3], loc=4, frameon=False)
    plt.gca().add_artist(first_legend)
    plt.ylabel("Growing Degree Days ($^\circ$C)")
    #plt.xlabel("Dato")
    plt.ylim(0,1000)
    location = 2
    locMnd = -70
else:
    plt.ylabel("Average day temperature ($^\circ$C)")
    plt.ylim(0,25)
    location = 1
    locMnd = -1.5

plt.legend([l[0] for l in plot_lines], ["2012","2013","2014"], loc=location)
plt.xlim(0,len(date))


mndSkift = [0,31,61,92,123]
mnd = ["May","June","July","Aug.", "Sep."]
#plt.xticks(mndSkift, mnd)
plt.xticks(mndSkift,"")
#plt.xticklabels(mnd)

for i in range(len(mnd)):
    plt.text(mndSkift[i]+10, locMnd, mnd[i])

plt.tight_layout()
plt.savefig(sys.argv[1].split(".")[0] + ".png")

