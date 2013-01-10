#!/usr/bin/python

import sys
import re
import datetime

#Le damos un anio y nos devuelve una lista con los nombres y el numero de ninos con ese nombre para ese anio
def dameNombres(file_year):
  #abrimos el archivo correspondiente a ese anio
  archivo = open('html/' + file_year + '.html', 'r')
  archivo_string = archivo.read()

  #encontramos el anio
  textos = re.search(r'(Popularity\sin\s)(\d*)', archivo_string)
  miyear = textos.group(2)

  #parseamos el documento html para quedarnos solo con los nombres y el numero asociado a cada nombre
  texto2 = re.findall(r'<td>\d+</td>\s*<td>(\w+)</td>\<td>(\d*\,*\d*)</td>\s*<td>(\w+)</td>\s*<td>(\d*\,*\d*)</td>', archivo_string)
  #texto2 me devuelve un array de tuplas de este estilo [('Pedro', '43,256', 'Marta', '321'), ('Pablo', '1,612', 'Pepa', '4,123'), ...]
  n2rM =  {}
  n2rF =  {}
  for rank_tuple in texto2:
    (boyname, rankboy, girlname, rankgirl) = rank_tuple  # desempaquetamos las tuplas
    if boyname not in n2rM:
      n2rM[boyname] = int(rankboy.replace(',', '')) #quito las comas y convierto los valores a numeros
    if girlname not in n2rF:
      n2rF[girlname] = int(rankgirl.replace(',', ''))

  #devolvemos la lista (M - Masculino, F - Femenino)
  listNames = {}
  listNames['M'] = n2rM
  listNames['F'] = n2rF

  return listNames
def listaAula(y1,tam,gen):
  listY = dameNombres(str(y1))[gen]
  listN = {}
  maximo=0
  while (sumValues(listN) < tam):
    for key in sorted(listY.keys()):
      if(listY.get(key,0) > maximo):
        maximo = listY[key]
        maxKey = key
    if(listN.get(maxKey,0) != 0):
      listN[maxKey]+=1
    else:
      listN[maxKey] = 1
    listY[maxKey] = float(listY[maxKey])/2
    maximo = 0
  return listN

def probLista(list20):
  for k in list20.keys():
    list20[k] = float(list20[k])/float(list20[sumValues(list20)])
  return list20

def reduceYear(y, size, gen):
  miLista = dameNombres(str(y))[gen]
  keysOrd = sorted(miLista, key=miLista.__getitem__, reverse=True)
  i=0
  list20 = {}
  for k in keysOrd:
    if(i>size): break
    else:
      list20[k] = miLista[k]
      i+=1
  for k in list20.keys():
    list20[k] = float(list20[k])/float(list20[maxKey(list20)])
  return list20

def num2prob(listaNum):
  suma = sumValues(listaNum)
  for k in sorted(listaNum.keys()):
    listaNum[k] = float(listaNum[k])/float(suma)
  return listaNum

#A partir de dos listas, crea una nueva anadiendo directamente los elementos no comunes y sumando los valores de los elementos comunes a las dos
def sum2Years(listY1, listY2):
  listY = {}
  for key in sorted(listY1.keys()):
    listY[key] = listY1[key] + listY2.get(key, 0)
    if(listY2.get(key,0) != 0): del listY2[key]
  for key in sorted(listY2.keys()):
    listY[key] = listY2[key]
  return listY

"""for key in sorted(listY.keys()):
  print key, listY[key]"""


#Nos devuelve la lista combinada de 
def sumYears(age2, age1):
  now = datetime.datetime.now()
  y1 = now.year - age1
  y2 = now.year - age2
  years = range(y1+1,y2+1,1)
  sumListM = dameNombres(str(y1))['M']
  for y in years:
    sumListM = sum2Years(sumListM,dameNombres(str(y))['M'])

  sumListF = dameNombres(str(y1))['F']
  for y in years:
    sumListF = sum2Years(sumListF,dameNombres(str(y))['F'])
  sumList = {}
  sumList['M'] = sumListM
  sumList['F'] = sumListF
  return sumList

def maxKey(lista):
  maxVal = 0
  for key in sorted(lista.keys()):
    if(lista[key] > maxVal):
      maxVal = lista[key]
      maxKey = key
  return maxKey

def sumValues(lista):
  suma = 0
  for key in sorted(lista.keys()):
    suma = suma + lista[key]
  return suma
def nameInYears(name):
  ann = ["1989","1990","1991","1992","1993","1994"]
  listaArr = []
  for a in ann:
    l = dameNombres(a)['M']
    for k in sorted(l.keys()):
      if(k == name):
        listaArr.append(l[k])
  return listaArr
