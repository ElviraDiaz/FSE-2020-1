import serial

puerto = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

for i in range(0, 16):
	puerto.write("\n{}: FSE 2020-1 Comunicacion UART RPi - FSE".format(i))

