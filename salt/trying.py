#!/usr/bin/python

import babynames
import sys
#import numpy as np
#from matplotlib import cm
#import matplotlib.pyplot as plt
"""
#data
x=[1989, 1990, 1991, 1992, 1993, 1994]
y=babynames.nameInYears("Jacob")

for i in range(0,len(x)):
  plt.bar(x[i],y[i],color=cm.jet(1.*i/len(x)))

plt.show()
"""
from pylab import *

def main():
    miAula = babynames.listaAula(1991,30,1994,70,15,'M')
    bar_graph(miAula, graph_title='Aula ejemplo')


def bar_graph(name_value_dict, graph_title='', output_name='bargraph.png'):
    figure(figsize=(20, 10)) # image dimensions   
    title(graph_title, size='x-small')
    
    # add bars
    for i, key in zip(range(len(name_value_dict)), name_value_dict.keys()):
        bar(i + 0.25 , name_value_dict[key], color='red')
    
    # axis setup
    xticks(arange(0.65, len(name_value_dict)), 
        [('%s: %d' % (name, value)) for name, value in 
        zip(name_value_dict.keys(), name_value_dict.values())], 
        size='xx-small')
    max_value = max(name_value_dict.values())
    print max_value
    #tick_range = arange(0, max_value, (max_value / 65))
    tick_range = arange(0,max_value,1)
    yticks(tick_range, size='xx-small')
    formatter = FixedFormatter([str(x) for x in tick_range])
    gca().yaxis.set_major_formatter(formatter)
    gca().yaxis.grid(which='major') 
    
    savefig(output_name)


if __name__ == "__main__":
    main()

"""
miAula = babynames.listaAula(1991,30,1994,70,65,'M')

x = miAula.keys()
y = miAula.values()
for i in range(0,len(x)):
  plt.bar(x[i],y[i],color=cm.jet(1.*i/len(x)))

plt.show()

listY = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5,'f':6}
keysOr = list(sorted(listY, key=listY.__getitem__, reverse=True))
tam = 3
valuesOr = []
r=0
for v in sorted(listY.values(), reverse=True):
	valuesOr.append(v)

misKeys = keysOr[:tam]
misValues = valuesOr[:tam]
print listY
print misKeys
print misValues


aulaKey, aulaVal = babynames.listaAula(1991,30,1994,70,4,'M')

for i in range(0,len(aulaKey)):
  plt.bar(aulaKey[i],aulaVal[i],color=cm.jet(1.*i/len(aulaKey)))

plt.show()
"""