import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import test

def click_success():
    print("hello world")
    return

click_success()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.beer_btn.clicked.connect(click_success)
    
    sys.exit(app.exec_())




