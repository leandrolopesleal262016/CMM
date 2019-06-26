#!/usr/bin/python3
#-*- coding: utf-8 -*-

from gtts import gTTS  # importamos o modúlo gTTS
import pygame
import time
import datetime
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import smbus  # para funcionamento dos módulos com interface I2C 
import spidev
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import serial # Para comunicação serial com arduino
import mysql.connector # faz a comunicação com o mysql no python 3.6
import socket
import threading # Modulo superior Para executar as threads
import _thread as thread # Modulo basico para executar as threads
import signal # Bibloteca para uso do time out
import sys
import smtplib  # Permite enviar emails
import json

##os.system("speak.set_voice('brazil')") # Inicia o TTS nativo do python
    

##host = '172.20.1.5'  # Host servidor  Moni
##port = 4010          # Porta máquina receptora testes


##host_servidor = '0.0.0.0'  # Host servidor SEA (PHP e moni como clientes)
##port_servidor = 5510

##port_gerenciador = 5511# Servidor para receber dados do gerenciador
##
##port_reset = 5512 # Porta para reset


mutex = thread.allocate_lock() # trava a thread para ser executada sózinha

GPIO.setwarnings(False) # desabilita mensagens de aviso

GPIO.setmode(GPIO.BCM) # Modo de endereço dos pinos BCM

#ser = serial.Serial("/dev/ttyS0", 9600) #Configura a serial e a velocidade de transmissao

spi =spidev.SpiDev() # Parametros da configuração da comunicação SPI (Entrada Portas Analógcas)
spi.open(0,0)
spi.max_speed_hz=1000000

pygame.init() # Inicia o pygame para uso do módulo de voz

bus = smbus.SMBus(1) # Parametros de configuração do módulo MCP23017 - SAIDA DOS RELÊS via I2C
MCP23017 = 0X20 # Endereço do módulo de saidas dos reles (A0 - A2)
MCP3008 = 0
bus.write_byte_data(MCP23017,0x00,0x00) #defina todo GPA como saida 0x00 
bus.write_byte_data(MCP23017,0x01,0x00) #defina todo GPB como saida 0x01 

# Define os pinos que serão entradas:

GPIO.setup(17,GPIO.IN)#GPIO0
GPIO.setup(18,GPIO.IN)#GPIO1
GPIO.setup(27,GPIO.IN)#GPIO2 
GPIO.setup(22,GPIO.IN)#GPIO3
GPIO.setup(23,GPIO.IN)#gpio4
GPIO.setup(24,GPIO.IN)#GPIO5
GPIO.setup(25,GPIO.IN)#GPIO6
GPIO.setup(4,GPIO.IN) #GPIO7 (in 8)


saidaA = 0b00000000  # Zera variaveis do port A e porta B
saidaB = 0b00000000

bus.write_byte_data(MCP23017,0x015,0) # Zera saidas do port B 
bus.write_byte_data(MCP23017,0x014,0) # Coloca todas as saidas do PORT A em 0

saidaB = saidaB + 0b00001000 # liga LED VERMELHO saida GPB3
bus.write_byte_data(MCP23017,0x015,saidaB)


def timeout(signum, frame):

    #raise Exception ("Excedeu o tempo esperado!\n")
    print ("Excedeu o tempo esperado",signum)
    return

signal.signal(signal.SIGALRM, timeout)

host_v = '172.20.6.154'  # modulo de voz
port_v = 5555          # Porta máquina receptora testes

try:
    
    signal.alarm(7)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect ((host_v,port_v))

    command = ("Teste do modulo de voz.")  # Envia abriu portão da eclusa para a central de monitormento
    s.send(str.encode(command))

    s.close()

    signal.alarm(0)

except Exception as err:
    
    print("Não conseguiu enviar o evento",err)
     

#################################################### LEITOR QR CODE  ##################################################################
host = '0.0.0.0'
port = 5400
    
