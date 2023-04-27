-- Crear un nuevo esquema llamado "coder" si es que no existe
CREATE SCHEMA IF NOT EXISTS coder;

-- Crear la tabla "courses" dentro del esquema "coder" si es que no existe
CREATE TABLE IF NOT EXISTS coder.courses (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Crear la tabla "reports_status" dentro del esquema "coder" si es que no existe
CREATE TABLE IF NOT EXISTS coder.reports_status (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Crear la tabla "reports" dentro del esquema "coder" si es que no existe
CREATE TABLE IF NOT EXISTS coder.reports (
    id SERIAL PRIMARY KEY,
    course_id INT NOT NULL,
    status_id INT NOT NULL,
    total_students INT NOT NULL,
    active_students INT NOT NULL,
    execution_time INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES coder.courses(id),
    FOREIGN KEY (status_id) REFERENCES coder.reports_status(id)
);

-- Insertar los valores de la tabla "courses" si es que no existen
INSERT INTO coder.courses (name)
SELECT *
FROM (VALUES
    ('Introducción a la Programación'),
    ('Programación Orientada a Objetos'),
    ('Estructuras de Datos en Programación'),
    ('Programación para Dispositivos Móviles'),
    ('Programación Web con HTML, CSS y JavaScript'),
    ('Desarrollo de Aplicaciones Web'),
    ('Programación Avanzada en C++'),
    ('Desarrollo de Videojuegos'),
    ('Programación Funcional con Haskell'),
    ('Machine Learning con Python'),
    ('Seguridad en Programación'),
    ('Programación Paralela y Concurrente')
) AS t(name)
WHERE NOT EXISTS (SELECT 1 FROM coder.courses WHERE name = t.name);

-- Insertar los valores de la tabla "reports_status" si es que no existen
INSERT INTO coder.reports_status (id, name)
SELECT *
FROM (VALUES (1, 'Planificada'), (2, 'Ejecutando'), (3, 'Finalizada OK'), (4, 'Finalizada con Error')) AS t(id, name)
WHERE NOT EXISTS (SELECT 1 FROM coder.reports_status WHERE id = t.id);