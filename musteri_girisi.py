import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("müşteriler.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS müşteriler (kullanıcı_adı TEXT,parola TEXT)")

        baglanti.commit()

    def init_ui(self):
        self.musteri_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.musteri_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        #self.setLayout(v_box)
        self.setLayout(h_box)

        self.setWindowTitle("Müşteri Girişi")
        self.giris.clicked.connect(self.login)

        self.show()

    def login(self):

        adi = self.musteri_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From müşteriler where kullanıcı_adı = ? and parola = ?",(adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir müşteri yok\nLütfen Tekrar Deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz " + adi)

            # Sinem CAN ve parola olarak 12345 yazıldığında Giriş Yap'a basınca Hoşgeldiniz Sinem CAN yazacaktır.

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())




