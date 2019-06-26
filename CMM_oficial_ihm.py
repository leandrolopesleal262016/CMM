#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 06/06/2019

import RPi.GPIO as GPIO
import time
from biblioteca_CMM_oficial import Rele,Narrador,Temperatura,Email,Clima,Evento#, Qrcode, Rele_qr
from IHM_Sociais import IHM
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import threading # Modulo superior Para executar as threads
import sys
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
import socket
import serial # Para comunicação serial com arduino

#ser = serial.Serial("/dev/ttyS0", 9600) #Configura a serial e a velocidade de transmissao

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

A = GPIO.input(4) # ENTRADAS NÃO FOTOACOPLADAS (As entradas A B C D então normalmente em nivel lógico HIGH (1))
B = GPIO.input(27)
C = GPIO.input(22)
D = GPIO.input(10)

hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
h = int(time.strftime('%H'))
data = time.strftime('%d/%m/%y')

global entradas
entradas = ["A", "B", "C", "D", "IN1", "IN2", "IN3", "ctw1", "ctw2", "qbv", "qde", "IN8"]
global mp3

############################ INICIA AS CLASSES DA Biblioteca_CMM_Bravas  ########################################

rele = Rele() # inicia a classe rele com port A em 0
narrador = Narrador()
temperatura = Temperatura()
email = Email()
clima = Clima()
evento = Evento("0054") # Inicia a classe evento com o codigo do cliente

##ihm = IHM() 

##qrcode = Qrcode() # Instancia a classe do leitor de qrcode
##wiegand = Wiegand()
##rele_qr = Rele_qr() # Instanciar loclamente com o IP do leitor para acionamento do rele do equipamento
## Ex. rele_qr = Rele_qr("172.20.9.5",5000) # Conecta com o Qrcode deste endereço para acionamento do rele e leitura da entrada auxiliar

##print("Conteudo do play1 ",ihm.get_cbox("play1"))
 
##############################################  Threads dos programas  ##########################################################
   

def thread_wiegand(Rele,wiegand): # Leitor Wiegand IP 

    sys.stdout.write("\nLeitor Wiegand IP em execução\n")

##    wiegand.leitor_ip("172.20.9.128",4000) # Conecta com o leitor deste endereço e inicia o programa leitor
        


def thread_qrcode(qrcode): # Programa do QR Code

    sys.stdout.write("\nPrograma QR Code em execução\n")

##    qrcode.leitor("172.20.9.5",5001) # Conecta com o Qrcode deste endereço e inicia o programa do leitor

class Entradas(): # Inicia a thread leitura das entradas para controle de todos os programas
    
##    sys.stdout.write("\nClasse leitura das entradas em execução\n")

##    entradas = []    # Cria uma lista  para inserir os dados de config.txt
##    txt = open("config.txt",'r')    
##    for line in txt: # Coloca cada linha do arquivo de texto config.txt na lista[]
##        entradas.append(line)


##    IN1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
##    IN2 = wiringpi.digitalRead(301)  # entradas constantes
##    IN3 = wiringpi.digitalRead(302)
##    IN4 = wiringpi.digitalRead(303)
##    IN5 = wiringpi.digitalRead(304)
##    IN6 = wiringpi.digitalRead(305)
##    IN7 = wiringpi.digitalRead(306)
##    IN8 = wiringpi.digitalRead(307)
##
##    A = GPIO.input(4) # Entrada A  # entradas constantes
##    B = GPIO.input(27) # Entrada B 
##    C = GPIO.input(22) # Entrada C 
##    D = GPIO.input(10) # Entrada D


    # Associa os dados salvos no config.txt as entradas correspondentes

