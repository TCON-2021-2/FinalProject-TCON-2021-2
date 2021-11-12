# PROYECTO FINAL TCON
* GITHUB https://github.com/TCON-2021-2/FinalProject-TCON-2021-2

* DOCENTE VENUSTIANO SOANCATL AGUILAR

## Autor
* Ricardo Amaya Rivera
* Juan Pablo Contreras Amaya

## Contrucción
* Ubuntu 20.04 LTS
* Docker

## Prerequisites
* WSL2

## Instrucciones

1. En la consola que utilizemos en nuestro caso la consola de uuntu, clonamos el repositorio y dentro de la carpeta ejecutamos el servicio con sudo y hacemos el docker compose del docker -HWC.yml 

2.Dentro de este musmo y luego de instalar Phyton en nuestro sistema operativo procedemos a ejecutar el archivo python con el nombre sendMessageToLogstash.py 

3.Podemos ingresar a elastic y ver como se esta ejecutando la aplicacion, ingesando en el localhost en el puerto 5601 

4.Ahora vamos a crear el index pattern que en nuestro caso se llamó ryjd 

5.A continuación un vistazo a la asrquitectura Hot, Warm, Cold

-Hot:


![](https://github.com/TCON-2021-2/FinalProject-TCON-2021-2/blob/main/img/hot.PNG)
 
 -Warm:
 
![](https://github.com/TCON-2021-2/FinalProject-TCON-2021-2/blob/main/img/warm.PNG)
 
 -Cold:
 
![](https://github.com/TCON-2021-2/FinalProject-TCON-2021-2/blob/main/img/cold.PNG)


-Se incluyeron politicas para realizar un respaldo.

![](https://github.com/TCON-2021-2/FinalProject-TCON-2021-2/blob/main/img/snapshots.PNG)

-Tambien se incluyo una fase de borrado.

![](https://github.com/TCON-2021-2/FinalProject-TCON-2021-2/blob/main/img/Delete.PNG)

