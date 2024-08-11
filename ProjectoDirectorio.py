import zipfile
import os
import re
import time
import shutil
import datetime
from pathlib import Path
import math


''' 
Descomentar solo cuando no se haya descomprimido el archivo
mi_zip = zipfile.ZipFile('Proyecto+Dia+9.zip', 'r');
mi_zip.extractall();
instrucciones = open('Instrucciones.txt', 'r');
print(instrucciones.read())
'''
inicio = time.time()
ruta = '/home/diego/Documentos/pythonProject/Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today();
nros_encontrados = [];
archivos_encontrados = [];

def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r');
    texto = este_archivo.read();
    if re.search(patron, texto):
        return re.search(patron, texto);
    else:
        return '';

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0;
    print('-'*30)
    print(f'Fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-----\t\t\t------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1;
    print('\n');
    print(f'Número encontrados: {len(nros_encontrados)}')
    fin = time.time()

    duracion = fin - inicio;
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')

crear_listas()
mostrar_todo()


