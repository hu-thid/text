import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('PyQt on Android')
    window.setGeometry(100, 100, 300, 200)

    label = QLabel('Hello PyQt on Android!', parent=window)
    label.move(50, 50)

    window.show()

    sys.exit(app.exec_())
