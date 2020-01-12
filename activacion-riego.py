#!/usr/bin/env python3

#Programa que mide la humedad del suelo y activa o desactiva el riego en función de la misma.

#Librerías.
from gpiozero import DigitalInputDevice
import RPi.GPIO as GPIO
import time

#Métodos
GPIO.setmode(GPIO.BCM) #Nos referimos a los pines por su número de Broadcomm SOC Channel.
GPIO.setwarnings(False) #Método para ocultar avisos.

#Relé conectado al GPIO27.
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.HIGH)

#Higrómetro conectado al GPIO17.
d0_input = DigitalInputDevice(17) 

#Función principal.
while True:
    
    if (not d0_input.value):
        GPIO.output(27, GPIO.LOW) #Relé apagado, se desactiva el riego.
        print("Riego desactivado")
        time.sleep(2)
    else:
        GPIO.output(27, GPIO.HIGH) #Relé encendido, se activa el riego.
        print("Riego activado")
        time.sleep(2)