##    line1 = (entradas[0])         # Coloca na variavel line1 o texto encontrado na linha 1
##    line1 = line1.replace("\n","")  # Retira o \n do texto
##
##    if line1 == 'IN1': # Caso encintre IN1 na primeira linha atribui IN1 ao pm1 (ponto magnetico 1)
##        i1 = IN1
##    if line1 == 'IN2':
##        i1 = IN2
##    if line1 == 'IN3':
##        i1 = IN3
##    if line1 == 'IN4':
##        i1 = IN4
##    if line1 == 'IN5':
##        i1 = IN5
##    if line1 == 'IN6':
##        i1 = IN6
##    if line1 == 'IN7':
##        i1 = IN7
##    if line1 == 'IN8':
##        i1 = IN8
##    if line1 == 'A':
##        i1 = A
##    if line1 == 'B':
##        i1 = B
##    if line1 == 'C':
##        i1 = C
##    if line1 == 'D':
##        i1 = D
##    if line1 == " --- ":
##        i1 = "0"
##    
##
##    line2 = (entradas[1])         
##    line2 = line2.replace("\n","")
##
##    if line2 == 'IN1':
##        i2 = IN1
##    if line2 == 'IN2':
##        i2 = IN2
##    if line2 == 'IN3':
##        i2 = IN3
##    if line2 == 'IN4':
##        i2 = IN4
##    if line2 == 'IN5':
##        i2 = IN5
##    if line2 == 'IN6':
##        i2 = IN6
##    if line2 == 'IN7':
##        i2 = IN7
##    if line2 == 'IN8':
##        i2 = IN8
##    if line2 == 'A':
##        i2 = A
##    if line2 == 'B':
##        i2 = B
##    if line2 == 'C':
##        i2 = C
##    if line2 == 'D':
##        i2 = D
##    if line2 == ' --- ':
##        i2 = "0"
##
##    line3 = (entradas[2])
##    line3 = line3.replace("\n","")
##
##    if line3 == 'IN1':
##        i3 = IN1
##    if line3 == 'IN2':
##        i3 = IN2
##    if line3 == 'IN3':
##        i3 = IN3
##    if line3 == 'IN4':
##        i3 = IN4
##    if line3 == 'IN5':
##        i3 = IN5
##    if line3 == 'IN6':
##        i3 = IN6
##    if line3 == 'IN7':
##        i3 = IN7
##    if line3 == 'IN8':
##        i3 = IN8
##    if line3 == 'A':
##        i3 = A
##    if line3 == 'B':
##        i3 = B
##    if line3 == 'C':
##        i3 = C
##    if line3 == 'D':
##        i3 = D
##    if line3 == ' --- ':
##        i3 = "0"
##
##
##    line4 = (entradas[3])
##    line4 = line4.replace("\n","")
##
##    if line4 == 'IN1':
##        i4 = IN1
##    if line4 == 'IN2':
##        i4 = IN2
##    if line4 == 'IN3':
##        i4 = IN3
##    if line4 == 'IN4':
##        i4 = IN4
##    if line4 == 'IN5':
##        i4 = IN5
##    if line4 == 'IN6':
##        i4 = IN6
##    if line4 == 'IN7':
##        i4 = IN7
##    if line4 == 'IN8':
##        i4 = IN8
##    if line4 == 'A':
##        i4 = A
##    if line4 == 'B':
##        i4 = B
##    if line4 == 'C':
##        i4 = C
##    if line4 == 'D':
##        i4 = D
##    if line4 == ' --- ':
##        i4 = "0"
##
##    
##    line5 = (entradas[4])
##    line5 = line5.replace("\n","")
##
##    if line5 == 'IN1':
##        i5 = IN1
##    if line5 == 'IN2':
##        i5 = IN2
##    if line5 == 'IN3':
##        i5 = IN3
##    if line5 == 'IN4':
##        i5 = IN4
##    if line5 == 'IN5':
##        i5 = IN5
##    if line5 == 'IN6':
##        i5 = IN6
##    if line5 == 'IN7':
##        i5 = IN7
##    if line5 == 'IN8':
##        i5 = IN8
##    if line5 == 'A':
##        i5 = A
##    if line5 == 'B':
##        i5 = B
##    if line5 == 'C':
##        i5 = C
##    if line5 == 'D':
##        i5 = D
##    if line5 == ' --- ':
##        i5 = "0"
##
##    line6 = (entradas[5])
##    line6 = line6.replace("\n","")
##
##    if line6 == 'IN1':
##        i6 = IN1
##    if line6 == 'IN2':
##        i6 = IN2
##    if line6 == 'IN3':
##        i6 = IN3
##    if line6 == 'IN4':
##        i6 = IN4
##    if line6 == 'IN5':
##        i6 = IN5
##    if line6 == 'IN6':
##        i6 = IN6
##    if line6 == 'IN7':
##        i6 = IN7
##    if line6 == 'IN8':
##        i6 = IN8
##    if line6 == 'A':
##        i6 = A
##    if line6 == 'B':
##        i6 = B
##    if line6 == 'C':
##        i6 = C
##    if line6 == 'D':
##        i6 = D
##    if line6 == ' --- ':
##        i6 = "0"            
##
##    line7 = (entradas[6])
##    line7 = line7.replace("\n","")
##
##    if line7 == 'IN1':
##        i7 = IN1
##    if line7 == 'IN2':
##        i7 = IN2
##    if line7 == 'IN3':
##        i7 = IN3
##    if line7 == 'IN4':
##        i7 = IN4
##    if line7 == 'IN5':
##        i7 = IN5
##    if line7 == 'IN6':
##        i7 = IN6
##    if line7 == 'IN7':
##        i7 = IN7
##    if line7 == 'IN8':
##        i7 = IN8
##    if line7 == 'A':
##        i7 = A
##    if line7 == 'B':
##        i7 = B
##    if line7 == 'C':
##        i7 = C
##    if line7 == 'D':
##        i7 = D
##    if line7 == ' --- ':
##        i7 = "0"
##
##    line8 = (entradas[7])
##    line8 = line8.replace("\n","")
##
##    if line8 == 'IN1':
##        i8 = IN1
##    if line8 == 'IN2':
##        i8 = IN2
##    if line8 == 'IN3':
##        i8 = IN3
##    if line8 == 'IN4':
##        i8 = IN4
##    if line8 == 'IN5':
##        i8 = IN5
##    if line8 == 'IN6':
##        i8 = IN6
##    if line8 == 'IN7':
##        i8 = IN7
##    if line8 == 'IN8':
##        i8 = IN8
##    if line8 == 'A':
##        i8 = A
##    if line8 == 'B':
##        i8 = B
##    if line8 == 'C':
##        i8 = C
##    if line8 == ' --- ':
##        i8 = "0"
##
##    line9 = (entradas[8])
##    line9 = (line9.replace("\n",""))
##
##    if line9 == 'IN1':
##        iA = IN1
##    if line9 == 'IN2':
##        iA = IN2
##    if line9 == 'IN3':
##        iA = IN3
##    if line9 == 'IN4':
##        iA = IN4
##    if line9 == 'IN5':
##        iA = IN5
##    if line9 == 'IN6':
##        iA = IN6
##    if line9 == 'IN7':
##        iA = IN7
##    if line9 == 'IN8':
##        iA = IN8
##    if line9 == 'A':
##        iA = A
##    if line9 == 'B':
##        iA = B
##    if line9 == 'C':
##        iA = C
##    if line9 == 'D':
##        iA = D
##    if line9 == ' --- ':
##        iA = "0"
##
##    line10 = (entradas[9])
##    line10 = (line10.replace("\n",""))
##
##    if line10 == 'IN1':
##        iB = IN1
##    if line10 == 'IN2':
##        iB = IN2
##    if line10 == 'IN3':
##        iB = IN3
##    if line10 == 'IN4':
##        iB = IN4
##    if line10 == 'IN5':
##        iB = IN5
##    if line10 == 'IN6':
##        iB = IN6
##    if line10 == 'IN7':
##        iB = IN7
##    if line10 == 'IN8':
##        iB = IN8
##    if line10 == 'A':
##        iB = A
##    if line10 == 'B':
##        iB = B
##    if line10 == 'C':
##        iB = C
##    if line10 == 'D':
##        iB = D
##    if line10 == ' --- ':
##        iB = "0"
##
##    line11 = (entradas[10])
##    line11 = (line11.replace("\n",""))
##
##    if line11 == 'IN1':
##        iC = IN1
##    if line11 == 'IN2':
##        iC = IN2
##    if line11 == 'IN3':
##        iC = IN3
##    if line11 == 'IN4':
##        iC = IN4
##    if line11 == 'IN5':
##        iC = IN5
##    if line11 == 'IN6':
##        iC = IN6
##    if line11 == 'IN7':
##        iC = IN7
##    if line11 == 'IN8':
##        iC = IN8
##    if line11 == 'A':
##        iC = A
##    if line11 == 'B':
##        iC = B
##    if line11 == 'C':
##        iC = C
##    if line11 == 'D':
##        iC = D
##    if line11 == ' --- ':
##        iC = "0"
##
##    line12 = (entradas[11])
##    line12 = (line12.replace("\n",""))
##
##    if line12 == 'IN1':
##        iD = IN1
##    if line12 == 'IN2':
##        iD = IN2
##    if line12 == 'IN3':
##        iD = IN3
##    if line12 == 'IN4':
##        iD = IN4
##    if line12 == 'IN5':
##        iD = IN5
##    if line12 == 'IN6':
##        iD = IN6
##    if line12 == 'IN7':
##        iD = IN7
##    if line12 == 'IN8':
##        iD = IN8
##    if line12 == 'A':
##        iD = A
##    if line12 == 'B':
##        iD = B
##    if line12 == 'C':
##        iD = C
##    if line12 == 'D':
##        iD = D
##    if line12 == ' --- ':
##        iD = "0"
    
    while(1):    

        global IN1
        global IN2
        global IN3
        global IN4
        global IN5
        global IN6
        global IN7
        global IN8
        global A
        global B
        global C
        global D

        IN1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
        IN2 = wiringpi.digitalRead(301)  # entradas constantes
        IN3 = wiringpi.digitalRead(302)
        IN4 = wiringpi.digitalRead(303)
        IN5 = wiringpi.digitalRead(304)
        IN6 = wiringpi.digitalRead(305)
        IN7 = wiringpi.digitalRead(306)
        IN8 = wiringpi.digitalRead(307)

        A = GPIO.input(4) # Entrada A  # entradas constantes
        B = GPIO.input(27) # Entrada B 
        C = GPIO.input(22) # Entrada C 
        D = GPIO.input(10) # Entrada D

        time.sleep(0.2)

  

