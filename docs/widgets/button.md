# Button

## 概述

PySide6 中的 Signals 和 Slots 机制，实现了组件和组件、组件和外部代码之间的通信。这种机制类似 JS 中的 event 和 event callback。以按钮为例，按钮提供了一个预定义的 clicked 信号，当按钮被点击时会触发对应的 slot 函数。

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

Qt 中提供了多种类型的按钮组件，其中：

- QAbstractButton 是所有按钮的基类，提供通用功能。
- QPushButton 是标准按钮，主要用于操作；
- QToolButton 是工具按钮，主要用于工具栏按钮等。