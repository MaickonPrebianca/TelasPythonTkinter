import tkinter as tk
import pandas as pd


class minhaTela2:
    def __init__(self, nomeApp):
        minhaTela2 = tk.Tk()
        minhaTela2.title(nomeApp)

        label_usuario = tk.Label(minhaTela2, text='Usuário:')
        label_usuario.grid(row=0, column=0, padx=10, pady=10)

        label_senha = tk.Label(minhaTela2, text='Senha:')
        label_senha.grid(row=1, column=0, padx=10, pady=10)

        entry_usuario = tk.Entry(minhaTela2, text='Usuário:', width=10)
        entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        entry_senha = tk.Entry(minhaTela2, show='*' , width=10)
        entry_senha.grid(row=1, column=1, padx=10, pady=10)

        botao_ok = tk.Button(minhaTela2, text = 'OK', command = self.pedir_acesso(entry_usuario.get())) #print("botao ok"))
        botao_ok.grid(rows=1, column=0, padx=10, pady=10)

        botao_cancelar = tk.Button(minhaTela2, text = 'Cancel', command = minhaTela2.destroy)
        botao_cancelar.grid(rows=1, column=1, padx=10, pady=10)
        
        minhaTela2.mainloop()
            
            
    def pedir_acesso(self, usuario):
        print(usuario)
        return usuario


