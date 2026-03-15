from PySide6.QtWidgets import QApplication, QProgressBar, QWidget, QVBoxLayout
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    progress_bar = QProgressBar()
    progress_bar.setValue(50)
    progress_bar.show()
    
    sys.exit(app.exec())