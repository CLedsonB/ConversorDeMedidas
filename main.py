from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# ________Constantes_____________________

corFundo = '#cccccc'
corFonte = '#3b3b3b'
corBorda = '#00aa00'
corTitulo = '#48b3e0'

larguraBotao = 10
alturaBotao = 4
espacoX = 5
espacoY = 5

# ________Janela Principal_______________

main = Tk()
main.title("Conversor de Medidas")
main.geometry("650x260")
main.configure(bg=corFundo)

# ________Frames da janela________________

f_cima = Frame(main, width=480, height=50, bg=corBorda, pady=0, padx=3, relief='flat')
f_cima.place(x=2, y=2)

f_esquerda = Frame(main, width=480, height=220, bg='green', pady=0, padx=3, relief='flat')
f_esquerda.place(x=2, y=54)

f_direita = Frame(main, width=198, height=273, bg='purple', pady=0, padx=3, relief='flat')
f_direita.place(x=454, y=2)

# ________Estilo para janela________________

estilo = ttk.Style(main)
estilo.theme_use("clam")

# ________Labels do frame cima____________

l_titulo = Label(f_cima, text="Convesor de Unidades de Medidas", height=1, padx=14,pady=6, relief='flat', anchor='center', font=('Ivy 7  bold'), bg=corFundo, fg=corTitulo)

l_titulo.place(x=1, y=1)

# ________Labels do frame esquerda________

b1 = Button(f_esquerda, text="Peso",width=larguraBotao, height=alturaBotao, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 3  bold'), bg=corTitulo, fg=corFundo)

b1.grid(row=0, column=0, sticky=NSEW)

imagem = PhotoImage(file="img/peso.png")
w = Label(b1, image=imagem)
w.imagem = imagem
w.pack()

# ________Labels do frame direita___________



main.mainloop()




