#include <QApplication>
#include <QPushButton>
#include <QMessageBox>
#include <QObject>
#include <QLabel>
#include <QVBoxLayout>
#include <QWidget>


int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    /*
    QPushButton btn("Hola Qt (Widgets)");
    QObject::connect(&btn, &QPushButton::clicked, [&]{
        QMessageBox::information(&btn, "Qt", "¡Hola desde Qt Widgets!");
    });
    btn.resize(220, 60);
    btn.show();
*/
    QWidget window;
    window.setWindowTitle("Contador (Signals & Slots)");

    auto *label = new QLabel("Contador: 0");
    auto *btn = new QPushButton("Sumar +1");

    auto *layout = new QVBoxLayout;
    layout->addWidget(label);
    layout->addWidget(btn);
    window.setLayout(layout);

    int count = 0;

    QObject::connect(btn, &QPushButton::clicked, [&](){
        count++;
        label->setText(QString("Contador: %1").arg(count));
    });

    window.show();
    return app.exec();
}