def qr_code():
        
    host = '0.0.0.0'
    port = 5400

    time.sleep(1.5)

    print("Servidor:",host,"porta:",port)
    
    while(1):        
              
        def setupServer():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # "AF_NET" trabalharemos com protocolo ipv4, .SOCK_STREAM USAREMOS TCP
            try:
                s.bind((host, port))
            except socket.error as msg:
                print ("Erro servidor qrcode cameras ip",msg)
            return s

        def setupConnection():
            s.listen(5)
            conn, address = s.accept()
            print ("Conectado com: " + address[0] + ":" + str(address[1]), "\n")
            return conn


        def dataTransfer(conn):  # Loop de transferencia e recepção de dados

            print("Programa leitor de qrcode cameras ip")

            consulta = 0
            id_valido = 0
            acesso = 0
            fora_do_horario = 0
            consta_no_banco = 0
            item = 0
            ja_encontrou = 0
            
            while True:
            
                dados = conn.recv(1024)  # Recebe o dado
                dados = dados.decode('utf-8')
                dados = str(dados)

                d = dados.replace("b'","")
                dados = d.replace("'","")                
                
                print(dados)
                                              
                ###################### Programa QR Code #########################################

                print("Entrou na lógica de leitura do qrcode")
            
                hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
                horario_atual = time.strftime("%H:%M")
                
                try: 

                    tamanho = 0
                    tamanho += len(dados)
                    
        ##            print ("Dados recebidos",dados,"tamanho",tamanho) # Dados lidos no cartão de QR Code

                    if (tamanho >= 16 or tamanho <8): # Se o QR Code lido não tiver exatamente o mesmo tamanho não consulta o banco de dados

                        consulta = 0
                        dados = 0

        ##                print ("colocou consulta = 0")

                    if (tamanho >= 8 and tamanho < 16): # Se tiver o tamanho exato, prossegue
                                        
                        dados = int(dados) # Elimina as '' e o \r
                        dados = str(dados)

                        print("Dados lidos pelo leitor " + dados + " " + hs)

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
                                
                                try:                    

                                    query = ("SELECT ID FROM qrcode WHERE ID = %s")%id_raiz # procura na coluna ID um código = ao id_raiz
                                    cursor.execute(query)

                                    for i in cursor: # Se o cursor encontrar o item especificado, prossegue...
                                                                                                        
                                        id_valido = 1 # Encontrou o ID raiz
                                        consulta = 1 # Habilita a consulta de data e horario
                                        ja_encontrou = 1 # Depois de encontrar encerra a consulta do ID raiz
                                        
                                                           
                                except Exception as e:
                                
                                    print("Erro id raiz: " + str(e))
                                    
                                if ja_encontrou == 1:
                                    
                                    ja_encontrou = 0

                                    break
                        item = item
                                
                except Exception as e:

                    print("Não foi possivel ler os dados recebidos ")

                    print("Tipo de erro: " + str(e))
                    
                if consulta == 0:

                    print("\nQR Code em formato invalido")
                    print("Texto",dados,"\n")

                    pygame.mixer.music.load('/home/pi//home/pi/mp3/206.mp3') # Formato de QR Code inválido
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)

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

                                #print("Aqui o item vale",item)
                            
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

                                    pygame.mixer.music.load('/home/pi/mp3/207.mp3') # Fora do horario
                                    pygame.mixer.music.play()
                                    while pygame.mixer.music.get_busy():
                                        time.sleep(0.1)

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

                                        pygame.mixer.music.load('/home/pi/mp3/212.mp3') # Este QRCode ja mudou 
                                        pygame.mixer.music.play()
                                        while pygame.mixer.music.get_busy():
                                            time.sleep(0.1)

                                        fora_do_horario = 1

                                        #time.sleep(1)
                                if confere_tabela_hora != horario_atual_hora and fora_do_horario == 0:

                                    host = '172.20.6.154'  # Host servidor  Moni
                                    port = 5555          # Porta máquina receptora testes

                                    try:
                                        
                                        signal.alarm(2)
                                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        s.connect ((host,port))

                                        command = ("Este Qr Code está fora do horário")  # Envia abriu portão da eclusa para a central de monitormento
                                        s.send(str.encode(command))

                                        reply = s.recv(1024)
                                        print(reply.decode('utf-8'))

                                        s.close()

                                        signal.alarm(0)
                                        
                                                    
                                    except Exception as err:
                                        
                                        print("Não conseguiu enviar o evento Abriu portão da Eclusa",err)
                                         

                                    fora_do_horario = 1

                                                           
                                
                                if (hf < h): # se o horario final é menor que o horario atual já expirou

                                    print("Horario do QR Code já Expirou\n")

                                    pygame.mixer.music.load('/home/pi/mp3/208.mp3') # Expirou
                                    pygame.mixer.music.play()
                                    while pygame.mixer.music.get_busy():
                                        time.sleep(0.1)

                                    time.sleep(3)

                                    #acesso = 0
                                    consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                if (hf > h and fora_do_horario == 0): # se o horario final for maior que o horario atual, QR Code ainda válido

                                    #print("Dentro do horario permitido\n")

                                    pygame.mixer.music.load('/home/pi/mp3/188.mp3') # Acesso por QR Code
                                    pygame.mixer.music.play()

                                    
                                    arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                    arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                    arquivo.close()
                    
                                    acesso = 1
                                    consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                     
                                    
                                if (hf == h): # se a hora final for a mesma da hora atual, verifica os minutos

                                    if mf == 0:

                                        print("Expirou a alguns minutos\n")

                                        pygame.mixer.music.load('/home/pi/mp3/211.mp3') # Expirou
                                        pygame.mixer.music.play()
                                        while pygame.mixer.music.get_busy():
                                            time.sleep(0.1)

                                        time.sleep(3)

                                        #acesso = 0
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                    if (mf != 0 and mf >= m): # se minutos finais forem menores do que minutos atuais, ainda válido

                                        print("Dentro do horario, faltando",mf - m, "minutos")

                                        pygame.mixer.music.load('/home/pi/mp3/188.mp3') # Acesso por QR Code
                                        pygame.mixer.music.play()

                                        arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                        arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                        arquivo.close()
                        
                                        acesso = 1
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                                                      

                                    if (mf != 0 and mf <= m):
                                
                                         print("Expirou\n")

                                         pygame.mixer.music.load('/home/pi/mp3/208.mp3') # Expirou
                                         pygame.mixer.music.play()
                                         while pygame.mixer.music.get_busy():
                                            time.sleep(0.1)

                                         time.sleep(3)

                                         #acesso = 0
                                         consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                         

                            if acesso == 1:

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
                                        msg = "QR Côldi não autorizado as segundas-feiras"
                                        
                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"
                                            

                                if dia == "Tuesday":
                                    
                                    if ter == "1":        
                                        liberado = "1"
                                        
                                    else:        
                                        msg = "QR Côldi não autorizado as terças-feiras"

                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"
                                        
                                        

                                if dia == "Wednesday":
                                        
                                    if qua == "1":        
                                        liberado = "1"
                                        
                                    else:        
                                        msg = "QR Côldi não autorizado as quartas-feiras"

                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"
                                        

                                if dia == "Thursday":
                                        
                                    if qui == "1":        
                                        liberado = "1"
                                        
                                    else:        
                                        msg = "QR Côldi não autorizado as quintas-feiras"

                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"

                                if dia == "Friday":
                                    
                                    if sex == "1":        
                                        liberado = "1"
                                        
                                    else:        
                                        msg = "QR Côldi não autorizado as sextas-feiras"

                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"
                                        

                                if dia == "Saturday":
                                    
                                    if sab == "1":        
                                        liberado = "1"
                                        
                                    else:        
                                        msg = "QR Côldi não autorizado aos sábados"


                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"
                                        

                                if dia == "Sunday":
                                        
                                    if dom == "1":        
                                        liberado = "1"
                                        
                                    else:
                                        
                                        msg = "QR Côldi não autorizado aos domingos"


                                        host = '172.20.6.154'  # modulo de voz
                                        port = 5555          # Porta máquina receptora testes

                                        try:
                                            
                                            signal.alarm(3)
                                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            s.connect ((host,port))

                                            command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                            s.send(str.encode(command))

                                            reply = s.recv(1024)
                                            print(reply.decode('utf-8'))

                                            s.close()

                                            signal.alarm(0)
                                            
                                                        
                                        except Exception as err:
                                            
                                            print("Não conseguiu enviar o evento",err)
                                            liberado = "0"

                                envia_evento = 0            

                                if liberado == "1":

                                    print("Acesso liberado")

                                    rele.pulsa(1)

        ##                            print("Vai tentar enviar pro narrador")                            
        ##                                                    
        ##                            try:
        ##                                
        ##                                signal.alarm(7)
        ##                                
        ##                                host = '172.20.6.154'  # modulo de voz
        ##                                port = 5555          # Porta máquina receptora testes
        ##                                
        ##                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ##                                s.connect ((host,port))
        ##
        ##                                command = ("ok")  
        ##                                s.send(str.encode(command))
        ##
        ##                                s.close()
        ##
        ##                                signal.alarm(0)
        ##
        ##                                liberado = 0
        ##                                acesso = 0
        ##                                envia_evento = 0
        ##            
        ##                            except Exception as err:
        ##                                
        ##                                print("Não conseguiu enviar o evento",err)
        ##                                return 

                            if acesso == 0 and consta_no_banco == 1 and fora_do_horario == 0:

                                msg = "QR Code com data expirada"

                                host = '172.20.6.154'  # modulo de voz
                                port = 5555          # Porta máquina receptora testes

                                try:
                                    
                                    signal.alarm(3)
                                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    s.connect ((host,port))

                                    command = (msg)  # Envia abriu portão da eclusa para a central de monitormento
                                    s.send(str.encode(command))

        ##                            reply = s.recv(1024)
        ##                            print(reply.decode('utf-8'))

                                    s.close()

                                    signal.alarm(0)

                                                                
                                                
                                except Exception as err:
                                    
                                    print("Não conseguiu enviar o evento",err)

                            consulta = 1


                            # Aqui será necessário verificar se ja passou do horario final e avisar
                        
                        except Exception as e:
                            
                            print("Tipo de erro: " + str(e))

                        
                    if id_valido == 0:

                        print("QR Code não cadastrado")

                        host = '172.20.6.154'  # modulo de voz
                        port = 5555          # Porta máquina receptora testes

                        try:
                            
                            signal.alarm(3)
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect ((host,port))

                            command = ("Qrcode não cadastrado")  # Envia abriu portão da eclusa para a central de monitormento
                            s.send(str.encode(command))
                            
        ##                    reply = s.recv(1024)
        ##                    print(reply.decode('utf-8'))

                            s.close()

                            signal.alarm(0)
                            
                                        
                        except Exception as err:
                            
                            print("Não conseguiu enviar o evento Abriu portão da Eclusa",err)
                             

                    
                    fora_do_horario = 0

                reply = "ok"                                
                conn.sendall(str.encode(reply))  # Envia o reply de volta para o cliente  
                    
                conn.close()
                #################################################################################

