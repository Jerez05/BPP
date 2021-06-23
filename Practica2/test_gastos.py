import pytest
import pandas as pd
import csv
import gastos


def test_abrirFichero():
    file = 'meses.csv'
    open(file, newline="") 
    resultado = "El fichero se ha abierto sin problemas"
    assert resultado == gastos.abrirFichero(file)

def test_comprobarColumnas():
    file = 'meses.csv'
    df = pd.read_csv(file, delimiter="\t")
    resultado = 12
    assert resultado == gastos.comprobarColumnas(file)

def test_comprobarContenido():
    file = 'años.csv'
    df = pd.read_csv("finanzas2020.csv", delimiter="\t")
    resultado = 223
    assert resultado == gastos.comprbarContenido(file)

def test_convertirDataset():
    file = 'años.csv'
    csvfile = open(file, newline="")
    read_csv=csv.reader(csvfile, delimiter='\t')
    dataset1=[]
    for row in read_csv:
        dataset1.append(row)
    r_aux = gastos.convertirDataset(file)
    resultado = '223'
    assert resultado == r_aux[1]
    return dataset1

dataset1 = test_convertirDataset()

def test_tratarDatos():
    dataset_temp1 = []
    for i in range(1, len(dataset1)):
        datos_temp =[]
        for n in dataset1[i]:
            try:
                dato = float(n)
                datos_temp.append(dato)
            except:
                dato = 0
                datos_temp.append(dato)
        dataset_temp1.append(datos_temp) 
    r_aux_temp = gastos.tratarDatos(dataset1)
    resultado = -491.0
    assert resultado == r_aux_temp[1]
    return dataset_temp1

dataset_temp1 = test_tratarDatos()

def test_crearDataframe():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    df1 = pd.DataFrame(dataset_temp1, columns=meses)
    r_aux_df = gastos.crearDataframe(dataset_temp1)
    resultado = 223.0
    assert resultado == r_aux_df[1]
    return df1

df1 = test_crearDataframe()


def test_Totales():
    Total1 = df1['Enero'].sum()
    Total2 = df1['Febrero'].sum()
    Total3 = df1['Marzo'].sum()
    Total4 = df1['Abril'].sum()
    Total5 = df1['Mayo'].sum()
    Total6 = df1['Junio'].sum()
    Total7 = df1['Julio'].sum()
    Total8 = df1['Agosto'].sum()
    Total9 = df1['Septiembre'].sum()
    Total10 = df1['Octubre'].sum()
    Total11 = df1['Noviembre'].sum()
    Total12 = df1['Diciembre'].sum()
    totales = [Total1, Total2, Total3, Total4, Total5, Total6, Total7, Total8, Total9, Total10, Total11, Total12]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dftotales = pd.DataFrame(list(zip(meses,totales)), columns = ['Meses','Totales'])
    r_aux_dftot = gastos.Totales(df1)
    resultado = 12064.0
    assert resultado == r_aux_dftot[1]
    return dftotales

dftotales1 = test_Totales()

def test_ahorroMax():
    max = dftotales1.loc[dftotales1['Totales'].idxmax()]  
    max = max.iloc[1]
    resultado = 12064.0
    assert resultado == gastos.ahorroMax(dftotales1)

def test_gastoMax():
    min = dftotales1.loc[dftotales1['Totales'].idxmin()]
    min = min.iloc[1]
    resultado = -18933.0
    assert resultado == gastos.gastoMax(dftotales1)

def test_gastosMed():
    median = dftotales1['Totales'].astype(float)
    median = dftotales1['Totales'].median(axis=0)
    resultado = -719.0
    assert resultado == gastos.gastosMed(dftotales1)

def test_gastosTotales():
    dfgastos = dftotales1['Totales']<0
    dffiltrado = dftotales1[dfgastos]
    gastos = dffiltrado['Totales'].sum()
    resultado = -51106
    assert resultado == gastos.gastosTotales(dftotales1)

def test_ingresosTotales():
    dfingresos = dftotales1['Totales'].mask(dftotales1['Totales'].lt(0),0)
    ingresos = dfingresos.sum()
    resultado = 35276.0
    assert resultado == gastos.ingresosTotales(dftotales1)