# Label 组件

## 概述

[QLabel](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.QLabel) 用于显示文本（可以是纯文本或富文本）和图片。

![](https://doc.qt.io/qtforpython-6/_images/fusion-label.png)

## 展示文本

```python
from PySide6.QtWidgets import QApplication, QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("Hello World")
    label.show()
    
    sys.exit(app.exec())
```

## 展示图片


```python
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
import sys
import os


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建一个 QPixmap 对象
    image_path = os.path.join(os.path.dirname(__file__), "../../images/image.png")
    pixmap = QPixmap(image_path)
    # 缩放图片
    scaled_pixmap = pixmap.scaledToWidth(300)

    label = QLabel()
    label.setPixmap(scaled_pixmap)
    label.show()
    
    sys.exit(app.exec())
```


## 展示富文本


```python
import sys
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("<h1 style='color: red;'>Hello World!</h1>")
    label.show()

    sys.exit(app.exec())
```


## 设置和获取内容

## 对齐

对齐包括水平方向和垂直方向。


设置文本居中的示例：

```python
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
```
