#!/usr/bin/python

import babynames
import sys
import matplotlib
matplotlib.use('Agg')
from pylab import *
import time

def main():
    tam = int(sys.argv[1])
    ano = int(sys.argv[2])
    gen = int(sys.argv[3])
    mf = 'M'
    if gen==0: mf = 'M'
    else: mf = 'F'
    name1 = ('img/' + str(int(time.time())) + '.png')
    name2 = ('img/' + str(int(time.time()) + int(time.time())) + '.png')
    name3 = ('img/' + str(5*int(time.time())+2) + '.png')
    miAula1 = babynames.listaAula(ano, tam, mf)
    miAula2 = babynames.probLista(babynames.listaAula(ano,tam,mf))
    miAula3 = babynames.reduceYear(ano, tam, mf)
    bar_graph(miAula1, graph_title='Aula ejemplo', output_name=name1)
    bar_graph(miAula2, graph_title='Probabilidades Aula ejemplo', output_name=name2)
    bar_graph(miAula3, graph_title='Probabilidades distribucion', output_name=name3)
    print name1
    print name2
    print name3
    print "Sistema D'Hont sobre 1000 nombres:"
    for k in sorted(miAula1.keys()):
        print k, miAula1[k]

    print "<br/> <br/>Probabilidades sistema D'Hont sobre 1000 nombres:"
    for k in sorted(miAula2.keys()):
        print k, miAula2[k]      

    print "<br/> <br/>Probabilidades Sistema D'Hont sobre " + str(tam) + " nombres:"
    for k in sorted(miAula3.keys()):
        print k, miAula3[k]



def bar_graph(name_value_dict, graph_title='', output_name='bargraph.png'):
    mifig = figure(figsize=(8, 4)) # image dimensions   
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
    tick_range = arange(0,max_value,0.25)
    yticks(tick_range, size='xx-small')
    formatter = FixedFormatter([str(x) for x in tick_range])
    gca().yaxis.set_major_formatter(formatter)
    gca().yaxis.grid(which='major') 
    mifig.savefig(output_name)
    

if __name__ == "__main__":
    main()