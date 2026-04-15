CREATE DATABASE IF NOT EXISTS parcial_db;
USE parcial_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

INSERT INTO usuarios (nombre)
SELECT * FROM (SELECT 'Juan') AS tmp
WHERE NOT EXISTS (
    SELECT nombre FROM usuarios WHERE nombre = 'Juan'
) LIMIT 1;