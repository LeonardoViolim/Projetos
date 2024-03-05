from tkinter import *
from tkinter import ttk

#Importando tkcalendar
from tkcalendar import Calendar, DateEntry

#Importando datautil
from dateutil.relativedelta import relativedelta

#Importando datetime
from datetime import date

janela =Tk()
janela.title("Calculadora de Idade")
janela.geometry('310x400')

#Cores
cor1 = "#3b3b3b" #Cinza
cor2 = "#333333" #Cinza escuro
cor3 = "#ffffff" #Branca
cor4 = "#fcc058"  #Laranja

#criando frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0,relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0,relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)


#Criando labels para frame cima
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor2,fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor2,fg=cor3)
l_idade.place(x=0, y=70)

#Funcao calcular idade
def calcular():
    
    inicial=cal_1.get()
    terminio=cal_2.get()
    
    # separando os valores e atribuindo em variaveis diferentes
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
 
    # Convertendo os valores em formato  datatime
    data_inicial = date(ano_1, mes_1, dia_1)
 
 
    # separando os valores e atribuindo em variaveis diferentes
    mes_2, dia_2, ano_2 = [int(f) for f in terminio.split('/')]
 
    # Convertendo os valores em formato  datatime
    data_nascimento = date(ano_2, mes_2, dia_2)
    
    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days
    
    app_1_anos['text'] = anos
    app_2_mes['text'] = meses
    app_3_dia['text'] = dias

#Criando labels para frame baixo
l_data_inicial = Label(frame_baixo, text="Data Inicial", height=1, padx=0,pady=0, relief='flat', anchor=NW, font=('Ivi 11 '), bg=cor1,fg=cor3)
l_data_inicial.place(x=40, y=30)
cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern ='mm/dd//y', y=2024)
cal_1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de Nascimento", height=1, padx=0,pady=0, relief='flat', anchor=NW, font=('Ivi 11 '), bg=cor1,fg=cor3)
l_data_nascimento.place(x=40, y=70)
cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern ='mm/dd//y', y=2024)
cal_2.place(x=180, y=70)


l_app_anos = Label(frame_baixo, text="27", height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1,fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Ivi 11 bold'), bg=cor1,fg=cor3)
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text="12", height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1,fg=cor3)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Ivi 11 bold'), bg=cor1,fg=cor3)
l_app_meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text="27", height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1,fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0,pady=0, relief='flat', anchor='center', font=('Ivi 11 bold'), bg=cor1,fg=cor3)
l_app_dias_nome.place(x=220, y=175)

#Criando botao calcular
b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief='raised', overrelief='ridge', font=('Ivi 10 bold'), bg=cor1,fg=cor3)
b_calcular.place(x=70, y=225)

janela.mainloop()


#Esta com erro na linha 44. Voltar depois para resolver.