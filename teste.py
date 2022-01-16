from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QDialog


class Tela_1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela 1 - TESTE")
        self.setGeometry(50, 50, 400, 400) 
        
        # CREATE LAYOUT
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        
        # CREATE WIDGETS      
        self.texto_final = QLineEdit()
        self.botao_add = QPushButton("Add")

        # ADD WIDGETS TO LAYOUT
        mainLayout.addWidget(self.texto_final)
        mainLayout.addWidget(self.botao_add)      

        # ADD CONNECT WIDGETS
        self.botao_add.clicked.connect(self.abrir_janela2)
    
    def abrir_janela2(self):
        texto_retornado = Tela_2().exec_()
        if texto_retornado:
            self.texto_final.setText(texto_retornado)


class Tela_2(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela 2 - TESTE")
        self.setGeometry(50, 50, 200, 200)
        
        # CREATE LAYOUT
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # CREATE WIDGETS      
        self.label = QLabel("Digite algo e clique no botão")
        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("Adicionar dados")
        
        # ADD WIDGETS TO LAYOUT
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.lineEdit)
        mainLayout.addWidget(self.pushButton)
        
        # CONNECT WIDGETS
        self.pushButton.clicked.connect(self.accept)
    
    def exec_(self):
        if super().exec_() == QDialog.Accepted:
            return self.lineEdit.text()
        

app = QApplication(argv)
w = Tela_1()
w.show()
exit(app.exec_())