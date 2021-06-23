import csv
import pandas as pd
import matplotlib.pyplot as plt

file = 'finanzas2020.csv'

def abrirFichero(file):
    try:
        open(file, newline="") 
    except IOError as err:
        print("No se ha encontrado el fichero. Error: ", err)
abrirFichero(file)

def comprovarColumnas(file):
    df = pd.read_csv(file, delimiter='\t')
    total_col=len(df.axes[1])
    if total_col == 12:
        print("Numero de columnas: "+str(total_col))
    else:
        print("El fichero debe de tener 12 columnas")
comprovarColumnas(file)

def comprovarContenido(file):
    df = pd.read_csv(file, delimiter='\t')
    try:
        print(df.head(5))
    except:
        print("El fichero no tiene contenido valido")
comprovarContenido(file)


def convertirDataset(file):
    csvfile = open(file, newline="")
    read_csv=csv.reader(csvfile, delimiter='\t')
    dataset=[]
    for row in read_csv:
        dataset.append(row)
    return(dataset)
    
convertirDataset(file)

dataset = convertirDataset(file)
def tratarDatos(n):
    dataset_temp = []
    for i in range(1, len(dataset)):
        datos_temp =[]
        for n in dataset[i]:
            try:
                dato = float(n)
                datos_temp.append(dato)
            except:
                dato = 0
                datos_temp.append(dato)
        dataset_temp.append(datos_temp) 
    return(dataset_temp)
    
tratarDatos(dataset)

dataset_temp = tratarDatos(dataset)

def crearDataframe(n):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    df = pd.DataFrame(dataset_temp, columns=meses)
    return(df)

crearDataframe(dataset_temp)

df = crearDataframe(dataset_temp)

def Totales(n):
    Total1 = df['Enero'].sum()
    Total2 = df['Febrero'].sum()
    Total3 = df['Marzo'].sum()
    Total4 = df['Abril'].sum()
    Total5 = df['Mayo'].sum()
    Total6 = df['Junio'].sum()
    Total7 = df['Julio'].sum()
    Total8 = df['Agosto'].sum()
    Total9 = df['Septiembre'].sum()
    Total10 = df['Octubre'].sum()
    Total11 = df['Noviembre'].sum()
    Total12 = df['Diciembre'].sum()

    totales = [Total1, Total2, Total3, Total4, Total5, Total6, Total7, Total8, Total9, Total10, Total11, Total12]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dftotales = pd.DataFrame(list(zip(meses,totales)), columns = ['Meses','Totales'])
    return(dftotales)
    
Totales(df)

dftotales = Totales(df)

def ahorroMax(n):
    max = dftotales.loc[dftotales['Totales'].idxmax()]
    print(f'El mes que más has ahorrado es: \n {max}')  
ahorroMax(dftotales)

def gastoMax(n):
    min = dftotales.loc[dftotales['Totales'].idxmin()]
    print(print(f'El mes que más has gastado es: \n {min}'))
gastoMax(dftotales)

def gastosMed(n):
    median=dftotales.iloc[[0]].median(axis=1)
    print(f'Tu media de gastos es: \n {median}')
gastosMed(dftotales)

def gastosTotales(n):
    dfgastos = dftotales['Totales']<0
    dffiltrado = dftotales[dfgastos]
    gastos = dffiltrado['Totales'].sum()
    print(f'Tus gastos totales son: {gastos}')
gastosTotales(dftotales)

def ingresosTotales(n):
    dfingresos = dftotales['Totales'].mask(dftotales['Totales'].lt(0),0)
    ingresos = dfingresos.sum()
    print(f' Tus ingresos totales son: {ingresos}')
ingresosTotales(dftotales)



def evolucionGastos(n):
    x_values = dftotales['Meses'].unique()
    y_values = dftotales['Totales'].unique()
    plt.figure(figsize=(13,6))
    plt.bar(x_values, y_values)
    plt.show()
evolucionGastos(dftotales)
