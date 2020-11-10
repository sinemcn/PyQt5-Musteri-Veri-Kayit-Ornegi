import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    #Eğer buraya yazarsak sayfanın sağında kalır ve esnemez.

    h_box.addWidget(okay)
    # h_box.addStretch() : Ortasına eklersek de Tamam butonu en solda İptal botunu ise en sağda kalır.
    h_box.addWidget(cancel)

    #h_box.addStretch()

    # Butonu buraya eklersek sayfanın solunda kalır esnemez.

    v_box = QtWidgets.QVBoxLayout()
    # v_box.addStretch() : Bu şekilde yazarsak sayfanın en altına yerleştirilir.
    v_box.addStretch()
    v_box.addLayout(h_box)

    v_box.addWidget(okay)
    # v_box.addStretch() : Bu şekilde ortaya koyarsak Tamam butonu en üstte, İptal butonu en altta kalır.
    # Ortaları boş kalır.
    v_box.addWidget(cancel)
    #v_box.addStretch()
    # Bu şekilde olursa sayfanın en üstünde yer alır.(Yatay şekilde)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")

    #pencere.setLayout(h_box)
    pencere.setLayout(v_box)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()