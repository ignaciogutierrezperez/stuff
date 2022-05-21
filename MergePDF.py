# Script to merge pdf files

from PyPDF2 import PdfFileMerger
import os
import time

start = int(round(time.time() * 1000))

path = os.getcwd() + '\PDF\\'
extension = 'pdf'
listPdfs = os.listdir(path)

listPdfs = list(filter(lambda x: extension in x, listPdfs))
list = sorted(listPdfs)

merger = PdfFileMerger()

for file in list:
    merger.append(path + file)

merger.write("outputs.pdf")
merger.close()

end = int(round(time.time() * 1000))
duration = (end - start)/1000

# Salida de resultados por pantalla
# Imprime en pantalla los ficheros del directorio
print("Original Files: ", listPdfs)
print("Merged file: outputs.pdf")
print("Progress duration: ", duration, " seconds")

input()
