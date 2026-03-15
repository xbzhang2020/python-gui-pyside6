import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QButtonGroup,
    QLabel,
)


@Slot()
def say_hello():
    print("Button clicked, Hello!")

@Slot()
def on_radio_toggled(button):
    if button.isChecked():
        print(f"Selected: {button.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()

    # 普通按钮
    push_button = QPushButton("Click me")
    push_button.clicked.connect(say_hello)
    layout.addWidget(push_button)

    # 单选按钮组
    layout.addWidget(QLabel("Select one: "))
    radio_group = QButtonGroup(window)  # 同组内互斥

    for i, text in enumerate(["Apple", "Banana", "Cherry"]):
        rb = QRadioButton(text)
        if i == 0:
            rb.setChecked(True)  # 默认选中第一项
        radio_group.addButton(rb)
        rb.toggled.connect(lambda: on_radio_toggled(rb))
        layout.addWidget(rb)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
