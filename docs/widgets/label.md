# Label 组件

[QLabel](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.QLabel) 控件主要用于显示文本、图片等信息内容。

![](https://doc.qt.io/qtforpython-6/_images/fusion-label.png)

常用方法如下：

- [setText()](#text)
- [setPixmap()](#image)
- [setAlignment()](#alignment)
- text()

## 展示文本 {#text}

展示文本内容。

```python
from PySide6.QtWidgets import QApplication, QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("Hello World")
    label.show()
    
    sys.exit(app.exec())
```

使用 `setText()` 可以动态设置标签的展示文本。

```python
label = QLabel()
label.setText("Hello World")
```

## 展示图片 {#image}


使用 `setPixmap()` 可以展示一张图片，它接收一个 QPixmap 对象。

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

## 对齐方式 {#alignment}

使用 `setAlignment()` 方法可以设置标签控件中内容的对齐方式。

实例：居中标签中的文本内容。

```python
from PySide6.QtCore import Qt

label.setAlignment(Qt.AlignmentFlag.AlignCenter)
```
