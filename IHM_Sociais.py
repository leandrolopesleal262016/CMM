
import RPi.GPIO as GPIO
import time
from biblioteca_CMM_oficial import Rele,Narrador,Temperatura,Email,Clima#, Qrcode, Rele_qr
##from IHM_qrcode import Qrcode
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import threading # Modulo superior Para executar as threads
import sys
import time
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
import mysql.connector

file = open("start_qrcode.txt","w")
file.write("0")
file.close()

def IHM():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
    GPIO.setup(27,GPIO.IN)
    GPIO.setup(22,GPIO.IN)
    GPIO.setup(10,GPIO.IN)

    A = GPIO.input(4) # ENTRADAS NÃO FOTOACOPLADAS (As entradas A B C D então normalmente em nivel lógico HIGH (1))
    B = GPIO.input(27)
    C = GPIO.input(22)
    D = GPIO.input(10)

    hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
    h = int(time.strftime('%H'))
    data = time.strftime('%d/%m/%y')

    global entradas
    entradas = [" --- ","A", "B", "C", "D", "IN1", "IN2", "IN3", "IN4", "IN5", "IN6", "IN7", "IN8"]
    global mp3

##    def cadastra(tabela,campo,valor):
##
##        try:  # Tenta conectar com o banco de dados
##
####            signal.alarm(2)
##            cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
##            cursor = cnx.cursor()
####            signal.alarm(0)
##              
##        except mysql.connector.Error as err:
##                
##            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
##      
##                print("Alguma coisa esta errada com o nome de usuario ou a senha!")
##
##                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
##                arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: Usuario ou senha invalidos\n")
##                arquivo.close()
##
##            elif err.errno == errorcode.ER_BAD_DB_ERROR:
##      
##                print("Esta base de dados não existe!")
##
##                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
##                arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: A base de dados não existe\n")
##                arquivo.close()
##
##            else:
##                              
##                print(err)
##
##                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
##                arquivo.write("Data: " + data + " " + hs + " Evento: Erro de acesso ao Banco pelo QR Code " + err + "\n")
##                arquivo.close()
##                            
##                time.sleep(0.1)                                      
##                pass
##        try:
##
##           valor = str(valor)
##           print("Valor ", valor)
##
##           query = ("INSERT INTO entradas (in1) VALUES (%s)")
##           query_data = (valor)
##           cursor.execute(query, query_data)
##           cnx.commit()
##
##        except Exception as err:
##
##            print(err)

    def monitor():

        lb_log["text"] = "Abrindo monitor de entradas e saídas..."

        file = open("start_monitor.txt","w")
        file.write("1")
        file.close()
        

    def thread_start_monitor():

         while(1):

            file = open("start_monitor.txt","r")
            texto = file.read()
            file.close

            if texto == "0":
                
                pass
            
            if texto == "1":

                
                file = open("start_monitor.txt","w")
                file.write("0")
                file.close()

                os.system("python3 /home/pi/CMM/monitor.py")

                lb_log["text"] = "Encerrado Monitor de entradas e saídas"
                

            time.sleep(0.2)

        
        

    def qr_code():        

        print("Chama a rotina do qr code aqui")
        lb_log["text"] = "Abrindo interface QR Code..."

        file = open("start_qrcode.txt","w")
        file.write("1")
        file.close()

        
    def thread_start_qr():

        while(1):

            file = open("start_qrcode.txt","r")
            texto = file.read()
            file.close

            if texto == "0":
                
                pass
            
            if texto == "1":

                                
                file = open("start_qrcode.txt","w")
                file.write("0")
                file.close()

                pid = os.popen("python3 /home/pi/CMM/IHM_qrcode.py").read()
                pid= str(pid)
                os.system("kill %s")%pid
                lb_log["text"] = "Encerrada a interface QR Code"
            time.sleep(0.5)
        
    

    ############################ INICIA AS CLASSES DA Biblioteca_CMM_Bravas  ########################################

    rele = Rele() # inicia a classe rele com port A em 0
    narrador = Narrador()
    temperatura = Temperatura()
    email = Email()
    clima = Clima()
##    
##    qrcode = Qrcode() # Instancia a classe do leitor de qrcode
    ##wiegand = Wiegand()
    ##rele_qr = Rele_qr() # Instanciar loclamente com o IP do leitor para acionamento do rele do equipamento
    ## Ex. rele_qr = Rele_qr("172.20.9.5",5000) # Conecta com o Qrcode deste endereço para acionamento do rele e leitura da entrada auxiliar
    verifica_qr = threading.Thread(target=thread_start_qr)
    verifica_qr.start()
    
    verifica_monitor = threading.Thread(target=thread_start_monitor)
    verifica_monitor.start()
    

    ################################  GUI (Graphic User Interface) ####################################

    # Configurações da janela

    janela = Tk()
    janela.title("CMM Controladora Multi Módulos")
    janela.geometry("700x520+20+50")
    janela.maxsize(width=700, height=530) # Limita o tamaho maximo
    janela.minsize(width=700, height=530) # Limita o tamanho minimo

    ############################# Saida do programa ###############################

    def on_closing():
            
            if messagebox.askokcancel("Sair", "Você gostaria de sair da aplicação?"):

                try:

                    sock.close()

                except:

                    print("Não havia nenhuma conexão estabelecida")

                finally:
                    janela.destroy()

    ########################### Setup ###############################################

    def salva(): # temos 24 combobox na janela

        lb_log["text"] = "Salvando configurações..."

        i1 = cbox1.get()
        i2 = cbox2.get()
        i3 = cbox3.get()
        i4 = cbox4.get()
        i5 = cbox5.get()
        i6 = cbox_qbv.get()
        i7 = cbox_mud.get()
        i8 = cbox_qd.get()
        i9 = cbox_ctw1.get()
        i10 = cbox_ctw2.get()
        i11 = cbox_ctw3.get()
        i12 = cbox_ctw4.get()
        
        out1 = cbox10.get()
        out2 = cbox20.get()
        out3 = cbox30.get()
        out4 = cbox40.get()
        out5 = cbox50.get()
        out6 = cbox60.get()
        out7 = cbox70.get()
        out8 = " --- " #cbox80.get()
        out10 = cbox100.get()
        out11 = cbox110.get()
        out12 = " --- " #cbox120.get()
        out13 = cbox130.get()
        out14 = cbox51.get()
        out15 = cbox52.get()
