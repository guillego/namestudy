#!/usr/bin/python

import babynames
import sys
import matplotlib
matplotlib.use('Agg')
from pylab import *
import time

def main():
    mitime =  time.time()
    name = ('img/' + str(int(mitime)) + '.png')
    tam = int(sys.argv[1])
    ano = int(sys.argv[2])
    miAula = babynames.listaAula(ano,30,1994,0,tam,'M')
    bar_graph(miAula, graph_title='Aula ejemplo', output_name=name)


def bar_graph(name_value_dict, graph_title='', output_name='bargraph.png'):
    mifig = figure(figsize=(14, 7)) # image dimensions   
    title(graph_title, size='x-small')
    
    # add bars
    for i, key in zip(range(len(name_value_dict)), name_value_dict.keys()):
        bar(i + 0.25 , name_value_dict[key], color='red')
    
    # axis setup
    xticks(arange(0.65, len(name_value_dict)), 
        [('%s' % (name)) for name, value in 
        zip(name_value_dict.keys(), name_value_dict.values())], 
        size='xx-small')
    max_value = max(name_value_dict.values())
    #tick_range = arange(0, max_value, (max_value / 65))
    tick_range = arange(0,max_value,1)
    yticks(tick_range, size='xx-small')
    formatter = FixedFormatter([str(x) for x in tick_range])
    gca().yaxis.set_major_formatter(formatter)
    gca().yaxis.grid(which='major') 
    mifig.savefig(output_name)
    print output_name
    for k in sorted(name_value_dict.keys()):
        print k, name_value_dict[k]

if __name__ == "__main__":
    main()