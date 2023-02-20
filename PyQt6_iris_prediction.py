from PyQt6 import QtCore, QtGui, QtWidgets
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 255)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QWidget {\n"
    "background-color: \"green\"\n"
    "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QWidget {\n"
    "\n"
    "    background-color: rgb(240, 240, 240);\n"
    "}")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 210, 190, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QWidget {\n"
    "background-color: \"red\"\n"
    "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cls_screen)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 68, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 96, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 40, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 12, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 40, 61, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 12, 61, 22))
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 68, 61, 22))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 96, 61, 22))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    
    def predict(self):
        textInput1 = self.lineEdit.text()
        textInput2 = self.lineEdit_2.text()
        textInput3 = self.lineEdit_3.text()
        textInput4 = self.lineEdit_4.text()
        lst = [float(textInput1), float(textInput2),
               float(textInput3), float(textInput4)]
        pred_list = np.array(lst).reshape(1, -1)
        iris = load_iris()
        model = RandomForestClassifier(n_estimators=10)
        model.fit(iris.data, iris.target)
        predict = model.predict(pred_list)
        if int(predict)==0:
                predict = 'Iris-Setosa'
        elif int(predict)==1:
                predict = 'Iris-Virginica'
        elif int(predict)==2:
                predict = 'Iris-Versicolour'
        else:
                predict = ""
        return self.label_5.setText(predict)
    
    def cls_screen(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.label_5.setText("")
        
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Iris Flower Predict"))
        self.pushButton.setText(_translate("Form", "Result"))
        self.pushButton_2.setText(_translate("Form", "Clear Screen"))
        self.label_3.setText(_translate("Form", "Sepal Length cm:"))
        self.label_4.setText(_translate("Form", "Sepal Width cm:"))
        self.label.setText(_translate("Form", "Petal Width cm:"))
        self.label_2.setText(_translate("Form", "Petal Length cm:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
