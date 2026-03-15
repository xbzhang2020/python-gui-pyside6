import sys
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QToolButton,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QTextBrowser,
    QLabel,
)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 单行文本输入
    # line_edit = QLineEdit()
    # line_edit.setText("Hello World")

    # 多行文本输入
    text_edit = QTextEdit()
    text_edit.setHtml("<h1>Hello World</h1>")

    # text_browser = QTextBrowser()
    # text_browser.setHtml("<h1>Hello World</h1><a href='https://www.baidu.com'>百度</a>")

    rich_text = QLabel("<h1>Hello World</h1><a href='https://www.baidu.com'>百度</a>")

    clear_button = QToolButton()
    clear_button.setText("Clear")
    clear_button.clicked.connect(text_edit.clear)

    get_button = QToolButton()
    get_button.setText("Get Text")
    get_button.clicked.connect(lambda: print(text_edit.toHtml()))

    layout = QHBoxLayout()
    # layout.addWidget(text_edit)
    layout.addWidget(rich_text)
    layout.addWidget(clear_button)
    layout.addWidget(get_button)

    window = QWidget()
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