##        out16 = cb3.get()
               
        lis = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,out1,out2,out3,out4,out5,out6,out7,out8,out10,out11,out12,out13]
        print(lis)

        txt = open("config.txt",'w')
        
        for i in lis: # Coloca cada linha do arquivo de texto na lista[]
            txt.write(i)
            txt.write("\n")

        
        txt.close() # Fecha o arquivo de texto

        lb_log["text"] = "Salvo"
        

    # Configurações do menu superior

    menubar = Menu(janela)
    janela.config(menu=menubar)

    filemenu1 = Menu(menubar,tearoff=0) # tearoff=0 para os menus não serem "flutuantes"
    filemenu2 = Menu(menubar,tearoff=0)
    filemenu3 = Menu(menubar,tearoff=0)

    menubar.add_cascade(label='Arquivo', menu=filemenu1) # Associa o menu a barra
    menubar.add_cascade(label='QR Code', menu=filemenu2)
    menubar.add_cascade(label='Monitor', menu=filemenu3)

##    filemenu1.add_command(label='Abrir...', accelerator="Teste+A")#,command=Open)
    filemenu1.add_command(label='Salvar', command=salva)
    filemenu1.add_separator() # Adiciona um separador entre as opções
    filemenu1.add_command(label='Sair',command=on_closing)#, command=Quit)
    filemenu2.add_command(label='Conectar com QR Code', command=qr_code)
    filemenu3.add_command(label='Abrir monitor', command=monitor)
     

    ############################# Background ######################################

    imagem = PhotoImage(file='/home/pi/img/SEA.png')
    label = Label(janela, image = imagem)
    label.pack()#fill = BOTH, expand = 1)

    #############################  Labels  ########################################

    Font_label = ("Arial",10,"bold italic")
    font1 = ("Arial", 8, "bold")
    font2 = ("Helvetica", 10,"italic")
    font3 = ("Helvetica", 8,"italic")

    # Labels pontos magneticos

    lb_saida = Label(janela,bg="black",fg="white",font=font3, text = "SAIDA")
    lb_saida.place(x=125, y=80)

    lb_pm1 = Label(janela,bg="black",fg="white", font=font3, text = "PM")
    lb_pm1.place(x=200, y=80)

    lb_qbv = Label(janela,bg="black",fg="white",font=font3, text = "Quebra de vidro")
    lb_qbv.place(x=245, y=80)

    lb_cx = Label(janela,bg="black",fg="white",font=font3, text =   "Chave Mudança")
    lb_cx.place(x=245, y=135)

    lb_qd = Label(janela,bg="black",fg="white",font=font3, text =   "Queda Energia")
    lb_qd.place(x=245, y=195)


    # Labels dos portões

    lb_garagem1 = Label(janela, bg="black",fg="white",text = "Garagem1")
    lb_garagem2 = Label(janela, bg="black",fg="white",text = "Garagem2")
##    mud_garagem = Label(janela, bg="black",fg="white",text = "Mudança g1",font=font3)

    lb_garagem1.place(x=340, y=100)
    lb_garagem2.place(x=340, y=130)
