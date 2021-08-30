from tkinter import *
import time
import palavras
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
frente = PhotoImage(file="images/card_front.png")
costa = PhotoImage(file="images/card_back.png")
certo_img = PhotoImage(file="images/right.png")
errado_img = PhotoImage(file="images/wrong.png")


def cria_botao(image, column, row, funcao):
    botao = Button(image=image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=funcao)

    botao.grid(row=row, column=column)

    return botao


def vira_canvas():
    canvas.itemconfig(fundo, image=costa)
    pal = lista.palavra
    canvas.itemconfig(texto, text="English", font=("Courier", 43, "normal"), fill="white")
    canvas.itemconfig(palavra, text=pal["English"], font=("Courier", 50, "bold"), fill="white")


def muda_canvas():
    global vira
    if vira is not None:
        window.after_cancel(vira)

    canvas.itemconfig(fundo, image=frente)
    pal = lista.palavra

    canvas.itemconfig(texto, text="French", font=("Courier", 43, "normal"), fill="black")
    canvas.itemconfig(palavra, text=pal["French"], font=("Courier", 50, "bold"), fill="black")
    vira = window.after(3000, func=vira_canvas)


def clicou_certo():
    lista.acertou()
    muda_canvas()


def clicou_errado():
    lista.falhou()
    muda_canvas()

def cria_canvas():
    canvas = Canvas(height=525, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    return canvas

lista = palavras.Palavras("data/missing_words.csv")

certo = cria_botao(image=certo_img, column=0, row=1, funcao=clicou_certo)
errado = cria_botao(image=errado_img, column=1, row=1, funcao=clicou_errado)
canvas = cria_canvas()

vira = None
fundo = canvas.create_image(400, 262, image=frente)
texto = canvas.create_text(400, 170)
palavra = canvas.create_text(400, 300)

clicou_errado()
window.mainloop()


