# Slider 滑块控件

[QSlider](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSlider.html) 允许用户通过拖动滑块来选择一个值。典型的应用场景有音量控制、亮度控制等。

示意图：

![](https://doc.qt.io/qtforpython-6/_images/fusion-slider.png)

使用示例：

```python
from PySide6.QtWidgets import QApplication, QSlider, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    slider = QSlider(Qt.Orientation.Horizontal)

    slider.show()
    sys.exit(app.exec())
```

在初始化一个滑块控件时可以设置滑块的方向，默认是垂直方向。

常用方法如下：

- [value()](#set-value)
- [setvalue()](#set-value)
- [setRange()](#set-range)
- [setSingleStep()](#set-step)
- [setTickPosition()](#set-tick)
- [setTickInterval](#set-tick)

## 获取与设置值 {#set-value}

使用 `value()` 方法获取滑块的值，使用 `setvalue()` 方法设置滑块的值。滑块的值改变时会触发 `valueChange` 信号，可以通过监听它实时获取滑块的值。

实例：获取与设置滑块的值。

```python
from PySide6.QtWidgets import (
    QApplication,
    QSlider,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    layout = QVBoxLayout()

    value = 0

    # 创建组件
    label = QLabel(str(value), alignment=Qt.AlignmentFlag.AlignCenter)
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.valueChanged.connect(lambda value: label.setText(str(value)))
    button1 = QPushButton("Get Value")
    button1.clicked.connect(lambda: print(slider.value()))
    button2 = QPushButton("Reset")
    button2.clicked.connect(lambda: slider.setValue(0))

    # 添加组件到布局
    layout.addWidget(slider)
    layout.addWidget(label)
    layout.addWidget(button1)
    layout.addWidget(button2)
    w.setLayout(layout)
    w.show()

    sys.exit(app.exec())
```

## 设置范围 {#set-range}

使用 `setRange()` 设置滑块的范围，或者分别使用 `setMinimum()` 和 `setMaximum()` 设置滑块的最小值、最小值。

```python
slider.setRange(0, 100)
```

## 设置步进 {#set-step}

使用 `setSingleStep()` 设置每次拖动滑块的步进值。当鼠标聚焦到 slider上时，可以按下向左/右按键触发滑块值的变化。使用 `setPageStep()` 设置每页的步进值，可以通过按下 PageUp/PageDown 触发。

```python
slider.setSingleStep(1)
slider.setPageStep(10)
```

## 设置刻度 {#set-tick}

使用 `setTickPosition()` 设置刻度线，使用 `setTickInterval()` 设置每个刻度值的间隔。

```python
slider.setTickPosition(QSlider.TickPosition.TicksBelow)
slider.setTickInterval(10)
```
