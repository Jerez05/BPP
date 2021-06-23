import pandas as pd

class comprobarFichero:
    '''
    Tratamientos de los datos.
    Atributos
    ----------------------------------------------------------------
    file: 
        Este es el nombre del fichero (CSV) que queremos tratar. 
    
    Metodos
    ----------------------------------------------------------------

        Comprovar que el fichero existe, tiene el formato correcto y contiene datos
    
            Abrir fichero:

                Intenta abrir el fichero.
                Si lo puede abrir muestra el mensaje "El fichero se ha abierto sin problemas".
                En caso contratio mmuestra el mensaje "No se ha encontrado el fichero. Error: (tipo de error)".

            Comprobar columnas:

                Transforma el fiechro CSV en un dataframe y obtiene el numero de columnas.
                Si el numero de columnas es igual a 12 muestra el mensaje "Numero de columnas: 12".
                Si el numero de columnas no es igual a 12 muestra el mensaje "El fichero debe de tener 12 columnas".

            Comprobar contenido:

               Transforma el fiechro CSV en un dataframe e intenta printar la primea fila.
               Si lo realiza muestra la primera fila de cada columna del dataframe.
               Si no lo realiza muestra el mensaje "El fichero no tiene contenido valido"

    Ejemplo
    -----------------------------------------------------------------
    >>> import gastos
    >>> g = gastosTratamientoDatos('filename')
    >>> res_abrirfichero = g.abrirFichero()
    >>> res_comprobarcolumnas = g.comprobarColumnas()
    '''
    def __init__(self, file):
        self.file = file
    
    def abrirFichero(self):
        '''
        Metodo abrir fichero. Compreuba que el fichero existe.
        Inputs
        ------
            self.file
        Outputs
        -------
            res_OK: muesta el mensaje "El fichero se ha abierto sin problemas"
            res_NOK: muesta el mensaje "No se ha encontrado el fichero. Error: (error)"
        '''
        res = open(self.file) if (self.file == True) else print("No se ha encontrado el fichero.")
        return res

    def comprobarColumnas(self):
        '''
        Metodo comrpbar columnas. Comprueba el numero de columnas
        Inputs
        ------
            self.file
        Outputs
        -------
            res_OK: muestra el mensaje "Numero de columnas: (nº)"
            res_NOK: "El fichero debe de tener 12 columnas"
        '''
        res = print(len(self.file)) if (len(self.file) == 12) else print("El fichero debe de tener 12 columnas")
        return res
    
    def comprobarContnido(self):
        '''Metodo comrpbar contenido. Comprueba si el fichero tiene contenido.
        Inputs
        ------
            self.file
        Outputs
        -------
            res_OK: mustra la segunda lista del dataframe
            res_NOK: "El fichero no tiene contenido valido"
        '''
        df = pd.read_csv(self.file, delimiter='\t')
        try:
            print(df.iloc[1, :])
        except ValueError:
            print("El fichero no tiene contenido valido")
        
        res= print(df.iloc[1, :]) if (df.loc[1, :] == True) else print("El fichero no tiene contenido valido")
        return res