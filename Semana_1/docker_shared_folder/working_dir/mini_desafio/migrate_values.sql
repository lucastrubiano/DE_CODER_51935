-- Generar 300 registros aleatorios para reports
INSERT INTO coder.reports (course_id, status_id, total_students, active_students, execution_time, created_at)
SELECT 
    ROUND(RANDOM() * 11 + 1), -- course_id entre 1 y 12
    ROUND(RANDOM() * 3 + 1), -- status_id entre 1 y 4
    ROUND(RANDOM() * 100), -- total_students entre 0 y 100
    ROUND(RANDOM() * 100), -- active_students entre 0 y 100
    ROUND(RANDOM() * 100), -- execution_time entre 0 y 100
    to_timestamp(
    extract(epoch from timestamp '2023-01-01') + 
    ROUND(random() * extract(epoch from timestamp '2023-04-30' - '2023-01-01'))
) AS created_at -- fecha aleatoria entre enero y abril del 2023
FROM 
    information_schema.tables t1,
    information_schema.tables t2;

UPDATE coder.reports 
SET execution_time = 
    CASE 
        WHEN status_id = 3 THEN ROUND(execution_time * 2)
        ELSE execution_time 
    END
WHERE status_id = 3;