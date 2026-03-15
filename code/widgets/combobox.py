from PySide6.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout()
    combobox = QComboBox()

    # 添加选项
    options = ["Apple", "Banana", "Cherry"]
    combobox.addItems(options)
    combobox.currentTextChanged.connect(lambda text: print(text))
    
    layout.addWidget(combobox)
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())