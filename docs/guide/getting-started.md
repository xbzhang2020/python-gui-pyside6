# 快速上手

## 安装

安装：

```shell
pip install pyside6
```

入门示例：

```python
import sys
import random
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "你好，世界"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
```

上述代码中，app.exec() 启动了一个应用程序的事件循环，当应用结束后，程序退出。Slot 装饰器用来标识一个事件回调。

## 入门示例

QApplication 是整个 GUI 应用的入口，负责管理 GUI 应用程序的控制流和主要设置。

```python
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    sys.exit(app.exec())
```