##        for i in ("IN1","IN2","IN3","IN4","IN5","IN6","IN7","IN8","A","B","C","D"):
##   
##            if i1 == (i):
##
##                i = i.replace('"',"")
##                pm1 = i
##                
##        for i in ("IN1","IN2","IN3","IN4","IN5","IN6","IN7","IN8","A","B","C","D"):
##   
##            if i2 == (i):
##
##                i = i.replace('"',"")
##                pm2 = i

        

##        pm1 = IN1
##        pm2 = IN2
##        pm3 = IN3
##        pm4 = IN4
##        pm5 = IN5
##        qbv = IN6
##        mud = IN7
##        qde = IN8
##        ctw1 = A
##        ctw2 = B
##        ctw3 = C
##        ctw4 = D

##        print(pm1,pm2,pm3,pm4,pm5,qbv,mud,qde,ctw1,ctw2,ctw3,ctw4,"\n")
            
        

        
        

        
##            if cont == 0: # Só executa uma vez
##
##                print("pm1",pm1,"pm2",pm2,"qbv",qbv,"mud",mud,"qde",qde,"ctw1",ctw1,"ctw2",ctw2)
##                cont = 1
##
##           
##            if pm1 == 0 and cont1 == 0:            
##                print("pm1 0")
##                cont1 = 1
##            if pm1 == 1 and cont1 == 1:            
##                print("pm1 1")
##                cont1 = 0
##            
##            if pm2 == 0 and cont2 == 0:           
##                print("pm2 0")
##                cont2 = 1
##            if pm2 == 1 and cont2 == 1:            
##                print("pm2 1")
##                cont2 = 0
##
##            if pm3 == 0 and cont3 == 0:            
##                print("pm3 0")
##                cont3 = 1
##            if pm3 == 1 and cont3 == 1:            
##                print("pm3 1")
##                cont3 = 0
##                
##            if pm4 == 0 and cont4 == 0:        
##                print("pm4 0")
##                cont4 = 1
##            if pm4 == 1 and cont4 == 1:            
##                print("pm4 1")
##                cont4 = 0
##
##            if pm5 == 0 and cont5 == 0:        
##                print("pm5 0")
##                cont5 = 1
##            if pm5 == 1 and cont5 == 1:            
##                print("pm5 1")
##                cont5 = 0
##
##            if qbv == 0 and cont6 == 0:        
##                print("qbv 0")
##                cont6 = 1
##            if qbv == 1 and cont6 == 1:            
##                print("qbv 1")
##                cont6 = 0
##
##            if mud == 0 and cont7 == 0:        
##                print("mud 0")
##                cont7 = 1
##            if mud == 1 and cont7 == 1:            
##                print("mud 1")
##                cont7 = 0
##
##            if qde == 0 and cont8 == 0:        
##                print("qde 0")
##                cont8 = 1
##            if qde == 1 and cont8 == 1:            
##                print("qde 1")
##                cont8 = 0
##
##            byte = (pm1,pm2,pm3,pm4,pm5,qbv,mud,qde)
##            byte = str(byte)
##            byte = byte.replace("'","")
##            byte = byte.replace("(","")
##            byte = byte.replace(")","")
##            
##            
##            o = open("in_out.cmm","w")
##            o.write(byte)
##            o.close()

