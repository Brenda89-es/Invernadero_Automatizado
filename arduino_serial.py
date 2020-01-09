#!/usr/bin/env python 

#Script escrito en lenguaje Python que conecta el Arduino con la Raspberry. 

import serial
import time
import os #La incluímos para utilizar la funcionalidad dependiente del sistema operativo.

f = open ("datos.txt", "w") #Creamos el fichero
f.close() #Eliminamos el fichero

#Conexión con el puerto al que está conectado el Arduino,
#si no lo sabemos hemos de comprobarlo en /dev/tty. 
#Asimismo, establecemos la tasa de transferencia en 9600 baudios.

arduino = serial.Serial ("/dev/ttyACM0", 9600) 

# De forma preventiva, apagamos el Arduino un segundo y lo volvemos a iniciar de manera que limpiemos el
# "ruido" que pudiera transmitirse por el puerto serial. 
arduino.setDTR(False) #Lo apagamos.
time.sleep(1)
arduino.flushInput() #Establecemos su entrada.
arduino.setDTR(True) #Lo encendemos.

try:
        auxiliar = True
		
        while auxiliar == True: 

            f = open ("datos.txt", "a") #a de append, se añaden datos a los que ya hay de forma continua.  
            
            datos = arduino.readline() #Lectura del Arduino con el método read.line()
            
            f.write(datos)
            
            f.close
            
            time.sleep(1)

except KeyboardInterrupt: 
    
    auxiliar = False #Si tecleamos CTRL-C auxiliar se convierte en falso, y el dejamos de recibir datos.
    
    print("\n\n")