##                    reply = "ok"                                
##                    conn.sendall(str.encode(reply))  # Envia o reply de volta para o cliente  
##                    
##                    conn.close()
                
##            conn.close()
            
        s = setupServer()

        while True:
          
          print ("\nEscutando a porta",port, "\n")
          
          try:

              conn = setupConnection()
              dataTransfer(conn) #,saidaA,saidaB,hs)
              print("Oiee")
             
          except:
            
              print("Encerrou conexão")



hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
hora = time.strftime('%H:%M')
h = int(time.strftime('%H'))
dia_mes = time.strftime("%d")
y = time.strftime("%Y")
m = time.strftime("%m")
data = time.strftime('%d/%m/%y')


out_A = 0b00000000
out_B = 0b00000000

########################################### CLASSES  #############################################

class Temperatura:
    
    def get_cpu_temp(self): # retorna o valor da temperatura da cpu do CLP
        tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
        cpu_temp = tempFile.read()
        tempFile.close()
        t = float(cpu_temp)/1000
        return round(t)

class Email:

    def enviar(self,mensagem):

        signal.alarm(10)

        try:

            self.mensagem = mensagem

            nome = os.popen('hostname').readline()
            ip = os.popen('hostname -I').readline()
            
            msg_e = ("Subject:CLP %s IP %s \r\n\r\n %s" %(nome,ip,mensagem))
            msn = str(msg_e)
            m = msn.replace("'","")
            s = m.replace (",","")
            n = s.replace ("(","")
            f = n.replace (")","")
            g = f.replace("\n)","")

            #print(g)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("leandrolopesleal26@gmail.com", "novajesuscr332")
            msg = ("%s" %g)
            
            server.sendmail("leandrolopesleal26@gmail.com", "leandrolopesleal26@gmail.com", msg)
            server.quit()

            print ("Email enviado!")

        except:

            print("Não consegui enviar o email")
            
        signal.alarm(0)

