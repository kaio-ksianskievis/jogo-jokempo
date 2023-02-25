from cgitb import text
from tkinter import *
import random
#cores
cinza = "#3b3b3b"
branco = "#FFFFFF"
amarelo = "#fff873"
verde = "#34eb3d"
#criação da janela
janela = Tk()
janela.title('JOGO')
janela.geometry('300x400')
janela.configure(bg=cinza)
#divisão da janela
frame_cima = Frame(janela,width=300,height=140,bg=cinza)
frame_cima.grid(row=0,column=0)
frame_baixo = Frame(janela,width=300,height=260)
frame_baixo.grid(row=1,column=0)
#botões
image1 = PhotoImage(file='img/icons8-hand-rock-50.png') #pedra
botao_pedra = Button(frame_baixo,command=lambda:jogada('pedra'),image=image1,width=60,height=75)
image2 = PhotoImage(file='img/icons8-hand-50.png') #papel
botao_papel  =Button(frame_baixo,command=lambda:jogada('papel'),image=image2,width=60,height=75)
image3 = PhotoImage(file='img/icons8-hand-scissors-50.png') #tesoura
botao_tesoura  =Button(frame_baixo,command=lambda:jogada('tesoura'),image=image3,width=60,height=75)
#FUNÇÕES
def iniciar():
    botao_pedra.place(x=20,y=80)
    botao_papel.place(x=118,y=80)
    botao_tesoura.place(x=215,y=80)
botao_jogar = Button(frame_baixo,command=lambda:(iniciar(),botao_jogar.destroy()),text='JOGAR',width=30,height=1,bg=cinza,fg=branco, relief=RAISED)
botao_jogar.place(x=35,y=120)
lista = ['pedra','papel','tesoura']
pc_jogadas =random.choice(lista)
jogada_jogador = None
pontos_pc = 0
pontos_jogador = 0
def jogada(jogada):
    global pontos_pc
    global pontos_jogador
    pc_jogadas =random.choice(lista)
    jogada_jogador = jogada
    if jogada_jogador == pc_jogadas:
        borda3['bg'] = amarelo
        borda1['bg'] = branco
        borda2['bg'] = branco
    if jogada_jogador =='pedra' and pc_jogadas == 'tesoura':
        borda1['bg'] = verde
        borda3['bg'] = branco
        borda2['bg'] = branco
        pontos_jogador = pontos_jogador + 1
        placar_jogador['text'] = pontos_jogador


    if jogada_jogador =='papel' and pc_jogadas == 'pedra':
        borda1['bg'] = verde
        borda3['bg'] = branco
        borda2['bg'] = branco
        pontos_jogador = pontos_jogador + 1
        placar_jogador['text'] = pontos_jogador

    if jogada_jogador =='tesoura' and pc_jogadas == 'papel':
        borda1['bg'] = verde
        borda3['bg'] = branco
        borda2['bg'] = branco
        pontos_jogador = pontos_jogador + 1
        placar_jogador['text'] = pontos_jogador

    if jogada_jogador =='pedra' and pc_jogadas == 'papel':
        borda2['bg'] = verde
        borda3['bg'] = branco
        borda1['bg'] = branco
        pontos_pc = pontos_pc + 1
        placar_pc['text']= pontos_pc
    if jogada_jogador =='papel' and pc_jogadas == 'tesoura':
        borda2['bg'] = verde
        borda3['bg'] = branco
        borda1['bg'] = branco
        pontos_pc = pontos_pc + 1
        placar_pc['text']= pontos_pc
    if jogada_jogador =='tesoura' and pc_jogadas == 'pedra':
        borda2['bg'] = verde
        borda3['bg'] = branco
        borda1['bg'] = branco
        pontos_pc = pontos_pc + 1
        placar_pc['text']= pontos_pc
    texto_jogador=Label(frame_baixo,text=jogada_jogador,width=8,height=1,bg=cinza,fg=branco,font=('ivy 13'))
    texto_jogador.place(x=10,y=20)
    texto_pc=Label(frame_baixo,text=pc_jogadas,width=8,height=1,bg=cinza,fg=branco,font=('ivy 13'))
    texto_pc.place(x=210,y=20)
    texto_x=Label(frame_baixo,text='X',width=4,height=1,bg=cinza,fg=branco,font=('ivy 13'))
    texto_x.place(x=130,y=20)
#escritas
escrita1 = Label(frame_cima,text='VOCÊ',width=10,height=2,bg=cinza,fg=branco,font=('ivy 13'))
escrita1.place(x=10,y=100)
escrita2 = Label(frame_cima,text='PC',width=10,height=2,bg=cinza,fg=branco,font=('ivy 13'))
escrita2.place(x=200,y=100)
placar_jogador = Label(frame_cima,text= pontos_jogador,font=('ivy 30'),bg=cinza,fg=branco)
placar_jogador.place(x=60,y=40)
placar_pc = Label(frame_cima,text=pontos_pc,font=('ivy 30'),bg=cinza,fg=branco)
placar_pc.place(x=210,y=40)
doispontos = Label(frame_cima,text=":",font=('ivy 30'),bg=cinza,fg=branco)
doispontos.place(x=145,y=40)
borda1= Label(frame_cima,height=140,bg=None)
borda1.place(x=0,y=0)
borda2= Label(frame_cima,height=140,bg=None)
borda2.place(x=295,y=0)
borda3= Label(frame_cima,width=300,bg=None)
borda3.place(x=0,y=133)

janela.mainloop()