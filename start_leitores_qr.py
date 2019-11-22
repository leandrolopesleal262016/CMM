import time
import biblioteca_CMM as cmm
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import threading # Modulo superior Para executar as threads
import sys
import _thread as thread


def log(texto): # Metodo para registro dos eventos no log.txt (exibido na interface grafica)

    hs = time.strftime("%H:%M:%S") 
    data = time.strftime('%d/%m/%y')

    texto = str(texto)

    escrita = ("{} - {}  Evento:  {}\n").format(data, hs, texto)
    escrita = str(escrita)

    l = open("/var/www/html/log/log.txt","a")
    l.write(escrita)
    l.close()

##log("Iniciou start dos leitores...")

banco = cmm.Banco() # Oprerações CRUD no banco CMM

cliente = banco.consulta("config","cliente")
nome_cliente = banco.consulta("config","nome_cliente")
ip_cliente = banco.consulta("config","ip_cliente")
notifica = banco.consulta("comandos","notifica") # Se vai notificar ou não o condfy

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

mensagem_1 = banco.consulta("leitores_qrcode","mensagem_1")
mensagem_2 = banco.consulta("leitores_qrcode","mensagem_2")
mensagem_3 = banco.consulta("leitores_qrcode","mensagem_3")
mensagem_4 = banco.consulta("leitores_qrcode","mensagem_4")
mensagem_5 = banco.consulta("leitores_qrcode","mensagem_5")
mensagem_6 = banco.consulta("leitores_qrcode","mensagem_6")
mensagem_7 = banco.consulta("leitores_qrcode","mensagem_7")
mensagem_8 = banco.consulta("leitores_qrcode","mensagem_8")
mensagem_9 = banco.consulta("leitores_qrcode","mensagem_9")
mensagem_10 = banco.consulta("leitores_qrcode","mensagem_10")
mensagem_11 = banco.consulta("leitores_qrcode","mensagem_11")
mensagem_12 = banco.consulta("leitores_qrcode","mensagem_12")
mensagem_13 = banco.consulta("leitores_qrcode","mensagem_13")
mensagem_14 = banco.consulta("leitores_qrcode","mensagem_14")
mensagem_15 = banco.consulta("leitores_qrcode","mensagem_15")
mensagem_16 = banco.consulta("leitores_qrcode","mensagem_16")


def thread_qr1(): # Programa do QR Code 1

    rele = 1
##    notifica = "1"
    
    while(1):

        try:
            
            qr1 = cmm.Qrcode(ip_qr1,cliente,rele,portao1,notifica,"Leitor 1",mensagem_1) # instancia a classe leitor (a thread quem da o start)   
            qr1.start() # Inicia o programa qrcode correspondente

        except Exception as err:
            
            time.sleep(3)

def thread_qr2(): # Programa do QR Code 2

    rele = 1
##    notifica = "1" 

    while(1):

        try:

            qr2 = cmm.Qrcode(ip_qr2,cliente,rele,portao2,notifica, "Leitor 2",mensagem_2)    
            qr2.start() 

        except:
            
            time.sleep(3)

def thread_qr3(): # Programa do QR Code 3

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr3 = cmm.Qrcode(ip_qr3,cliente,rele,portao3,notifica, "Leitor 3",mensagem_3)    
            qr3.start()

        except:
            
            time.sleep(3)

def thread_qr4(): # Programa do QR Code 4

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr4 = cmm.Qrcode(ip_qr4,cliente,rele,portao4,notifica, "Leitor 4",mensagem_4)     
            qr4.start()

        except:
            
            time.sleep(3)

def thread_qr5(): # Programa do QR Code 5

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr5 = cmm.Qrcode(ip_qr5,cliente,rele,portao5,notifica, "Leitor 5",mensagem_5)     
            qr5.start()

        except:
            
            time.sleep(3)

def thread_qr6(): # Programa do QR Code 6

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr6 = cmm.Qrcode(ip_qr6,cliente,rele,portao6,notifica, "Leitor 6",mensagem_6)    
            qr6.start()

        except:
            
            time.sleep(3)

def thread_qr7(): # Programa do QR Code 7

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr7 = cmm.Qrcode(ip_qr7,cliente,rele,portao7,notifica, "Leitor 7",mensagem_7)     
            qr7.start()

        except:
            
            time.sleep(3)

