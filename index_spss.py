#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#sys.setdefaultencoding("utf-8")
#reload(sys)
import savReaderWriter
import locale
import os
import collections


archivo='B:\pdfSag\sav\servicios.sav'
savFileName = 'someFile.sav'
locale.setlocale(locale.LC_ALL, 'Spanish_Spain.1252')
def escrituraspss():
    savFileName = 'someFile.sav'
    records = [[b'Test1', 1, 1], [b'Test2', 2, 1]]
    varNames = ['var1', 'v2', 'v3']
    varTypes = {'var1': 5, 'v2': 0, 'v3': 0}

    with savReaderWriter.SavWriter(savFileName, varNames, varTypes,ioLocale='Spanish_Spain.1252') as writer:
        for record in records:
            writer.writerow(record)



def leerSPSS():
    with savReaderWriter.SavReader(archivo, ioLocale='Spanish_Spain.1252') as reader:
        for line in reader:
            codigo=str(line[2]).strip()+str(line[4]).strip()+str(line[3]).strip()
            for firma in os.listdir(os.path.join('c:\\','dropbox', 'sag', 'dvd', 'firmapruebas')):
                formulario=firma.replace('.','_').split('_')
                formulariobus=formulario[0]+formulario[1]+formulario[3]
                if codigo==formulariobus:
                    rutanueva= str(line[2]).strip()+"_"+ str(line[4]).strip()+"_"+str(int(line[5])).strip()+"_"+str(line[3]).strip()+".png"
                    os.rename(os.path.join('c:\\','dropbox', 'sag', 'dvd', 'firmapruebas16',firma),os.path.join('c:\\','dropbox', 'sag', 'dvd', 'firmapruebas16', rutanueva) )






with savReaderWriter.SavReader(archivo, ioLocale='Spanish_Spain.1252') as reader:
    for linea in reader:
        if linea[6]==5001:
            print linea



def frimasarchivo():
    listafor=[]
    for firma in os.listdir(os.path.join('c:\\','dropbox', 'sag', 'dvd', 'firmapruebas')):
        formulario=firma.replace('.','_').split('_')
        formulariobus=formulario[0]+formulario[1]+formulario[3]
        listafor.append(formulariobus)
    return listafor

def leervaloresVariables():
    with savReaderWriter.SavHeaderReader(archivo,ioLocale='Spanish_Spain.1252') as header:
        return header.valueLabels.items()

def leercabezotes():
    with savReaderWriter.SavHeaderReader(archivo,ioLocale='Spanish_Spain.1252') as header:
        return header.varNames

def leerSPSSPrueba():
    data=[]
    with savReaderWriter.SavReader(archivo,returnHeader=True, ioLocale='Spanish_Spain.1252') as reader:
        for linea in reader:
            data.append(linea)
        return data

def leerrotulos():
    with savReaderWriter.SavHeaderReader(archivo,ioLocale='Spanish_Spain.1252') as header:
        return header.varLabels


def leervaloresVariables():
    h=savReaderWriter.SavHeaderReader(archivo,ioUtf8=True,ioLocale='Spanish_Spain.1252')
    return h.valueLabels



nombrevaribales=leercabezotes()
nvariables=len(nombrevaribales)
valores=leerSPSSPrueba()
labels=leerrotulos()
valoreslabel=leervaloresVariables()

for g,k in valoreslabel.items():
    print g,k

lista=[]
for x in valores:
    lista.append(collections.OrderedDict([(nombrevaribales[n],x[n]) for n in range(nvariables)]))













