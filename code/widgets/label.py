from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys
import os


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建一个 QPixmap 对象
    image_path = os.path.join(os.path.dirname(__file__), "../../images/image.png")
    pixmap = QPixmap(image_path)
    # 缩放图片
    scaled_pixmap = pixmap.scaledToWidth(300)

    label = QLabel("Hello World")
    # label.setFixedSize(300, 300)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # label.setPixmap(scaled_pixmap)
    # print(label.text())
    label.show()

    # label.setAlignment()
    sys.exit(app.exec())