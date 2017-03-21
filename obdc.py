__author__ = 'jhovanny'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#sys.setdefaultencoding("utf-8")
#reload(sys)
import pyodbc
import os
import itertools


""""
toma una base de datos en acces y la transforma en sintaxis para crear bd en spss, metadata es la funciona que toa como argumento la bd

"""

def mostrarTablas(mdbfile):
    conn_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ os.getcwd() + "\\%s" %mdbfile
    cnx= pyodbc.connect(conn_string,autocommit=True)

    try:

        cursor=cnx.cursor()
        for x in cursor.tables():
            print x.table_name
    finally:
        cnx.close()

def mostrarTablas1(mdbfile):
    conn_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ os.getcwd() + "\\%s" %mdbfile
    cnx= pyodbc.connect(conn_string,autocommit=True)

    try:

        cursor=cnx.cursor()
        for x in cursor.columns("Tabla de preguntas"):
            print x.column_name
    finally:
        cnx.close()



def safeunicode(obj, encoding='utf-8'):
    r"""
    Converts any given object to unicode string.

        >>> safeunicode('hello')
        u'hello'
        >>> safeunicode(2)
        u'2'
        >>> safeunicode('\xe1\x88\xb4')
        u'\u1234'
    """
    t = type(obj)
    if t is unicode:
        return obj
    elif t is str:
        return obj.decode(encoding)
    elif t in [int, float, bool]:
        return unicode(obj)
    elif hasattr(obj, '__unicode__') or isinstance(obj, unicode):
        return unicode(obj)
    else:
        return str(obj).decode(encoding)


def safestr(obj, encoding='utf-8'):
    r"""
    Converts any given object to utf-8 encoded string.

        >>> safestr('hello')
        'hello'
        >>> safestr(u'\u1234')
        '\xe1\x88\xb4'
        >>> safestr(2)
        '2'
    """
    if isinstance(obj, unicode):
        return obj.encode(encoding)
    elif isinstance(obj, str):
        return obj
    elif hasattr(obj, 'next'): # iterator
        return itertools.imap(safestr, obj)
    else:
        return str(obj)




def esEscala(mdbfile, pregunta):
    conn_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ os.getcwd() + "\\%s" %mdbfile
    cnx= pyodbc.connect(conn_string,autocommit=True)
    val=None
    try:
        cursor=cnx.cursor()
        registros=cursor.execute("select * from [valores] where idp=%d" % pregunta ).fetchone()
        if registros:
            val=True
            return val
    finally:
        cnx.close()
        return val


def valores(mdbfile, pregunta):
    conn_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ os.getcwd() + "\\%s" %mdbfile
    cnx= pyodbc.connect(conn_string,autocommit=True)
    val={}
    try:
        cursor=cnx.cursor()
        registros=cursor.execute("select * from [valores] where idp=%d" % pregunta ).fetchall()
        for registro in registros:
            val[registro[1]]=registro[2]
    finally:
        cnx.close()
        return val



def metadata(mdbfile):
    conn_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="+ os.getcwd() + "\\%s" %mdbfile
    cnx= pyodbc.connect(conn_string,autocommit=True)
    preguntas=[]
    dicPreguntas={}
    vartypes={}
    varlabels={}
    measureLevels={}
    valueLabels={}

    try:
        cursor=cnx.cursor()
        registros=cursor.execute("select * from [Tabla de preguntas] order by [Numero item] asc" ).fetchall()
        for x in registros:

            preguntas.append("p%d" % x[0])
            dicPreguntas["p%d" % x[0]]=x[1]
            tipo=0 if x[4]==1 else x[5]
            if esEscala(mdbfile, x[0]) and tipo==0:
                measureLevels["p%d" % x[0]]="nominal"
                valueLabels["p%d" % x[0]]=valores(mdbfile,x[0])
            elif tipo>0:
                measureLevels["p%d" % x[0]]="nominal"
            else:
                measureLevels["p%d" % x[0]]="scale"
            vartypes["p%d" % x[0]]=tipo
            varlabels["p%d" % x[0]]=x[1]

    finally:
        cnx.close()
        return preguntas, dicPreguntas, vartypes, varlabels, measureLevels, valueLabels
