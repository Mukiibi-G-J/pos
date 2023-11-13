from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.j import *
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.web_view = QWebEngineView(self)
        self.web_view.setUrl(QUrl("http://localhost:8000"))
        self.setCentralWidget(self.web_view)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

