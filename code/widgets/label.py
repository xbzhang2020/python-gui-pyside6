from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap
import sys
import os


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建一个 QPixmap 对象
    image_path = os.path.join(os.path.dirname(__file__), "../../images/image.png")
    pixmap = QPixmap(image_path)
    # 缩放图片
    scaled_pixmap = pixmap.scaledToWidth(300)

    label = QLabel()
    label.setPixmap(scaled_pixmap)
    label.show()
    
    sys.exit(app.exec())