class Rele:

    def __init__(self,out_A,out_B):

        self.out_A = out_A
        self.out_B = out_B
        self.zera_A = 0b00000000
        self.zera_B = 0b00000000
        self.rele1 =  0b00000001
        self.rele2 =  0b00000010
        self.rele3 =  0b00000100
        self.rele4 =  0b00001000
        self.rele5 =  0b00010000
        self.rele6 =  0b00100000
        self.rele7 =  0b01000000
        self.rele8 =  0b10000000
        self.rele9 =  0b00000001
        self.rele10 = 0b10000010
        self.rele11 = 0b00000100
        self.rele12 = 0b00001000
        self.rele13 = 0b00010000
                   

    def liga(self,out):

        
        if out == 1 : self.out_A = self.out_A + self.rele1
        if out == 2 : self.out_A = self.out_A + self.rele2
        if out == 3 : self.out_A = self.out_A + self.rele3
        if out == 4 : self.out_A = self.out_A + self.rele4
        if out == 5 : self.out_A = self.out_A + self.rele5
        if out == 6 : self.out_A = self.out_A + self.rele6
        if out == 7 : self.out_A = self.out_A + self.rele7
        if out == 8 : self.out_A = self.out_A + self.rele8
        if out == 9 : self.out_B = self.out_B + self.rele9
        if out == 10: self.out_B = self.out_B + self.rele10
        if out == 11: self.out_B = self.out_B + self.rele11
        if out == 12: self.out_B = self.out_B + self.rele12
        if out == 13: self.out_B = self.out_B + self.rele13

        if out >= 1 and out <=8:

            bus.write_byte_data(MCP23017,0x014,self.out_A)
            print("ligou", out)
            
            return self.out_A

        if out >= 9 and out <= 13:
            
            bus.write_byte_data(MCP23017,0x015,self.out_B)
            print("ligou", out)
            return out_B
        
        
    def desliga(self,out):

 
        if out == 1 : self.out_A = self.out_A - self.rele1
        if out == 2 : self.out_A = self.out_A - self.rele2
        if out == 3 : self.out_A = self.out_A - self.rele3
        if out == 4 : self.out_A = self.out_A - self.rele4
        if out == 5 : self.out_A = self.out_A - self.rele5
        if out == 6 : self.out_A = self.out_A - self.rele6
        if out == 7 : self.out_A = self.out_A - self.rele7
        if out == 8 : self.out_A = self.out_A - self.rele8
        if out == 9 : self.out_B = self.out_B - self.rele9
        if out == 10: self.out_B = self.out_B - self.rele10
        if out == 11: self.out_B = self.out_B - self.rele11
        if out == 12: self.out_B = self.out_B - self.rele12
        if out == 13: self.out_B = self.out_B - self.rele13

        if out >= 1 and out <=8:
            
            bus.write_byte_data(MCP23017,0x014,self.out_A)
            print("desligou",out)
            
            return self.out_A
            

        if out >= 9 and out <= 13:

            bus.write_byte_data(MCP23017,0x015,self.out_B)
            print("desligou",out)
            
            return out_B
               
        
    def pulsa(self,out):

        if out == 1 : rele = self.rele1
        if out == 2 : rele = self.rele2
        if out == 3 : rele = self.rele3
        if out == 4 : rele = self.rele4
        if out == 5 : rele = self.rele5
        if out == 6 : rele = self.rele6
        if out == 7 : rele = self.rele7
        if out == 8 : rele = self.rele8
        if out == 9 : rele = self.rele9
        if out == 10 : rele = self.rele10
        if out == 11 : rele = self.rele11
        if out == 12 : rele = self.rele12
        if out == 13 : rele = self.rele13
        if out > 13 :
          
          print ("Não há nenhum rele",out)
          return

        if out >= 1 and out <=8:
            
            print("\npulso rele",out,"aguarde...")
            self.out_A = self.out_A + rele
            bus.write_byte_data(MCP23017,0x014,self.out_A)
            time.sleep(2)
            self.out_A = self.out_A - rele
            bus.write_byte_data(MCP23017,0x014,self.out_A)
            
            return self.out_A
            

        if out >= 9 and out <= 13:

            print("\npulso rele",out,"aguarde...")
            self.out_B = self.out_B + rele
            bus.write_byte_data(MCP23017,0x015,self.out_B)
            time.sleep(2)
            self.out_B = self.out_B - rele
            bus.write_byte_data(MCP23017,0x015,self.out_B)
            
            return out_B

        if out > 13:

            print("Na há nenhum rele",out)

        
            
    def zera_tudo(self):
 
        self.out_A = self.zera_A
        self.out_B = self.zera_B
        bus.write_byte_data(MCP23017,0x014,self.out_A)
        bus.write_byte_data(MCP23017,0x015,self.out_B)
        print("desligou tudo")

    def zera_portA(self):
 
        self.out_A = self.zera_A
        bus.write_byte_data(MCP23017,0x014,self.out_A)
        print("desligou portA")

    def zera_portB(self):
 
        self.out_B = self.zera_B
        bus.write_byte_data(MCP23017,0x015,self.out_B)
        print("desligou portB")

    def teste(self):
        
        rele.pulsa(1)
        time.sleep(0.5)
        rele.pulsa(2)
        time.sleep(0.5)
        rele.pulsa(3)
        time.sleep(0.5)
        rele.pulsa(4)
        time.sleep(0.5)
        rele.pulsa(5)
        time.sleep(0.5)
        rele.pulsa(6)
        time.sleep(0.5)
        rele.pulsa(7)
        time.sleep(0.5)
        rele.pulsa(8)
        time.sleep(0.5)
        rele.pulsa(9)
        time.sleep(0.5)
        rele.pulsa(10)
        time.sleep(0.5)
        rele.pulsa(11)
        time.sleep(0.5)
        rele.pulsa(12)
        time.sleep(0.5)
        rele.pulsa(13)
        time.sleep(0.5)

   
