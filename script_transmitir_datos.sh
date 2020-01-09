#!/bin/bash

#Script que transmiste los datos de la Raspberry al PC. 

#Se comprueba si existe el fichero con los datos, si es así, éste se elimina, para añadir los datos desde cero.

if [ -f "datos.txt" ]; then
    cat /dev/null > datos.txt
fi

#Se envia el fichero datos.txt por ssh al PC, se establece la conexión por ssh con la IP de la 
#Raspberry y la contraseña de usuario.

aux=true
while [ $aux ]
do
    pscp -pw milano pi@192.168.1.129:/home/pi/datos.txt datos.txt 
    sleep 5    
done