##    mud_garagem.place(x=360, y=160)


    lb_pm1 = Label(janela, bg="black",fg="white",text = "Portão da Rua")
    lb_pm1.place(x=10, y=100)

    lb_pm1 = Label(janela, bg="black",fg="white",text = "Portão Eclusa")
    lb_pm1.place(x=10, y=130)

    lb_pm1 = Label(janela, bg="black",fg="white",text = "Portão Acesso")
    lb_pm1.place(x=10, y=160)

    lb_pm1 = Label(janela,bg="black",fg="white", text = " Hall Entrada")
    lb_pm1.place(x=10, y=190)

    lb_pm1 = Label(janela, bg="black",fg="white",text = " Hall  Saída")    
    lb_pm1.place(x=10, y=220)


    lb_intertravamento = Label(janela, bg="black",fg="white",text = "Intertravamento")    
    lb_intertravamento.place(x=10,y=300)

    # Label Rele garagem

    lb_rl_gar = Label(janela ,bg="black",fg="white",font=font3, text = "Rele Abre")
    lb_rl_gar .place(x=415, y=80)

    lb_pm_gar  = Label(janela ,bg="black",fg="white",font=font3, text = "PM")
    lb_pm_gar .place(x=490, y=80)

    lb_sinal = Label(janela, bg="black",fg="white", font=font3, text = "Sinaleira")
    lb_sinal.place(x=535, y=80)

    lb_bar = Label(janela, bg="black",fg="white", font=font3, text = "Barreira")
    lb_bar.place(x=595, y=80)

    lb_mud = Label(janela, bg="black",fg="white", font=font3, text = "Mudança")
    lb_mud.place(x=645, y=80)

    # Gravador de voz

    lb1 = Label (janela, text = "Insira o texto a ser gravado",bg="black",fg="white",font = Font_label)
    lb1.place(x=10, y=5)

    lb_nome = Label (janela, text = "Nome do mp3",bg="black",fg="white",font = Font_label)
    lb_nome.place(x=345, y=5)

    # Temperatura CPU
    
    temp = str(temperatura.cpu())
    lb_temp_cpu = Label (janela, text = ("Temp CPU " + temp + "°C") ,bg="black",fg="white",font = font2)
    lb_temp_cpu.place(x=585,y=18)

    def temp_cpu():

        temp = str(temperatura.cpu())
        lb_temp_cpu = Label (janela, text = ("Temp CPU " + temp + "°C") ,bg="black",fg="white",font = font2)
        lb_temp_cpu.place(x=585,y=18)

        janela.after(2000,temp_cpu)

    temp_cpu()

    # Label Entrada acionamentos dos portões

    lb_social = Label (janela, text = "Abre Social" ,bg="black",fg="white")
    lb_social.place(x=370, y=222)

    lb_eclusa = Label (janela, text = "Abre Eclusa" ,bg="black",fg="white")
    lb_eclusa.place(x=370, y=256)

    lb_hall1 = Label (janela, text = "Abre Hall 1" ,bg="black",fg="white")
    lb_hall1.place(x=370, y=293)

    lb_hall2 = Label (janela, text = "Abre Hall 2" ,bg="black",fg="white")
    lb_hall2.place(x=370, y=330)

    lb_garagem1 = Label (janela, text = "Garagem 1" ,bg="black",fg="white")
    lb_garagem1.place(x=540, y=222)

    lb_garagem2 = Label (janela, text = "Garagem 2" ,bg="black",fg="white")
    lb_garagem2.place(x=540, y=256)
    

    # Label Feed back do programa (rodapé da janela)

    lb_log = Label (janela, text = "Feed back do programa",width=96,font = font2,padx=5,relief = RIDGE, bd=1, anchor = W) # GROOVE, RIDGE, FLAT
    lb_log.place(x=5, y=475)

    ####################################  Caixa de entrada #######################################

    ed1 = Entry(janela, width=40)  # Caixa de texto
    ed1.place(x=10, y=30)

    ed_nome = Entry(janela, width=15)  # Caixa de texto
    ed_nome.place(x=347, y=30)

    cb1 = StringVar()
    cb2 = StringVar()
    cb3 = StringVar()
    cb4 = StringVar()
    cb5 = StringVar()
    cb_qbv = StringVar()
    cb_cx = StringVar()
    cb_qd = StringVar()
    ctw1 = StringVar()
    ctw2 = StringVar()
    ctw3 = StringVar()
    ctw4 = StringVar()

    # Combobox Entradas (IN1, IN2, ...)

    ins = [] # Cria um alista vazia na variavel lista
    txt = open("config.txt",'r')
    
    for line in txt: # Coloca cada linha do arquivo de texto na lista[]
        ins.append(line)

    txt.close() # Fecha o arquivo de texto
    
    
    item1=(ins[0])
    item1 = item1.replace("\n","")
    item2=(ins[1])
    item2 = item2.replace("\n","")
    item3=(ins[2])
    item3 = item3.replace("\n","")
    item4=(ins[3])
    item4 = item4.replace("\n","")
    item5=(ins[4])
    item5 = item5.replace("\n","")
    item6=(ins[5])
    item6 = item6.replace("\n","")
    item7=(ins[6])
    item7 = item7.replace("\n","")
    item8=(ins[7])
    item8 = item8.replace("\n","")
    item9=(ins[8])
    item9 = item9.replace("\n","")
    item10=(ins[9])
    item10 = item10.replace("\n","")
    item11=(ins[10])
    item11 = item11.replace("\n","")
    item12=(ins[11])
    item12 = item12.replace("\n","")

    # Combobox das entradas 

    cbox1 = ttk.Combobox(janela, width=4 ,values= entradas,state='readonly',textvariable=cb1,)
    cbox1.place(x=190, y=100)
    cbox1.set(item1)   ##    cbox1.bind('<<ComboSelected>>',atualiza_entradas(1))

    cbox2 = ttk.Combobox(janela, width=4 ,values= entradas,state='readonly',textvariable=cb2)
    cbox2.place(x=190, y=130)
    cbox2.set(item2)

    cbox3 = ttk.Combobox(janela, width=4 ,values= entradas,state='readonly',textvariable=cb3)
    cbox3.place(x=190, y=160)
    cbox3.set(item3)

    cbox4 = ttk.Combobox(janela, width=4 ,values= entradas,state='readonly',textvariable=cb4)
    cbox4.place(x=190, y=190)
    cbox4.set(item4)

    cbox5 = ttk.Combobox(janela, width=4 ,values= entradas,state='readonly',textvariable=cb5)
    cbox5.place(x=190, y=220)
    cbox5.set(item5)

    cbox_qbv = ttk.Combobox(janela, width=5 ,values= entradas,state='readonly',textvariable=cb_qbv)
    cbox_qbv.place(x=260, y=100)
    cbox_qbv.set(item6)

    cbox_mud = ttk.Combobox(janela, width=5 ,values= entradas,state='readonly',textvariable=cb_cx)
    cbox_mud.place(x=260, y=160)
    cbox_mud.set(item7)

    cbox_qd = ttk.Combobox(janela, width=5 ,values= entradas,state='readonly',textvariable=cb_qd)
    cbox_qd.place(x=260, y=220)
    cbox_qd.set(item8)

    cbox_ctw1 = ttk.Combobox(janela, width=6 ,values= entradas, state='readonly',textvariable=ctw1)
    cbox_ctw1.set(item9)
    cbox_ctw1.place(x=455,y=331)

    cbox_ctw2 = ttk.Combobox(janela, width=6 ,values= entradas, state='readonly',textvariable=ctw2)
    cbox_ctw2.set(item10)
    cbox_ctw2.place(x=455,y=294)

    cbox_ctw3 = ttk.Combobox(janela, width=6 ,values= entradas, state='readonly',textvariable=ctw3)
    cbox_ctw3.set(item11)
    cbox_ctw3.place(x=455,y=257)

    cbox_ctw4 = ttk.Combobox(janela, width=6 ,values= entradas, state='readonly',textvariable=ctw4)
    cbox_ctw4.set(item12)
    cbox_ctw4.place(x=455,y=220)

    cbox_tx1 = ttk.Combobox(janela, width=6 ,values= entradas, state='readonly',textvariable=ctw3)
    cbox_tx1.set(item11)
    cbox_tx1.place(x=630,y=257)

    cbox_tx2 = ttk.Combobox(janela, width=6 ,values= entradas, state='readonly',textvariable=ctw4)
    cbox_tx2.set(item12)
    cbox_tx2.place(x=630,y=220)

