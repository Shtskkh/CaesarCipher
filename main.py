import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from caesar_cipher import encrypt

class CaesarCipher(QMainWindow):
    def __init__(self):
        super(CaesarCipher, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.encrypt)

    def encrypt(self):
        text = self.ui.textEdit.toPlainText()
        if self.ui.radioButton.isChecked():
            lang = "ru"
        else:
            lang = "en"
        self.ui.textEdit_2.setText(encrypt(text,lang))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarCipher()
    window.show()

    sys.exit(app.exec())