##        result = (pm1,pm2,pm3,pm4,pm5,qbv,mud,qde,ctw1,ctw2,ctw3,ctw4)
##        result = str(result)
##        result = result.replace("'","")
##        print(result)
##        return(result)
        
  
######################################  CLASSES  ###########################################

class Intertravamento(Rele): # Inicia a thread dos portoes sociais importando a classe Rele

            
    def __init__(self,Rele):

        global ctw1
        global ctw2        
        global pm1
        global pm2        
        global audio

        audio = 1 # Deixa ativo ass mensagens de audio de abertura
        cont = 0

        a = open("status_social.cmm","r")
        abre_social = a.read()
        a.close()

        b = open("status_eclusa.cmm","r")
        abre_eclusa = b.read()
        b.close()
        
        if cont == 0: # Executa uma unica vez

            print("Estado das enradas A B C D ",A,B,C,D," ligado (0)")
            cont = 1

    def abre_social(self):                          
    
        
        if pm1 == 1: # O portão social já esta aberto

            print("O portão social já esta aberto")
                        
            os.system("mpg123 /home/pi/CMM/mp3/social_aberto.mp3")
            time.sleep(1)

        else: # Se o portão Social esta fechado então pode abrir
            
            if pm2 == 0: # Se Ponto magnético Eclusa fechado
                
                s = open("status_social.cmm","w")
                s.write("1")
                s.close()

                rele.liga(2) # Aqui abrimos o contato da eclusa para impedir que ela seja aberta enquanto o social esta aberto
                
                print("Abrindo portão Social")

                if audio == 1: # Ativa as mensagens de abertura e fechamento

                    os.system("mpg123 /home/pi/CMM/mp3/abrindo_social.mp3")                   
                
                time.sleep(2) # Tempo de espera para o portão começar a abrir

                if pm1 == 0: # Portão fechado pois não abriu com o comando

                    print("Portão Social emperrado")
                    evento.enviar("E","130","011") # Envia portão emperrado
                    
                    rele.desliga(2) # Fecha o contato e libera a eclusa para ser acionada

                    os.system("mpg123 /home/pi/CMM/mp3/social_emperrado.mp3")

                if pm1 == 1: # Portão abriu

                    evento.enviar("E","133","001") # Envia abriu portão
                    
                    contador = 200 # Tempo maximo para o social ficar aberto 20 segundos
                    print("Esperando por 20 segundos o portão social fechar...")

                    while contador > 0: # enquanto portão está aberto
                        
                        # Esperando o portão social fechar...

                        if pm1 == 0: # portão fechou

                            print("Portão social fechou")
                            evento.enviar("R","133","001") # Envia fechamento
                            contador = 1
                                                        
                            s = open("status_social.cmm","w")
                            s.write("0")
                            s.close()

                            rele.desliga(2) # Fecha o contato e libera a eclusa para ser acionada

                        if (pm1 == 1 and contador == 1): # Portão ainda aberto após 15 segundos de espera

                            print("Portão social aberto por muito tempo")
                            
                            evento.enviar("E","905","001") # Envia falha no fechamento

                            os.system("mpg123 /home/pi/CMM/mp3/obstrucao.mp3")
                            
                            status = open("status_social.cmm","w") # Para não disparar o arrombamento
                            status.write("1")
                            status.close()

                            contador = 1

                            rele.desliga(2) # Fecha o contato e libera a eclusa para ser acionada
                            
                        if ctw2 == 0: # Entrada para abrir o portão da eclusa
                            print("Agurade o fechamento do social")
                            os.system("mpg123 /home/pi/CMM/mp3/aguarde_social.mp3") # Necessario manter esse audio sempre ativo
                            time.sleep(1)
                            
                        time.sleep(0.1) # 1 segundo
                        contador = contador - 1
                        print(contador)
                        
            if pm2 == 1:

                os.system("mpg123 /home/pi/CMM/mp3/aguarde_social.mp3")
                time.sleep(1)
                    
    def abre_eclusa(self):
        

        if pm2 == 1: # O portão Eclusa já esta aberto

            print("O portão Eclusa já esta aberto")

            os.system("mpg123 /home/pi/CMM/mp3/eclusa_aberto.mp3")
            time.sleep(1)

        else: # Se o portão Eclusa esta fechado então pode abrir


            if pm1 == 0: # Ponto magnético Social fechado, pode abrir a eclusa
                
                s = open("status_eclusa.cmm","w")
                s.write("1")
                s.close()

                rele.liga(1) # Impede o social de abrir enquanto a eclusa esta aberta 
                print("Abrindo portão Eclusa")

                if audio == 1:
                    os.system("mpg123 /home/pi/CMM/mp3/abrindo_eclusa.mp3")
                
                time.sleep(2) # Tempo de espera para o portão abrir

                if pm2 == 0: # Portão fechado não abriu após o comando

                   print("Portão emperrado")
                   evento.enviar("E","130","012") # Envia portão emperrado
                   if audio == 1:
                       os.system("mpg123 /home/pi/CMM/mp3/eclusa_emperrado.mp3")
                       
                   rele.desliga(1) # Libera o social para abrir mesmo com a eclusa aberta 

                if pm2 == 1: # Portão aberto

                    evento.enviar("E","133","003") # Envia abertura
                    
                    contador = 200 # Tempo maximo para o social ficar aberto 20 segundos
                    print("Esperando por 20 segundos o portão Eclusa fechar...")

                    while contador > 0: # enquanto portão está aberto
                        
                        # Esperando o portão social fechar...

                        if pm2 == 0: # portão fechou

                            print("Portão Eclusa fechou")
                            evento.enviar("R","133","003") # Envia fechamento
                            contador = 1
                            
                            s = open("status_social.cmm","w")
                            s.write("0")
                            s.close()

                            rele.desliga(1) # Libera o social para abrir 

                        if (pm2 == 1 and contador == 1): # Portão ainda aberto após 15 segundos de espera

                            print("Portão Eclusa aberto por muito tempo")
                            
                            evento.enviar("E","905","003") # Envia falha no fechamento
                            
                            os.system("mpg123 /home/pi/CMM/mp3/obstrucao.mp3")
                            
                            status = open("status_eclusa.cmm","w") # Para não disparar o arrombamento
                            status.write("1")
                            status.close()

                            contador = 1

                            rele.desliga(1) # Libera o social para abrir mesmo com a eclusa aberta

                        if ctw1 == 0: # Alguem esta tentando abrir o social com a eclusa aberta

                            print("Agurde o fechamento da eclusa")
                            os.system("mpg123 /home/pi/CMM/mp3/aguarde_eclusa.mp3") # Manter esse audio sempre ativo
                            time.sleep(1)
                            

                        time.sleep(0.1) # 1 segundo
                        contador = contador - 1
                        print(contador)
                        
            if pm1 == 1:

                os.system("mpg123 /home/pi/CMM/mp3/aguarde_eclusa.mp3")
                time.sleep(1)
                                