# Combobox Garagem pm e barreira

    cbox_pm_g1 = ttk.Combobox(janela, width=3 ,values= entradas,state='readonly',textvariable=cb1,)
    cbox_pm_g1.place(x=485, y=100)
    cbox_pm_g1.set(item1)

    cbox_pm_g2 = ttk.Combobox(janela, width=3 ,values= entradas,state='readonly',textvariable=cb2)
    cbox_pm_g2.place(x=485, y=130)
    cbox_pm_g2.set(item2)

    cbox_b1 = ttk.Combobox(janela, width=3 ,values= entradas,state='readonly',textvariable=cb1,)
    cbox_b1.place(x=600, y=100)
    cbox_b1.set(item1)

    cbox_b2 = ttk.Combobox(janela, width=3 ,values= entradas,state='readonly',textvariable=cb2)
    cbox_b2.place(x=600, y=130)
    cbox_b2.set(item2)

    cbox_mud1 = ttk.Combobox(janela, width=3 ,values= entradas,state='readonly',textvariable=cb1,)
    cbox_mud1.place(x=650, y=100)
    cbox_mud1.set(item1)

    cbox_mud2 = ttk.Combobox(janela, width=3 ,values= entradas,state='readonly',textvariable=cb2)
    cbox_mud2.place(x=650, y=130)
    cbox_mud2.set(item2)

    # Combobox Saidas Portões (OUT1, OUT2, ...)

    c10 = StringVar()
    c20 = StringVar()
    c30 = StringVar()
    c40 = StringVar()
    c50 = StringVar()
    c51 = StringVar()
    c52 = StringVar()

    out = [] # Cria um alista vazia na variavel lista
    txt = open("config.txt",'r')
    
    for line in txt: # Coloca cada linha do arquivo de texto na lista[]
        out.append(line)

    txt.close() # Fecha o arquivo de texto
        
    item13=(out[12])
    item13 = item13.replace("\n","")
    item14=(out[13])
    item14 = item14.replace("\n","")
    item15=(out[14])
    item15 = item15.replace("\n","")
    item16=(out[15])
    item16 = item16.replace("\n","")
    item17=(out[16])
    item17 = item17.replace("\n","")
    item18=(out[17])
    item18 = item18.replace("\n","")
    item19=(out[18])
    item19 = item19.replace("\n","")
    item20=(out[19])
    item20 = item20.replace("\n","")
    item21=(out[20])
    item21 = item21.replace("\n","")
    item22=(out[21])
    item22 = item22.replace("\n","")
    item23=(out[22])
    item23 = item23.replace("\n","")
    item24=(out[23])
    item24 = item24.replace("\n","")
    item25=(out[24])
    item25 = item25.replace("\n","")
    item26=(out[25])
    item26 = item26.replace("\n","")
    
    
    global saidas
    saidas=[" --- ","OUT1", "OUT2", "OUT3", "OUT4", "OUT5", "OUT6", "OUT7", "OUT8", "OUT9", "OUT 10", "OUT 11", "OUT 12", "OUT 13", "OUT 14", "OUT 15", "OUT 16"]

    cbox10 = ttk.Combobox(janela, width=6 , values = saidas,state='readonly',textvariable=c10)
    cbox10.set(item13)
    cbox10.place(x=115, y=100)

    cbox20 = ttk.Combobox(janela, width=6 ,values = saidas,state='readonly',textvariable=c20)
    cbox20.set(item14)
    cbox20.place(x=115, y=130)

    cbox30 = ttk.Combobox(janela, width=6 ,values = saidas,state='readonly',textvariable=c30)
    cbox30.set(item15)
    cbox30.place(x=115, y=160)

    cbox40 = ttk.Combobox(janela, width=6 ,values = saidas,state='readonly',textvariable=c40)
    cbox40.set(item16)
    cbox40.place(x=115, y=190)

    cbox50 = ttk.Combobox(janela, width=6 ,values = saidas,state='readonly',textvariable=c50)
    cbox50.set(item17)
    cbox50.place(x=115, y=220)

    cbox51 = ttk.Combobox(janela, width=6 ,values = saidas,state='readonly',textvariable=c51)
    cbox51.set(item24)
    cbox51.place(x=120, y=300)

    cbox52 = ttk.Combobox(janela, width=6 ,values = saidas,state='readonly',textvariable=c52)
    cbox52.set(item25)
    cbox52.place(x=190, y=300)

    # Combobox Saida acinamento garagem

    c60 = StringVar()
    c70 = StringVar()
    c80 = StringVar()
    c100 = StringVar()
    c110 = StringVar()
    c120 = StringVar()

    cbox60 = ttk.Combobox(janela,textvariable=c60, state='readonly', width=6 ,values=saidas)
    cbox60.set(item18)
    cbox60.place(x=415, y=100)

    cbox70 = ttk.Combobox(janela,textvariable=c70, state='readonly', width=6 ,values=saidas)
    cbox70.set(item19)
    cbox70.place(x=415, y=130)

