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

	lecturaADC  = float( tramaSeparada[0] )
	tempKelvin  = float( tramaSeparada[1] )
	tempCelsius = float( tramaSeparada[2] )

	puerto.write("Valor ADC:   {} \n".format(lecturaADC))
	puerto.write("Temperatura: {}°K  {}°C \n".format(tempKelvin, tempCelsius))
	puerto.write("\n")

