# QMainWindow


Qt 中的 QMainWindow 可以帮助我们快速搭建一个窗体应用程序。它提供了一个 GUI 应用程序所需的便捷结构，包含工具栏、菜单栏、中央区域、状态栏等部分。

![](https://doc.qt.io/qtforpython-6/_images/mainwindowlayout.png)

示例如下：

```python
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt


def on_open():
    print("open")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 主窗口
    window = QMainWindow()
    window.setWindowTitle("Hello World")

    # 中心部件
    widget = QLabel("Hello World")
    widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

    window.setCentralWidget(widget)
    window.show()

    sys.exit(app.exec())
```

