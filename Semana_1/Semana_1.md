# Semana 1

### ¿Cómo ejecutar Docker?

Primero crear y ejecutar la imagen de docker
```bash
sudo docker-compose up --build
```

Buscar la IP interna de la base de datos Postgres
```bash
# Windows
docker inspect pgadmin4 -f “{{json .NetworkSettings.Networks }}”
docker inspect postgres_db -f “{{json .NetworkSettings.Networks }}”

# Linux
docker inspect pgadmin4 | grep IPAddress
docker inspect postgres_db | grep IPAddress
```

En mi caso el output fue:
```bash
# Linux
# pgadmin4 --> 172.19.0.2
# postgres_db --> 172.19.0.3
```

Ingresar en la página de [PG Admin 4](http://127.0.0.1:10003/), con el user: **admin@admin.com** y contraseña: **admin**.
Luego click en **Agregar un Nuevo Servidor**

Por cualquier problema reiniciar el servicio de Docker y parar los containers:
```bash
sudo systemctl restart docker.socket docker.service
docker container ls
docker rm -f <container id>
```

### Links:
- [Jupyter - Pyspark](http://127.0.0.1:8888/)
- [PG Admin 4](http://127.0.0.1:10003/)

### Ejercicios Python:
1. Escribir un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
2. Escribir un programa que pida al usuario cuántos números quiere introducir. Luego que lea todos los números y realice una media aritmética.
3. Utilizando la función range() y la conversión a listas generar las siguientes listas dinámicamente:
    - Todos los números del 0 al 10 [0, 1, 2, ..., 10]
    - Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
    - Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
    - Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
    - Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
4. Dadas dos listas (las que se quiera crear), generar una tercera con los elementos que estén presentes en AMBAS listas. Retornar esta nueva lista pero sin elementos duplicados.
5. Escribir un programa que sume todos los números enteros impares desde el 0 hasta el 100.
6. Contar cuantas veces aparece un elemento en una lista

### Ejercicio SQL