##!/usr/bin/env python3
# coding=UTF-8

from gtts import gTTS  # importamos o modúlo gTTS
import time
import wiringpi
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import smbus  # para funcionamento dos módulos com interface I2C 
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import serial # Para comunicação serial com arduino
import mysql.connector # faz a comunicação com o mysql no python 3.6
import socket
import signal # Bibloteca para uso do time out
import sys
import smtplib  # Permite enviar emails
from urllib import request #para efetuar a requisicao
import json #para ler o JSON
from banco import Banco # Classe para Iterações com banco de dados CMM


print('''

Iniciando bibliotecas...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Shield BRAVAS
 
  ''')

#############################################  Configuracoes  ###################################################################################

hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
h = int(time.strftime('%H'))
data = time.strftime('%d/%m/%y')

os.system("amixer set PCM 100%") # ajusta o volume master

bus = smbus.SMBus(1) # esta linha especifica qual dispositivo I2C a ser usado. 1 significa que o dispositivo I2C está localizado em / dev / I2C-1

out_A = 0b11111111 # Todos reles em 0

wiringpi.wiringPiSetup() # configura os 3 PCF8574 da placa de expansao

wiringpi.pcf8574Setup(100,0x25) # Definindo os pinos do rele como saida
for x in range (0, 9):                  

        wiringpi.pinMode(100+x,1)        
        wiringpi.digitalWrite(100+x,1)  # Inicia com o rele desligado


wiringpi.pcf8574Setup(200,0x26) # Definindo os pinos de saida digital como saida
for x in range (0, 9):

        wiringpi.pinMode(200+x,1)
        wiringpi.digitalWrite(200+x,1) 


wiringpi.pcf8574Setup(300, 0x27); # # Definindo os pinos de entrada digital como entradas

def timeout(signum, frame):

    print("Excedeu o tempo esperado",signum)
    return
    
signal.signal(signal.SIGALRM, timeout) # Inicia o modulo para funcionamento dos time out
socket.setdefaulttimeout(2) # limite de 2 segundos para enviar o socket

  
########################################## Envio de Eventos para o MONI ######################################################

class Evento:
    
    
    def __init__(self,cliente):        

        self.host = '172.20.1.5'  # Host servidor  Moni
        self.port = 4010          # Porta máquina receptora

        self.protocolo = "7000 18"  # Protocolo
        self.cliente = cliente  # Cliete
        self.zona = "00" # Partição
        self.finalizador = "" # Finalizador
      
    def enviar(self,cond,evento,setor): # cond = condição, se E (evento) ou R (restauração)
               
        self.cond = cond
        self.evento = evento
        self.setor = setor
        protocolo = self.protocolo
        cliente = self.cliente
        zona = self.zona
        finalizador = self.finalizador
        
        tupla = (protocolo,cliente,cond,evento,zona,setor,finalizador) # Monta a string para enviar

        contact_texto = str(tupla)
        
        a = (contact_texto.split ("'")[1])
        b = (contact_texto.split ("'")[3])
        c = (contact_texto.split ("'")[5])
        d = (contact_texto.split ("'")[7])
        e = (contact_texto.split ("'")[9])
        f = (contact_texto.split ("'")[11])
        g = ""
       
        t = (a,b,c,d,e,f,g)
        
        evento =''.join(t) # Junta as partes dixando nulo os espaços

                
        try:
            socket.setdefaulttimeout(2)
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect ((self.host,self.port))

            command = (evento)  # Envia evento
            s.send(str.encode(command))

            reply = s.recv(1024)
            print(reply.decode('utf-8'))

            s.close()
                        
            print("Evento enviado ",evento)

            return
                
        except Exception as err:  # Caso o evento que chegou for igual ao ultimo recebido ignora

            print(err)

            arquivo = open("/home/pi/CMM/buffer_eventos.txt", "a+") # Escreve o evento no registro de log
            arquivo.write( evento + "\n")
            arquivo.close()
            
            return
            

############################################### Classe para Acionamento de rele  #############################################

