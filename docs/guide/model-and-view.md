
#### Model & View

**MVC 模式**

模型：管理视图所需的数据结构。
视图：负责展示。
控制器：

模型与视图结构的好处是：解耦，可以独立管理。同一个模型可以适配多个视图层，同一个视图层代码也可以适配多个不同的数据模型。例如以下的树状视图和列表视图，可以使用同一个数据模型。

![](https://doc.qt.io/qtforpython-6/_images/shareddirmodel.png)

Model: 所有的 models 继承自 QAbstractItemModel 类，它定义了一个接口供 views 和 delegates 使。数据本身不用存储在模型中，可以存储在单独的数据结构、文件或数据库中。如果是渲染列表和表格，可以基于 QAbstractListModel 和 QAbstractTableModel，它们提供了更好的封装。

View: Qt 中提供了 QListView、QTableView、QTreeView 视图，它们都基于 QAbstractItemView 类。

Delegates: QAbstractItemDelegate 所有代理的基类。 

一个简单的模型/视图实现如下：

```python
import sys
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QListView, QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    model = QStringListModel(["Apple", "Banana", "Orange"])
    view = QListView()
    view.setModel(model)
    view.show()

    sys.exit(app.exec())
```
