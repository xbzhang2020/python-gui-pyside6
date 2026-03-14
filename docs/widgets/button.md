# Button 控件

Button 组件主要用于用户与界面的交互，当用户按下按钮时会触发相应的行为动作。Qt 中这种触发信号响应动作的机制称为信号（Singals）和槽（Slots）。

Qt 中提供了多种类型的按钮控件，包括：

- [QAbstractButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html#PySide6.QtWidgets.QAbstractButton)：是一个抽象的基类，提供了一系列通用的职责，被其他具体的按钮控件继承。
- [QPushButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html#PySide6.QtWidgets.QPushButton)：点击按钮或命令按钮，是最常使用的按钮类型。
- [QCommandLinkButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCommandLinkButton.html#PySide6.QtWidgets.QCommandLinkButton): 链接按钮，一般用于导航链接。
- [QToolButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton)：工具按钮，主要是在工具栏中使用。
- [QRadioButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html#PySide6.QtWidgets.QRadioButton)：单选按钮，用于在多个选项中选中一个按钮。
- [QCheckbox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCheckBox.html#PySide6.QtWidgets.QCheckBox)：多选框，支持选中多个选项。

## 简单按钮

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

上述实例中，使用 `@Slot` 装饰器将一个普通函数包装为槽。按钮对象提供了一个 clicked 信号，通过信号对象的 connect() 方法将槽与信号关联起来。这样，在用户触发点击信号时，会执行对应的槽函数。


## 单选按钮

## 多选框

## 菜单按钮

## 工具按钮
