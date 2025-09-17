--crear una tabla llamada readings el cual tenga id (autoincrement, PK)
--device_id (texto)
--ts_utc (fecha-hora UTC)
--temp_c (número con decimales)
--hum_pct (número con decimales) 

CREATE TABLE readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(255) NOT NULL,
    ts_utc DATETIME NOT NULL,
    temp_c DECIMAL(5, 2) NOT NULL,
    hum_pct DECIMAL(5, 2) NOT NULL
);

-- 2 Insertar datos: al menos 10 lecturas para dev001 con diferentes timestamps.

INSERT INTO readings (device_id, ts_utc, temp_c, hum_pct) VALUES
('dev001', '2024-06-01 10:00:00', 22.5, 45.0),
('dev001', '2024-06-01 11:00:00', 23.0, 50.0),
('dev001', '2024-06-01 12:00:00', 24.0, 55.0),
('dev001', '2024-06-01 13:00:00', 25.5, 60.0),
('dev001', '2024-06-01 14:00:00', 26.0, 65.0),
('dev001', '2024-06-01 15:00:00', 27.0, 70.0),
('dev001', '2024-06-01 16:00:00', 28.5, 75.0),
('dev001', '2024-06-01 17:00:00', 29.0, 80.0),
('dev001', '2024-06-01 18:00:00', 30.0, 85.0),
('dev001', '2024-06-01 19:00:00', 31.5, 90.0);

--3  Consulta: obtener las últimas 5 lecturas de dev001, ordenadas por ts_utc descendente.

SELECT * FROM readings
WHERE device_id = 'dev001'
ORDER BY ts_utc DESC
LIMIT 5;

-- Promedio de temperatura y humedad en todo el período

SELECT 
    AVG(temp_c) AS avg_temp,
    AVG(hum_pct) AS avg_hum
FROM readings
WHERE device_id = 'dev001';

-- Máxima temperatura registrada y cuándo ocurrió

SELECT ts_utc, temp_c
FROM readings
WHERE device_id = 'dev001'
ORDER BY temp_c DESC
LIMIT 1;

-- Cantidad de lecturas por día (si tuvieras más días)
SELECT DATE(ts_utc) AS day, COUNT(*) AS total_readings
FROM readings
WHERE device_id = 'dev001'
GROUP BY DATE(ts_utc);
