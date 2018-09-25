# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_error.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_error(object):
    def setupUi(self, admin_error):
        admin_error.setObjectName("admin_error")
        admin_error.resize(358, 225)
        admin_error.setMinimumSize(QtCore.QSize(358, 225))
        admin_error.setMaximumSize(QtCore.QSize(358, 225))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/images/icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_error.setWindowIcon(icon)
        admin_error.setStyleSheet("QWidget#admin_error{\n"
"border-image: url(':/images/gradient.png');\n"
"}")

        self.verticalLayoutWidget = QtWidgets.QWidget(admin_error)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 300, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(admin_error)
        QtCore.QMetaObject.connectSlotsByName(admin_error)

    def retranslateUi(self, admin_error):
        _translate = QtCore.QCoreApplication.translate
        admin_error.setWindowTitle(_translate("admin_error", "Warning"))
        self.label.setText(_translate("admin_error", "<html><head/><body><p><span style=\" color:#ffffff;\">Incorrect Username and/or Password!</span></p></body></html>"))
        self.label_3.setText(_translate("admin_error", "<html><head/><body><p><span style=\" color:#ffffff;\">Try again</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_error = QtWidgets.QWidget()
    ui = Ui_admin_error()
    ui.setupUi(admin_error)
    admin_error.show()
    sys.exit(app.exec_())

