__author__ = 'jhovanny'
import json
import urllib2
from obdc import *
import savReaderWriter


"""
se obtiene el metadato de la base de datos
"""

#file="Hogares.sav"
file="Agropecuario.sav"
pregunta, dicpreguntas, vartypes, varlabels, medicion, valuelabels= metadata("Agropecuario-ccc.mdb")


"""
obtiene los datos en formato json
se obtiene los odentificadores unicos de las encuestas
"""

j='{"uno":[1,2,3,4],"numeros":"uno"}'
h=json.loads(j)


req = urllib2.Request('http://r-visual.com/json.php')
req.add_header('User-Agent', 'Opera/9')
p = urllib2.urlopen(req)
c=p.read()
h=json.loads(c)
Identificadores=set()
for reg in h:
    Identificadores.add(reg["idproyecto"]+"-" + reg["idformulario"]+"-"+reg["idencuestador"]+"-"+reg["imei"])


"""
devuelve encuesta en formato json segun la clavesuministrada
"""
def preguntas(clave):
    pregunta={}
    encuesta={}
    pregunntaOrd={}
    for reg in h:
        if clave==reg["idproyecto"]+"-" + reg["idformulario"]+"-"+reg["idencuestador"]+"-"+reg["imei"]:
            pregunta[int(reg["idpregunta"])]=int(reg["valor"]) if reg["valor"].isdigit() else reg["valor"]
    for x in sorted(pregunta):
        pregunntaOrd[x]=pregunta[x]
    #encuesta[clave]=pregunntaOrd
    #return encuesta
    return pregunntaOrd

""""
inserta las preguntas no contestadas
"""

def encuestaPregunta(regis, pregunt):
    encuestaTotal=[]
    for p in pregunt:
        if int(p[1:]) in regis.keys():
            encuestaTotal.append(regis[int(p[1:])])
        else:
            encuestaTotal.append("")

    return encuestaTotal

encuestas={}

for x in Identificadores:
    encuestas[x]=preguntas(x)

encuestasFinal=[]
for w in encuestas:
    encuestasFinal.append(encuestaPregunta(preguntas(w),pregunta))

with savReaderWriter.SavWriter(file,pregunta,vartypes,valuelabels,varlabels,formats=None,missingValues=None,measureLevels = medicion, ioUtf8=True, ioLocale='Spanish_Spain.1252') as sav:
    sav.writerows(encuestasFinal)




















