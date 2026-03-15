from PySide6.QtWidgets import QApplication, QMenu, QMenuBar, QWidget, QVBoxLayout, QToolBar
from PySide6.QtGui import QAction
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = QWidget()
    window.setFixedSize(400, 300)
    layout = QVBoxLayout()

    # 顶部菜单栏
    menu_bar = QMenuBar()

    # 文件菜单
    file_menu = QMenu("File")
    menu_bar.addMenu(file_menu)

    # 文件菜单添加 action
    new_action = QAction("New", window)
    new_action.triggered.connect(lambda: print("New"))
    file_menu.addAction(new_action)

    open_action = QAction("Open", window)
    open_action.triggered.connect(lambda: print("Open"))
    file_menu.addAction(open_action)

    save_action = QAction("Save", window)
    save_action.triggered.connect(lambda: print("Save"))
    file_menu.addAction(save_action)

    # ToolBar
    tool_bar = QToolBar("Main Toolbar")
    tool_bar.addAction(new_action)
    tool_bar.addAction(open_action)
    tool_bar.addAction(save_action)
    layout.addWidget(tool_bar)

    layout.addWidget(menu_bar)
    window.setLayout(layout)
    window.show()
    
    sys.exit(app.exec())