##    cbox80 = ttk.Combobox(janela,textvariable=c80, state='readonly', width=6 ,values=saidas)
##    cbox80.set(item20)
##    cbox80.place(x=435, y=160)


    cbox100 = ttk.Combobox(janela,textvariable=c100, state='readonly', width=6 ,values=saidas)
    cbox100.set(item21)
    cbox100.place(x=530, y=100)

    cbox110 = ttk.Combobox(janela,textvariable=c110, state='readonly', width=6 ,values=saidas)
    cbox110.set(item22)
    cbox110.place(x=530, y=130)

##    cbox120 = ttk.Combobox(janela,textvariable=c120, state='readonly', width=6 ,values=saidas)
##    cbox120.set(item23)
##    cbox120.place(x=550, y=160)


    # Luz Eclusa

    cbox130 = ttk.Combobox(janela, width=6 ,values=saidas ,state='readonly')
    cbox130.set(item24)
    cbox130.place(x=260, y=331)

    # Combobox dos players MP3 (play1, play2, ...)

    mp3 = os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3
    
    class Cbox:

        def __init__(self):

##            self.play1 = StringVar()
##            self.play2 = StringVar()
##            self.play3 = StringVar()
##            self.play4 = StringVar()
            self.play5 = StringVar()
            self.play6 = StringVar()
            self.play7 = StringVar()
            self.play8 = StringVar()

            self.mp3= os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3        
            
##            self.cbbox_play4 = ttk.Combobox(janela,textvariable=self.play4, width=6 ,state='readonly',values=entradas)
##            self.cbbox_play4.set(" --- ")
##            self.cbbox_play4.place(x=455,y=331)
##
##            self.cbbox_play3 = ttk.Combobox(janela,textvariable=self.play3, width=6 ,state='readonly',values=entradas)
##            self.cbbox_play3.set(" --- ")
##            self.cbbox_play3.place(x=455,y=294)
##
##            self.cbbox_play2 = ttk.Combobox(janela,textvariable=self.play2, width=6 ,state='readonly',values=entradas)
##            self.cbbox_play2.set(" --- ")
##            self.cbbox_play2.place(x=455,y=257)
##
##            self.cbbox_play1 = ttk.Combobox(janela,textvariable=self.play1, width=6 ,state='readonly',values=entradas)
##            self.cbbox_play1.set(" --- ")
##            self.cbbox_play1.place(x=455,y=220)

            self.cbbox_play8 = ttk.Combobox(janela,textvariable=self.play8, width=11 ,state='readonly',values=self.mp3)
            self.cbbox_play8.place(x=590,y=331)

            self.cbbox_play7 = ttk.Combobox(janela,textvariable=self.play7, width=11 ,state='readonly',values=self.mp3)
            self.cbbox_play7.place(x=590,y=294)

##            self.cbbox_play6 = ttk.Combobox(janela,textvariable=self.play6, width=11 ,state='readonly',values=self.mp3)
##            self.cbbox_play6.place(x=590,y=257)
##
##            self.cbbox_play5 = ttk.Combobox(janela,textvariable=self.play5, width=11 ,state='readonly',values=self.mp3)
##            self.cbbox_play5.place(x=590,y=220)

        def get_cbox(self,c):

            self.c = c
            self.p = 0

##            if self.c == 1:
##                self.p = self.play1.get()
##                return self.p
##            if self.c == 2:
##                self.p = self.play2.get()
##                return self.p
##            if self.c == 3:
##                self.p = self.play3.get()
##                return self.p
##            if self.c == 4:
##                self.p = self.play4.get()
##                return self.p
            if self.c == 5:
                self.p = self.play5.get()
                return self.p
            if self.c == 6:
                self.p = self.play6.get()
                return self.p
            if self.c == 7:
                self.p = self.play7.get()
                return self.p
            if self.c == 8:
                self.p = self.play8.get()
                return self.p

        
       
    mp3 = os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3
    cbox = Cbox()

