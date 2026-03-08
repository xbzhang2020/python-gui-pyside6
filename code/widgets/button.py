import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
)


@Slot()
def say_hello(self):
    print("Button clicked, Hello!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    button = QPushButton("Click me")
    button.clicked.connect(say_hello)
    button.show()

    sys.exit(app.exec())
