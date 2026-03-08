import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("比例布局示例")
        self.resize(900, 600)

        central = QWidget()
        main_layout = QVBoxLayout()

        # ===== 顶部导航栏（固定高度）=====
        nav_bar = QWidget()
        # nav_bar.setFixedHeight(60)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QLabel("系统导航栏"))

        nav_bar.setLayout(nav_layout)
        nav_bar.setStyleSheet("background-color: #2c3e50; color: white;")

        # ===== 内容区：左侧边栏（固定宽度）+ 右侧主内容 =====
        content_layout = QHBoxLayout()

        left_sidebar = QTextEdit("左侧边栏")
        # left_sidebar.setFixedWidth(200)  # 固定宽度

        right_panel = QTextEdit("右侧主内容")

        content_layout.addWidget(left_sidebar)
        content_layout.addWidget(right_panel)  # 右侧拉伸占满剩余空间

        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        # 组装
        main_layout.addWidget(nav_bar)
        main_layout.addWidget(content_widget)

        # 顶部和左侧固定，主内容区拉伸
        # main_layout.setStretch(0, 0)  # 导航栏不拉伸
        # main_layout.setStretch(1, 1)  # 内容区拉伸

        central.setLayout(main_layout)
        self.setCentralWidget(central)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()