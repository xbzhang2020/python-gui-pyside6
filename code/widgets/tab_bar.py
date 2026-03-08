"""
TabBar 是 Qt 中的一个部件，用于显示多个标签页的标签栏。
用户可以通过点击标签来切换不同的标签页。
"""
import sys
from PySide6.QtWidgets import QApplication, QTabBar, QVBoxLayout, QWidget, QLabel, QStackedWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()

    stack_widget = QStackedWidget()
    stack_widget.insertWidget(0, QLabel("Tab 1"))
    stack_widget.insertWidget(1, QLabel("Tab 2"))
    stack_widget.insertWidget(2, QLabel("Tab 3"))

    tab_bar = QTabBar()
    tab_bar.addTab("Tab 1")
    tab_bar.addTab("Tab 2")
    tab_bar.addTab("Tab 3")
    tab_bar.currentChanged.connect(stack_widget.setCurrentIndex)

    layout.addWidget(tab_bar)
    layout.addWidget(stack_widget)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())