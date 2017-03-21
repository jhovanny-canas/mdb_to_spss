__author__ = 'jhovanny'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#sys.setdefaultencoding("utf-8")
#reload(sys)
import savReaderWriter
import locale
import os
import collections
from obdc import *

varLabels = {'var1': 'This is variable 1',
                 'v2': 'This is v2!',
                 'bdate': 'dob'}

file="Agropecuario.sav"
#file="Hogares.sav"

preguntas, dicpreguntas, vartypes, varlabels, medicion, valuelabels= metadata("Agropecuario-ccc.mdb")

with savReaderWriter.SavWriter(file,preguntas,vartypes,valuelabels,varlabels,formats=None,missingValues=None,measureLevels = medicion,  ioLocale='Spanish_Spain.1252') as sav:
    pass

