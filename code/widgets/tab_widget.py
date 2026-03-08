"""
TabWidget 是 Qt 中的一个容器部件，用于管理多个子部件（称为标签页）。
每个标签页可以包含不同的内容，用户可以通过切换标签页来查看不同的内容。
"""

from PySide6.QtWidgets import QApplication, QTabWidget, QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Fusion 样式使标签栏左对齐（Mac 默认样式会居中）

    tab_widget = QTabWidget()
    tab_widget.setTabPosition(QTabWidget.TabPosition.North)
    # tab_widget.setTabShape(QTabWidget.TabShape.Triangular)

    tab_widget.addTab(QLabel("Tab 1"), "Tab 1")
    tab_widget.addTab(QLabel("Tab 2"), "Tab 2")
    tab_widget.addTab(QLabel("Tab 3"), "Tab 3")
    tab_widget.show()
    
    sys.exit(app.exec())