# Semana 2
Ejemplo en vivo de la clase de la semana 2.

1. Abrir el docker de la semana 1 o algún otro entorno de pruebas de preferencia.

2. Ejecutar el contenedor de postgres db:
```bash
# Windows
cd C:\\{...relative_path}\dateng_coder\Semana_1
docker-compose up --build postgres_db
docker-compose up postgres_db

# Linux
cd {...relative_path}/dateng_coder/Semana_1
sudo docker-compose up postgres_db
```

3. Abrir dbeaver y crear una conexión a la base de datos postgres_db. (Con la IP necesaria de la base de datos)

4. Abrir el script **script_1_tables_migration.sql** y ejecutarlo en la base de datos postgres_db.
    * Contiene el Momento 1 (creacion de tablas)
    * Y el Momento 2 (Insercion de registros - analogo - OLTP)

5. Abrir el script **script_2_olap_query** y ejecutarlo en la base de datos postgres_db.
    * Contiene el Momento 3 (Generacion de consulta analoga a OLAP)