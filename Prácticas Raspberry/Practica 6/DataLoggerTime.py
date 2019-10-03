#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import SDL_DS1307

# Se corrobora que el número de argumentos recibidos sea el correcto
if len(sys.argv) == 3:
	ruta = "/media/pi/ADAN/" + sys.argv[1]
	archivo = open(ruta, "w")
else:
	print("Modo de uso: ")
	print(" python DataLoggerTime.py <nombreArchivo> <númeroEntero>")
	exit()

# Se crea el objeto ds1307 a partir de la librería SDL_DS1307.py
ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
ds1307.write_now()

# Se determina el número de muestras a tomar
numero = int(sys.argv[2])

for i in range(1, numero+1):

	tiempo = ds1307.read_datetime()
	archivo.write( "Muestra {} tomada a las: {}\n".format(i, tiempo) )
	archivo.flush()
	time.sleep(1)

archivo.close()
