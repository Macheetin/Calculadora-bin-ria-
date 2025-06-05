import tkinter as tk
from tkinter import messagebox

def converter():
    numero = entrada.get()
    tipo = opcao.get()

    if tipo == "Binário para Decimal":
        try:
            decimal = int(numero, 2)  # converte binário para decimal
            resultado.config(text=f"Resultado: {decimal}")
        except ValueError:
            messagebox.showerror("Erro", "Número binário inválido. Use apenas 0 e 1.")
    elif tipo == "Decimal para Binário":
        try:
            decimal = int(numero)
            if decimal < 0:
                raise ValueError
            binario = bin(decimal)[2:]  # remove o prefixo '0b'
            resultado.config(text=f"Resultado: {binario}")
        except ValueError:
            messagebox.showerror("Erro", "Número decimal inválido. Digite apenas números inteiros positivos.")
    else:
        messagebox.showwarning("Aviso", "Selecione uma opção de conversão.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora Binário <-> Decimal")
janela.geometry("400x250")
janela.resizable(False, False)

# Campo de entrada
tk.Label(janela, text="Digite o número:").pack(pady=5)
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack()

# Opções de conversão
opcao = tk.StringVar(value="Binário para Decimal")
tk.Radiobutton(janela, text="Binário para Decimal", variable=opcao, value="Binário para Decimal").pack()
tk.Radiobutton(janela, text="Decimal para Binário", variable=opcao, value="Decimal para Binário").pack()

# Botão de conversão
tk.Button(janela, text="Converter", command=converter, bg="lightblue", font=("Arial", 12)).pack(pady=10)

# Resultado
resultado = tk.Label(janela, text="Resultado:", font=("Arial", 12))
resultado.pack(pady=10)

# Iniciar a interface
janela.mainloop()
