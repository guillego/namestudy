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

#Crea la lista del "aula" con la capacidad especificada en 'tam' y la distribuye siguiendo el Sistema D'Hont
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

#Dada una lista con nombres y un numero de presonas con ese nombre, calcula la probabilidad de cada nombre
def probLista(laLista):
  for k in laLista.keys():
    laLista[k] = float(laLista[k])/float(sumValues(laLista))
  return laLista

#Dada una lista con 1000 nombres, la reduce a los 'size' valores más altos
def reduceYear(y, size, gen):
  miLista = dameNombres(str(y))[gen]
  keysOrd = sorted(miLista, key=miLista.__getitem__, reverse=True)
  i=0
  laLista = {}
  for k in keysOrd:
    if(i>size): break
    else:
      laLista[k] = miLista[k]
      i+=1
  for k in laLista.keys():
    laLista[k] = float(laLista[k])/float(sumValues(laLista))
  return laLista

#Calcula el nombre con mas popularidad en un anio
def maxKey(lista):
  maxVal = 0
  for key in sorted(lista.keys()):
    if(lista[key] > maxVal):
      maxVal = lista[key]
      maxKey = key
  return maxKey

#Halla el numero de personas total sumando el numero de personas con cada nombre
def sumValues(lista):
  suma = 0
  for key in sorted(lista.keys()):
    suma = suma + lista[key]
  return suma