##    print("Lido no cbox",cbox.get_cbox(1))

    #################### Metodos e funções usadas dentro da interface ###########################

    def gravar():

        lb_log["text"] = "Gravando o texto..."
        janela.update() # Atualiza a janela principal
        msg = ed1.get()
        nome = ed_nome.get()

        if nome != "":
        
            try:

                lb_log["text"] = "Ouça como ficou..."
                narrador.gravar(msg,nome)
                lb_log["text"] = ("Terminou de narrar o texto gravado em " + nome + '.mp3')
                mp3 = os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3
                janela.update()
                #cbox.plays(mp3)
##                cbox = Cbox()
                
            except Exception as err:
                
                lb_log["text"] = ("Não conseguiu gravar o texto",err)
                print(err)

        else:

            messagebox.showinfo("Nome do arquivo","Insira o nome que terá o seu\n         arquivo mp3")
            lb_log["text"] = "Insira o nome que tera sua mensagem mp3"

            
    def tocar(a):            
                
        print(a)

        if a == 1:
             p1 = cbox.get_cbox(1)
             print("p1 ",p1)
        if a == 2:
             p1 = cbox.get_cbox(2)
             print("p1 ",p1)
        if a == 3:
             p1 = cbox.get_cbox(3)
             print("p1 ",p1)
        if a == 4:
             p1 = cbox.get_cbox(4)
             print("p1 ",p1)
        if a == 5:
             p1 = cbox.get_cbox(5)
             print("p1 ",p1)
        if a == 6:
             p1 = cbox.get_cbox(6)
             print("p1 ",p1)
        if a == 7:
             p1 = cbox.get_cbox(7)
             print("p1 ",p1)
        if a == 8:
             p1 = cbox.get_cbox(8)
             print("p1 ",p1)

        lb_log["text"] = "Reproduzindo audio"
        janela.update()
       
        print(os.popen("mpg123 /home/pi/MP3/" + p1 ).read())

        lb_log["text"] = "Terminou a reprodução do audio"
   
    ################################# GIFS ######################################

