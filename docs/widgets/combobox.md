# Combobox 下拉列表控件

[QComboBox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QComboBox.html) 是一个下拉选择器，允许用户从下拉列表中选择一项。

<div style="display: flex; gap: 12px;">
<img src="https://doc.qt.io/qtforpython-6/_images/collapsed_combobox.png"/>
<!-- <img src="https://doc.qt.io/qtforpython-6/_images/expanded_combobox.png"/> -->
</div>

常用方法如下：

- [addItems()](#basic)

常用的信号如下：

- [currentTextChanged](#basic)

## 基本使用 {#basic}

```python
from PySide6.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()
    combobox = QComboBox()

    # 添加选项
    options = ["Apple", "Banana", "Cherry"]
    combobox.addItems(options)
    combobox.currentTextChanged.connect(lambda text: print(text))

    layout.addWidget(combobox)
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
```
