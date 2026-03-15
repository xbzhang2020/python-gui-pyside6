# Table 表格控件

Qt 提供了两种创建表格的方式。

- [QTabWidget](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html#PySide6.QtWidgets.QTabWidget)
- [QTableView](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html#PySide6.QtWidgets.QTableView)

![](https://doc.qt.io/qtforpython-6/_images/fusion-tableview.png)

## 基本使用

Qt 中可以使用 QTableWidget 渲染表格，在渲染时需要指定表格的行和列的个数，然后使用 QTableWidgetItem 渲染每一个单元格。

```python
import sys
from PySide6.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)

data = [
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"name": "1984", "author": "George Orwell", "year": 1949},
    {"name": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"name": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"name": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
]

if __name__ == "__main__":
    app = QApplication(sys.argv)

    table = QTableWidget()
    table.setRowCount(len(data))
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["Name", "Author", "Year"])

    for i, book in enumerate(data):
        name_item = QTableWidgetItem(str(book["name"]))
        author_item = QTableWidgetItem(str(book["author"]))
        year_item = QTableWidgetItem(str(book["year"]))
        table.setItem(i, 0, name_item)
        table.setItem(i, 1, author_item)
        table.setItem(i, 2, year_item)

    table.show()

    sys.exit(app.exec())
```

## 表格视图