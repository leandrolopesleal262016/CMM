#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
from tkinter import * # importa todos os objetos da biblioteca do tkinter
from functools import partial
import socket
import time
import threading
from datetime import datetime, timedelta
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import sys
import mysql.connector
import signal
from tkinter import messagebox

###################################### Classe Leitor QR Code  #############################################

class Qrcode:

    def __init__(self):

        hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
        h = int(time.strftime("%H"))
        data = time.strftime('%d/%m/%y')

        print("Dia",data,hs,"hs\n")
        
    ##    host_servidor = '0.0.0.0'
    ##
    ##    port_gerenciador = 5511
    ##
    ##    ip_qrcode = '172.20.9.5'
    ##    port_qr = 5000 # Porta para acionamento de rele 5001 (leitura dos dados do qr code)

        conectar = 0

        ##txt = open("conectar_qr1.txt", "w") # Zera os arquivos "conectar" para não tentar conectar no inicio
        ##txt.write("0")
        ##txt.close()
        ##
        ##txt = open("conectar_qr2.txt", "w") 
        ##txt.write("0")
        ##txt.close()
        ##
        ##txt = open("conectar_qr3.txt", "w") 
        ##txt.write("0")
        ##txt.close()
        ##
        ##txt = open("conectar_qr4.txt", "w") 
        ##txt.write("0")
        ##txt.close()

        #################################  Entrada dos pontos magneticos ##########################################

        global A,B,C,D
        A = 7
        B = 27
        C = 22
        D = 10

        GPIO.setwarnings(False) # desabilita mensagens de aviso
        GPIO.setmode(GPIO.BCM) # Modo de endereço dos pinos BCM

        GPIO.setup(A,GPIO.IN)#, pull_up_down = GPIO.PUD_UP) # PM1 (ponto magnético) (com pull up)
        GPIO.setup(B,GPIO.IN)#, pull_up_down = GPIO.PUD_UP) # PM2 (ponto magnético) (com pull up)
        GPIO.setup(C,GPIO.IN)#, pull_up_down = GPIO.PUD_UP) # PM1 (ponto magnético) (com pull up)
        GPIO.setup(D,GPIO.IN)#, pull_up_down = GPIO.PUD_UP) # PM2 (ponto magnético) (com pull up)

        in1 = GPIO.input(A)
        in2 = GPIO.input(B)
        in3 = GPIO.input(C)
        in4 = GPIO.input(D)

        pm1 = in1
        pm2 = in2

        print("PM1 Entrada",GPIO.input(A))
        print("PM2 Eclusa",GPIO.input(B))
        print("PM3 Acesso",GPIO.input(C))
        print("PM4 Acesso",GPIO.input(D))

            
    def Start(self):

        def on_closing():
            
            if messagebox.askokcancel("Sair", "Você gostaria de sair da aplicação?"):

                try:

                    sock.close()
                    
                    
                except:

                    print("Não havia nenhuma conexão estabelecida")

                finally:
                    janela_qrcode.destroy()
        
        def leitor_qrcode(qr):

            hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
            h = int(time.strftime("%H"))
            data = time.strftime('%d/%m/%y')                
                
            if qr == "1":

                ip = ed1.get()
                
                if ip == "":

                    ip1 = open("conecta_automatico_qr1.txt", "r")
                    ip1 = ip1.readline()
                    ip = ip1

            if qr == "2":

                ip = ed2.get()

                if ip == "":

                    ip2 = open("conecta_automatico_qr2.txt", "r")
                    ip2 = ip2.readline()
                    ip = ip2

            if qr == "3":

                ip = ed3.get()

                if ip == "":

                    ip3 = open("conecta_automatico_qr3.txt", "r")
                    ip3 = ip3.readline()
                    ip = ip3

            if qr == "4":

                ip = ed4.get()

                if ip == "":

                    ip4 = open("conecta_automatico_qr4.txt", "r")
                    ip4 = ip4.readline()
                    ip = ip4

            ip_qrcode = ip

            
            try:

                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_address = (ip_qrcode, 5001) # Endereço do QR Code porta centrral        
                time.sleep(0.1)
                sock.connect(server_address)
                
                
                if qr == "1":

                    bt["text"] = ip_qrcode
                    ed1.config(state=DISABLED) # Desbilita o Entry
                    bt.config(state=DISABLED) # Desabilita o botão Conectar
                    bt1.config(state=NORMAL)
                    check1.select()  # Deixa a caixa selecionada
                    conecta_automatico("1") # Adiciona o ip do entry no arquivo de inicio automático
                    

                if qr == "2":

                    bt2["text"] = ip_qrcode
                    ed2.config(state=DISABLED)
                    bt2.config(state=DISABLED) # Desabilita o botão
                    bt3.config(state=NORMAL)
                    check2.select()  # Deixa a caixa selecionada
                    conecta_automatico("2")
                    


                if qr == "3":

                    bt4["text"] = ip_qrcode
                    ed3.config(state=DISABLED)
                    bt4.config(state=DISABLED) # Desabilita o botão
                    bt5.config(state=NORMAL)
                    check3.select()  # Deixa a caixa selecionada
                    conecta_automatico("3")


                if qr == "4":

                    bt6["text"] = ip_qrcode
                    ed4.config(state=DISABLED)
                    bt6.config(state=DISABLED) # Desabilita o botão
                    bt7.config(state=NORMAL)
                    check4.select() # Deixa a caixa selecionada
                    conecta_automatico("4")

                

                print('\nConectado com Leitor QR CODE {} port {}'.format(*server_address),"\n")
                
                lb_log["text"] = ("Conectado com Leitor " + qr + " IP "  + ip_qrcode)

                if qr == 1:

                    automatico1 = ed1["text"]
                    
                    if aumatico1 != "":

                        messagebox.showinfo("Conectado","Conectado com o Leitor " + qr + " \n          IP " + ip_qrcode)
                
                if qr == 2:

                    automatico2 = ed2["text"]
                    
                    if aumatico2 != "":

                        messagebox.showinfo("Conectado","Conectado com o Leitor " + qr + " \n          IP " + ip_qrcode)

                if qr == 3:

                    automatico3 = ed3["text"]
                    
                    if aumatico3 != "":

                        messagebox.showinfo("Conectado","Conectado com o Leitor " + qr + " \n          IP " + ip_qrcode)

                if qr == 4:

                    automatico4 = ed4["text"]
                    
                    if aumatico4 != "":

                        messagebox.showinfo("Conectado","Conectado com o Leitor " + qr + " \n          IP " + ip_qrcode)
                
                
                consulta = 0
                id_valido = 0
                acesso = 0
                fora_do_horario = 0
                consta_no_banco = 0
                item = 0
                ja_encontrou = 0

                while(1):

                    consulta = 0
                    id_valido = 0
                    acesso = 0
                    fora_do_horario = 0
                    consta_no_banco = 0
                    item = 0
                    ja_encontrou = 0

                    in1 = GPIO.input(A)
                    in2 = GPIO.input(B)

                    pm1 = in1
                    pm2 = in2


                    hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
                    horario_atual = time.strftime("%H:%M")
                    
                    try: 

                        tamanho = 0

                        dados = sock.recv(128)
                        tamanho += len(dados)
                        
            ##            print ("Dados recebidos",dados,"tamanho",tamanho) # Dados lidos no cartão de QR Code

                        if (tamanho >= 16 or tamanho <8): # Se o QR Code lido não tiver exatamente o mesmo tamanho não consulta o banco de dados

                            consulta = 0
                            dados = 0

            ##                print ("colocou consulta = 0")

                        if (tamanho >= 8 and tamanho < 16): # Se tiver o tamanho exato, prossegue
                                            
                            dados = int(dados) # Elimina as '' e o \r
                            dados = str(dados)

                            print("Dados lidos pelo leitor " + dados)

                            dados = dados[3:] # elimina os 3 primeiros digitos da string dados

                            
                            print("Dados editados",dados,type(dados))

                            dados = int(dados)

                            consulta = 1
                                
                            tabela = [601, 403, 820, 417, 217, 162, 684, 895, 797, 413, 577, 527, 921, 203, 565, 620, 369, 471, 316, 988, 387, 418, 643, 987, 297, 108, 396, 880, 436, 465, 899, 671, 422, 253, 765, 992, 259, 286, 932, 627, 474, 378, 894, 216, 594, 289, 258, 490, 647, 487, 409, 888, 221, 805, 535, 713, 363, 925, 964, 327, 618, 379, 739, 132, 205, 902, 335, 396, 407, 871, 867, 213, 982, 980, 252, 228, 881, 137, 138, 216, 825, 536, 681, 895, 921, 711, 375, 908, 429, 656, 304, 560, 988, 642, 965, 183, 629, 432, 360, 728, 801, 796, 716, 631, 495, 587, 917, 732, 275, 119, 558, 675, 672, 729, 612, 517, 962, 995, 668, 144, 513, 987, 109, 563, 177, 257, 975, 626, 575, 813, 377, 363, 484, 170, 284, 869, 726, 502, 841, 808, 219, 286, 670, 614]                         
                            tempo_validade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440]
             
                            if (1):

                                
                                for item in tabela:
                                         
                                    id_raiz = int(dados / item)  # divide o valor lido no QR por cada numero da tabela e consulta no banco

                                    # Dividiu o id recebido pelos dados da tabela "item" que resultou no id_raiz

            ##                        print("\n",id_raiz)
                                    
                                    try:  # Tenta conectar com o banco de dados

                                        signal.alarm(2)
                                        cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
                                        cursor = cnx.cursor()
                                        signal.alarm(0)
                                          
                                    except mysql.connector.Error as err:

                                        print("Opa, problema com o banco de dados",err)                                                                              
                                        print(err)

                                        arquivo = open("QR_Code.log", "a+") # Escreve o evento no registro de log
                                        arquivo.write("Data: " + data + " " + hs + " Evento: Erro de acesso ao Banco pelo QR Code " + err + "\n")
                                        arquivo.close()
                                                    
                                        time.sleep(0.1)
                                           
                                    
                                    try:                    

                                        query = ("SELECT ID FROM qrcode WHERE ID = %s")%id_raiz # procura na coluna ID um código = ao id_raiz
                                        cursor.execute(query)

                                        for i in cursor: # Se o cursor encontrar o item especificado, prossegue...
                                                                                                            
                                            id_valido = 1 # Encontrou o ID raiz
                                            consulta = 1 # Habilita a consulta de data e horario
                                            ja_encontrou = 1 # Depois de encontrar encerra a consulta do ID raiz
                                            
                                                               
                                    except Exception as e:
                                    
                                        print("Tipo de erro: " + str(e))
                                        break
                                        
                                    if ja_encontrou == 1:
                                        
                                        ja_encontrou = 0

                                        break
                            item = item
                                    
                    except Exception as e:

                        print("Não foi possivel ler os dados recebidos\n")
                        print("Tipo de erro: " + str(e))
                        
                    if consulta == 0:

                        print("\nQR Code em formato invalido")
                        print("Texto",dados,"\n")
                         
                        os.system("mpg123 /home/pi/mp3/206.mp3")#  Formato de QR Code inválido

                        arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de log
                        arquivo.write("Data: " + data + " " + hs + " Evento: Tentativa de uso de QR Code invalido\n")
                        arquivo.close()
                            
                        texto_recebido = ("")

                        time.sleep(3)


                    if consulta == 1 :

                        item = item

                        try:  # Tenta conectar com o banco de dados

                            signal.alarm(2)
                            cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
                            cursor = cnx.cursor()
                            signal.alarm(0)
                              
                        except mysql.connector.Error as err:
                                
                            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                      
                                print("Alguma coisa esta errada com o nome de usuario ou a senha!")

                                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                                arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: Usuario ou senha invalidos\n")
                                arquivo.close()

                            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                      
                                print("Esta base de dados não existe!")

                                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                                arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: A base de dados não existe\n")
                                arquivo.close()

                            else:
                                              
                                print(err)

                                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                                arquivo.write("Data: " + data + " " + hs + " Evento: Erro de acesso ao Banco pelo QR Code " + err + "\n")
                                arquivo.close()
                                            
                                time.sleep(0.1)
                                      
                                pass
                        

                        if id_valido == 1: # Se o cursor encontrou o ID correspondente prossegue...

                            hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
                            horario_atual = time.strftime("%H:%M")

                            # print("Este ID consta no banco",id_raiz)

                            consta_no_banco = 1

                            try:                    

                                # Primeiro ve se a data ainda não expirou e se o ID ja está liberado o horario
             
                                query = ("SELECT * FROM qrcode WHERE data_final >= CURDATE() AND ID = %s")%id_raiz # Verifica só id e data
                                cursor.execute(query)
                                      
                                for i in cursor: # Se encontrar o item especificado, divide as informações e salva nas variaveis

                                                         
                                    ID = i[0]
                                    nome = i[1]
                                    ap = i[2]
                                    bloco = i[3]
                                    cond = i[4]
                                    hora_inicio = i[5]
                                    hora_final = i[6]
                                    data_inicio = i[7]
                                    data_final = i[8]
                                    dias_semana = i[9]

                                    print("\nID",ID,"\nNome",nome,"valido de",data_inicio.strftime('%d/%m/%Y'),"até",data_final.strftime('%d/%m/%Y'),"das",hora_inicio,"as",hora_final,"hs","dias da semana",dias_semana)

                                    hora_i = str(hora_inicio)
                                    hora_f = str(hora_final)
                                    hs = str(hs)


                                    h_i = (hora_i.split(":")[0])
                                    m_i = (hora_i.split(":")[1])
                                    h_f = (hora_f.split(":")[0])
                                    m_f = (hora_f.split(":")[1])

                                    hi = int(h_i )  # Hora inicial como um inteiro para comparar com a hora atual
                                    mi = int(m_i)  # Minuto inicial como um inteiro para comparar com o minuto atual

                                    hf = int(h_f )  # Hora final como um inteiro para comparar com a hora atual
                                    mf = int(m_f)  # Minuto final como um inteiro para comparar com o minuto atual

                                    h = hs.split(":")[0] # Hora e minutos atuais do sistema
                                    m = hs.split(":")[1]
                                    h = int(h)
                                    m = int(m)

                                    consta_no_banco = 1

                                # Calculos para verificar a compatibilidade do código dinamico com o horario

                                    tabela = [601, 403, 820, 417, 217, 162, 684, 895, 797, 413, 577, 527, 921, 203, 565, 620, 369, 471, 316, 988, 387, 418, 643, 987, 297, 108, 396, 880, 436, 465, 899, 671, 422, 253, 765, 992, 259, 286, 932, 627, 474, 378, 894, 216, 594, 289, 258, 490, 647, 487, 409, 888, 221, 805, 535, 713, 363, 925, 964, 327, 618, 379, 739, 132, 205, 902, 335, 396, 407, 871, 867, 213, 982, 980, 252, 228, 881, 137, 138, 216, 825, 536, 681, 895, 921, 711, 375, 908, 429, 656, 304, 560, 988, 642, 965, 183, 629, 432, 360, 728, 801, 796, 716, 631, 495, 587, 917, 732, 275, 119, 558, 675, 672, 729, 612, 517, 962, 995, 668, 144, 513, 987, 109, 563, 177, 257, 975, 626, 575, 813, 377, 363, 484, 170, 284, 869, 726, 502, 841, 808, 219, 286, 670, 614]
                                    tempo_validade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440]
                                 
                                    minutos_equivalentes = (tempo_validade[tabela.index(item)])-10 # minutos equivalentes a mesma posição em que foi encointrado o multiplicador valido
                                    posicao_multiplicador = tabela.index(item)

                                    print("Posição do multiplicador valido",tabela.index(item))
                                    print("Minutos equivalente",minutos_equivalentes)

                                    
                                    confere_tabela = hora_inicio + timedelta(minutes = minutos_equivalentes) # Horario correspondente ao qr code usado

                                    print("\nQr correspondente as",confere_tabela)

                                    confere_tabela = str(confere_tabela)
                                    confere_tabela_hora = int(confere_tabela.split(":")[0])
                                    confere_tabela_minuto = int(confere_tabela.split(":")[1])
                                    confere_tabela_segundos = 00

            ##                        print("Horario correspondente",confere_tabela_hora, confere_tabela_minuto, confere_tabela_segundos)
                                                                                   
                                    now = datetime.now()

                                    horario_atual_hora = now.hour  # Estes valores são do tipo inteiro
                                    horario_atual_minuto = now.minute
                                    horario_atual_segundo = now.second

                                    print("Horario atual no CMM ",hs)

                                    if (hi > h): # se o horario inicial é menor do que a hora atual, ainda não foi liberado

                                        print("Ainda não liberado\n")

                                        os.system("mpg123 /home/pi/mp3/207.mp3")

                                        #acesso = 0
                                        fora_do_horario = 1
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                    # Aqui se compara o horario atual com o horario correspondente

                                    if confere_tabela_hora == horario_atual_hora :

                                        ja_mudou = 0

                                        #print ("A hora correspondente ao QR code lido é igual a hora atual")

                                        for i in range(1,11):

                                            if confere_tabela_minuto == horario_atual_minuto:

                                                print ("Qr Code dentro dos 10 minutos validos")

                                                ja_mudou = 1

                                                fora_do_horario = 0
                                                                                    
                                                break
                                            
                                            horario_atual_minuto = horario_atual_minuto - 1 # Verifica se esta dentro dos 10 minutos atuais

                                        if ja_mudou == 0 and fora_do_horario == 0:

                                            print("Este QRCode ja mudou")
                                            lb_log["text"] = "Este QRCode ja mudou"

                                            os.system("mpg123 /home/pi/mp3/212.mp3")

                                            fora_do_horario = 1

                                            #time.sleep(1)
                                    if confere_tabela_hora != horario_atual_hora and fora_do_horario == 0:

                                        lb_log["text"] = "Este QR Code está fora do horario permitido"
                                        os.system("mpg123 /home/pi/mp3/207.mp3")
                                        print("Fora do horario permitido")

                                        fora_do_horario = 1

                                                               
                                    
                                    if (hf < h): # se o horario final é menor que o horario atual já expirou

                                        print("Horario do QR Code já Expirou\n")

                                        os.system("mpg123 /home/pi/mp3/208.mp3")

                                        time.sleep(3)

                                        #acesso = 0
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                    if (hf > h and fora_do_horario == 0): # se o horario final for maior que o horario atual, QR Code ainda válido

                                        #print("Dentro do horario permitido\n")

        ##                                os.system("mpg123 /home/pi/mp3/188.mp3")

                                        
                                        arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                        arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                        arquivo.close()
                        
                                        acesso = 1
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                         
                                        
                                    if (hf == h): # se a hora final for a mesma da hora atual, verifica os minutos

                                        if mf == 0:

                                            print("Expirou a alguns minutos\n")

                                            os.system("mpg123 /home/pi/mp3/211.mp3")

                                            time.sleep(3)

                                            #acesso = 0
                                            consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                        if (mf != 0 and mf >= m): # se minutos finais forem menores do que minutos atuais, ainda válido

                                            print("Dentro do horario, faltando",mf - m, "minutos")

        ##                                    os.system("mpg123 /home/pi/mp3/188.mp3") # Acesso por QR Code
                                            

                                            arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                            arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                            arquivo.close()
                            
                                            acesso = 1
                                            consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                                                          

                                        if (mf != 0 and mf <= m):
                                    
                                             print("Expirou\n")

                                             os.system("mpg123 /home/pi/mp3/208.mp3") # Expirou
                                             

                                             time.sleep(3)

                                             #acesso = 0
                                             consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                             

                                if acesso == 1: #Verifica o dia da semana que esta autorizado

                                    dia = time.strftime("%A")
                                    print ("Hoje é",dia)

                                    liberado = "0"

                                    b = str(dias_semana)

                                    print("b = ",b)

                                    seg = b[0]
                                    ter = b[1]
                                    qua = b[2]
                                    qui = b[3]
                                    sex = b[4]
                                    sab = b[5]
                                    dom = b[6]

                                    if dia == "Monday":
                                            
                                        if seg == "1":        
                                            liberado = "1"
                                            
                                        else:        
                                            print("QR Côldi não autorizado as segundas-feiras")
                                            liberado = "0"
                                                

                                    if dia == "Tuesday":
                                        
                                        if ter == "1":        
                                            liberado = "1"
                                            
                                        else:        
                                            print("QR Côldi não autorizado as terças-feiras")
                                            liberado = "0" 

                                    if dia == "Wednesday":
                                            
                                        if qua == "1":        
                                            liberado = "1"
                                            
                                        else:        
                                            print("QR Côldi não autorizado as quartas-feiras")
                                            liberado = "0"

                                    if dia == "Thursday":
                                            
                                        if qui == "1":        
                                            liberado = "1"
                                            
                                        else:        
                                            print("QR Côldi não autorizado as quintas-feiras")
                                            liberado = "0"                                            

                                    if dia == "Friday":
                                        
                                        if sex == "1":        
                                            liberado = "1"
                                            
                                        else:        
                                            print("QR Côldi não autorizado as sextas-feiras")
                                            liberado = "0"                                                
                                                            
                                            
                                    if dia == "Saturday":
                                        
                                        if sab == "1":        
                                            liberado = "1"
                                            
                                        else:        
                                            print("QR Côldi não autorizado aos sábados")
                                            liberado = "0"
                                            

                                    if dia == "Sunday":
                                            
                                        if dom == "1":        
                                            liberado = "1"
                                            
                                        else:
                                            
                                            print("QR Côldi não autorizado aos domingos")
                                            liberado = "0"
                                           

                                    if liberado == "1": # Intertravamento

                                        in1 = GPIO.input(A)
                                        in2 = GPIO.input(B)

                                        pm1 = in1
                                        pm2 = in2

                                        print("PM1",pm1)
                                        print("PM2",pm2)

                                        inter = intertravamento.get() ###  intertravamento ###

                                        if inter == 0:

                                             if (qr == "1" or qr == "2"):

                                                 print ("Acesso por qr code Portão 1")
                                            
                                                 rele_qr = rele_qrcode(ip_qrcode) # Aciona o rele correspondente ao qrcode informado no argumento
                                                
                                                 os.system("mpg123 /home/pi/mp3/188.mp3")

                                             if (qr == "3" or qr == "4"):

                                                 print ("Acesso por qr code Portão 2")
                                            
                                                 rele_qr = rele_qrcode(ip_qrcode) # Aciona o rele correspondente ao qrcode informado no argumento
                                                
                                                 os.system("mpg123 /home/pi/mp3/188.mp3")
                                        

                                        if (qr == "1" and pm2 == 1 and inter == 1): # leitor 1 e portao 2 aberto

                                            print("O portão 2 ainda esta aberto")

                                            os.system("mpg123 /home/pi/mp3/049.mp3") # Aguarde o fechamento
                                            liberado = 0

                                        if (qr == "2" and pm2 == 1 and inter == 1): # leitor 2 e portao 2 aberto

                                            print("O portão 2 ainda esta aberto")

                                            os.system("mpg123 /home/pi/mp3/049.mp3") # Aguarde o fechamento
                                            liberado = 0

                                        if (qr == "1" and pm2 == 0 and inter == 1): # Portao 2 fechado

                                            print ("Acesso por qr code Portão 1")
                                            
                                            rele_qr = rele_qrcode(ip_qrcode) # Aciona o rele correspondente ao qrcode informado no argumento
                                            
                                            os.system("mpg123 /home/pi/mp3/188.mp3")
                                            
                                            lb_log["text"] = ("QR CODE "+ "Nome " + nome + " " + data + " " +  " Cliente " + cond +" Ap " + ap + " bloco " + bloco + "  " + hs + " Leitor QR " + qr )

                                        if (qr == "2" and pm2 == 0 and inter == 1): # Portao 2 fechado

                                            print ("Acesso por qr code Portão 1")
                                            
                                            rele_qr = rele_qrcode(ip_qrcode) # Aciona o rele correspondente ao qrcode informado no argumento
                                            
                                            os.system("mpg123 /home/pi/mp3/188.mp3")
                                            
                                            lb_log["text"] = ("QR CODE "+ "Nome " + nome + " " + data + " " +  " Cliente " + cond +" Ap " + ap + " bloco " + bloco + "  " + hs + " Leitor QR " + qr )
                                            

                                        if (qr == "3" and pm1 == 1 and inter == 1): # leitor 3 e portao 2 aberto

                                            print("O portão 1 ainda esta aberto")

                                            os.system("mpg123 /home/pi/mp3/049.mp3") # Aguarde o fechamento
                                            liberado = 0

                                        if (qr == "4" and pm1 == 1 and inter == 1): # leitor 4e portao 2 aberto

                                            print("O portão 1 ainda esta aberto")

                                            os.system("mpg123 /home/pi/mp3/049.mp3") # Aguarde o fechamento
                                            liberado = 0


                                        if (qr == "3" and pm1 == 0 and inter == 1): # Portao 2 fechado

                                            print ("Acesso por qr code Portão 2")
                                            
                                            rele_qr = rele_qrcode(ip_qrcode) # Aciona o rele correspondente ao qrcode informado no argumento
                                            
                                            os.system("mpg123 /home/pi/mp3/188.mp3")
                                            
                                            lb_log["text"] = ("QR CODE "+ "Nome " + nome + " " + data + " " +  " Cliente " + cond +" Ap " + ap + " bloco " + bloco + "  " + hs + " Leitor QR " + qr )
                                            
                                        if (qr == "4" and pm1 == 0 and inter == 1): # Portao 2 fechado

                                            print ("Acesso por qr code Portão 2")
                                            
                                            rele_qr = rele_qrcode(ip_qrcode) # Aciona o rele correspondente ao qrcode informado no argumento
                                            
                                            os.system("mpg123 /home/pi/mp3/188.mp3")
                                            
                                            lb_log["text"] = ("QR CODE "+ "Nome " + nome + " " + data + " " +  " Cliente " + cond +" Ap " + ap + " bloco " + bloco + "  " + hs + " Leitor QR " + qr )
                                            
                                        

                                if acesso == 0 and consta_no_banco == 1 and fora_do_horario == 0:

                                    print("QR Code com data expirada")

                                    os.system("mpg123 /home/pi/mp3/210.mp3")# Data Expirada
                                    print("data expirada")

                                    consulta = 1


                                # Aqui será necessário verificar se ja passou do horario final e avisar
                            
                            except Exception as e:
                                
                                print("Tipo de erro: " + str(e))

                            
                        if id_valido == 0:

                            print("QR Code não cadastrado")

                            try:

                                os.system("mpg123 /home/pi/mp3/189.mp3") # QR Code não cadastrado

                            except Exception as err:

                                print(err)

                        fora_do_horario = 0

            except Exception as err:

                print("opa",err)

                lb_log["text"] = ("Não conseguiu conectar com " + ip_qrcode)
                messagebox.showerror("Erro","Não foi possivel conectar a este endereço, verifique os dados inseridos e tente novamente!")

            
            
        def rele_qrcode(ip): 
            
            print ("IP do QR Code a ser acionado " + ip)

            class Rele_qr:
                   
                    def __init__(self,ip):

                            self.ip = ip
                            self.porta = 5000 # Porta acionamento rele do qr code

                    def liga(self):

                        try:

                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                            server_address = (self.ip,self.porta) # Endereço do Leitor de QR Code 
                            
                            print('Conectou com QR CODE {} port {}'.format(*server_address),"\n")

                            comando = ("ron\r\n")

                            sock.connect(server_address)              
                            sock.send(str.encode(comando))

                            sock.close()

                            print("ligou rele QR Code")
                          
                        except Exception as err:

                              print("Erro no envio para o QR Code",err)

                    def desliga(self):

                        try:

                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                            server_address = (self.ip,self.porta) # Endereço do Leitor de QR Code 
                            
                            print('Conectou com QR CODE {} port {}'.format(*server_address),"\n")

                            comando = ("rof\r\n")

                            sock.connect(server_address)              
                            sock.send(str.encode(comando))

                            sock.close()

                            print("Desligou rele QR Code")
                          
                        except Exception as err:

                              print("Erro no envio para o QR Code",err)


                    def pulso(self):

                        def __init__(self):

                            Rele_qr.__init__(self)

                        try:

                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                            server_address = (self.ip,self.porta) # Endereço do Leitor de QR Code 
                            
                            print("Conectou com QR CODE\n",self.ip,self.porta)

                            comando = ("p2\r\n") # pulsa por 2 segundos

                            sock.connect(server_address)              
                            sock.send(str.encode(comando))

                            sock.close()

                            print("Pulsou rele QR Code")
                            lb_log["text"] = ("Pulsou rele do Leitor " + ip)
                          
                        except Exception as err:

                              print("Erro no envio para o QR Code",err)
                              
            rele = Rele_qr(ip)
            rele.pulso()

        def registra_endereco(qr): # Somente registar o novo endereço de qr code e registar 1 em cadastrar

            if qr == "1":

        ##        print("Reconheceu registro qr1")
                

                adress1 = ed1.get()

                arquivo = open("adress_qr1.txt", "w") # Escreve o evento no registro de log
                arquivo.write(adress1 + "\n")
                arquivo.close()

                lb_log["text"] = "Tentando conectar ao IP " + adress1 + " QR CODE 1..."

                arquivo = open("conectar_qr1.txt", "w") # Escreve o evento no registro de log
                arquivo.write("1")
                arquivo.close()

                
                
            if qr == "2":

        ##        print("Reconheceu registro qr2")
                        
                adress2 = ed2.get()

                
                arquivo = open("adress_qr2.txt", "w") # Escreve o evento no registro de log
                arquivo.write(adress2 + "\n")
                arquivo.close()

                lb_log["text"] = "Tentando conectar ao IP " + adress2 + " QR CODE 2..."

                arquivo = open("conectar_qr2.txt", "w") # Escreve o evento no registro de log
                arquivo.write("1")
                arquivo.close()

            if qr == "3":

        ##        print("Reconheceu registro qr3")

                adress3 = ed3.get()

                arquivo = open("adress_qr3.txt", "w") # Escreve o evento no registro de log
                arquivo.write(adress3 + "\n")
                arquivo.close()

                lb_log["text"] = "Tentando conectar ao IP " + adress3 + " QR CODE 3..."

                arquivo = open("conectar_qr3.txt", "w") # Escreve o evento no registro de log
                arquivo.write("1")
                arquivo.close()

            if qr == "4":

        ##        print("Reconheceu registro qr4")

                adress4 = ed4.get()

                arquivo = open("adress_qr4.txt", "w") # Escreve o evento no registro de log
                arquivo.write(adress4 + "\n")
                arquivo.close()

                lb_log["text"] = "Tentando conectar ao IP " + adress4 + " QR CODE 4..."

                arquivo = open("conectar_qr4.txt", "w") # Escreve o evento no registro de log
                arquivo.write("1")
                arquivo.close()

        def conecta():

            while(1):

                txt1 = open("conectar_qr1.txt", "r") # Escreve o evento no registro de log
                
                for line1 in txt1:
                    line1 = line1
                    
                txt1.close()

                if line1 == "0": # Não exixte um novo endereço para conectar

                    pass
                    

                if line1 == "1":
                    
                    
                    txt1 = open("conectar_qr1.txt", "w") # Escreve o evento no registro de log
                    txt1.write("0")
                    txt1.close()

        ##            print ("Chamando a rotina conectar...")

                    
                    qr1 = threading.Thread(target = leitor_qrcode, args = ("1"))
                    qr1.start()

        ##            ed1.delete(0, 'end') # Limpa os dados do entry
                                
                    
        ##############################################################################################
                    
                txt2 = open("conectar_qr2.txt", "r") # Escreve o evento no registro de log
                
                for line2 in txt2:
                    line2 = line2
                    
                txt2.close()

                if line2 == "0": # Não exixte um novo endereço para conectar

                    pass
                    

                if line2 == "1":            
                   
                    txt2 = open("conectar_qr2.txt", "w") # Escreve o evento no registro de log
                    txt2.write("0")
                    txt2.close()
                    
                    qr2 = threading.Thread(target = leitor_qrcode, args = ("2"))
                    qr2.start()

        ##            ed2.delete(0, 'end') # Limpa os dados do entry

        ##############################################################################################
                    
                txt3 = open("conectar_qr3.txt", "r") # Escreve o evento no registro de log
                
                for line3 in txt3:
                    line3 = line3
                    
                txt2.close()

                if line3 == "0": # Não exixte um novo endereço para conectar

                    pass
                    

                if line3 == "1":            
                    
                    txt3 = open("conectar_qr3.txt", "w") # Escreve o evento no registro de log
                    txt3.write("0")
                    txt3.close()
                    
                    qr3 = threading.Thread(target = leitor_qrcode, args = ("3"))
                    qr3.start()

        ##            ed3.delete(0, 'end') # Limpa os dados do entry

        ##############################################################################################
                    
                txt4 = open("conectar_qr4.txt", "r") # Escreve o evento no registro de log
                
                for line4 in txt4:
                    line4 = line4
                    
                txt4.close()

                if line4 == "0": # Não exixte um novo endereço para conectar

                    pass
                    

                if line4 == "1":            
                   
                    txt4 = open("conectar_qr4.txt", "w") # Escreve o evento no registro de log
                    txt4.write("0")
                    txt4.close()
                    
                    qr4 = threading.Thread(target = leitor_qrcode, args = ("4"))
                    qr4.start()

        ##            ed4.delete(0, 'end') # Limpa os dados do entry


                time.sleep(2)
            

        def rele(qr):

            txt = open("adress_qr" + qr + ".txt", "r") # Escreve o evento no registro de log
                
            adress = txt.readline()
                        
            txt.close()

            print(adress, type(adress))

        ##    messagebox.askyesno("Acionamento","Quer enviar o comando de acionamento para o equipamento?")
            
            
            rele_qr = rele_qrcode(adress) # Aciona o rele correspondente ao qrcode informado



        # Faz a leitura dos IPs que vão se conectar automaticamente

        txt = open("conecta_automatico_qr1.txt", "r") 
        t1 = txt.readline()
        txt.close()
        txt = open("conecta_automatico_qr2.txt", "r") 
        t2 = txt.readline()
        txt.close()
        txt = open("conecta_automatico_qr3.txt", "r") 
        t3 = txt.readline()
        txt.close()
        txt = open("conecta_automatico_qr4.txt", "r") 
        t4 = txt.readline()
        txt.close()

        print("\nAutomático 1",t1)
        print("\nAutomático 2",t2)
        print("\nAutomático 3",t3)
        print("\nAutomático 4",t4)



        ################################## Threadds ########################################

        con = threading.Thread(target = conecta)
        rg = threading.Thread(target = registra_endereco, args = ("0"))

        con.start()
        rg.start()

        ################################### Classes  #######################################

        janela_qrcode = Tk() # instancia a classe da janela_qrcode
        janela_qrcode.eval('tk::PlaceWindow %s center' % janela_qrcode.winfo_toplevel()) # Posiciona as mensagebox no centro

        janela_qrcode.title("QR Code CEINTEL") # Titulo da janela_qrcode

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()

        def bt_click():

            print("clicou")
            lb["text"] = "Pulsou rele do QR Code"
            rele_qr.pulso()

        def feed_back(mensagem):

            lb["text"] = mensagem

        def conecta():    
            
            lb_conexao["text"] = ed.get()

        def conecta_automatico(ch):

            ch1 = CheckVar1.get() # Armazena o valor do checkbox
            ch2 = CheckVar2.get()
            ch3 = CheckVar3.get()
            ch4 = CheckVar4.get()

            c1 = ed1.get()
            c2 = ed2.get()
            c3 = ed3.get()
            c4 = ed4.get()

            est1 = ed1["state"]
            est2 = ed2["state"]
            est3 = ed3["state"]
            est4 = ed4["state"]
            
        ##    print("Campo 1",c1)
        ##    print("Campo 2",c2)
        ##    print("Campo 3",c3)
        ##    print("Campo 4",c4)

        #  Registra no arquivo de texto 0 ou o ip caso seja selecionado o check Automático
               

            if (ch == "1" and ch1 == 0 and est1 == "disabled"):

                f = open("conecta_automatico_qr1.txt","w")
                f.write("")
                f.close()

                nm1 = bt["text"]
                messagebox.showinfo("Conexão automatica","Removido o IP " + nm1 + "\n   do reinicio automático")
                
            if (ch == "1" and ch1 == 1 and c1 != ""): # Se checkbox 1 estiver selecionado e houver algo no entry e este não estiver desabilitado registra

                try:

                    messagebox.showinfo("Conexão automatica","O sistema irá se conectar\nautomaticamente a este IP\nquando for reiniciado!")

                    print("Atualizou o inicio automatico do Leitor 1 com o IP " + c1)
                    lb_log["text"] = ("Atualizou o inicio automatico do Leitor 1 com o IP " + c1)
                    f = open("conecta_automatico_qr1.txt","w")
                    f.write(c1)
                    f.close()
                    
                except Exception as err:

                    print("Erro",err)
                    

            if (ch == "2" and ch2 == 0 and est2 == "disabled"):

                f = open("conecta_automatico_qr2.txt","w")
                f.write("")
                f.close()

                nm2 = bt2["text"]
                messagebox.showinfo("Conexão automatica","Removido o IP " + nm2 + "\n   do reinicio automático")
                
            if (ch == "2" and ch2 == 1 and c2 != ""): # Se checkbox 2 estiver selecionado e houver algo no entry e este não estiver desabilitado registra

                try:

                    messagebox.showinfo("Conexão automatica","O sistema irá se conectar\nautomaticamente a este IP\nquando for reiniciado!")

                    print("Atualizou o inicio automatico do Leitor 2 com o IP " + c2)
                    lb_log["text"] = ("Atualizou o inicio automatico do Leitor 2 com o IP " + c2)
                    f = open("conecta_automatico_qr2.txt","w")
                    f.write(c2)
                    f.close()
                    
                except Exception as err:

                    print("Erro",err)
                    

            if (ch == "3" and ch3 == 0 and est3 == "disabled"):

                f = open("conecta_automatico_qr3.txt","w")
                f.write("")
                f.close()

                nm3 = bt4["text"]
                messagebox.showinfo("Conexão automatica","Removido o IP " + nm3 + "\n   do reinicio automático")
                
            if (ch == "3" and ch3 == 1 and c3 != ""): # Se checkbox 3 estiver selecionado e houver algo no entry e este não estiver desabilitado registra

                try:

                    messagebox.showinfo("Conexão automatica","O sistema irá se conectar\nautomaticamente a este IP\nquando for reiniciado!")

                    print("Atualizou o inicio automatico do Leitor 3 com o IP " + c3)
                    lb_log["text"] = ("Atualizou o inicio automatico do Leitor 3 com o IP " + c3)
                    f = open("conecta_automatico_qr3.txt","w")
                    f.write(c3)
                    f.close()
                    
                except Exception as err:

                    print("Erro",err)


            if (ch == "4" and ch4 == 0 and est4 == "disabled"):

                f = open("conecta_automatico_qr4.txt","w")
                f.write("")
                f.close()

                nm4 = bt6["text"]
                messagebox.showinfo("Conexão automatica","Removido o IP " + nm4 + "\n   do reinicio automático")
                
            if (ch == "4" and ch4 == 1 and c4 != ""): # Se checkbox 4 estiver selecionado e houver algo no entry e este não estiver desabilitado registra

                try:

                    messagebox.showinfo("Conexão automatica","O sistema irá se conectar\nautomaticamente a este IP\nquando for reiniciado!")

                    print("Atualizou o inicio automatico do Leitor 4 com o IP " + c4)
                    lb_log["text"] = ("Atualizou o inicio automatico do Leitor 1 com o IP " + c4)
                    f = open("conecta_automatico_qr4.txt","w")
                    f.write(c4)
                    f.close()
                    
                except Exception as err:

                    print("Erro",err)


        def atualiza():

            while(1):
                
                hora = time.strftime('%H:%M')
                data = time.strftime('%d/%m/%y')

                lb_relogio = Label (janela_qrcode, text = (data + "  " + hora + " hs") ,bg="black",fg="white",font = font2)
                lb_relogio.place(x=400,y=280)

                time.sleep(30)

        def aviso_intertravamento():

            i = intertravamento.get()

            if i == 1:

                messagebox.showinfo("Intertravamento","Com intertravamento acionado\n           os leitores 1 e 2 \n são correspondentes ao portão 1 \n           e os leitores 3 e 4 \n são correspondentes ao portão 2")

        def Help():
            text = Text(janela_qrcode)
            text.pack();
            text.insert('insert', 'Ao clicar no botão da\n'
                                  'respectiva cor, o fundo da tela\n'
                                  'aparecerá na cor escolhida.')

        
        menubar = Menu(janela_qrcode)
        janela_qrcode.config(menu=menubar)
        janela_qrcode.title('QR CODE CEINTEL')
        janela_qrcode.geometry('150x150')
            
        filemenu = Menu(menubar,tearoff=0)
        filemenu1 = Menu(menubar,tearoff=0)

        menubar.add_cascade(label='Sistema', menu=filemenu) # Associa o menu a barra
        menubar.add_cascade(label='Sobre', menu=filemenu1)

        filemenu.add_command(label='Reiniciar', )  ##filemenu.add_command(label='Salvar como...',accelerator="Teste+A", command=Save)
        filemenu.add_separator() # Adiciona um separador entre as opções

        filemenu.add_command(label='Sair', command=on_closing)
        filemenu1.add_command(label='Ajuda', command=Help)

        def porta_aberta():

            if var1.get() == 1:

                lb_log["text"] = "Iniciou o programa 'Notificação de porta aberta'"

                pa = threading.Thread(target = run_porta_aberta) # Envia feedback de temperatura do sistema e tensão de baterias a cada minuto
                pa.start()

        ##    if var1.get() == 0:

        ##        lb_log["text"] = "Encerrando o programa 'Notificação de porta aberta'"
        ##        os.system("killall python3 /home/pi/run_porta_aberta.py")

        def run_porta_aberta():

            cont = 1
            cont2 = 1
            contador1 = 0
            contador2 = 0
                
            while(var1.get() == 1):
                        
                in1 = GPIO.input(A)
                in2 = GPIO.input(B)

                pm1 = in1
                pm2 = in2

                if pm1 == 1 and cont == 1: # Abriu porta 1

                    contador1 = contador1 + 1
            ##        print("contador1",contador1)

                    if contador1 == 10:

                        try:

            ##                print('A porta esta aberta a mais de 10 segundos\n')
                            lb_log["text"] = 'A porta 1 esta aberta a mais de 10 segundos'
                            os.system("mpg123 001.mp3")
                            cont = 2
                            
                        except Exception as err:

                            print(err0)

                if pm1 == 1 and cont == 2: 

                    contador1 = contador1 + 1
            ##        print("contador1",contador1)

                    if contador1 == 20:

            ##            print('A porta esta aberta a mais de 20 segundos\n')
                        lb_log["text"] = 'A porta 1 esta aberta a mais de 20 segundos'
                        os.system("mpg123 002.mp3")
                        cont = 3

                if pm1 == 1 and cont == 3: 

                    contador1 = contador1 + 1
            ##        print("contador1",contador1)

                    if contador1 == 30:

            ##            print('A porta esta aberta a mais de 30 segundos\n')
                        lb_log["text"] = 'A porta 1 esta aberta a mais de 30 segundos'
                        os.system("mpg123 003.mp3")
                        cont = 1
                        contador1 = 0

                if pm1 == 0:
                    
                     contador1 = 0
                     cont = 1

                if pm2 == 1 and cont2 == 1: # Abriu porta 1

                    contador2 = contador2 + 1
            ##        print("contador2",contador2)

                    if contador2 == 10:

                        try:

            ##                print('A porta esta aberta a mais de 10 segundos\n')
                            lb_log["text"] = 'A porta 2 esta aberta a mais de 10 segundos'
                            os.system("mpg123 001.mp3")
                            cont2 = 2
                            
                        except Exception as err:

                            print(err)

                if pm2 == 1 and cont2 == 2: 

                    contador2 = contador2 + 1
            ##        print("contador2",contador2)

                    if contador2 == 20:

            ##            print('A porta esta aberta a mais de 20 segundos\n')
                        lb_log["text"] = 'A porta 2 esta aberta a mais de 20 segundos'
                        os.system("mpg123 002.mp3")
                        cont2 = 3

                if pm2 == 1 and cont2 == 3: 

                    contador2 = contador2 + 1
            ##        print("contador2",contador2)

                    if contador2 == 30:

            ##            print('A porta esta aberta a mais de 30 segundos\n')
                        lb_log["text"] = 'A porta 2 esta aberta a mais de 30 segundos'
                        os.system("mpg123 003.mp3")
                        cont2 = 1
                        contador2 = 0

                if pm2 == 0:
                    
                     contador2 = 0
                     cont2 = 1
                     
                             
                time.sleep(1)
                
            
            lb_log["text"] = "Encerrando o programa 'Notificação de porta aberta'"


        ############################# Background ######################################

        imagem = PhotoImage(file='/home/pi/img/QR_CMM.png')
        label = Label(janela_qrcode, image = imagem)
        label.pack()

            
        #######################################  LABELS  #######################################

        lb1 = Label(janela_qrcode, text="IP Leitor 1",bg="black",fg="white")# adiciona um label
        lb1.place(x=10, y=10) # Metodo de posicionamento do tipo place (x,y)

        lb3 = Label(janela_qrcode, text="IP Leitor 2",bg="black",fg="white")# adiciona um label
        lb3.place(x=10, y=60) # Metodo de posicionamento do tipo place (x,y)

        lb4 = Label(janela_qrcode, text="IP Leitor 3",bg="#4682B4",fg="white")# adiciona um label
        lb4.place(x=10, y=110) # Metodo de posicionamento do tipo place (x,y)

        lb5 = Label(janela_qrcode, text="IP Leitor 4",bg="#4682B4",fg="white")# adiciona um label
        lb5.place(x=10, y=160) # Metodo de posicionamento do tipo place (x,y)

        font2 = ("Helvetica", 8,"italic")

        lb_log = Label (janela_qrcode, text = "Feed back do programa",width=79,font = font2,padx=5,relief = RIDGE, bd=1, anchor = W) # GROOVE, RIDGE, FLAT
        lb_log.place(x=9, y=304)
        ######################################## BOTOES  ############################################

        bt = Button(janela_qrcode, width = 7, text = "Conectar", command = registra_endereco) # inclusão de button
        bt["command"] = partial(registra_endereco, "1")
        bt.place(x=150, y=30) # posição dentro da janela_qrcode

        bt1 = Button(janela_qrcode, width=7, text = "Pulso rele", command = rele) # inclusão de button
        bt1["command"] = partial(rele, "1")
        bt1.place(x=250, y=30) # posição dentro da janela_qrcode

        bt2 = Button(janela_qrcode, width = 7, text = "Conectar", command = registra_endereco) # inclusão de button
        bt2["command"] = partial(registra_endereco, "2")
        bt2.place(x=150, y=80) # posição dentro da janela_qrcode

        bt3 = Button(janela_qrcode, width=7, text = "Pulso rele", command = rele) # inclusão de button
        bt3["command"] = partial(rele, "2")
        bt3.place(x=250, y=80) # posição dentro da janela_qrcode

        bt4 = Button(janela_qrcode, width = 7, text = "Conectar", command = registra_endereco) # inclusão de button
        bt4["command"] = partial(registra_endereco, "3")
        bt4.place(x=150, y=130) # posição dentro da janela_qrcode

        bt5 = Button(janela_qrcode, width=7, text = "Pulso rele", command = rele) # inclusão de button
        bt5["command"] = partial(rele, "3")
        bt5.place(x=250, y=130) # posição dentro da janela_qrcode

        bt6 = Button(janela_qrcode, width = 7, text = "Conectar", command = registra_endereco) # inclusão de button
        bt6["command"] = partial(registra_endereco, "4")
        bt6.place(x=150, y=180) # posição dentro da janela_qrcode

        bt7 = Button(janela_qrcode, width=7, text = "Pulso rele", command = rele) # inclusão de button
        bt7["command"] = partial(rele, "4")
        bt7.place(x=250, y=180) # posição dentro da janela_qrcode

        bt1.config(state=DISABLED) # Iniciam desabilitados (habilitam depois de conectado)
        bt3.config(state=DISABLED)
        bt5.config(state=DISABLED)
        bt7.config(state=DISABLED)

        #############################  Check Button   ##################################

        var1 = IntVar()

        ch1 = Checkbutton(janela_qrcode, text="Porta aberta", state=ACTIVE, variable = var1,command=porta_aberta)
        ch1.place(x=360, y=225)

        ##lb_programa1 = Label (janela_qrcode, text = "Porta aberta")
        ##lb_programa1.place(x=390, y=215)

        check1 = Checkbutton(janela_qrcode, text="Automático",state=ACTIVE,variable = CheckVar1,command = conecta_automatico)
        check1["command"] = partial(conecta_automatico,"1")
        check1.place(x=360,y=35)


        check2 = Checkbutton(janela_qrcode, text="Automático",state=ACTIVE,variable = CheckVar2,command = conecta_automatico)
        check2["command"] = partial(conecta_automatico,"2")
        check2.place(x=360,y=85)

        check3 = Checkbutton(janela_qrcode, text="Automático",state=ACTIVE,variable = CheckVar3,command = conecta_automatico)
        check3["command"] = partial(conecta_automatico,"3")
        check3.place(x=360,y=135)

        check4 = Checkbutton(janela_qrcode, text="Automático",state=ACTIVE,variable = CheckVar4,command = conecta_automatico)
        check4["command"] = partial(conecta_automatico,"4")
        check4.place(x=360,y=185)

        intertravamento = IntVar()
        check_intertravamento = Checkbutton(janela_qrcode, text="Intertravamento",command = aviso_intertravamento, state=ACTIVE,variable = intertravamento)
        check_intertravamento.place(x=360,y=250)
        ######################################## ENTRADA TEXTO ######################################

        ed1 = Entry(janela_qrcode, width=15)
        ed1.place(x=10, y= 35)

        ed2 = Entry(janela_qrcode, width=15)
        ed2.place(x=10, y= 85)

        ed3 = Entry(janela_qrcode, width=15)
        ed3.place(x=10, y= 135)

        ed4 = Entry(janela_qrcode, width=15)
        ed4.place(x=10, y= 185)

        ####################################### Threads  #######################################

        a = threading.Thread(target = atualiza)
        a.start()

        ############################## Configuraçoes janela_qrcode ############################


        def conecta_ao_iniciar():

            try:

                txt = open("conecta_automatico_qr1.txt", "r")         
                a = txt.readline()                
                txt.close()

            except:

                txt = open("conecta_automatico_qr1.txt", "w") 
                txt.write("")
                txt.close()
                a = ""

            try:

                txt = open("conecta_automatico_qr2.txt", "r")         
                b = txt.readline()                
                txt.close()

            except:

                txt = open("conecta_automatico_qr2.txt", "w") 
                txt.write("")
                txt.close()
                b = ""

            try:        

                txt = open("conecta_automatico_qr3.txt", "r")         
                c = txt.readline()                
                txt.close()

            except:

                txt = open("conecta_automatico_qr3.txt", "w") 
                txt.write("")
                txt.close()
                c = ""

            try:
                
                txt = open("conecta_automatico_qr4.txt", "r")         
                d = txt.readline()                
                txt.close()

            except:

                txt = open("conecta_automatico_qr4.txt", "w") 
                txt.write("")
                txt.close()
                d = ""

        ##    print("a,b,c,d",a,b,c,d)    

            if a != "":
                               
                txt = open("adress_qr1.txt", "w")         
                txt.write(a)
                txt.close()

                txt = open("conectar_qr1.txt", "w")         
                txt.write("1")
                txt.close()

            if b != "":

                txt = open("adress_qr2.txt", "w")         
                txt.write(b)
                txt.close()

                txt = open("conectar_qr2.txt", "w")         
                txt.write("1")
                txt.close()

            if c != "":

                txt = open("adress_qr3.txt", "w")         
                txt.write(c)
                txt.close()

                txt = open("conectar_qr3.txt", "w")         
                txt.write("1")
                txt.close()

            if d != "":

                txt = open("adress_qr4.txt", "w")         
                txt.write(d)
                txt.close()

                txt = open("conectar_qr4.txt", "w")         
                txt.write("1")
                txt.close()

        conecta_ao_iniciar()

        janela_qrcode.protocol("WM_DELETE_WINDOW", on_closing)

        janela_qrcode.maxsize(width=500, height=355) # Limita o tamaho maximo
        janela_qrcode.minsize(width=500, height=355) # Limita o tamanho minimo

        ##janela_qrcode.attributes('-fullscreen',True) # Maximiza a tela sem deixar nenhum acesso alem da janela_qrcode

        lb_log["text"] = ("CMM QR Code v1.4 2019 PORTARIA REMOTA")

        janela_qrcode.geometry("500x355+750+50") # Tamanho e posição da janela_qrcode (Largura,Altura,Left,Top) 
        janela_qrcode.mainloop()
        
qr = Qrcode()
qr.Start()
