#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if len(sys.argv) == 3:
	ruta = "/media/pi/ADAN/" + sys.argv[1]
	archivo = open(ruta, "w")
else:
	print("Modo de uso:")
	print("  python DataLogger.py <nombreArchivo> <númeroEntero>")
	exit()

numero = int(sys.argv[2])

for i in range(0, numero+1):
	archivo.write( "{},Hola USB,data {}\n".format(i, i) )
	archivo.flush()

archivo.close()