##    class AnimatedGif(object):
##        
##        """ Animated GIF Image Container. """
##        def __init__(self, image_file_path):
##            # Read in all the frames of a multi-frame gif image.
##            self._frames = []
##
##            frame_num = 0  # Number of next frame to read.
##            while True:
##                try:
##                    frame = PhotoImage(file=image_file_path,
##                                       format="gif -index {}".format(frame_num))
##                except TclError:
##                    break
##                self._frames.append(frame)
##                frame_num += 1
##
##        def __len__(self):
##            return len(self._frames)
##
##        def __getitem__(self, frame_num):
##            return self._frames[frame_num]
##
##
##    def update_label_image(label, ani, ms_delay, frame_num):
##        global cancel_id
##        label.configure(image=ani[frame_num])
##        frame_num = (frame_num+1) % len(ani)
##        cancel_id = janela.after(
##            ms_delay, update_label_image, label, ani, ms_delay, frame_num)
##
##    def enable_animation():
##
##        bt_start["text"] = "Stop"
##        global cancel_id
##        if cancel_id is None:  # Animation not started?
##            ms_delay = 6000 // len(ani)  # Show all frames in 1000 ms.
##            cancel_id = janela.after(
##                ms_delay, update_label_image, animation, ani, ms_delay, 0)
##
##        
##    def cancel_animation():
##
##        bt_start["text"] = "Start"
##        global cancel_id
##        if cancel_id is not None:  # Animation started?
##            janela.after_cancel(cancel_id)
##            cancel_id = None
##
##    global cancel_id
##    cancel_id = None
##    
##    ani = AnimatedGif("/home/pi/gifs/globo.gif")    
##
##    animation = Label(image=ani[0],bg='black')  # Display first frame initially.
##    animation.place(x=603,y=360)

    #############################################################################

    
    def atualiza(): # Atualiza informações a cada 2 segundos
            
        temp = str(temperatura.cpu())

        text = ("Temp CPU " + temp + "°C")
        lb_temp_cpu["text"] = text
        
        janela.after(2000,atualiza)
                    

    ############### Metodos para iniciar funções no tkinter  ######################

    def start_stop():
        
        salva()
        lb_log["text"] = "Programa alterado, as novas configurações foram salvas"
        

    def liga(p): # Muda a função do botão de liga para pulso

        if p == 1: # De qual checkbox veio       
            p1 = pulso1.get() # obtem o valor da variavel referente ao checkbox
            if p1 == 1: # Se o valor for 1 escreve PULSO no botão se for 0 esvreve ON
                bt_rl1["text"] = "PULSO"            
            else:
                bt_rl1["text"] = "ON"

        if p == 2:        
            p2 = pulso2.get()
            if p2 == 1:
                bt_rl2["text"] = "PULSO"            
            else:
                bt_rl2["text"] = "ON"    
        
        if p == 3:        
            p3 = pulso3.get()
            if p3 == 1:
                bt_rl3["text"] = "PULSO"            
            else:
                bt_rl3["text"] = "ON"

        if p == 4:        
            p4 = pulso4.get()
            if p4 == 1:
                bt_rl4["text"] = "PULSO"            
            else:
                bt_rl4["text"] = "ON"

        if p == 5:        
            p5 = pulso5.get()
            if p5 == 1:
                bt_rl5["text"] = "PULSO"            
            else:
                bt_rl5["text"] = "ON"

        if p == 6:        
            p6 = pulso6.get()
            if p6 == 1:
                bt_rl6["text"] = "PULSO"            
            else:
                bt_rl6["text"] = "ON"

       
    def aciona(r): # LISTA COM TODAS AS POSSIVEIS SAIDAS SELECIONADAS (16)

        lista = [" --- ","OUT1","OUT2","OUT3","OUT4","OUT5","OUT6","OUT7","OUT8","OUT9","OUT 10","OUT 11","OUT 12","OUT 13","OUT 14","OUT 15","OUT 16"]

        
        if r == 1:
            out1 = c60.get()
            if out1 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:
                for i in lista:
                    if out1 == i:
                        r1 = (lista.index(i))                        
                rl1 = bt_rl1["text"]
                if rl1 == "ON":            
                    rele.liga(r1)
                    bt_rl1["text"] = "OFF"
                if rl1 == "OFF":            
                    rele.desliga(r1)
                    bt_rl1["text"] = "ON"
                if rl1 == "PULSO":
                    rele.pulso(r1,2)
                

        if r == 2:
            out2 = c70.get()
            if out2 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:
                for i in lista:
                    if out2 == i:
                        r2 = (lista.index(i))
                rl2 = bt_rl2["text"]
                if rl2 == "ON":
                    rele.liga(r2)
                    bt_rl2["text"] = "OFF"
                if rl2 == "OFF":
                    rele.desliga(r2)
                    bt_rl2["text"] = "ON"
                if rl2 == "PULSO":
                    rele.pulso(r2,2)
                

        if r == 3:
            out3 = c80.get()
            if out3 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:           
                for i in lista:
                    if out3 == i:
                        r3 = (lista.index(i))       
                rl3 = bt_rl3["text"]
                if rl3 == "ON":
                    rele.liga(r3)
                    bt_rl3["text"] = "OFF"
                if rl3 == "OFF":
                    rele.desliga(r3)
                    bt_rl3["text"] = "ON"            
                if rl3 == "PULSO":
                    rele.pulso(r3,2)

        if r == 4:
            out4 = c100.get()
            if out4 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:
                for i in lista:
                    if out4 == i:
                        r4 = (lista.index(i))        
                rl4 = bt_rl4["text"]
                if rl4 == "ON":
                    rele.liga(r4)
                    bt_rl4["text"] = "OFF"
                if rl4 == "OFF":
                    rele.desliga(r4)
                    bt_rl4["text"] = "ON"
                if rl4 == "PULSO":
                    rele.pulso(r4,2)

        if r == 5:
            out5 = c110.get()
            if out5 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:
                for i in lista:
                    if out5 == i:
                        r5 = (lista.index(i)) 
                rl5 = bt_rl5["text"]
                if rl5 == "ON":
                    rele.liga(r5)
                    bt_rl5["text"] = "OFF"
                if rl5 == "OFF":
                    rele.desliga(r5)
                    bt_rl5["text"] = "ON"
                if rl5 == "PULSO":
                    rele.pulso(r5,2)

        if r == 6:
            out6 = c120.get()
            if out6 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:
                for i in lista:
                    if out6 == i:
                        r6 = (lista.index(i)) 
                rl6 = bt_rl6["text"]
                if rl6 == "ON":
                    rele.liga(r6)
                    bt_rl6["text"] = "OFF"
                if rl6 == "OFF":
                    rele.desliga(r6)
                    bt_rl6["text"] = "ON"
                if rl6 == "PULSO":
                    rele.pulso(r6,2)

        if r == 7:
            out7 = c10.get()
            if out7 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out7 == i:
                        r7 = (lista.index(i))
                rele.pulso(r7,2)

                    
        if r == 8:
            out8 = c20.get()
            if out8 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out8 == i:
                        r8 = (lista.index(i))
                rele.pulso(r8,2)

        if r == 9:
            out9 = c30.get()
            if out9 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out9 == i:
                        r9 = (lista.index(i))
                rele.pulso(r9,2)

        if r == 10:
            out10 = c40.get()
            if out10 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out10 == i:
                        r10 = (lista.index(i))
                rele.pulso(r10,2)

        if r == 11:
            out11 = c50.get()
            if out11 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out11 == i:
                        r11 = (lista.index(i))
                rele.pulso(r11,2)

        if r == 12:
            out12 = c51.get()
            if out12 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out12 == i:
                        r12 = (lista.index(i))
                rele.pulso(r12,2)

        if r == 13:
            out13 = c52.get()
            if out13 == " --- ":
                messagebox.showerror('Erro','Escolha um rele\n para acionar')
            else:            
                for i in lista:
                    if out13 == i:
                        r13 = (lista.index(i))
                rele.pulso(r13,2)

        
    #############################  Botões  ########################################

    bt_n = Button(janela, text="Gravar",width=4, command = gravar) # Botão narrar
    #bt_n["command"] = partial (gravar,1) # reescreve uma função
    bt_n.place(x=485 ,y=22)

    # Botões acionamento portoes sociais

    bt1 = Button(janela, text="Rua",width=4) # Botão rele Rua
    bt1["command"] = partial (aciona,7) # reescreve uma função
    bt1.place(x=10, y=255)

    bt2 = Button(janela, text="Eclusa",width=4) # Botão rele Eclusa
    bt2["command"] = partial (aciona,8) # reescreve uma função
    bt2.place(x=75, y=255)

    bt3 = Button(janela, text="Acesso",width=4) # Botão rele Acesso
    bt3["command"] = partial (aciona,9) # reescreve uma função
    bt3.place(x=140, y=255)

    bt4 = Button(janela, text="Hall 1",width=4) # Botão rele Hall 1
    bt4["command"] = partial (aciona,10) # reescreve uma função
    bt4.place(x=205, y=255)

    bt5 = Button(janela, text="Hall 2",width=4) # Botão rele Hall 2
    bt5["command"] = partial (aciona,11) # reescreve uma função
    bt5.place(x=270, y=255)

    # Botoes acionamento portoes garagem

    btg1 = Button(janela, text="Garagem 1",width=6) # Botão rele Rua
    btg1["command"] = partial (aciona,12) # reescreve uma função
    btg1.place(x=416, y=160)

    btg2 = Button(janela, text="Garagem 2",width=6) # Botão rele Eclusa
    btg2["command"] = partial (aciona,13) # reescreve uma função
    btg2.place(x=500, y=160)

    
    # Acionamento de saida selecionada
