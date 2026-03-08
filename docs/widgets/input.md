# LineEdit

QLineEdit 控件可以用于输入文本。

```python
import sys
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QToolButton,
    QHBoxLayout,
    QWidget,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    line_edit = QLineEdit()
    line_edit.setText("Hello World")

    button = QToolButton()
    button.setText("Clear")
    button.clicked.connect(line_edit.clear)

    layout = QHBoxLayout()
    layout.addWidget(line_edit)
    layout.addWidget(button)

    window = QWidget()
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

```