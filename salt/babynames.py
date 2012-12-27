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
      n2rM[boyname] = int(rankboy.replace(',', ''))
    if girlname not in n2rF:
      n2rF[girlname] = int(rankgirl.replace(',', ''))

  #devolvemos la lista (M - Masculino, F - Femenino)
  listNames = {}
  listNames['M'] = n2rM
  listNames['F'] = n2rF

  return listNames

def listaAula(ed1,por1,ed2,por2,tam,gen):
  now = datetime.datetime.now()
  y1 = now.year - ed1
  y2 = now.year - ed2
  milista1 = dameNombres(str(ed1))[gen]
  listY = milista1
  if (por2 > 0):
    for key in sorted(milista1.keys()):
      milista1[key] = round(float(milista1[key])*float(por1)/100)
    milista2 = dameNombres(str(ed2))[gen]
    for key in sorted(milista2.keys()):
      milista2[key] = round(float(milista2[key])*float(por2)/100)

    listY = {}
    for key in sorted(milista1.keys()):
      milista1[key] = milista1[key] + milista2.get(key, 0)
      if(milista2.get(key,0) != 0): del milista2[key]
    for key in sorted(milista2.keys()):
      listY[key] = milista2[key]

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
  """suma = sumValues(listY)
  for key in sorted(listY.keys()):
    listY[key] = 2.4*float(tam)*float(listY[key])/float(suma)
  for key in sorted(listY.keys()):
    listY[key] = round(listY[key])
  for key in sorted(listY.keys()):
    if(listY[key] < 1): del listY[key]"""
  suma = sumValues(listN)
  #keysOr = list(sorted(listY, key=listY.__getitem__, reverse=True))
  #valuesOr = []
  #for v in sorted(listY.values(), reverse=True):
    #valuesOr.append(v)

  #misKeys = keysOr[:tam]
  #misValues = valuesOr[:tam]
  #miAula = {}
  #for n in range(0,tam):
    #miAula[misKeys[n]] = misValues[n]
  return listN

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
  #mVal = 0
  #for r in listaArr:
  #  if(r > mVal):
  #    mVal = r
  #for r in range(len(listaArr)):
  #  listaArr[r] = float(listaArr[r])/float(mVal)
  return listaArr

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--nombre_archivo] file [file ...]'
    sys.exit(1)

  summary = False
  if args[0] == '--nombre_archivo':
    summary = True
    del args[0]

  for cosa in args:
      mistring = dame_nombres(cosa)
      if summary:
          outf = open(cosa + '.summary', 'w')
          outf.write(mistring + '\n')
          outf.close()

if __name__ == '__main__':
  main()
