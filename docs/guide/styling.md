# 样式

Qt 中可以使用类似 CSS 的语法来为组件设置样式。示例如下：

```python
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()
    w = QLabel("This is a placeholder text")
    w.setAlignment(Qt.AlignmentFlag.AlignCenter)
    w.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        """)
    w.show()
    sys.exit(app.exec())
```

也可以将样式写在 `.qss` 文件中，单独维护样式。

```css
QLabel#title {
    background-color: #262626;
    color: #FFFFFF;
    font-family: Titillium;
    font-size: 18px;
}
```

```python
import sys
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication()

    w = QLabel("This is a placeholder text")
    w.setObjectName("title")
    w.show()
   
    with open("base_label.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec())
```

