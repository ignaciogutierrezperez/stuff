# Script para unir varios ficheros pdf en uno solo

# Carga las librerias
# PyPDF2 permite la manipulacion de ficheros pdf
from PyPDF2 import PdfFileMerger, PdfFileReader
# os permite trabajar con directorios, ficheros...
import os
# time sirve para calcular el momento actual
import time

# Momento en milisegundos en el que se inicia el script
start = int(round(time.time() * 1000))

# Establece la ruta donde se encuentran los documentos pdf a mezclar
path = os.getcwd() + '\PDF\\'
# Genera una lista con los ficheros pdf de la carpeta
listaPdfs = os.listdir(path)

# Filtra los ficheros que ha encontrado en la carpeta y se queda solo con los pdf
# Buscamos quedarnos solo con los ficheros pdf 
extension = 'pdf'
  
# Utiliza la funcion lambda para filtrar la lista de ficheros en la carpeta
# para quedarse solo con los archivos pdf  
listaPdfs = list(filter(lambda x: extension in x, listaPdfs)) 

# Ordena la lista 
lista = sorted(listaPdfs)

# Inicializa la funcion que permite mezclar los ficheros
merger = PdfFileMerger()

# Recorre la lista con los ficheros pdf de la carpeta de entrada y los une
for file in lista:
    merger.append(path + file)
    
# Crea el fichero de salida
merger.write("outputs.pdf")

# Cierra los ficheros y libera espacio en memoria
merger.close()

# Momento en milisegundos en el que finaliza el script
end = int(round(time.time() * 1000))
# Duracion en segundos
duration = (end - start)/1000

# Salida de resultados por pantalla
# Imprime en pantalla los ficheros del directorio
print("Union de varos ficheros pdf en uno solo")
print("Ficheros de entrada: ", listaPdfs)
print("Fichero de salida: outputs.pdf")
print("Duracion del proceso: ", duration, " segundos")

# Fin del script
input()

    
