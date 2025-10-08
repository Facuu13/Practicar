
# Módulo 1 — Arquitectura + “Hola mundo”

## 1) ¿Qué es Qt (práctico)?

* **Framework C++** para apps gráficas y no-gráficas.
* Dos formas principales de UI:

  * **Qt Widgets** (clásico, basado en `QWidget`). Ideal para escritorios, herramientas, formularios.
  * **Qt Quick/QML** (moderno, declarativo). Ideal para UIs fluidas/táctiles y embebidos con GPU.
* **Event loop**: todo vive en un bucle de eventos (`app.exec()`); los objetos (**QObject**) se comunican con **signals/slots**.
* **Gestión de memoria**: jerarquía padre-hijo (si el padre muere, borra a los hijos).

> Regla mental: *Widgets = C++ puro; Quick/QML = C++ + QML (declarativo)*.

---

### 🧩 1. `main.cpp`

Es el **programa principal en C++**, donde se define el punto de entrada (`main()`).

Qt es un *framework*, o sea, una gran colección de clases que amplían el lenguaje C++ para construir ventanas, botones, diálogos, etc.

El código era este:

```cpp
#include <QApplication>
#include <QPushButton>
#include <QMessageBox>
#include <QObject>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QPushButton btn("Hola Qt (Widgets)");
    QObject::connect(&btn, &QPushButton::clicked, [&]{
        QMessageBox::information(&btn, "Qt", "¡Hola desde Qt Widgets!");
    });
    btn.resize(220, 60);
    btn.show();

    return app.exec();
}
```

#### 🔍 Explicación línea por línea

| Parte                     | Explicación                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `#include <QApplication>` | Incluye la clase principal que maneja el *event loop* (bucle de eventos). Es necesaria en toda app Qt con GUI. |
| `#include <QPushButton>`  | Clase que representa un botón con texto.                                                                       |
| `#include <QMessageBox>`  | Clase que muestra cuadros de diálogo (ventanas emergentes).                                                    |
| `#include <QObject>`      | Clase base de todos los objetos de Qt; necesaria para signals/slots.                                           |

---

#### 🧠 Dentro del `main()`

```cpp
QApplication app(argc, argv);
```

* Crea la aplicación Qt.
* Se encarga de inicializar el entorno gráfico, los eventos del mouse/teclado, etc.
* `argc, argv` se pasan igual que en cualquier programa C++.

---

```cpp
QPushButton btn("Hola Qt (Widgets)");
```

* Crea un botón con el texto “Hola Qt (Widgets)”.
* Es un objeto **visible en pantalla** cuando lo mostramos con `show()`.

---

```cpp
QObject::connect(&btn, &QPushButton::clicked, [&]{
    QMessageBox::information(&btn, "Qt", "¡Hola desde Qt Widgets!");
});
```

* Esto es lo más importante de Qt: la conexión **signal-slot**.

  * El botón emite una *signal* llamada `clicked` cuando se hace clic.
  * La conectamos con una *lambda* (una función anónima).
  * Cuando el usuario hace clic → se ejecuta el código que muestra un cuadro de mensaje.

> Qt usa este sistema para manejar eventos sin necesidad de bucles manuales.

---

```cpp
btn.resize(220, 60);
btn.show();
```

* Define el tamaño de la ventana del botón.
* `show()` lo muestra en pantalla.

---

```cpp
return app.exec();
```

* Inicia el **bucle de eventos** (event loop).
* Qt se queda corriendo, esperando clicks, movimientos, etc.
* El programa termina cuando el usuario cierra la ventana.

---

✅ En resumen:

1. Se crea la aplicación Qt.
2. Se crea un botón.
3. Se conecta la señal de click con una función.
4. Se muestra el botón.
5. Se ejecuta el bucle principal (`app.exec()`).

---
