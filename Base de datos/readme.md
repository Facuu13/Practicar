
---

# 📌 Repaso SQL – Parte 1: Fundamentos

## 1. ¿Qué es SQL?

* **SQL (Structured Query Language)** es el lenguaje para interactuar con **bases de datos relacionales**.
* Relacional significa que los datos están en **tablas** y esas tablas pueden estar **relacionadas entre sí**.
* Cada tabla tiene:

  * **Filas (rows / registros)** → un dato concreto (ej: un usuario).
  * **Columnas (columns / atributos)** → características de ese dato (ej: nombre, edad).

---

## 2. Crear una tabla

Supongamos que queremos guardar **usuarios** en una base de datos.

```sql
-- Creamos una tabla llamada 'usuarios'
CREATE TABLE usuarios (
    id INT PRIMARY KEY,        -- ID único por cada usuario (clave primaria)
    nombre VARCHAR(50),        -- Nombre de hasta 50 caracteres
    edad INT                   -- Edad como número entero
);
```

🔎 Explicación:

* `CREATE TABLE` → comando para crear la tabla.
* `id INT PRIMARY KEY` → columna `id`, tipo entero, y clave primaria (no puede repetirse).
* `nombre VARCHAR(50)` → texto con máximo 50 caracteres.
* `edad INT` → número entero.

👉 Con esto ya tenemos una tabla lista para guardar usuarios.

---

## 3. Insertar datos

Ahora vamos a agregar registros:

```sql
-- Insertamos un usuario
INSERT INTO usuarios (id, nombre, edad)
VALUES (1, 'Ana', 25);

-- Otro usuario
INSERT INTO usuarios (id, nombre, edad)
VALUES (2, 'Juan', 30);
```

🔎 Explicación:

* `INSERT INTO usuarios (...) VALUES (...)` → agrega un registro.
* En el primer caso:

  * `id = 1`
  * `nombre = 'Ana'`
  * `edad = 25`

👉 Ahora la tabla `usuarios` tiene 2 registros.

---

## 4. Consultar datos (SELECT)

Para ver lo que guardamos:

```sql
-- Seleccionar todos los datos de la tabla
SELECT * FROM usuarios;
```

Resultado esperado:

| id | nombre | edad |
| -- | ------ | ---- |
| 1  | Ana    | 25   |
| 2  | Juan   | 30   |

🔎 Explicación:

* `SELECT *` → el `*` significa “todas las columnas”.
* `FROM usuarios` → de la tabla `usuarios`.

Podemos filtrar:

```sql
-- Traer solo los usuarios mayores de 25
SELECT nombre, edad
FROM usuarios
WHERE edad > 25;
```

Resultado esperado:

| nombre | edad |
| ------ | ---- |
| Juan   | 30   |

🔎 Explicación:

* `WHERE` aplica una condición (como un `if`).
* Solo devuelve filas donde la condición se cumple.

---

## 5. Actualizar datos (UPDATE)

Supongamos que Ana cumplió años:

```sql
-- Cambiamos la edad de Ana a 26
UPDATE usuarios
SET edad = 26
WHERE id = 1;
```

🔎 Explicación:

* `UPDATE usuarios` → tabla a modificar.
* `SET edad = 26` → nuevo valor.
* `WHERE id = 1` → condición para que no cambien todos.

---

## 6. Borrar datos (DELETE)

Si eliminamos un usuario:

```sql
-- Eliminamos a Juan de la tabla
DELETE FROM usuarios
WHERE id = 2;
```

🔎 Explicación:

* `DELETE FROM usuarios` → indica la tabla.
* `WHERE id = 2` → condición: solo borra a Juan.

---

👉 Hasta acá vimos lo **esencial de SQL**:

* **Crear tablas (CREATE)**
* **Agregar datos (INSERT)**
* **Leer datos (SELECT)**
* **Modificar datos (UPDATE)**
* **Borrar datos (DELETE)**

Estos 4 se conocen como **operaciones CRUD** (Create, Read, Update, Delete).

---

# 📌 Repaso SQL – Parte 2: Consultas Avanzadas

---

## 1. JOIN (combinar tablas)

Las **relaciones** entre tablas son clave en SQL. Ejemplo:
Tenemos dos tablas:

```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    usuario_id INT,
    producto VARCHAR(50),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
```

Insertamos algunos datos:

```sql
INSERT INTO usuarios VALUES (1, 'Ana'), (2, 'Juan');
INSERT INTO pedidos VALUES (1, 1, 'Laptop'), (2, 2, 'Celular'), (3, 1, 'Mouse');
```

🔎 Tablas:
**usuarios**

| id | nombre |
| -- | ------ |
| 1  | Ana    |
| 2  | Juan   |

**pedidos**

| id | usuario\_id | producto |
| -- | ----------- | -------- |
| 1  | 1           | Laptop   |
| 2  | 2           | Celular  |
| 3  | 1           | Mouse    |

### INNER JOIN (solo coincidencias)

