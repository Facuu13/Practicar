
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

## 2) “Hola mundo” con **Qt Widgets** (C++)

**main.cpp**

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

    return app.exec(); // event loop
}
```

**CMakeLists.txt (Qt 6)**

```cmake
cmake_minimum_required(VERSION 3.16)
project(hello_qt_widgets LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)

find_package(Qt6 6.2 COMPONENTS Widgets REQUIRED)

add_executable(hello_qt_widgets main.cpp)
target_link_libraries(hello_qt_widgets PRIVATE Qt6::Widgets)
```

**Cómo compilar (ejemplos)**

* Linux (Debian/Ubuntu): `sudo apt install qt6-base-dev`

  ```
  mkdir build && cd build
  cmake ..
  make
  ./hello_qt_widgets
  ```
* Windows (MinGW): instalar Qt 6 + MinGW desde el instalador de Qt.

  ```
  mkdir build && cd build
  cmake -G "MinGW Makefiles" -S .. -B . -DCMAKE_PREFIX_PATH="C:/Qt/6.6.0/mingw_64"
  mingw32-make
  .\hello_qt_widgets.exe
  ```

---

## 3) “Hola mundo” con **Qt Quick / QML**

**Idea:** UI declarativa en QML; el motor se arranca desde C++.

**main.cpp**

```cpp
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QUrl>
#include <QObject>

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    const QUrl url(u"qrc:/main.qml"_qs);
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
        &app, [url](QObject *obj, const QUrl &objUrl) {
            if (!obj && url == objUrl) QCoreApplication::exit(-1);
        }, Qt::QueuedConnection);

    engine.load(url);
    return app.exec();
}
```

**main.qml** (UI)

```qml
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    width: 320; height: 200
    visible: true
    title: "Hola Qt (QML)"

    Button {
        anchors.centerIn: parent
        text: "Saludar"
        onClicked: text = "¡Hola!"
    }
}
```

**qml.qrc** (recurso para empaquetar QML)

```xml
<RCC>
  <qresource prefix="/">
    <file>main.qml</file>
  </qresource>
</RCC>
```

**CMakeLists.txt (Qt 6 Quick)**

```cmake
cmake_minimum_required(VERSION 3.16)
project(hello_qml LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 6.2 COMPONENTS Quick REQUIRED)

add_executable(hello_qml
    main.cpp
    qml.qrc
)
target_link_libraries(hello_qml PRIVATE Qt6::Quick)
```

**Notas rápidas**

* **Widgets** usa `QApplication`. **Quick** usa `QGuiApplication`.
* En **QML**, el binding es reactivo (cambios de propiedades re-renderizan).

---

## 4) Conceptos clave que acabás de usar

* **Event loop**: procesa eventos (clicks, timers, red…). Tu programa “vive” ahí.
* **Signals/Slots**: *señales* emiten eventos; *slots* reaccionan. En el ejemplo Widgets conectamos `clicked` → lambda.
* **Parenting**: `QObject` padre gestiona vida de sus hijos (menos `std::unique_ptr`, etc.).

---

