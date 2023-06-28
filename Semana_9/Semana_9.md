## Solución Microdesafío - Semana 9

1. Descomprimir la carpeta en `Semana_9`
2. Abrir la terminal 
3. Ir a la carpeta raiz: `cd Semana_9/web-page`
4. Verificar el contenido de la carpeta con: `ls`
5. Creamos la imagen con:
```
docker build -t img-web-estatica .
```
6. Verifica las imagenes disponibles con: `docker ps -a`
7. Analiza las imagenes: `docker images`
8. Ejecuta tu imagen con:
```
docker run -it -d -p 1080:80 img-web-estatica
```
9. Lanza tu servicio en una página web con la dirección: `http://localhost:1080`
<!-- en mi caso: http://192.168.1.100:1080 -->
10. Deberás visualizar tu página web

