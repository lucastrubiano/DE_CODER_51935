# Semana 2
Ejemplo en vivo de la clase de la semana 2.

1. Abrir el docker de la semana 1 o algún otro entorno de pruebas de preferencia.

2. Ejecutar la imagen de postgres db:
```bash
# Windows
docker-compose up postgres_db

# Linux
sudo docker-compose up postgres_db
```

3. Abrir dbeaver y crear una conexión a la base de datos postgres_db. (Con la IP necesaria de la base de datos)

4. Abrir el script Ejemplo_en_vivo.sql y ejecutarlo en la base de datos postgres_db.