class Abre(Rele): # Inicia a thread dos portoes sociais importando a classe Rele


    def social(self):

        status = open("status_social.cmm","w") # Para não dispara o arrombamento
        status.write("1")
        status.close()

        rele.pulso(4,2) # Pulso para abrir direto o portão sem intertravamento (Social)
        
        print("Abrindo portão social")
        evento.enviar("E","133","001") # Envia abertura

    def eclusa(self):

        status = open("status_eclusa.cmm","w") # Para não dispara o arrombamento
        status.write("1")
        status.close()        
    
        rele.pulso(5,2) # Pulso para abrir direto o portão sem intertravamento (Eclusa)

        print("Abrindo portão eclusa")      
        evento.enviar("E","133","003") # Envia abertura
        
                

################################################ THREADS ROTINAS #################################################


def Garagem(Rele): # Inicia a thread do portão da garagem importando a classe Rele
       
    sys.stdout.write("\nPrograma Garagem em execução na thread\n")
    
    while(1):

        i1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
        i2 = wiringpi.digitalRead(301)
        i3 = wiringpi.digitalRead(302)
        i4 = wiringpi.digitalRead(303)
        i5 = wiringpi.digitalRead(304)
        i6 = wiringpi.digitalRead(305)
        i7 = wiringpi.digitalRead(306)
        i8 = wiringpi.digitalRead(307)

        in1 = i1
        in2 = i2
        in3 = i3
        ctw1 = i4
        ctw2 = i5
        qbv = i6
        qde = i7
        in8 = i8

        
               
        time.sleep(1)    



def Arrombamento(Rele): # Inicia a thread arrombamento de portões
    
    sys.stdout.write("\nPrograma arrombamento de portões em execução\n")

    ar1 = 0 # Variavel arrombamento portão 1
    ar2 = 0
    ar3 = 0
    ar4 = 0
    ar5 = 0
    ar6 = 0
    ar7 = 0
    reset_ar1 = 0 # Reseta a variavel do portão para 0
    reset_ar2 = 0
    reset_ar3 = 0
    reset_ar4 = 0
    reset_ar5 = 0 
    reset_ar6 = 0
    reset_ar7 = 0
    cont1 = 30 # Contador individual para cada reset de arrombamento
    cont2 = 30
    cont3 = 30
    cont4 = 30
    cont5 = 30
    cont6 = 30
    cont7 = 30
    
    while(1):

        a = open("status_social.cmm","r")
        abre_social = a.read()
        a.close()

        b = open("status_eclusa.cmm","r")
        abre_eclusa = b.read()
        b.close()  
        
        global pm1
        global pm2

        if abre_social == "0" and pm1 == 1 and ar1 == 0:

            time.sleep(0.5) # Filtra algum possivel ruido de até 500 milissegundos

            if pm1 == 1: # Se realmente foi um arrombamento liga sirene e notifica o Moni

                print("Arrombamento do portão social")
                os.system("mpg123 /home/pi/CMM/mp3/violacao_social.mp3")
                rele.liga(8)
                evento.enviar("E","120","002")
                
                ar1 = 1
                reset_ar1 = 1

        if ar1 == 1 and reset_ar1 == 1:

            cont1 = cont1 - 1 # A primeira vez que acontece o arrombamento reseta depois de 30 segundos
            time.sleep(1)

            if cont1 <= 0:

                evento.enviar("R","120","002")

                cont1 = 60 # Se apos o reset o portão continuar aberto envia o evento novamente  espera 60 segundos
                ar1 = 0
                reset_ar1 = 0
                rele.desliga(8)

                

        if abre_eclusa == "0" and pm2 == 1 and ar2 == 0:

            time.sleep(0.5) # Filtra algum possivel ruido de até 500 milissegundos

            if pm2 == 1: # Se realmente foi um arrombamento liga sirene e notifica o Moni

                print("Arrombamento do portão Eclusa")
                os.system("mpg123 /home/pi/CMM/mp3/violacao_eclusa.mp3")
                rele.liga(8)
                evento.enviar("E","120","004")
                
                ar2 = 1
                reset_ar2 = 1

        if ar2 == 1 and reset_ar2 == 1:

            cont2 = cont2 - 1 # A primeira vez que acontece o arrombamento reseta depois de 30 segundos
            time.sleep(1)

            if cont2 <= 0:

                evento.enviar("R","120","004")

                cont2 = 60 # Se apos o reset o portão continuar aberto envia o evento novamente  espera 60 segundos
                ar2 = 0
                reset_ar2 = 0
                rele.desliga(8)

        
        time.sleep(1)

