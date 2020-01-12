#! /usr/bin/gnuplot

#Script encargado de graficar los datos incluidos en el documento de texto plano datos.txt recibidos de la raspberry al PC.

set multiplot layout 2,3 #Distribución de los gráficos, dos filas por tres columnas.
set grid #Mallado. 

unset key 
set time top #Colocación del tiempo.

# Gráfico 1: Temperatura. 
set title "Temperatura vs medidas"
set xlabel "Nº medidas"
set ylabel "T  [C]"
set yrange [0:50]
plot "datos.txt" using 1:2 with impulses lw 4 lt rgb "red"

# Gráfico 2: Humedad ambiental.
set title "Humedad Ambietal vs medidas"
set xlabel "Nº medidas"
set ylabel "H  [%]"
set yrange [0:100]
plot "datos.txt" using 1:3 with impulses lw 4 lt rgb "blue"

# Gráfico 3: Presión.
set title "Presión atmosférica"
set xlabel "Nº medidas"
set ylabel "Atm"
set yrange [0.90:1.15]
plot "datos.txt" using 1:4 with impulses lw 4 lt rgb "purple"

# Gráfico 4: Higrometría.
set title "Humedad suelo"
set xlabel "Nº medidas"
set ylabel "H [%]"
set yrange [0:105]
plot "datos.txt" using 1:5 with impulses lw 4 lt rgb "green"

# Gráfico 5: Luminosidad.
set title "Luminosidad"
set xlabel "Nº medidas"
set ylabel "L [%]"
set yrange [0:100]
plot "datos.txt" using 1:6 with impulses lw 4 lt rgb "orange"

unset multiplot

# Pausa de 7 segundos  para que el archivo acumule más datos para graficar.
pause 7

# releer el archivo con 7 segundos de datos.
reread

    
