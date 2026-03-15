# Tree 树形控件

树形控件用于展示多层次的结构列表。Qt 中提供了两种创建树形控件的方式。

- [QTreeWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeWidget.html#PySide6.QtWidgets.QTreeWidget)
- [QTreeView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTreeView.html#PySide6.QtWidgets.QTreeView)

![](https://doc.qt.io/qtforpython-6/_images/fusion-treeview.png)

## 基本使用

Qt 中使用 QTreeWidget 可以渲染树形结构。

```python
import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

data = {
    "Project A": ["file_a.py", "file_a.txt", "something.xls"],
    "Project B": ["file_b.csv", "photo.jpg"],
    "Project C": [],
}

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建树形结构
    tree = QTreeWidget()
    tree.setColumnCount(2)
    tree.setHeaderLabels(["Name", "Type"])

    # 插入节点
    items = []
    for key, values in data.items():
        item = QTreeWidgetItem([key])
        for value in values:
            ext = value.split(".")[-1].upper()
            child = QTreeWidgetItem([value, ext])
            item.addChild(child)
        items.append(item)

    tree.insertTopLevelItems(0, items)
    tree.show()

    sys.exit(app.exec())
```

## 树形视图

