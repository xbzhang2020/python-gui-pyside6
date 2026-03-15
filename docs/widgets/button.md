# Button 控件

Button 控件主要用于用户与界面的交互，当用户按下按钮时会触发相应的行为动作。Qt 中这种触发信号响应动作的机制称为信号（Singals）和槽（Slots）。

Qt 中提供了多种类型的按钮控件，包括：

- [QAbstractButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QAbstractButton.html#PySide6.QtWidgets.QAbstractButton)：是一个抽象的基类，提供了一系列通用的职责，被其他具体的按钮控件继承。
- [QPushButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html#PySide6.QtWidgets.QPushButton)：点击按钮或命令按钮，是最常使用的按钮类型。
- [QCommandLinkButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCommandLinkButton.html#PySide6.QtWidgets.QCommandLinkButton): 链接按钮。
- [QToolButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.QToolButton)：工具按钮，主要是在工具栏中使用。
- [QRadioButton](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html#PySide6.QtWidgets.QRadioButton)：单选按钮，用于在多个选项中选中一个按钮。
- [QCheckbox](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCheckBox.html#PySide6.QtWidgets.QCheckBox)：多选框，支持选中多个选项。
- [QButtonGroup](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QButtonGroup.html#PySide6.QtWidgets.QButtonGroup)：按钮组，是一个管理按钮控件状态的容器。

## 简单按钮

**QPushButton** 用于创建一个简单按钮。

![](https://doc.qt.io/qtforpython-6/_images/fusion-pushbutton.png)

```python
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QHBoxLayout,
    QWidget,
)


@Slot()
def say_hello(self):
    print("Button clicked, Hello!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QHBoxLayout()

    push_button = QPushButton("Click me")
    push_button.clicked.connect(say_hello)
    layout.addWidget(push_button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
```

上述实例中，使用 `@Slot` 装饰器将一个普通函数包装为槽。按钮对象提供了一个 clicked 信号，通过信号对象的 connect() 方法将槽与信号关联起来。这样，在用户触发点击信号时，会执行对应的槽函数。

## 单选按钮

**QRadioButton** 用于创建一个单选按钮。多个单选按钮放入同一个 **QButtonGroup** 后，可以实现选项互斥，同一时刻只能选中一项。

![](https://doc.qt.io/qtforpython-6/_images/fusion-radiobutton.png)

```python
import sys
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

def on_radio_toggled(button):
    if button.isChecked():
        print(f"Selected: {button.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    radio_group = QButtonGroup(window)  # 同组内互斥
    for i, text in enumerate(["Option1", "Option2"]):
        rb = QRadioButton(text)
        if i == 0:
            rb.setChecked(True)  # 默认选中第一项
        radio_group.addButton(rb)
        rb.toggled.connect(lambda checked=False, b=rb: on_radio_toggled(b))
        layout.addWidget(rb)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())
```

- 使用 **QButtonGroup** 将多个 `QRadioButton` 归为一组，实现互斥选择。
- 通过 **toggled** 信号在用户切换选项时执行逻辑。
- 需要获取当前选中的按钮时，使用 `radio_group.checkedButton()`。

## 多选框

**QCheckBox** 用于多选框，同一组内可以同时选中多项。若用 **QButtonGroup** 管理多个多选框，需调用 `setExclusive(False)`，否则会变成互斥（只能选一项）。

![](https://doc.qt.io/qtforpython-6/_images/checkboxes-exclusive.png)

```python
import sys
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QVBoxLayout,
    QWidget,
)

def on_checkbox_toggled(checkbox):
    print(f"{checkbox.text()}: {checkbox.isChecked()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()

    checkbox_group = QButtonGroup(window)
    checkbox_group.setExclusive(False)  # 允许多选
    for text in ["Option 1", "Option 2", "Option 3"]:
        cb = QCheckBox(text)
        checkbox_group.addButton(cb)
        cb.toggled.connect(lambda checked=False, c=cb: on_checkbox_toggled(c))
        layout.addWidget(cb)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())
```

- QButtonGroup 需要设置 `setExclusive(False)` 才能多选。
- 通过 **toggled** 或 **stateChanged** 信号响应勾选/取消。
- 获取当前已选中的多选框：遍历 `checkbox_group.buttons()` 并用 `btn.isChecked()` 判断。

## 工具按钮

QToolButton 用于创建一个工具按钮。相比于普通的按钮，工具按钮通常不展示标签，而是展示一个图标。

![](https://doc.qt.io/qtforpython-6/_images/assistant-toolbar.png)

```python
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QToolButton
)

edit_button = QToolButton(window)
edit_button.setIcon(QIcon("images/edit.png"))
edit_button.clicked.connect(lambda: print("Edit button clicked"))
```

QToolButton 通常搭配 QToolBar 使用，用于创建一个工具栏。

```python
edit_button = QToolButton(window)
edit_button.setIcon(QIcon("images/edit.png"))
edit_button.clicked.connect(lambda: print("Edit button clicked"))

download_button = QToolButton(window)
download_button.setIcon(QIcon("images/download.png"))
download_button.clicked.connect(lambda: print("Download button clicked"))

# 工具栏
toolbar = QToolBar("Main Toolbar")
toolbar.addWidget(edit_button)
toolbar.addWidget(download_button)
```

## 下拉菜单

按钮与 QMenu 搭配，可以创建一个下拉菜单。

![](https://doc.qt.io/qtforpython-6/_images/fusion-pushbutton-menu.png)
