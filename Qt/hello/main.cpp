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