class Rele:  # Inicia a classe para acionamento dos reles  (liga / desliga / pulsa)
    
    def __init__(self):

        self.out_A = 0b11111111
        
        self.rele1 =  0b11111110
        self.rele2 =  0b11111101
        self.rele3 =  0b11111011
        self.rele4 =  0b11110111
        self.rele5 =  0b11101111
        self.rele6 =  0b11011111
        self.rele7 =  0b10111111
        self.rele8 =  0b01111111

        self.rele9  =  0b11111110
        self.rele10 =  0b11111101
        self.rele11 =  0b11111011
        self.rele12 =  0b11110111
        self.rele13 =  0b11101111
        self.rele14 =  0b11011111
        self.rele15 =  0b10111111
        self.rele16 =  0b01111111

        self.banco = Banco()

        self.banco.atualiza("status","out1","0")
        self.banco.atualiza("status","out2","0")
        self.banco.atualiza("status","out3","0")
        self.banco.atualiza("status","out4","0")
        self.banco.atualiza("status","out5","0")
        self.banco.atualiza("status","out6","0")
        self.banco.atualiza("status","out7","0")
        self.banco.atualiza("status","out8","0")
        self.banco.atualiza("status","out9","0")
        self.banco.atualiza("status","out10","0")
        self.banco.atualiza("status","out11","0")
        self.banco.atualiza("status","out12","0")
        self.banco.atualiza("status","out13","0")
        self.banco.atualiza("status","out14","0")
        self.banco.atualiza("status","out15","0")
        self.banco.atualiza("status","out16","0")
        

 
    def liga(self,out):

        if out == 1 : self.out_A = 100
        if out == 2 : self.out_A = 101
        if out == 3 : self.out_A = 102
        if out == 4 : self.out_A = 103
        if out == 5 : self.out_A = 104
        if out == 6 : self.out_A = 105
        if out == 7 : self.out_A = 106
        if out == 8 : self.out_A = 107
        
        if out == 9  : self.out_A = 200
        if out == 10 : self.out_A = 201
        if out == 11 : self.out_A = 202
        if out == 12 : self.out_A = 203
        if out == 13 : self.out_A = 204
        if out == 14 : self.out_A = 205
        if out == 15 : self.out_A = 206
        if out == 16 : self.out_A = 207


        if out >= 1 and out <=16: # Saidas dos reles
            
            wiringpi.digitalWrite(self.out_A, 0) 
            sys.stdout.write("on" + str(out) + "\n")

            if out == 1:

                self.banco.atualiza("status","out1","1")

            if out == 2:

                self.banco.atualiza("status","out2","1")

            if out == 3:

                self.banco.atualiza("status","out3","1")

            if out == 4:

                self.banco.atualiza("status","out4","1")

            if out == 5:

                self.banco.atualiza("status","out5","1")
                
            if out == 6:

                self.banco.atualiza("status","out6","1")

            if out == 7:

                self.banco.atualiza("status","out7","1")

            if out == 8:

                self.banco.atualiza("status","out8","1")

            if out == 9:

                self.banco.atualiza("status","out9","1")

            if out == 10:

                self.banco.atualiza("status","out10","1")

            if out == 11:

                self.banco.atualiza("status","out11","1")

            if out == 12:

                self.banco.atualiza("status","out12","1")

            if out == 13:

                self.banco.atualiza("status","out13","1")

            if out == 14:

                self.banco.atualiza("status","out14","1")

            if out == 15:

                self.banco.atualiza("status","out15","1")

            if out == 16:

                self.banco.atualiza("status","out16","1")
            
   
    def desliga(self,out):

 
        if out == 1 : self.out_A = 100
        if out == 2 : self.out_A = 101
        if out == 3 : self.out_A = 102
        if out == 4 : self.out_A = 103
        if out == 5 : self.out_A = 104
        if out == 6 : self.out_A = 105
        if out == 7 : self.out_A = 106
        if out == 8 : self.out_A = 107

        if out == 9  : self.out_A = 200
        if out == 10 : self.out_A = 201
        if out == 11 : self.out_A = 202
        if out == 12 : self.out_A = 203
        if out == 13 : self.out_A = 204
        if out == 14 : self.out_A = 205
        if out == 15 : self.out_A = 206
        if out == 16 : self.out_A = 207

        if out >= 1 and out <=16: # Saidas dos reles
            
            wiringpi.digitalWrite(self.out_A, 1)
            sys.stdout.write("off"+ str(out) + "\n")

            if out == 1:

                self.banco.atualiza("status","out1","0")

            if out == 2:

                self.banco.atualiza("status","out2","0")

            if out == 3:

                self.banco.atualiza("status","out3","0")

            if out == 4:

                self.banco.atualiza("status","out4","0")

            if out == 5:

                self.banco.atualiza("status","out5","0")

            if out == 6:

                self.banco.atualiza("status","out6","0")

            if out == 7:

                self.banco.atualiza("status","out7","0")

            if out == 8:

                self.banco.atualiza("status","out8","0")

            if out == 9:

                self.banco.atualiza("status","out9","0")

            if out == 10:

                self.banco.atualiza("status","out10","0")

            if out == 11:

                self.banco.atualiza("status","out11","0")

            if out == 12:

                self.banco.atualiza("status","out12","0")

            if out == 13:

                self.banco.atualiza("status","out13","0")

            if out == 14:

                self.banco.atualiza("status","out14","0")
                
            if out == 15:

                self.banco.atualiza("status","out15","0")

            if out == 16:

                self.banco.atualiza("status","out16","0")
            
     
    def pulso(self,out,tempo):

        def __init__(self):

            Rele.__init__(self) # Inicia o construtor da classe Rele para ser usado aqui
            self.out = out
            self.tempo = out

        rele.liga(out)
        time.sleep(tempo)
        rele.desliga(out)

