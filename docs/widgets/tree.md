# Tree

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

