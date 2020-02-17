# Utilidad para descomprimir ficheros dicom

## Instalación

- En caso de no tener anaconda instalado, descargamos miniconda de [este](https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Windows-x86_64.exe) en el caso de una versión de Windows de 64 bits o en [este](https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Windows-x86.exe) enlace si nuestra versión es de 32 bits, pasando a instalarlo posteriormente. En caso de tener Anaconda, debemos asegurarnos de que la versión de Python es la 3.6 En caso contrario, creamos un entorno con esa versión de python.
- Posteriormente,[descargamos](https://github.com/aotal/DecompressDicom/archive/master.zip) el fichero zip y lo descomprimimos en nuestro ordenador, o bien clonamos el proyecto mediante la instrucción:

  ```
  $ git clone https://github.com/aotal/DecompressDicom.git

  ```

- Creamos una carpeta en nuestro disco y descargamos en ella el contenizo del zip descomprimido.
- Abrimos un terminal de anaconda y navegamos hasta la carpeta creada
  ```
  cd /ruta/carpeta/creada
  ```
- Para instalar las librerías en el entorno _base_, ejecutamos el siguiente comando
  ```
  conda env update --file environment.yml
  ```
- En caso de querer ejecutarlo en otro entorno, lo creamos mediante la instrucción:

  ```
  conda create --name elnombrequequeramos python=3.6
  ```
  y una vez terminado nos saldrá un mensaje con las instrucciones para activar el entorno. Lo activamos y ejecutamos la instrucción del punto previo.

## Instrucciones de uso

- Creamos la carpeta dentro de la carpeta  _/ruta/carpeta/creada_
  ```
  mkdir Input
  ```

- Copiamos los ficheros dicom comprimidos dentro de las carpetas  tal y como queremos que salgan ordenados, ya que el programa respeta la estructura de ficheros.

- Una vez hecho eso, ejecutamos la instrucción:

  ```
  python Decom.py
  ```

Nos apareceran los ficheros descomprimidos una vez terminado el proceso en una carpeta _Output_. Esa carpeta se borrara cada vez que se reinicie el proceso.
