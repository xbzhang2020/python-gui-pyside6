# ProgressBar 进度条

[QProgressBar](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QProgressBar.html#PySide6.QtWidgets.QProgressBar) 提供一个水平或垂直方向的进度条。

![](https://doc.qt.io/qtforpython-6/_images/fusion-progressbar.png)

## 基本使用

```python
from PySide6.QtWidgets import QApplication, QProgressBar, QWidget, QVBoxLayout
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    progress_bar = QProgressBar()
    progress_bar.setValue(50)
    progress_bar.show()
    
    sys.exit(app.exec())
```