```sql
SELECT usuarios.nombre, pedidos.producto
FROM usuarios
INNER JOIN pedidos ON usuarios.id = pedidos.usuario_id;
```

👉 Resultado:

| nombre | producto |
| ------ | -------- |
| Ana    | Laptop   |
| Juan   | Celular  |
| Ana    | Mouse    |

🔎 Explicación: Une filas donde `usuarios.id = pedidos.usuario_id`.

### LEFT JOIN (todo de la izquierda, aunque no haya coincidencia)

```sql
SELECT usuarios.nombre, pedidos.producto
FROM usuarios
LEFT JOIN pedidos ON usuarios.id = pedidos.usuario_id;
```

Si un usuario no tiene pedidos, igual aparece con `NULL`.

---

## 2. Funciones de agregación

Sirven para hacer cálculos sobre varias filas.

```sql
-- Cuántos usuarios hay
SELECT COUNT(*) FROM usuarios;

-- Edad promedio (supongamos que usuarios tiene columna edad)
SELECT AVG(edad) FROM usuarios;

-- Máxima y mínima edad
SELECT MAX(edad), MIN(edad) FROM usuarios;
```

👉 Estas funciones devuelven **un solo valor**.

---

## 3. GROUP BY y HAVING

Permite agrupar resultados.

Ejemplo: contar cuántos pedidos hizo cada usuario:

```sql
SELECT usuarios.nombre, COUNT(pedidos.id) AS total_pedidos
FROM usuarios
INNER JOIN pedidos ON usuarios.id = pedidos.usuario_id
GROUP BY usuarios.nombre;
```

👉 Resultado:

| nombre | total\_pedidos |
| ------ | -------------- |
| Ana    | 2              |
| Juan   | 1              |

🔎 Explicación:

* `GROUP BY usuarios.nombre` → agrupa por usuario.
* `COUNT(pedidos.id)` → cuenta los pedidos en cada grupo.

### HAVING (filtrar grupos)

```sql
-- Solo mostrar usuarios con más de 1 pedido
SELECT usuarios.nombre, COUNT(pedidos.id) AS total_pedidos
FROM usuarios
INNER JOIN pedidos ON usuarios.id = pedidos.usuario_id
GROUP BY usuarios.nombre
HAVING COUNT(pedidos.id) > 1;
```

👉 Solo aparece Ana.

---

## 4. ORDER BY (ordenar resultados)

```sql
-- Ordenar usuarios por edad descendente
SELECT nombre, edad
FROM usuarios
ORDER BY edad DESC;
```

👉 `ASC` = ascendente (default), `DESC` = descendente.

---

## 5. LIMIT (limitar resultados)

```sql
-- Traer solo el primer usuario
SELECT * FROM usuarios
LIMIT 1;

-- Traer los 3 usuarios más jóvenes
SELECT nombre, edad
FROM usuarios
ORDER BY edad ASC
LIMIT 3;
```

👉 Muy usado para **paginación** en apps.

---

## 6. DISTINCT (evitar duplicados)

```sql
-- Mostrar edades únicas de los usuarios
SELECT DISTINCT edad FROM usuarios;
```

---

## 7. BETWEEN, IN y LIKE (filtros avanzados)

```sql
-- BETWEEN: valores en un rango
SELECT * FROM usuarios WHERE edad BETWEEN 20 AND 30;

-- IN: valores dentro de una lista
SELECT * FROM usuarios WHERE nombre IN ('Ana', 'Pedro');

-- LIKE: búsqueda con patrón
SELECT * FROM usuarios WHERE nombre LIKE 'A%';   -- nombres que empiezan con A
SELECT * FROM usuarios WHERE nombre LIKE '%n';   -- nombres que terminan en n
```

---

# ✅ Resumen hasta acá

Ya vimos:

* **CRUD** (INSERT, SELECT, UPDATE, DELETE)
* **JOINs** (INNER, LEFT)
* **Agregaciones** (COUNT, SUM, AVG, MAX, MIN)
* **GROUP BY + HAVING**
* **ORDER BY + LIMIT**
* **DISTINCT**
* **Filtros avanzados (BETWEEN, IN, LIKE)**

---

# 🔗 FOREIGN KEY (FK)

## ¿Qué es?

Una **foreign key** es una restricción que **enlaza** una columna (o conjunto de columnas) de una tabla **hija** con la **primary key (o UNIQUE)** de una tabla **padre**.
Sirve para garantizar **integridad referencial**: no pueden existir registros “huérfanos” en la tabla hija.

### Reglas básicas

* La FK **debe** apuntar a una columna que sea **PK** o tenga **UNIQUE** en la tabla padre.
* Los **tipos** deben ser compatibles (INT ↔ INT, etc.).
* Una FK **puede ser NULL** (si no pones `NOT NULL`): significa “sin relación”.
* Podés definir **acciones** ante cambios en el padre: `ON DELETE` / `ON UPDATE`.

---

## Ejemplo 1: FK básica + errores comunes