rele = Rele()

############################## Classe para acionamento do rele do leitor de QR CODE  ########################################

class Rele_qr:
           
            def __init__(self,ip,porta):

                    self.ip = ip
                    self.porta = porta   

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

                    comando = ("p2\r\n") # pulsa rele por 2 segundos

                    sock.connect(server_address)              
                    sock.send(str.encode(comando))

                    sock.close()

                    print("Pulsou rele QR Code")
                    
                                      
                except Exception as err:

                      print("Erro no envio para o QR Code",err)

####################################### LEITOR IP Wiegand (Fabricante 3SR Automação)  #######################################

class Wiegand:
    
    def __init__(self):
                       
            Rele.__init__(self) # Inicia o construtor da classe Rele para ser usado aqui

    def leitor_ip(self,ip,porta):

            
            self.ip = ip
            self.porta = porta
            
            try:
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_address = (ip, porta) # Endereço do QR Code ex.'172.20.2.134'
                sock.connect(server_address)

                print('\nConectado com Leitor IP {} port {}'.format(*server_address),"\n")
                
            except Exception as err:

                ip = str(ip)
                porta = str(porta)

                print("Não conectou com o Leitor wiegand IP " + ip )
           
            else:
            
                while(1):

                        hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
                        horario_atual = time.strftime("%H:%M")

                        try: 

                            dados = sock.recv(128)
                            tamanho = len(dados)

                            print("Dados recebidos",dados)

                        except Exception as err:

                            print("Não conseguiu ler dados wiegand",err)

                        time.sleep(0.2)

            time.sleep(0.1)

################################################# LEITOR QR CODE  ############################################################