def Servidor(Rele): # Inicia a thread do portão da garagem importando a classe Rele
    
    sys.stdout.write("\nPrograma de automação em execução\n")
    
    host = '0.0.0.0'
    port = 5510

    time.sleep(0.1)
    
    print("Servidor: ",host, " porta: ", port)

    while(1):

        
        ############################################### Thread servidor p/ PHP e MONI #################################################################

        while(1):


            def setupServer():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # "AF_NET" trabalharemos com protocolo ipv4, .SOCK_STREAM USAREMOS TCP
                
                try:
                    s.bind((host, port))
                except socket.error as msg:
                    print (msg)
                
                return s

            def setupConnection():
                s.listen(5)
                conn, address = s.accept()
                print ("Conectado com: " + address[0] + ":" + str(address[1]), "\n")
                return conn


            def dataTransfer(conn):  # Loop de transferencia e recepção de dados

                while True:

                    global pm1
                    global pm2
                    global pm5
                    global qbv
                    global mud
                    global qde
                    global ctw1
                    global ctw2
                                      
                    data = conn.recv(1024)  # Recebe o dado
                    data = data.decode('utf-8')
                    dataMessage = data.split(' ',1)# Separa o comando do resto dos dados
                    command = dataMessage[0]

                    (comando,resto) = data.split("\r") # Divide os dados da variavel data e guarda uma parte em comando e eoutra em resto


                    if(comando == "SET 1"):

                        print("Abrindo portão Social pelo Moni")
                        
                        abre.social() # Abre sem intertravamento porem fica aguardando o portão fechar

                        time.sleep(2)
                        cont = 20
                                            
                        while (cont > 0):

                            if pm1 == 1: # Se o portão esta aberto

                                print("Aguardando portão social fechar",cont)

                            if pm1 == 0: # Portão fechou

                                print("Portão social fechou")

                                status = open("status_social.cmm","w") # Para não dispara o arrombamento
                                status.write("0")
                                status.close()

                                cont = 1

                            cont = cont - 1
                            time.sleep(1)
                            
                        conn.close()                        
                                            

                    elif(comando == "SET 2"):
                        
                        print("Abrindo portão Eclusa pelo Moni")
                        
                        abre.eclusa() # Abre sem intertravamento

                        time.sleep(2)
                        cont = 20
                                            
                        while (cont > 0):

                            if pm2 == 1: # Se o portão esta aberto

                                print("Aguardando portão eclusa fechar",cont)

                            if pm2 == 0: # Portão fechou

                                print("Portão eclusa fechou")

                                status = open("status_eclusa.cmm","w") # Para não dispara o arrombamento
                                status.write("0")
                                status.close()

                                cont = 1

                            cont = cont - 1
                            time.sleep(1)
                        
                        conn.close()
                        
                       
                    elif(comando == "SET 3"):
                        print("reconheceu SET 3")
                        

                    elif(comando == "SET 4"):
                        print("reconheceu SET 4")
                        

                    elif(comando == "SET 5"):
                        print("reconheceu SET 5")
                        

                    elif(comando == "SET 6"):
                        print("SET 6, RESET SOCIAL")
                        

                    elif(comando == "SET 8"):
                        
                        print("SET 8, RESET ECLUSA")
                        

                    elif(comando == "SET 9"):
                        
                        print("SET 9, RESET INTERFONES")
                        

                    elif(comando == "SET 10"):
                        
                        print("SET 10, AUXILIAR 1 (ON/OFF)")
                        

                    elif(comando == "SET 11"):
                        
                        print("SET 11, AUXILIAR 2 (ON/OFF)")
                        

                    elif(comando == "SET 12"):
                        
                        print("APRESENTAÇÃO")
                        

                    else:

                        print(comando) 

                        reply = 'ok'
                        conn.sendall(str.encode(reply))  # Envia o reply de volta para o cliente
                        conn.close()


            s = setupServer()

            while True:
                
              time.sleep(1) 

              print ("\nEscutando na porta",port, "\n")
              try:

                  conn = setupConnection()
                  dataTransfer(conn)
                  print("Oiee")


              except Exception as err:

                  print("Encerrou conexão")

        
        time.sleep(0.1)

