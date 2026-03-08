"""
布局：
- 如果控件没有设置大小，则按照布局容器的大小自动调整
- 如果控件设置了大小，则按照控件大小，剩余的空白部分会被平均分配给每个控件之间的空间。
- 如果控件设置了拉伸因子，则按照拉伸因子分配剩余的空白部分。
- 如果设置了控件之间的间隔，则按照间隔分配剩余的空白部分。
"""
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QWidget()
    # widget.setFixedSize(500, 100)
    layout = QHBoxLayout()
    # layout.setContentsMargins(0, 0, 0, 0)
    # layout.setSpacing(0)  # 让 label2 紧挨着 label1，无间隙
    # layout.setStretchFactor(0, 1)

    label1 = QLabel("Label 1")
    label1.setFixedSize(100, 100)
    label1.setStyleSheet("background-color: red;")
    label2 = QLabel("Label 2")

    label2.setFixedSize(100, 100)
    label2.setStyleSheet("background-color: blue;")
    layout.addWidget(label1)
    # layout.addSpacing(2)
    layout.addWidget(label2)
    layout.addStretch()  # 多余空间推到右侧，label1 和 label2 始终紧挨着靠左

    widget.setLayout(layout)
    widget.show()
    
    sys.exit(app.exec())