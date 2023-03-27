import tkinter as tk

# quando clicar no botão exibe algo na tela
def clicado():
    label = tk.Label(root, text="Funciona")
    label.pack()

# pega informação da tela
def pega_info_exibe():
    texto = entry.get()
    print(texto)
    label = tk.Label(root, text=texto)
    label.pack()

# Inicia a interface
root = tk.Tk()

# Redimensionar a tela inicial do TK
root.geometry("500x300")

root.iconbitmap("icone.ico")

# Alterar nome da janela
root.title("Hosting")

# Label de mensagem simples
label = tk.Label(root, text="Testando TKinter")
label.pack() # Organizar o widgets da janela

# Label de textos
label = tk.Message(root, text="Testando Textos e separação de linha \n Testando Textos e separação de linha")
label.pack()

# Carrega a imagem a partir do arquivo
photo = tk.PhotoImage(file="minion.png")
photo = photo.subsample(10)

# Cria um rótulo de imagem e exibe a imagem
label = tk.Label(root, image=photo)
label.pack()

# Caixa de entrada de texto 
entry = tk.Entry(root, width=30)
button =tk.Button(root, text="clique aqui", bg="blue", fg="white", command=clicado)
entry.pack()
button.pack()

button =tk.Button(root, text="Olha cmd", bg="blue", fg="white", command=pega_info_exibe)
button.pack()

# Botão para fechar a janela
fechar =tk.Button(root, text="Fechar", bg="red", fg="white", command=root.destroy)
fechar.pack()

root.mainloop() # Iniciar a exibição da janela