class Qrcode:

    def __init__(self):
                       
            Rele.__init__(self) # Inicia o construtor da classe Rele para ser usado aqui

    def leitor(self,ip,porta):

            self.ip = ip
            self.porta = porta
                
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            server_address = (ip, porta) # Endereço do QR Code ex.'172.20.2.134'
            
            time.sleep(0.1)
            
            print('\nConectado com Leitor QR CODE {} port {}'.format(*server_address),"\n")
            sock.connect(server_address)

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

                hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
                horario_atual = time.strftime("%H:%M")

                # Tabela para sincronização com o aplicativo CONDFY para verificar a compatibilidade do código dinamico com o horario

                tabela = [601, 403, 820, 417, 217, 162, 684, 895, 797, 413, 577, 527, 921, 203, 565, 620, 369, 471, 316, 988, 387, 418, 643, 987, 297, 108, 396, 880, 436, 465, 899, 671, 422, 253, 765, 992, 259, 286, 932, 627, 474, 378, 894, 216, 594, 289, 258, 490, 647, 487, 409, 888, 221, 805, 535, 713, 363, 925, 964, 327]
                tempo_validade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
               
                try: 

                    tamanho = 0

                    dados = sock.recv(128)
                    tamanho += len(dados)
                    
        ##            print ("Dados recebidos",dados,"tamanho",tamanho) # Dados lidos no cartão de QR Code

                    if (tamanho >= 16 or tamanho <8): # Se o QR Code lido não tiver exatamente o mesmo tamanho não consulta o banco de dados

                        consulta = 0
                        dados = 0

                    if (tamanho >= 8 and tamanho < 16): # Se tiver o tamanho exato, prossegue
                                        
                        dados = int(dados) # Elimina as '' e o \r
                        dados = str(dados)

                        dados = dados[3:] # elimina os 3 primeiros digitos da string dados
                        
                        print("Dados editados",dados,type(dados))

                        dados = int(dados)

                        consulta = 1
                        

                        if (1):

                            
                            for item in tabela:
                                     
                                id_raiz = int(dados / item)  # divide o valor lido no QR por cada numero da tabela e consulta no banco

                                # Dividiu o id recebido pelos dados da tabela "item" que resultou no id_raiz

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
                                
                                    print("Tipo de erro: " + str(e))
                                    
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

                    os.system('mpg123 mp3/206.mp3') # Formato de QR Code inválido
                    
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

                                # Mostar os dados do QR Code

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
                                                     
                                now = datetime.now()

                                horario_atual_hora = now.hour  # Estes valores são do tipo inteiro
                                horario_atual_minuto = now.minute
                                horario_atual_segundo = now.second

                                print("Horario atual no CMM ",hs)

                                if (hi > h): # se o horario inicial é menor do que a hora atual, ainda não foi liberado

                                    print("Ainda não liberado\n")

                                    os.system('mpg123 mp3/207.mp3') # Fora do horario
                                    
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

                                        os.system('mpg123 mp3/212.mp3') # Este QRCode ja mudou 
                                        
                                        fora_do_horario = 1

                                        #time.sleep(1)
                                if confere_tabela_hora != horario_atual_hora and fora_do_horario == 0:

                                    os.system('mpg123 mp3/212.mp3') # Este QRCode ja mudou 
                                   
                                    fora_do_horario = 1
                                                           
                                
                                if (hf < h): # se o horario final é menor que o horario atual já expirou

                                    print("Horario do QR Code já Expirou\n")

                                    os.system('mpg123 mp3/208.mp3') # Expirou
                                    
                                    time.sleep(3)

                                    #acesso = 0
                                    consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                if (hf > h and fora_do_horario == 0): # se o horario final for maior que o horario atual, QR Code ainda válido

                                    #print("Dentro do horario permitido\n")

                                    os.system('mpg123 mp3/188.mp3') # Acesso por QR Code
                                                               
                                    arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                    arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                    arquivo.close()
                    
                                    acesso = 1
                                    consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                     
                                    
                                if (hf == h): # se a hora final for a mesma da hora atual, verifica os minutos

                                    if mf == 0:

                                        print("Expirou a alguns minutos\n")

                                        os.system('mpg123 mp3/211.mp3') # Expirou
                                       
                                        time.sleep(3)

                                        #acesso = 0
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                                    if (mf != 0 and mf >= m): # se minutos finais forem menores do que minutos atuais, ainda válido

                                        print("Dentro do horario, faltando",mf - m, "minutos")

                                        os.system('mpg123 mp3/188.mp3') # Acesso por QR Code
                                        
                                        arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                        arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                        arquivo.close()
                        
                                        acesso = 1
                                        consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                                                      

                                    if (mf != 0 and mf <= m):
                                
                                         print("Expirou\n")

                                         os.system('mpg123 mp3/208.mp3') # Expirou
                                      
                                         time.sleep(3)

                                         #acesso = 0
                                         consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                         

                            if acesso == 1:

                                Rele.pulso(0,1,2) # (self,rele,tempo)
                                                                

                            if acesso == 0 and consta_no_banco == 1 and fora_do_horario == 0:

                                print("QR Code com data expirada")

                                os.system('mpg123 mp3/210.mp3') # Data Expirada
                             
                                consulta = 1


                            # Aqui será necessário verificar se ja passou do horario final e avisar
                        
                        except Exception as e:
                            
                            print("Tipo de erro: " + str(e))

                        
                    if id_valido == 0:

                        print("QR Code não cadastrado")

                        os.system('mpg123 mp3/189.mp3') # Não cadastrado
                        
                    fora_do_horario = 0
                    
                    
            
