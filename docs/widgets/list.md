# List

Qt 中可以使用 QListWidget 渲染列表。

```python
import sys
from PySide6.QtWidgets import QApplication, QListWidget

data = [
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"name": "1984", "author": "George Orwell", "year": 1949},
    {"name": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"name": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"name": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    list_widget = QListWidget()
    for item in data:
        list_widget.addItem(f"{item['name']} - {item['author']} - {item['year']}")

    list_widget.show()
    sys.exit(app.exec())
```
