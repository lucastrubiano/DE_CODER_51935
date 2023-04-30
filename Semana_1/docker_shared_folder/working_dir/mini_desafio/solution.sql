-- Ejercicio:

/*
Tenemos un aplicativo llamado CoderReport que se encarga de generar reportes de los alumnos que cursan en CoderHouse. Estos reportes de vez en cuando se generan de forma erronea debido a alumnos que no existen o que no estan activos en el sistema. Por lo tanto, necesitamos obtener unas metricas para saber que tan grave es este problema y si es necesario tomar alguna medida al respecto.

Para esto se pide lo siguiente:

Analizar las ejecuciones de los reportes del mes de Marzo de 2023.
De las ejecuciones obtener las que fueron correctas y las que fallaron. No las que están planificadas.
Agrupar por curso, la cantidad de ejecuciones correctas y fallidas. Y el promedio de tiempo de ejecución de cada una (correctas e incorrectas).
*/

-- Solución:

SELECT
    c.id AS course_id,
    c.name AS course_name,
    COUNT(*) FILTER (WHERE rs.name = 'Finalizada OK') AS correct_executions,
    COUNT(*) FILTER (WHERE rs.name = 'Finalizada con Error') AS failed_executions,
    ROUND(AVG(r.execution_time) FILTER (WHERE rs.name = 'Finalizada OK'), 2) AS avg_correct_execution_time,
    ROUND(AVG(r.execution_time) FILTER (WHERE rs.name = 'Finalizada con Error'), 2) AS avg_failed_execution_time,
    MIN(r.created_at) AS first_execution_date,
    MAX(r.created_at) AS last_execution_date
FROM
    coder.reports r
    INNER JOIN coder.courses c ON r.course_id = c.id
    INNER JOIN coder.reports_status rs ON r.status_id = rs.id
WHERE
    r.created_at BETWEEN '2023-03-01' AND '2023-03-31'
GROUP BY
    c.id, c.name
ORDER BY
    c.id asc;