##
##    bt_rl1 = Button(janela, text="ON",width=2, height=1, command=aciona) # Botão rele 
##    bt_rl1["command"] = partial (aciona,1) # reescreve uma função
##    bt_rl1.place(x=370, y=100)
##
##    bt_rl2 = Button(janela, text="ON",width=2, height=1, command=aciona) # Botão rele 
##    bt_rl2["command"] = partial (aciona,2) # reescreve uma função
##    bt_rl2.place(x=370, y=137)
##
##    bt_rl3 = Button(janela, text="ON",width=2, height=1, command=aciona) # Botão rele 
##    bt_rl3["command"] = partial (aciona,3) # reescreve uma função
##    bt_rl3.place(x=370, y=174)
 

##    bt_rl4 = Button(janela, text="ON",width=2, height=1, command=aciona) # Botão rele 
##    bt_rl4["command"] = partial (aciona,4) # reescreve uma função
##    bt_rl4.place(x=540, y=100)
##
##    bt_rl5 = Button(janela, text="ON",width=2, height=1, command=aciona) # Botão rele 
##    bt_rl5["command"] = partial (aciona,5) # reescreve uma função
##    bt_rl5.place(x=540, y=137)
##
##    bt_rl6 = Button(janela, text="ON",width=2, height=1, command=aciona) # Botão rele 
##    bt_rl6["command"] = partial (aciona,6) # reescreve uma função
##    bt_rl6.place(x=540, y=174)


##    bt_play1 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
##    bt_play1["command"] = partial (tocar,1,) # reescreve uma função
##    bt_play1.place(x=370, y=217)
##
##    bt_play2 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
##    bt_play2["command"] = partial (tocar,2) # reescreve uma função
##    bt_play2.place(x=370, y=251)
##
##    bt_play3 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
##    bt_play3["command"] = partial (tocar,3) # reescreve uma função
##    bt_play3.place(x=370, y=288)
##
##    bt_play4 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
##    bt_play4["command"] = partial (tocar,4) # reescreve uma função
##    bt_play4.place(x=370, y=325)


##    bt_play5 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
##    bt_play5["command"] = partial (tocar,5) # reescreve uma função
##    bt_play5.place(x=540, y=217)
##
##    bt_play6 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
##    bt_play6["command"] = partial (tocar,6) # reescreve uma função
##    bt_play6.place(x=540, y=251)

    bt_play7 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
    bt_play7["command"] = partial (tocar,7) # reescreve uma função
    bt_play7.place(x=540, y=288)

    bt_play8 = Button(janela, text="Play",width=1, height=1, command = tocar) # Botão rele 7
    bt_play8["command"] = partial (tocar,8) # reescreve uma função
    bt_play8.place(x=540, y=325)

    # Botão Start

    bt_start = Button(janela, text="Aplicar",width=6,command = start_stop)
    bt_start.place(x=610, y=430)


    # Check box Programas Intertravamento, Saudação, Iluminação Automática

    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()

    pulso1 = IntVar()
    pulso2 = IntVar()
    pulso3 = IntVar()
    pulso4 = IntVar()
    pulso5 = IntVar()
    pulso6 = IntVar()

##    check1 = Checkbutton(janela, text="Intertravamento Sociais",variable = CheckVar1)
##    check1.place(x=10,y=300)

    check1 = Checkbutton(janela, text="Sauda",variable = CheckVar2)
    check1.place(x=260, y=300)

    check1 = Checkbutton(janela, text=" Iluminação Automática da Eclusa ",variable = CheckVar3)
    check1.place(x=10,y=330)

    # cHECK BOX PARA HAHILITAR PULSO DO RELE

##    check30 = Checkbutton(janela,variable = pulso3)
##    check30["command"] = partial (liga,3) # reescreve uma função
##    check30.place(x=495, y=180)
##
##    check20 = Checkbutton(janela,variable = pulso2)
##    check20["command"] = partial (liga,2) # reescreve uma função
##    check20.place(x=495, y=140)
##
##    check10 = Checkbutton(janela,variable = pulso1)
##    check10["command"] = partial (liga,1) # reescreve uma função
##    check10.place(x=495, y=105)


##    check60 = Checkbutton(janela,variable = pulso6)
##    check60["command"] = partial (liga,6) # reescreve uma função
##    check60.place(x=662, y=180)
##
##    check50 = Checkbutton(janela,variable = pulso5)
##    check50["command"] = partial (liga,5) # reescreve uma função
##    check50.place(x=662, y=140)
##
##    check40 = Checkbutton(janela,variable = pulso4)
##    check40["command"] = partial (liga,4) # reescreve uma função
##    check40.place(x=662, y=105)                  

    janela.protocol("WM_DELETE_WINDOW", on_closing)
    janela.mainloop()

    print("A janela foi fechada")
