from PySide6.QtWidgets import (
    QApplication,
    QSlider,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    layout = QVBoxLayout()

    value = 0

    # 创建组件
    label = QLabel(str(value), alignment=Qt.AlignmentFlag.AlignCenter)
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.valueChanged.connect(lambda value: label.setText(str(value)))
    button1 = QPushButton("Get Value")
    button1.clicked.connect(lambda: print(slider.value()))
    button2 = QPushButton("Reset")
    button2.clicked.connect(lambda: slider.setValue(0))

    # 设置滑块的范围
    slider.setRange(0, 100)
    slider.setSingleStep(1)
    slider.setPageStep(10)
    slider.setFocus()  # 让滑块获得焦点，方向键（左/右）才能生效

    # 设置刻度
    slider.setTickPosition(QSlider.TickPosition.TicksBelow)
    slider.setTickInterval(10)

    # 添加组件到布局
    layout.addWidget(slider)
    layout.addWidget(label)
    layout.addWidget(button1)
    layout.addWidget(button2)
    w.setLayout(layout)
    w.show()

    sys.exit(app.exec())