```sql
-- Tabla PADRE
CREATE TABLE usuarios (
    id INT PRIMARY KEY,        -- PK: única e índice automático
    nombre VARCHAR(50) NOT NULL
);

-- Tabla HIJA con FK a usuarios(id)
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    usuario_id INT,            -- FK apunta a usuarios.id
    producto VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pedidos_usuario
      FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
      -- sin ON DELETE/UPDATE explícito => comportamiento por defecto (RESTRICT/NO ACTION)
);

-- Datos de ejemplo
INSERT INTO usuarios (id, nombre) VALUES (1, 'Ana'), (2, 'Juan');

-- ✅ OK: usuario_id=1 existe en usuarios.id
INSERT INTO pedidos (id, usuario_id, producto) VALUES (101, 1, 'Laptop');

-- ❌ ERROR: 999 no existe en usuarios.id (viola integridad referencial)
-- INSERT INTO pedidos (id, usuario_id, producto) VALUES (102, 999, 'Mouse');

-- ❌ ERROR: no puedo borrar a Ana porque tiene pedidos asociados (RESTRICT por defecto)
-- DELETE FROM usuarios WHERE id = 1;
```

**Qué pasa acá:**

* La FK evita insertar un `usuario_id` que no exista.
* También impide borrar/modificar el padre si eso deja huérfanos a los hijos (salvo que definas otra acción).

---

## Ejemplo 2: ON DELETE / ON UPDATE

Las acciones más usadas:

| Acción                         | Efecto cuando se borra/actualiza el padre            |
| ------------------------------ | ---------------------------------------------------- |
| `CASCADE`                      | Borra/actualiza automáticamente los hijos.           |
| `SET NULL`                     | Pone la FK de los hijos en `NULL`.                   |
| `RESTRICT/NO ACTION` (default) | Impide la operación si hay hijos relacionados.       |
| `SET DEFAULT`                  | Pone la FK en su valor `DEFAULT` (si está definido). |

Probemos con `CASCADE` y `SET NULL` en dos tablas de ejemplo:

```sql
-- Variante con borrado en cascada
CREATE TABLE pedidos_cascade (
    id INT PRIMARY KEY,
    usuario_id INT,
    producto VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pedidos_cascade
      FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
      ON DELETE CASCADE      -- si borro el usuario, se borran sus pedidos
      ON UPDATE CASCADE      -- si cambio usuarios.id, se propaga
);

INSERT INTO pedidos_cascade VALUES (201, 1, 'Teclado'), (202, 1, 'Mouse');

-- ✅ Borro el usuario 1: se borran automáticamente (201, 202)
-- DELETE FROM usuarios WHERE id = 1;


-- Variante con SET NULL (permite pedidos sin usuario)
CREATE TABLE pedidos_setnull (
    id INT PRIMARY KEY,
    usuario_id INT,
    producto VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pedidos_setnull
      FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
      ON DELETE SET NULL
);

INSERT INTO usuarios (id, nombre) VALUES (3, 'Lucía');
INSERT INTO pedidos_setnull VALUES (301, 3, 'Monitor');

-- ✅ Borro a Lucía: pedido queda con usuario_id = NULL (no huérfano, sino “sin dueño”)
-- DELETE FROM usuarios WHERE id = 3;
```

> 💡 **Buenas prácticas**
>
> * **Indexá la FK** (`usuario_id`) para mejorar JOINs y cascadas:
>
>   ```sql
>   CREATE INDEX idx_pedidos_usuario_id ON pedidos(usuario_id);
>   ```
> * Elegí `CASCADE` con cuidado: es cómodo, pero puede borrar mucho más de lo esperado.
> * `SET NULL` requiere que la FK **no** sea `NOT NULL`.

---

## Ejemplo 3: Relaciones muchos-a-muchos (tabla puente)

Cuando una entidad se relaciona con **muchas** de la otra y viceversa (p. ej. usuarios ↔ cursos), se usa una **tabla intermedia** con **dos FKs** y **PK compuesta**:

```sql
CREATE TABLE cursos (
    id INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL
);

CREATE TABLE usuario_curso (
    usuario_id INT NOT NULL,
    curso_id   INT NOT NULL,
    fecha_inscripcion DATE NOT NULL DEFAULT CURRENT_DATE,
    -- PK compuesta evita duplicados (mismo usuario, mismo curso)
    CONSTRAINT pk_usuario_curso PRIMARY KEY (usuario_id, curso_id),
    -- Dos FKs
    CONSTRAINT fk_uc_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    CONSTRAINT fk_uc_curso   FOREIGN KEY (curso_id)   REFERENCES cursos(id)   ON DELETE CASCADE
);

-- Insertamos relaciones
INSERT INTO cursos VALUES (10, 'SQL Básico'), (20, 'Django Intro');
INSERT INTO usuario_curso (usuario_id, curso_id) VALUES (2, 10), (2, 20);  -- Juan en 2 cursos

-- Si borro un curso o un usuario, las filas puente se limpian con CASCADE
```

---