##qrcode = Qrcode()

################################## Classe para envio de email para Leandro Leal (Desenvolvedor do CMM) #############################

class Email:

    def enviar(self,mensagem):

        

        try:

            signal.alarm(7)

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
            server.login("leandrolopesleal26@gmail.com", "jesuscr332")
            msg = ("%s" %g)
            
            server.sendmail("leandrolopesleal26@gmail.com", "leandrolopesleal26@gmail.com", msg)
            server.quit()

            print ("Email enviado!")

            signal.alarm(0)

        except Exception as err:

            print("Não consegui enviar o email",err)
            
        

############################################# Retorna o valor da temperatura da cpu do CLP ##########################################

class Temperatura:
    
    def cpu(self): 
        tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
        cpu_temp = tempFile.read()
        tempFile.close()
        t = float(cpu_temp)/1000
        return round(t)

############################################# Consulta do clima da cidade de Bauru ###################################################

class Clima:

    def clima_atual(self):

        data = request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Bauru,BR&lang=pt&units=metric&APPID=dd7227b5df6988b8ba34bffd5b6e3450")
        html = data.read()
        html = html.decode('utf-8')

        html = html.replace("b'","")
        
        weathe = json.loads(html)
        temperatura = (weathe['main']['temp'])
        temperatura = round(temperatura)
        temperatura = str(temperatura)

        nebulosidade = str(weathe['clouds']['all'])

        umidade = str(weathe['main']['humidity'])

        tempo = weathe['weather']
        tempo = tempo[0]
        tempo = tempo['description']


        feed_back_clima = str("Em Bauru " + tempo + " e " + temperatura + " graus")

            
        return (feed_back_clima)


######################################### Classe Narrador (retorna o mp3 da frase recebida) #############################################

class Narrador: 

    def falar(self, mensagem): # Narra as mensagens de texto recebidas

        try:
      
            voz = gTTS(mensagem, lang="pt")  # guardamos o nosso texto na variavel voz
            voz.save("mensagem.mp3")  # salvamos com o comando save em mp3

            print ("Reproduzindo Texto no narrador")
            
            os.system("mpg123 mensagem.mp3")
            
            print("terminou o narração")

        except Exception as err:

            print("Erro no narrador",err)

    def gravar(self,mensagem,nome): # Grava a mensagem recebida em um arquivo mp3 com o nome passado no argumento
        
        try:

            print ("Gravando texto...")
      
            voz = gTTS(mensagem, lang="pt")  # guardamos o nosso texto na variavel voz
            voz.save("/home/pi/CMM/mp3/" + nome + ".mp3")  # salva o texto narrado com o nome informado

            print("Salvou o texto em " + nome + ".mp3")

            os.system("mpg123 /home/pi/CMM/mp3/" + nome + ".mp3")

        except Exception as err:

            print("Erro no gravador",err)





            
