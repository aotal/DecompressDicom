#!/usr/bin/env python
# coding: utf-8

import glob2
import os
import shutil
import numpy as np
import pydicom as dc
from tqdm import tqdm


# Funciones que nos harán falta:


def getLastDirectory(x): return os.path.basename(
    os.path.normpath(x))  # Busca los directorios en Input


def Decompress(FileInput, FileOutput):  # Descomprime el dicom en si
    Out = dc.read_file(FileInput,force=True)
   # Out.file_meta.TransferSyntaxUID = dc.uid.ImplicitVRLittleEndian  # or whatever is the correct transfer syntax for the file
    Out.decompress()
    dc.write_file(FileOutput, Out)

# Si existe el directorio Output lo elimina


if os.path.exists('./Output/'):
    shutil.rmtree('./Output/')

print('Cargando imágenes de cada uno de los subdirectorios...')
# Carga de todas las imágenes
direc = glob2.glob("./Input/**/", recursive=True)
files = []
for X in tqdm(direc):
    files.append(glob2.glob(X + "/**", recursive=True))
# Almacena los nombres de los ficheros del directorio Input (y sus subdirectorios) en una lista
files = [j for i in files for j in i]
files = [x for x in list(set(files)) if not os.path.isdir(x) and os.path.splitext(x)[1]!='.db']


# Crea los directorios correspondientes de Input en Output


for X in direc:
    if (getLastDirectory(X) != 'Input'):
        os.makedirs('./Output/' + getLastDirectory(X))


# De la lista files compone la lista de los ficheros de salida, filesOutput


filesOutput = [X.replace('./Input\\', './Output\\') for X in files]

# Escribe los ficheros descomprimidos

print('Descomprimiendo...')
for i in tqdm(range(len(files))):
    Decompress(files[i], filesOutput[i])
