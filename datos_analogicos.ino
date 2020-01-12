/*Programa que toma valores analogicos de temperatura, humedad, presion, luminosidad, humedad del suelo*/

//Librerias necesarias para el sensor BME/BME280.
# include <Wire.h>
# include <Adafruit_Sensor.h>
# include <Adafruit_BME280.h>


//Declaracion de variables necesarias y su pin analogico correspondiente.
# define BME_SDA A4
# define BME_SCL A5
# define SEALEVELPRESSURE_HPA (1013.25) //Valor de la presion.

Adafruit_BME280 bme;

int contador;
int humedad = A3;
int luminosidad = A2;
int valor_luminosidad;

void setup() 
{
    Serial.begin(9600);  
    bme.begin(0x76);   //Jumper,valor hexadecimal que establecemos.
    contador = 1; //Contador desde el valor 1, no desde 0. 
    delay(2000);  
}

void loop() 
{
    //Declaracion de variables. 
    float Temperatura, Humedad, Presion;
    
    //Lectura
    Temperatura = bme.readTemperature();
    Humedad = bme.readHumidity();
    Presion = bme.readPressure();   
    humedad = map(analogRead(A3),1023, 0, 0, 100); //Mapeo de la variable para que los valores vayan de 0 a 100.
    valor_luminosidad = map(analogRead(A2), 1023, 0 , 0, 100); //Mapeo de la variable, valores de 0 a 100.

    //Salidad
    Serial.print(contador); Serial.print("\t"); 
    Serial.print(Temperatura); Serial.print("\t"); 
    Serial.print(Humedad); Serial.print("\t");
    Serial.print(Presion/100/1013); Serial.print("\t");
    Serial.print(humedad); Serial.print("\t");
    Serial.println(valor_luminosidad);

    delay(1000);

    contador++;
}
