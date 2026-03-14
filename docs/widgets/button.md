# Button 组件

Button 组件主要用于用户与界面的交互，当用户按下按钮时会触发相应的行为动作。Qt 中这种触发信号响应动作的机制称为信号（Singals）和槽（Slots）。

Qt 中提供了多种类型的按钮控件，最常用的是 QPushButton 按钮。

- QAbstractButton 是所有按钮的基类，提供通用功能。
- QPushButton 是标准按钮，主要用于操作；
- QToolButton 是工具按钮，主要用于工具栏按钮。


使用示例：

```python
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
```

