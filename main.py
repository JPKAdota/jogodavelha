import tkinter
from tkinter import *
from tkinter import ttk

# cores ---------------------------------------
from django.conf.locale import bg

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"  # azul / blue
co5 = "#fff873"  # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"  # vermelha / red
co8 = co4  # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b"  # preta / black

# criando janela principal
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

# Dividindo a janela em dois frames ---------------------------------------

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando o frame de cima ---------------------------------------
app_x = Label(frame_cima, text='x', height=1, relief='flat', anchor='center', font='Ivy 40 bold', bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font='Ivy 7 bold', bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_x_pontos.place(x=70, y=22)

app_separa = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_separa.place(x=105, y=20)

app_o = Label(frame_cima, text='o', height=1, relief='flat', anchor='center', font='Ivy 40 bold', bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font='Ivy 7 bold', bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text="0", height=1, relief='flat', anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_o_pontos.place(x=130, y=22)

# Criando Lógica do App -------------------------------------------

jogador_1 = "x"
jogador_2 = "o"

score_1 = 0
score_2 = 0

tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

jogando = 'x'
jogar = ''
contador = 0

def iniciar_jogo():
    # para controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar

        # comparando o valor recebido
        if i ==str(1):
            if b_0['text']=='':
                if jogando == 'x':
                    cor=co7
                if jogando == 'o':
                    cor=co8
                b_0['fg']= cor
                b_0['text']= jogando
                tabela[[0][0]]= jogando

                if jogando =='x':
                    jogando ='0'
                    jogar = 'Jogador 1'
                else:
                    jogando =='o'
                    jogar ="Jogador 2"

                contador += 1


        print(i)

    # decidir o vencedor
    def vencedor():
        pass

    # para terminar o jogo
    def terminar():
        pass

    # Configurando o frame de baixo ---------------------------------------
    # Linhas verticais -------------------------------------------

    app_linha_vert1 = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font='Ivy 5 bold',
                            bg=co0, fg=co0)
    app_linha_vert1.place(x=90, y=15)
    app_linha_vert2 = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font='Ivy 5 bold',
                            bg=co0, fg=co0)
    app_linha_vert2.place(x=160, y=15)

    # Linhas horizontais -------------------------------------------

    app_linha_hor1 = Label(frame_baixo, text='', width=190, relief='flat', padx=2, anchor='center', font='Ivy 1 bold',
                           bg=co0, fg=co0)
    app_linha_hor1.place(x=30, y=63)
    app_linha_hor2 = Label(frame_baixo, text='', width=190, relief='flat', padx=2, anchor='center', font='Ivy 1 bold',
                           bg=co0, fg=co0)
    app_linha_hor2.place(x=30, y=123)

    # Botões linha 0 -------------------------------------------

    b_0 = Button(frame_baixo,command=lambda:controlar('1'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                 relief='flat')
    b_0.place(x=35, y=15)
    b_1 = Button(frame_baixo,command=lambda:controlar('2'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                 relief='flat')
    b_1.place(x=103, y=15)
    b_2 = Button(frame_baixo,command=lambda:controlar('3'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                 relief='flat')
    b_2.place(x=173, y=15)

    # Botões linha 1 -------------------------------------------

    b1_0 = Button(frame_baixo,command=lambda:controlar('4'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                  relief='flat')
    b1_0.place(x=35, y=76)
    b1_1 = Button(frame_baixo,command=lambda:controlar('5'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                  relief='flat')
    b1_1.place(x=103, y=76)
    b1_2 = Button(frame_baixo,command=lambda:controlar('6'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                  relief='flat')
    b1_2.place(x=173, y=76)

    # Botões linha 2 -------------------------------------------

    b2_0 = Button(frame_baixo,command=lambda:controlar('7'),text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                  relief='flat')
    b2_0.place(x=35, y=140)
    b2_1 = Button(frame_baixo,command=lambda:controlar('8'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                  relief='flat')
    b2_1.place(x=103, y=140)
    b2_2 = Button(frame_baixo,command=lambda:controlar('9'), text='', width=3, height=1, font='Ivy 17 bold', overrelief=RIDGE, bg=fundo, fg=co7,
                  relief='flat')
    b2_2.place(x=173, y=140)

# Botõe jogar -------------------------------------------

b_jogar = Button(frame_baixo,command= iniciar_jogo, text='jogar', width=10, height=1, font='Ivy 10 bold', overrelief=RIDGE, bg=fundo, fg=co0,
                 relief='raised')
b_jogar.place(x=85, y=210)

janela.mainloop()
