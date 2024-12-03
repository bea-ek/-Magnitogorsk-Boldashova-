import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class WidgetArt(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetArt()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())