def Portoes_sociais(Rele): # Programa
    
    sys.stdout.write("\nPrograma Sociais em execução\n")
    
    intertravamento = Intertravamento(Rele) # Inicia a classe para usar o intertravamento
    quebra_vidro = 0

    entradas = []    # Cria uma lista  para inserir os dados de config.txt
    txt = open("config.txt",'r')    
    for line in txt: # Coloca cada linha do arquivo de texto config.txt na lista[]
        entradas.append(line)

    global IN1
    global IN2
    global IN3
    global IN4
    global IN5
    global IN6
    global IN7
    global IN8
    global A
    global B
    global C
    global D
    
    # Associa os dados salvos no config.txt as entradas correspondentes

    line1 = (entradas[0])         # Coloca na variavel line1 o texto encontrado na linha 1
    line1 = line1.replace("\n","")  # Retira o \n do texto
    line2 = (entradas[1])         
    line2 = line2.replace("\n","")
    line3 = (entradas[2])
    line3 = line3.replace("\n","")
    line4 = (entradas[3])
    line4 = line4.replace("\n","")
    line5 = (entradas[4])
    line5 = line5.replace("\n","")  
    line6 = (entradas[5])
    line6 = line6.replace("\n","")  
    line7 = (entradas[6])
    line7 = line7.replace("\n","")
    line8 = (entradas[7])
    line8 = line8.replace("\n","")
    line9 = (entradas[8])
    line9 = (line9.replace("\n",""))
    line10 = (entradas[9])
    line10 = (line10.replace("\n",""))
    line11 = (entradas[10])
    line11 = (line11.replace("\n",""))
    line12 = (entradas[11])
    line12 = (line12.replace("\n",""))

    if line1 == "IN1":
        pm1 = IN1
    if line1 == "IN2":
        pm1 == IN2
    if line1 == "IN3":
        pm1 == IN3
    if line1 == "IN4":
        pm1 == IN4
    if line1 == "IN5":
        pm1 == IN5
    if line1 == "IN6":
        pm1 == IN6
    if line1 == "IN7":
        pm1 == IN7
    if line1 == "IN8":
        pm1 == IN8
    if line1 == "A":
        pm1 == A
    if line1 == "B":
        pm1 == B
    if line1 == "C":
        pm1 == C
    if line1 == "D":
        pm1 == D
    if line1 == " --- ":
        pm1 == None

    while(1):

        
       


        pm1
        pm2
        qbv
        mud
        qde
        ctw1
        ctw2
        
##        i1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
##        i2 = wiringpi.digitalRead(301)
##        i3 = wiringpi.digitalRead(302)
##        i4 = wiringpi.digitalRead(303)
##        i5 = wiringpi.digitalRead(304)
##        i6 = wiringpi.digitalRead(305)
##        i7 = wiringpi.digitalRead(306)
##        i8 = wiringpi.digitalRead(307)
##
##        pm1 = i1
##        pm2 = i2
##        in3 = i3
##        ctw1 = i4
##        ctw2 = i5
##        qbv = i6
##        qde = i7
##        in8 = i8

##        a = open("status_social.cmm","r") # Verifica se alguem registrou abrir para o portão social
##        abre_social = a.read()
##        a.close()
##
##        b = open("status_eclusa.cmm","r") # Verifica se alguem registrou abrir para o portão eclusa
##        abre_eclusa = b.read()
##        b.close()
        
        
        if ctw1 == "1":

            status = open("status_social.cmm","w")
            status.write("1")
            status.close()
     
            intertravamento.abre_social()

            status = open("status_social.cmm","w")
            status.write("0")
            status.close()

        if ctw2 == "1":

            status = open("status_eclusa.cmm","w")
            status.write("1")
            status.close()

            intertravamento.abre_eclusa()

            status = open("status_eclusa.cmm","w")
            status.write("0")
            status.close()


        if qbv == 0 and quebra_vidro == 0: # Se o quebra de vidro foi acionado

            print("Quebra de vidro acionado")

            rele.liga(8) # Liga sirene

            abre.social() # Ao invocar esta função ela ja coloca o arquivo de texto em 1 para não gerear arrombamento
            abre.eclusa()

            os.system("mpg123 /home/pi/CMM/mp3/emergencia.mp3")

            time.sleep(1)

            rele.liga(3) # Foto dos 2 poortões (mantem os doid portões abertos)            

            quebra_vidro = 1

            evento.enviar("E","130","007") # Envia violação quebra de vidro           

            time.sleep(10)

        if qbv == 1 and quebra_vidro == 1:

            print("Quebra de vidro restaurado")
            
            rele.desliga(3) # Desliga fotocelula

            evento.enviar("R","130","007") # Envia violação quebra de vidro

            time.sleep(15) # Aguarda os portoes fecharem

            rele.desliga(8) # Desliga sirene

            status = open("status_social.cmm","w") # Volta o arquivo para zero para ativar a verificação de arrombamento
            status.write("0")
            status.close()

            status = open("status_eclusa.cmm","w")
            status.write("0")
            status.close()

            quebra_vidro = 0

            print("Sistema em modo automatico")
            os.system("mpg123 /home/pi/CMM/mp3/automatico.mp3")
                              
        
        time.sleep(0.1)

def Queda_energia(Rele): # Inicia a thread do portão da garagem importando a classe Rele
    
    sys.stdout.write("\nPrograma de automação em execução\n")

    queda_energia = 0

    while(1):
        
        i7 = wiringpi.digitalRead(306)        
        
        qde = i7        

        if qde == 0 and queda_energia == 0: # Queda de energia 

            print("Queda de energia")

            os.system("mpg123 /home/pi/CMM/mp3/queda_energia.mp3")
            
            evento.enviar("E","301","000") # Envia queda de energia elétrica

            time.sleep(3)

            queda_energia = 1

        if qde == 1 and queda_energia == 1: # Restaurou energia eletrica

            print("Restaurou energia eletrica")

            os.system("mpg123 /home/pi/CMM/mp3/restaurou_energia.mp3")

            evento.enviar("R","301","000") # Envia restauração de energia elétrica

            time.sleep(3)

            queda_energia = 0
        
        time.sleep(0.1)
        
        
def Mudanca(Rele):
    
    sys.stdout.write("\nPrograma chave de mudança em execução\n")

    chave_mudanca = 0    

    while(1):

        global mud
        
