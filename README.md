# Invernadero_Automatizado
Invernadero_Automatizado con Raspberry Pi 3 B, como ejemplo de su uso como ordenador de placa reducida. 

En este repositorio se incluye todo el código necesario por el que se automatiza un invernadero con Raspberry Pi 3 Modelo B y se trasmiten los datos obtenidos de la misma al PC. A la Raspberry se le conecta por puerto serial un Arduino UNO R3 que le comunica valores detectados mediante sensores analógicos de temperatura, humedad, presión, luminosidad e higrometría.

Pasos en la ejecución del código( dar permisos con chmod):
  1) Activación/desactivación del riego: ./riego(higro-rele).py (Terminal, Raspberry)
  
  2) Transmisión y graficado de los datos:
  
      2.1) datos_analogicos.ino (Escrito con Arduino IDE, ejecutar en  Arduino UNO R3)
      
      2.2) ./arduino_serial.py (Ejecutar en Raspberry Pi 3B). Obtención de los datos medidos por el Arduino y comunicados vía serial a Raspberry.
      
      2.3) "datos.txt". Fichero de texto plano que creamos en la Raspberry y en donde se van a almacenar los datos medidos por los sensores conectados a Arduino. 
      
      2.4)./script_transmitir_datos.sh (Ejercutar en el terminal en el PC), lo ejecutamos en nuestro ordenador personal, cambiar la direcció IP y la contraseña, con éste script extraemos los datos por ssh. 
      
      2.5) ./script_graficar.sh (Ejecutar en el terminal en el  PC), lo llamos desde la terminal, es necesario tener instalado GNUPLOT (o cambiar en el script por otro para graficar). 

Además, se incluye la grabación del funcionamiento del invernadero y del código encargado de transmitir los datos. Datos que se almacenan y grafican en tiempo real. Los vídeos no se pueden ver desde la plataforma Github pero se pueden descargar.

Finalmente, se incluye un documento pdf en el que se explica todo el proyecto. 
