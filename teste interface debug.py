import serial

# Abre a porta serial com o Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# Define um dicionário que mapeia os botões aos comandos
button_commands = {
    'botao1': b'1',
    'botao2': b'2',
    'botao3': b'3'
}

# Define a função que será executada quando o botão for clicado
def change_color(button):
    # Envia o comando correspondente ao botão para o Arduino
    ser.write(button_commands[button])

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
