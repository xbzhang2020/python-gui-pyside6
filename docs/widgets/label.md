# Label 组件

## 概述

QLabel 控件可以用于显示文本（可以是纯文本或富文本）和图片。

显示富文本的示例程序：

```python
import sys
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("<h1 style='color: red;'>Hello World!</h1>")
    label.show()

    sys.exit(app.exec())
```

## 对齐

设置文本居中的示例：

```python
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
```