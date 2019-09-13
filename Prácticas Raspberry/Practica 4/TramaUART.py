# -*- coding: utf-8 -*-
import serial  #Se importa la librería para comunicación serial

#Se crea un handler para la comunicación serial
puerto = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=360.0)

while True:

	caracterEntrada = puerto.read(1) #Se lee el primer caracter de la trama
	tramaEntrada = ""                #Variable que almacena la trama completa

	while( caracterEntrada != '\n' ):  #Se lee la trama hasta el salto de línea
		tramaEntrada += caracterEntrada
		caracterEntrada = puerto.read(1)

	#Con la cadena leída completamente, se separan los campos
	tramaSeparada = tramaEntrada.split(",")

	entero = int(tramaSeparada[0])
	iniciales = tramaSeparada[1]
	bandera = int(tramaSeparada[2])
	voltaje = float(tramaSeparada[3])

	#Constraints
	if( entero < 0 or entero > 4095 ):
		print("Entero no valido")
	elif( bandera != 0 and bandera != 1 ):
		print("Bandera no valida")
	elif( voltaje < 0.0 or voltaje > 3.3 ):
		print("Voltaje fuera de rango")
	else:  #Todo OK
		print("\nNúmero entero: {}".format(entero))
		print("Iniciales: {}".format(iniciales))
		print("Bandera: {}".format(bandera))
		print("Voltaje: {}".format(voltaje))

