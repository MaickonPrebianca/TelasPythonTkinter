import tkinter as tk
import pandas as pd


class minhaTela():
    def __init__(self):
        minhaTela = tk.Tk()
        minhaTela.title("Tela de acesso")

        label_usuario = tk.Label(minhaTela, text='Usuário:')
        label_usuario.grid(row=0, column=0, padx=10, pady=10)

        label_senha = tk.Label(minhaTela, text='Senha:')
        label_senha.grid(row=1, column=0, padx=10, pady=10)

        entry_usuario = tk.Entry(minhaTela, text='Usuário:', width=10)
        entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        entry_senha = tk.Entry(minhaTela, show='*' , width=10)
        entry_senha.grid(row=1, column=1, padx=10, pady=10)

        botao_ok = tk.Button(minhaTela, text = 'OK', command = minhaTela.pedir_acesso)
        botao_ok.grid(rows=2, column=0, padx=10, pady=10)

        botao_cancelar = tk.Button(minhaTela, text = 'Cancel', command = minhaTela.destroy)
        botao_cancelar.grid(rows=2, column=1, padx=10, pady=10)
        
        minhaTela.mainloop()  

        
    def pedir_acesso(self):
        print(self.entry_usuario.get())
        print(self.entry_senha.get())


    def cancelar_acesso(self):
        self.close()