rele = Rele(out_A,out_B) # inicia a classe rele com port A e B em 0
#evento = Evento()  # Inicia a classe Evento
email = Email()  # Inicia a classe email
temp = Temperatura() # Inicia a classe para obter temperatura da CPU

#-------------------------------- Acionamento dos Reles ------------------------------------------

#rele.teste()    # Aciona as 13 saidas com pulso de 1 segundo

#rele.liga(1)    # Liga rele 1 (podendo ser de 1 a 13)

#rele.desliga(1) # Desliga rele 1

#rele.pulso(3)   # Pulsa o rele 3 por 2 segundos (podendo ser de 1 a 13)

#rele.zera_tudo()# Zera todas as saidas, ou só o port A ou B (rele.zera_portA,rele.zera_portB)

# obter temperatura  temp.get_cpu_temp()

#---------------------------------------------------------------------------------------------------


#********************************* Envio de Email  ************************************************

#email.enviar("Esta e a minha mensagem ") # Não usar nenhum caracter especial na mensagem

#**************************************************************************************************

#$$$$$$$$$$$$$$$$$$$$$$$$$ Envio de evento contact_id para o Moni $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#evento.enviar_contact_id('E','130','001') # Evento ou Restauração / Evento / Setor

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


######################################################### Start das Threads ####################################################

##s = threading.Thread(target = servidor_php, args=(saidaA,saidaB,hs,data)) # Inicia o servidor endereço 172.20.6.14 porta 5510
##s.start()
qr = threading.Thread(target = qr_code) # Ativa a conexão com o qr code
qr.start()

###################################################################################################################################

php = 0
AP01 = 0
cont = 0

      
while(True):     

    if (cont == 0):

      vrg = 0
                
      print ("Programa Automático em execução\n")
      
      bus.write_byte_data(MCP23017,0x014,0b00000000) # Zera as saídas do Port A (inicia reles de 1 -8 desligados)
      bus.write_byte_data(MCP23017,0x015,0b00000000)  # Zera as saídas do Port B (inicia reles 9,10 desligados, saidas 11,12,13 (transistors) desligados
      cont = 1
           
      pygame.mixer.music.load('/home/pi/mp3/200.mp3') # Sistema carregado
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy():
        time.sleep(0.1)

      time.sleep(1)

      

    time.sleep(1)
