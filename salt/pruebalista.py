#!/usr/bin/python

import babynames
import sys
import numpy as np
import matplotlib.pyplot as plt

#lista = babynames.sumYears(19,22)

#for key in sorted(lista.keys()):
#  print key, lista[key]

#lista = babynames.sumYears(19,22)['M']


#!/usr/bin/env python
# a bar plot with errorbars


#mu, sigma = 100, 15
#x = mu + sigma * np.random.randn(10000)
ArrAnn = tuple(babynames.nameInYears("Peter"))

N = 5
menStd =   (2, 3, 4, 1, 2)
ind = np.arange(ArrAnn)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, ArrAnn, width, color='r', yerr=menStd)

# add some
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1990', '1991', '1992', '1993', '1994') )

ax.legend( (rects1[0], 'Men')

#for rect in rects1:
#	height = rect.get_height()
#    ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#    ha='center', va='bottom')

#plt.show()
print rects1
