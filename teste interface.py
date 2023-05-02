import tkinter as tk
from tkinter.colorchooser import askcolor

# Define a função que será executada quando o botão for clicado
def change_color(button):
    # Pede ao usuário para selecionar uma cor usando a caixa de diálogo
    color = askcolor(parent=root, color=button['bg'], title="LED Color")

    # Define a cor de fundo do botão para a cor selecionada
    button.configure(bg=color[1])

# Cria a janela principal
root = tk.Tk()
root.geometry("400x200")

# Cria os botões coloridos
button1 = tk.Button(root, text="Botão 1", bg="red", command=lambda: change_color(button1))
button2 = tk.Button(root, text="Botão 2", bg="green", command=lambda: change_color(button2))
button3 = tk.Button(root, text="Botão 3", bg="blue", command=lambda: change_color(button3))

# Posiciona os botões na janela
button1.pack()
button2.pack()
button3.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
