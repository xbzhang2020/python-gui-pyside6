import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QButtonGroup,
    QLabel,
    QCheckBox,
    QCommandLinkButton,
    QToolButton,
    QToolBar,
)


@Slot()
def say_hello():
    print("Button clicked, Hello!")

@Slot()
def on_radio_toggled(button):
    if button.isChecked():
        print(f"Selected: {button.text()}")

@Slot()
def on_checkbox_toggled(checkbox):
    print(f"{checkbox.text()}: {checkbox.isChecked()}")

@Slot()
def on_tool_button_clicked():
    print("Tool button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()

    # 普通按钮
    push_button = QPushButton("Click me")
    push_button.clicked.connect(say_hello)
    layout.addWidget(push_button)

    # 单选按钮组
    layout.addWidget(QLabel("Select one: "))
    radio_group = QButtonGroup(window)  # 同组内互斥

    for i, text in enumerate(["Apple", "Banana", "Cherry"]):
        rb = QRadioButton(text)
        if i == 0:
            rb.setChecked(True)  # 默认选中第一项
        radio_group.addButton(rb)
        rb.toggled.connect(lambda checked=False, b=rb: on_radio_toggled(b))
        layout.addWidget(rb)

    # 多选框：可同时选中多项，不需互斥
    layout.addWidget(QLabel("Select multiple: "))
    checkbox_group = QButtonGroup(window)
    checkbox_group.setExclusive(False)  # 允许多选
    for text in ["Option 1", "Option 2", "Option 3"]:
        cb = QCheckBox(text)
        checkbox_group.addButton(cb)
        cb.toggled.connect(lambda checked=False, c=cb: on_checkbox_toggled(c))
        # 下面的写法存在闭包问题，无法正确获取 checkbox 的值
        # cb.toggled.connect(lambda: on_checkbox_toggled(cb)) 
        layout.addWidget(cb)

    # 链接按钮
    link_button = QCommandLinkButton("Link Button")
    link_button.clicked.connect(say_hello)
    layout.addWidget(link_button)

    # 工具按钮
    edit_button = QToolButton(window)
    edit_button.setIcon(QIcon("images/edit.png"))
    edit_button.clicked.connect(lambda: print("Edit button clicked"))
    # layout.addWidget(edit_button)

    download_button = QToolButton(window)
    download_button.setIcon(QIcon("images/download.png"))
    download_button.clicked.connect(lambda: print("Download button clicked"))
    # layout.addWidget(download_button)

    # 工具栏
    toolbar = QToolBar("Main Toolbar")
    toolbar.addWidget(edit_button)
    toolbar.addWidget(download_button)
    layout.addWidget(toolbar)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