##        i8 = wiringpi.digitalRead(307)
##        
##        mud = i8 

        if mud == 0 and chave_mudanca == 0: # Queda de energia 

            print("Chave de mudança acionada")

            rele.liga(8) # Liga sirene

            abre.social() # Ao invocar esta função ela ja coloca o arquivo de texto em 1 para não gerear arrombamento
            abre.eclusa()

            os.system("mpg123 /home/pi/CMM/mp3/mudanca.mp3")

            time.sleep(1)

            rele.liga(3) # Foto dos 2 poortões (mantem os doid portões abertos)  
            
            evento.enviar("E","130","008") # Envia chave de mudança acionada

            time.sleep(3)

            chave_mudanca = 1

        if mud == 1 and chave_mudanca == 1: # Restaurou energia eletrica

            print("Chave de mudança restaurada")

            rele.desliga(3) # Desliga fotocelula
            
            os.system("mpg123 /home/pi/CMM/mp3/restaurou_mudanca.mp3")

            evento.enviar("R","130","008") # Envia violação quebra de vidro

            time.sleep(15) # Aguarda os portoes fecharem

            rele.desliga(8) # Desliga sirene

            status = open("status_social.cmm","w") # Volta o arquivo para zero para ativar a verificação de arrombamento
            status.write("0")
            status.close()

            status = open("status_eclusa.cmm","w")
            status.write("0")
            status.close()

            

            evento.enviar("R","130","008") # Envia restauração de energia elétrica

            time.sleep(3)

            chave_mudanca = 0
        
        time.sleep(0.1)
        

        
        time.sleep(1)
        

# Thread para feedback de temperatura, ajuste de volume, reset, graficos,

def Sistema(Rele,Temperatura): 
    
    sys.stdout.write("\nPrograma do sistema em execução\n")

    cont = 600 # Equivale a 60 segundos

    ihm = IHM() # Inicia a interface grafica de configuração dos sociais
    
    while(1):

##        i1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas        i2 = wiringpi.digitalRead(301)
##        i2 = wiringpi.digitalRead(301)
##        i3 = wiringpi.digitalRead(302)
##        i4 = wiringpi.digitalRead(303)
##        i5 = wiringpi.digitalRead(304)
##        i6 = wiringpi.digitalRead(305)
##        i7 = wiringpi.digitalRead(306)
##        i8 = wiringpi.digitalRead(307)
##
##        in1 = i1
##        in2 = i2
##        in3 = i3
##        ctw1 = i4
##        ctw2 = i5
##        qbv = i6
##        qde = i7
##        in8 = i8
##
##        
##        if ctw2 == 0:
##
##            rele.pulso(5,2)
##
##        if cont > 0:
##
##            cont = cont - 1
##
##        if cont == 0:
##
##            sys.stdout.write("\nTemperatura " + str(temperatura.cpu()) + "°C\n")  # obter temperatura
##
##            cont = 600            

        time.sleep(1)

        
#################### Instancia as Classes  #############################################

intertravamento = Intertravamento(Rele)
abre = Abre()

####################  Declara as threads dos programas disponiveis  ####################

entradas = threading.Thread(target=Entradas)
sociais = threading.Thread(target=Portoes_sociais, args=(Rele,)) # deixar virgula depois do arg 1
garagem = threading.Thread(target=Garagem, args=(Rele,))
arrombamento = threading.Thread(target=Arrombamento, args=(Rele,))
servidor = threading.Thread(target=Servidor, args=(Rele,))
##automacao4 = threading.Thread(target=Automacao4, args=(Rele,))
Queda_energia = threading.Thread(target=Queda_energia, args=(Rele,))
mudanca = threading.Thread(target=Mudanca, args=(Rele,))
sistema = threading.Thread(target=Sistema, args=(Rele,Temperatura,))
##qrcode = threading.Thread(target=thread_qrcode, args=(qrcode,))
##wiegand = threading.Thread(target=thread_wiegand, args=(Rele,wiegand))


######################################### Start dos Programas  #############################################################

entradas.start() # Inicia o programa leitura das entradas
sociais.start() # Inicia o programa dos portões sociais
##garagem.start() # Inicia o programa do portão de garagem
##arrombamento.start() # Inicia o programa de automação
####servidor.start() # Inicia o programa de automação
##automacao4.start() # Inicia o programa de automação
##Queda_energia.start() # Inicia o programa de automação
##mudanca.start() # In icia a leitura de interrupções
sistema.start()
##qrcode.start()
##wiegand.start()

time.sleep(0.2) # Tempo para colocar as linhas impressas após as linhas de inicio de programa

#########################################   INSTRUCOES   ################################################

##rele_qr.pulsa() # Pusa por 2 segundos o rele do QR Code
##rele_qr.liga()
##rele_qr.desliga()

##narrador.falar("Teste do narrador") # fala o texto enviado - depende de internet
##narrador.gravar("Qrcode não cadastrado","semCadastro") # Grava o texto enviado em nome.mp3

##rele.liga(1)    # Liga rele 1 (podendo ser de 1 a 8)
##rele.desliga(1)  # Desliga rele 1 (podendo ser de 1 a 8)
##rele.pulsa(8,2)  # rele.pulso(rele,tempo)  Pulsa o rele pelo tempo indicado em segundos

##os.system("mpg123 nome.mp3") # Reproduz um arquivo mp3 , necessario instalar mpg123 (sudo apt-get install mpg123)

##print ("\nTemperatura",temperatura.cpu(),"°C\n")  # obter temperatura

##email.enviar("O Programa acabou de reiniciar\nPosso enviar qualquer mensagem aqui...") # Não usar nenhum caracter especial na mensagem

##tempo = clima.clima_atual()
##print(tempo)

##evento.enviar_contact_id('E','130','001') # Evento ou Restauração / Evento / Setor

###################################################################################################

sys.stdout.write("\nTemperatura " + str(temperatura.cpu()) + "°C\n")  # obter temperatura



while(1):

    
    

    time.sleep(1)