def thread_qr8(): # Programa do QR Code 8

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr8 = cmm.Qrcode(ip_qr8,cliente,rele,portao8,notifica, "Leitor 8",mensagem_8)     
            qr8.start()

        except:
            
            time.sleep(3)

def thread_qr9(): # Programa do QR Code 9

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr9 = cmm.Qrcode(ip_qr9,cliente,rele,portao9,notifica, "Leitor 9",mensagem_9)     
            qr9.start()

        except:
            
            time.sleep(3)

def thread_qr10(): # Programa do QR Code 10

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr10 = cmm.Qrcode(ip_qr10,cliente,rele,portao10,notifica, "Leitor 10",mensagem_10)    
            qr10.start()

        except:
            
            time.sleep(3)

def thread_qr11(): # Programa do QR Code 11

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr11 = cmm.Qrcode(ip_qr11,cliente,rele,portao11,notifica, "Leitor 11",mensagem_11)    
            qr11.start()

        except:
            
            time.sleep(3)

def thread_qr12(): # Programa do QR Code 12

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr12 = cmm.Qrcode(ip_qr12,cliente,rele,portao12,notifica, "Leitor 12",mensagem_12)     
            qr12.start()

        except:
            
            time.sleep(3)

def thread_qr13(): # Programa do QR Code 13

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr13 = cmm.Qrcode(ip_qr13,cliente,rele,portao13,notifica, "Leitor 13",mensagem_13)     
            qr13.start()

        except:
            
            time.sleep(3)

def thread_qr14(): # Programa do QR Code 14

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr14 = cmm.Qrcode(ip_qr14,cliente,rele,portao14,notifica, "Leitor 14",mensagem_14)    
            qr14.start()

        except:
            
            time.sleep(3)

def thread_qr15(): # Programa do QR Code 15

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr15 = cmm.Qrcode(ip_qr15,cliente,rele,portao15,notifica, "Leitor 15",mensagem_15)     
            qr15.start()

        except:
            
            time.sleep(3)

def thread_qr16(): # Programa do QR Code 16

    rele = 3
##    notifica = "0"

    while(1):

        try:

            qr16 = cmm.Qrcode(ip_qr16,cliente,rele,portao16,notifica, "Leitor 16",mensagem_16)     
            qr16.start()

        except:
            
            time.sleep(3)
    

if ip_qr1 != "":
            
    qrcode1 = threading.Thread(target=thread_qr1) # Cria e da start ma thread
    qrcode1.start()

if ip_qr2 != "":
    
    qrcode2 = threading.Thread(target=thread_qr2) 
    qrcode2.start()

if ip_qr3 != "":
            
    qrcode3 = threading.Thread(target=thread_qr3) 
    qrcode3.start()

if ip_qr4 != "":    
    
    qrcode4 = threading.Thread(target=thread_qr4) 
    qrcode4.start()

if ip_qr5 != "":    
    
    qrcode5 = threading.Thread(target=thread_qr5) 
    qrcode5.start()

if ip_qr6 != "":    
     
    qrcode6 = threading.Thread(target=thread_qr6) 
    qrcode6.start()

if ip_qr7 != "":    
    
    qrcode7 = threading.Thread(target=thread_qr7) 
    qrcode7.start()

if ip_qr8 != "":    
    
    qrcode8 = threading.Thread(target=thread_qr8) 
    qrcode8.start()

if ip_qr9 != "":    
    
    qrcode9 = threading.Thread(target=thread_qr9) 
    qrcode9.start()

if ip_qr10 != "":    
     
    qrcode10 = threading.Thread(target=thread_qr10) 
    qrcode10.start()

if ip_qr11 != "":    
     
    qrcode11 = threading.Thread(target=thread_qr11) 
    qrcode11.start()

if ip_qr12 != "":
    
    qrcode12 = threading.Thread(target=thread_qr12) 
    qrcode12.start()

if ip_qr13 != "":    
    
    qrcode13 = threading.Thread(target=thread_qr13) 
    qrcode13.start()

if ip_qr14 != "":    
     
    qrcode14 = threading.Thread(target=thread_qr14) 
    qrcode14.start()

if ip_qr15 != "":    
    
    qrcode15 = threading.Thread(target=thread_qr15) 
    qrcode15.start()

if ip_qr16 != "":    
    
    qrcode16 = threading.Thread(target=thread_qr16) 
    qrcode16.start()





    
    



