import RPi.GPIO as GPIO
import time
import biblioteca_CMM as cmm

from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import threading # Modulo superior Para executar as threads
import sys
import socket
import serial # Parhome/pi/CMM/mp3a comunicação serial com arduino
import _thread as thread
import libscrc # biblioteca para calculo do CRC (Controle de Redundancia) - usado no protocolo modbus


def log(texto): # Metodo para registro dos eventos no log.txt (exibido na interface grafica)

    hs = time.strftime("%H:%M:%S") 
    data = time.strftime('%d/%m/%y')

    texto = str(texto)

    escrita = ("{} - {}  Evento:  {}\n").format(data, hs, texto)
    escrita = str(escrita)

    l = open("/var/www/html/log/log.txt","a")
    l.write(escrita)
    l.close()

banco = cmm.Banco() # Oprerações CRUD no banco CMM

cliente = banco.consulta("config","cliente")
nome_cliente = banco.consulta("config","nome_cliente")
ip_cliente = banco.consulta("config","ip_cliente")

rele = 1
notifica = "0"

portao1 = banco.consulta("leitores_qrcode","portao_1")
portao2 = banco.consulta("leitores_qrcode","portao_2")
portao3 = banco.consulta("leitores_qrcode","portao_3")
portao4 = banco.consulta("leitores_qrcode","portao_4")
portao5 = banco.consulta("leitores_qrcode","portao_5")
portao6 = banco.consulta("leitores_qrcode","portao_6")
portao7 = banco.consulta("leitores_qrcode","portao_7")
portao8 = banco.consulta("leitores_qrcode","portao_8")
portao9 = banco.consulta("leitores_qrcode","portao_9")
portao10 = banco.consulta("leitores_qrcode","portao_10")
portao11 = banco.consulta("leitores_qrcode","portao_11")
portao12 = banco.consulta("leitores_qrcode","portao_12")
portao13 = banco.consulta("leitores_qrcode","portao_13")
portao14 = banco.consulta("leitores_qrcode","portao_14")
portao15 = banco.consulta("leitores_qrcode","portao_15")
portao16 = banco.consulta("leitores_qrcode","portao_16")


ip_qr1 = banco.consulta("leitores_qrcode","leitor_1")
ip_qr2 = banco.consulta("leitores_qrcode","leitor_2")
ip_qr3 = banco.consulta("leitores_qrcode","leitor_3")
ip_qr4 = banco.consulta("leitores_qrcode","leitor_4")
ip_qr5 = banco.consulta("leitores_qrcode","leitor_5")
ip_qr6 = banco.consulta("leitores_qrcode","leitor_6")
ip_qr7 = banco.consulta("leitores_qrcode","leitor_7")
ip_qr8 = banco.consulta("leitores_qrcode","leitor_8")
ip_qr9 = banco.consulta("leitores_qrcode","leitor_9")
ip_qr10 = banco.consulta("leitores_qrcode","leitor_10")
ip_qr11 = banco.consulta("leitores_qrcode","leitor_11")
ip_qr12 = banco.consulta("leitores_qrcode","leitor_12")
ip_qr13 = banco.consulta("leitores_qrcode","leitor_13")
ip_qr14 = banco.consulta("leitores_qrcode","leitor_14")
ip_qr15 = banco.consulta("leitores_qrcode","leitor_15")
ip_qr16 = banco.consulta("leitores_qrcode","leitor_16")

def thread_qr1(): # Programa do QR Code 1
    
    qr1.start() # Inicia o programa qrcode correspondente

def thread_qr2(): # Programa do QR Code 2
    
    qr2.start() 

def thread_qr3(): # Programa do QR Code 3
    
    qr3.start() 

def thread_qr4(): # Programa do QR Code 4
    
    qr4.start()

def thread_qr5(): # Programa do QR Code 5
    
    qr5.start() 

def thread_qr6(): # Programa do QR Code 6
    
    qr6.start()

def thread_qr7(): # Programa do QR Code 7
    
    qr7.start() 

def thread_qr8(): # Programa do QR Code 8
    
    qr8.start()

def thread_qr9(): # Programa do QR Code 9
    
    qr9.start() 

def thread_qr10(): # Programa do QR Code 10
    
    qr10.start()

def thread_qr11(): # Programa do QR Code 11
    
    qr11.start()

def thread_qr12(): # Programa do QR Code 12
    
    qr12.start()

