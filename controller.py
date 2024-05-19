from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QStyleFactory, QTableWidgetItem
from StoreSystemInterface import Ui_MainWindow  
from PyQt5.QtGui import QColor

class Controller:
    def __init__(self):
        self.app = QApplication([])

        # Create the main window
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

# Functionality for changing Stacked Widgets
    def ChangeWidgetLogin(self, index):
        self.ui.LoginStackeckedWidget.setCurrentIndex(index)

    def ChangeWidgetMain(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)


    def run(self):
        self.ChangeWidgetLogin(1    )  # Change to the login widget initially
        self.main_window.show()
        self.app.exec_()


if __name__ == "__main__":
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    controller = Controller()
    controller.run()

