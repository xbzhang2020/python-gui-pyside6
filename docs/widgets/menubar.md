# MenuBar 菜单栏

菜单有多种形式，可以是上下文菜单、弹窗菜单。

Qt 中与菜单有关的控件如下：

- [QMenu](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenu.html) 提供了一个菜单项，可以在菜单栏、上下文菜单、其他弹出菜单中使用。
- [QMenuBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenuBar.html#PySide6.QtWidgets.QMenuBar) 提供了一个水平方向的菜单栏。

![](https://doc.qt.io/qtforpython-6/_images/fusion-menu.png)


## 顶部菜单栏

QMenuBar 可以创建一个水平的菜单栏，通常出现在应用程序的顶部。它由一个菜单项列表组成。点击每个菜单项会触发对应的动作。

```python
from PySide6.QtWidgets import QApplication, QMenu, QMenuBar, QWidget, QVBoxLayout
from PySide6.QtGui import QAction
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = QWidget()
    window.setFixedSize(400, 300)
    layout = QVBoxLayout()

    # 顶部菜单栏
    menu_bar = QMenuBar()

    # 文件菜单
    file_menu = QMenu("File")
    menu_bar.addMenu(file_menu)

    # 文件菜单添加 action
    new_action = QAction("New", window)
    new_action.triggered.connect(lambda: print("New"))
    file_menu.addAction(new_action)

    open_action = QAction("Open", window)
    open_action.triggered.connect(lambda: print("Open"))
    file_menu.addAction(open_action)

    save_action = QAction("Save", window)
    save_action.triggered.connect(lambda: print("Save"))
    file_menu.addAction(save_action)

    layout.addWidget(menu_bar)
    window.setLayout(layout)
    window.show()
    
    sys.exit(app.exec())
```

## 上下文菜单

上下文菜单也称为右键菜单。

## 导航菜单

导航菜单用于在多个页面之间的导航，Qt 中没有提供导航菜单。可以使用 QListView 和 QStasckedWidget 模拟实现一个导航菜单。

