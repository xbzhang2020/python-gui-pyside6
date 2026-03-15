# TextEdit 文本编辑控件

Qt 提供了多个与文本编辑有关的控件，允许用户输入和编辑文本内容。

- [QLineEdit](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html): 编辑单行纯文本内容。
- [QPlainTextEdit](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPlainTextEdit.html): 用于编辑和展示纯文本内容。
- [QTextEdit](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTextEdit.html)：用于编辑和展示纯文本、富文本内容。

## 单行纯文本

QLineEdit 允许用户输入和编辑单行纯文本，并提供了很多实用的编辑功能，比如撤销、恢复、剪切、粘贴、拖拽等。

![](https://doc.qt.io/qtforpython-6/_images/fusion-lineedit.png)

```python
import sys
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QToolButton,
    QHBoxLayout,
    QWidget,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    line_edit = QLineEdit()
    line_edit.setText("Hello World")

    clear_button = QToolButton()
    clear_button.setText("Clear")
    clear_button.clicked.connect(line_edit.clear)

    get_button = QToolButton()
    get_button.setText("Get Text")
    get_button.clicked.connect(lambda: print(line_edit.text()))

    layout = QHBoxLayout()
    layout.addWidget(line_edit)
    layout.addWidget(clear_button)
    layout.addWidget(get_button)

    window = QWidget()
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
```

## 多行纯文本

QPlainTextEdit 和 QTextEdit 都可以创建多行文本。它们的主要区别是 QTextEdit 可以处理纯文本和富文本，而 QPlainTextEdit 只用于处理纯文本。

```python
text_edit = QTextEdit()
text_edit.setText("Hello World")
```

## 富文本

QTextEdit 可以用于编辑和展示富文本。

```python
text_edit = QTextEdit()
text_edit.setHtml("<h1>Hello World</h1>")
```