def thread_qr13(): # Programa do QR Code 13
    
    qr13.start()

def thread_qr14(): # Programa do QR Code 14
    
    qr14.start()

def thread_qr15(): # Programa do QR Code 15
    
    qr15.start()

def thread_qr16(): # Programa do QR Code 16
    
    qr16.start()
    

if ip_qr1 != "":   
    
    qr1 = cmm.Qrcode(ip_qr1,cliente,rele,portao1,notifica,"Leitor 1") # instancia a classe leitor (a thread quem da o start)
    qrcode1 = threading.Thread(target=thread_qr1) # Cria e da start ma thread
    qrcode1.start()

if ip_qr2 != "":    
    
    qr2 = cmm.Qrcode(ip_qr2,cliente,rele,portao2,notifica, "Leitor 2") 
    qrcode2 = threading.Thread(target=thread_qr2) 
    qrcode2.start()

if ip_qr3 != "":
    
    qr3 = cmm.Qrcode(ip_qr3,cliente,rele,portao3,notifica, "Leitor 3") 
    qrcode3 = threading.Thread(target=thread_qr3) 
    qrcode3.start()

if ip_qr4 != "":
    
    qr4 = cmm.Qrcode(ip_qr4,cliente,rele,portao4,notifica, "Leitor 4") 
    qrcode4 = threading.Thread(target=thread_qr4) 
    qrcode4.start()

if ip_qr5 != "":
    
    qr5 = cmm.Qrcode(ip_qr5,cliente,rele,portao5,notifica, "Leitor 5") 
    qrcode5 = threading.Thread(target=thread_qr5) 
    qrcode5.start()

if ip_qr6 != "":
    
    qr6 = cmm.Qrcode(ip_qr6,cliente,rele,portao6,notifica, "Leitor 6") 
    qrcode6 = threading.Thread(target=thread_qr6) 
    qrcode6.start()

if ip_qr7 != "":
    
    qr7 = cmm.Qrcode(ip_qr7,cliente,rele,portao7,notifica, "Leitor 7") 
    qrcode7 = threading.Thread(target=thread_qr7) 
    qrcode7.start()

if ip_qr8 != "":
    
    qr8 = cmm.Qrcode(ip_qr8,cliente,rele,portao8,notifica, "Leitor 8") 
    qrcode8 = threading.Thread(target=thread_qr8) 
    qrcode8.start()

if ip_qr9 != "":
    
    qr9 = cmm.Qrcode(ip_qr9,cliente,rele,portao9,notifica, "Leitor 9") 
    qrcode9 = threading.Thread(target=thread_qr9) 
    qrcode9.start()

if ip_qr10 != "":
    
    qr10 = cmm.Qrcode(ip_qr10,cliente,rele,portao10,notifica, "Leitor 10") 
    qrcode10 = threading.Thread(target=thread_qr10) 
    qrcode10.start()

if ip_qr11 != "":
    
    qr11 = cmm.Qrcode(ip_qr11,cliente,rele,portao11,notifica, "Leitor 11") 
    qrcode11 = threading.Thread(target=thread_qr11) 
    qrcode11.start()

if ip_qr12 != "":
    
    qr12 = cmm.Qrcode(ip_qr12,cliente,rele,portao12,notifica, "Leitor 12") 
    qrcode12 = threading.Thread(target=thread_qr12) 
    qrcode12.start()

if ip_qr13 != "":
    
    qr13 = cmm.Qrcode(ip_qr13,cliente,rele,portao13,notifica, "Leitor 13") 
    qrcode13 = threading.Thread(target=thread_qr13) 
    qrcode13.start()

if ip_qr14 != "":
    
    qr41 = cmm.Qrcode(ip_qr14,cliente,rele,portao14,notifica, "Leitor 14") 
    qrcode14 = threading.Thread(target=thread_qr14) 
    qrcode14.start()

if ip_qr15 != "":
    
    qr15 = cmm.Qrcode(ip_qr15,cliente,rele,portao15,notifica, "Leitor 15") 
    qrcode15 = threading.Thread(target=thread_qr15) 
    qrcode15.start()

if ip_qr16 != "":
    
    qr16 = cmm.Qrcode(ip_qr16,cliente,rele,portao16,notifica, "Leitor 16") 
    qrcode16 = threading.Thread(target=thread_qr16) 
    qrcode16.start()





    
    



