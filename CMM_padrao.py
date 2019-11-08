#!/usr/bin/env python3
# coding=UTF-8

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 05/11/2019

import RPi.GPIO as GPIO
import time
import biblioteca_CMM as cmm
import cmm_io_entradas as entradas
import cmm_io_saidas as saidas

from atualiza_monitor import Monitor
import modulo_garagem as modulo_garagem
import servidor_qr as servidor_qr

from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import threading # Modulo superior Para executar as threads
import sys
import socket
import _thread as thread

socket.setdefaulttimeout(2) # limite de 2 segundos para enviar o socket

os.system("sudo chmod 777 -R /var/www/html/log") # Permissão para escrever no log
os.system("mpg123 /home/pi/CMM/mp3/sistema_carregado.mp3")

def log(texto): # Metodo para registro dos eventos no log.txt (exibido na interface grafica)

    hs = time.strftime("%H:%M:%S") 
    data = time.strftime('%d/%m/%y')

    texto = str(texto)

    if texto == "*":

        l = open("/var/www/html/log/log.txt","a")
        l.write("\n")
        l.close()

    else:        

        texto = texto.replace("'","")
        texto = texto.replace(",","")
        texto = texto.replace("(","")
        texto = texto.replace(")","")

        escrita = ("{} - {}  Evento:  {}\n").format(data, hs, texto)
        escrita = str(escrita)

        l = open("/var/www/html/log/log.txt","a")
        l.write(escrita)
        l.close()
    
log("Reiniciou o sistema") 

# Imprimi o nome e o IP do equipamento no log da interface

nome = os.popen('hostname').readline()
nome = str(nome)
nome = nome.replace("\n","")
ip = os.popen('hostname -I').readline()
ip = str(ip)
ip = ip.replace("\n","")
txt = ("Nome desta maquina",nome)
txt = str(txt)
log(txt)

print("Nome desta maquina",nome,"com IP",ip)

############################ INICIA AS CLASSES DA biblioteca_CMM ###############################################

rele = cmm.Rele() # inicia a classe rele com port A em 0
narrador = cmm.Narrador()
temperatura = cmm.Temperatura()
email = cmm.Email()
clima = cmm.Clima()
banco = cmm.Banco() # Oprerações CRUD no banco CMM
cliente = banco.consulta("config","cliente")
evento = cmm.Evento("0054") # Inicia a classe evento com o codigo do cliente

################################################################################################################

def thread_monitor(): # Programa que mantem a conexão com o QR Code

    print("\nPrograma Monitor em execução\n")

    monitor = Monitor()

    while(1):        

        monitor.loop()
        time.sleep(0.3)
    
monitor = threading.Thread(target=thread_monitor)
monitor.start()

def gar1():

    exp1 = banco.consulta("entradas","exp1")       

    if(exp1 == "garagem1"):

##        log("Programa Garagem 1 executando no expansor 1...")
        
        modulo_garagem.Garagem1()

g1 = threading.Thread(target=gar1)
g1.start()

def gar2():

    exp2 = banco.consulta("entradas","exp2")    

    if(exp2 == "garagem2"):

##        log("Programa Garagem 2 executando no expansor 2...")
        
        modulo_garagem.Garagem2()

g2 = threading.Thread(target=gar2)
g2.start()


def Serv_qr():    
        
        servidor_qr.Servidor_qr()

sqr = threading.Thread(target=Serv_qr)
sqr.start()

# Zera registros para não abrir porto por eventos que ficaram na memoria

status = open("/home/pi/CMM/status_social.cmm","w") 
status.write("0")
status.close()

status = open("/home/pi/CMM/status_eclusa.cmm","w") 
status.write("0")
status.close()

banco.atualiza("comandos","abre_social_externo","0")
banco.atualiza("comandos","abre_social_interno","0")

banco.atualiza("comandos","reset","0")


def Intertravamento(comando): # Inicia a thread dos portoes sociais importando a classe Rele

        audio = banco.consulta("comandos","audio")
        eventos = banco.consulta("comandos","eventos")
                       
        hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log        
                
        cont = 0

        a = open("/home/pi/CMM/status_social.cmm","r")
        abre_social = a.read()
        a.close()

        b = open("/home/pi/CMM/status_eclusa.cmm","r")
        abre_eclusa = b.read()
        b.close()

        ihm_soc1 = banco.consulta("comandos","abre_social_externo")
        ihm_soc2 = banco.consulta("comandos","abre_social_interno")
    
        if comando == "abre_social":
            
            pm1 = entradas.pm1()
                                
            if pm1 == "0": # O portão social já esta aberto

                log("O portão Social já esta aberto")
                            
                os.system("mpg123 /home/pi/CMM/mp3/social_aberto.mp3")
                time.sleep(1)

            else: # Se o portão Social esta fechado então pode abrir
               
                pm2 = entradas.pm2()

                if pm2 == "0":

                    log("Agurade o fechamento do Social Externo")
                    os.system("mpg123 /home/pi/CMM/mp3/aguarde_fechamento.mp3") # Necessario manter esse audio sempre ativo
                    time.sleep(1)
                                
                if pm2 == "1": # Se Ponto magnético Eclusa fechado
                    
                    s = open("/home/pi/CMM/status_social.cmm","w")
                    s.write("1")
                    s.close()

                    saidas.liga_blq2() # Aqui abrimos o contato da eclusa para impedir que ela seja aberta enquanto o social esta aberto
                  
                    social(ihm_soc1)
                   
                    time.sleep(1) # Tempo minimo para o portão abrir
                   
                    pm1 = entradas.pm1()
                                        
                    if pm1 == "1": # Portão fechado pois não abriu com o comando
                        
                        fechadura = banco.consulta("config","fechadura")

                        if fechadura == "magnetica":

                            os.system("mpg123 /home/pi/CMM/mp3/empurre.mp3")
                            
                            saidas.pulso_abre1() # Pulso para abrir direto o portão sem intertravamento (Social)

                            log("Abrindo novamente o social...")

                            saidas.desliga_blq2()

                            status = open("/home/pi/CMM/status_social.cmm","w") 
                            status.write("0")
                            status.close()
                            

                        if fechadura == "motor":

                            log("Portão Social emperrado")

                            os.system("mpg123 /home/pi/CMM/mp3/social_emperrado.mp3")
                                                    
                            saidas.desliga_blq2() # Fecha o contato e libera a eclusa para ser acionada

                            status = open("/home/pi/CMM/status_social.cmm","w") 
                            status.write("0")
                            status.close()

                                               
                            if eventos == "1":

                                evento.enviar("E","132","008") # Envia portão emperrado                        

                    if pm1 == "0": # Portão abriu

                        if eventos == "1":

                            evento.enviar("E","133","001") # Envia abriu portão
                        
                        contador = 200 # Tempo maximo para o social ficar aberto 30 segundos
                        log("Esperando por 20 segundos o portão Social fechar...")

                        while contador > 0: # enquanto portão está aberto
                            
                            pm1 = entradas.pm1()
                            
                            if pm1 == "1": # portão fechou

                                log("Portão Social fechou")

                                if eventos == "1":

                                    evento.enviar("R","133","001") # Envia fechamento
                                
                                contador = 1
                                                            
                                s = open("/home/pi/CMM/status_social.cmm","w")
                                s.write("0")
                                s.close()

                                saidas.desliga_blq2() # Fecha o contato e libera a eclusa para ser acionada

                                break

                            if (pm1 == "0" and contador == 1): # Portão ainda aberto após 15 segundos de espera

                                log("Portão Social aberto por muito tempo")

                                if eventos == "1":

                                    evento.enviar("E","132","010") # Envia falha no fechamento social

                                os.system("mpg123 /home/pi/CMM/mp3/obstrucao.mp3")
                                
                                status = open("/home/pi/CMM/status_social.cmm","w") # Para não disparar o arrombamento
                                status.write("1")
                                status.close()

                                contador = 0

                                saidas.desliga_blq2() # Fecha o contato e libera a eclusa para ser acionada                                
                               
                            ctw2 = entradas.ctw2()                            
                            
                            if (ctw2 == "1"):# Entrada para abrir o portão da eclusa
                                
                                log("Aguarde o fechamento do Social Externo")
                                os.system("mpg123 /home/pi/CMM/mp3/aguarde_fechamento.mp3") # Necessario manter esse audio sempre ativo
                                time.sleep(1)
                                
                            time.sleep(0.1) # 1 segundo
                            contador = contador - 1                            
                
                pm2 = entradas.pm2()
  
                        
        if comando == "abre_eclusa":
            
            pm2 = entradas.pm2()           

            if pm2 == "0": # O portão Eclusa já esta aberto

                log("O portão Eclusa já esta aberto")

                os.system("mpg123 /home/pi/CMM/mp3/eclusa_aberto.mp3")
                time.sleep(1)

            else: # Se o portão Eclusa esta fechado então pode abrir
                
                pm2 = entradas.pm2()
                pm1 = entradas.pm1()

                if pm1 == "1": # Ponto magnético Social fechado, pode abrir a eclusa
                    
                    s = open("/home/pi/CMM/status_eclusa.cmm","w")
                    s.write("1")
                    s.close()

                    saidas.liga_blq1() # Impede o social de abrir enquanto a eclusa esta aberta
                    
                    eclusa(ihm_soc2)                                        
                   
                    time.sleep(1) # Tempo de espera para o portão abrir
                    
                    pm2 = entradas.pm2()
                    
                    if pm2 == "1": # Portão fechado não abriu após o comando

                       fechadura = banco.consulta("config","fechadura")

                       if fechadura == "magnetica":

                           os.system("mpg123 /home/pi/CMM/mp3/empurre.mp3")

                           log("Abrindo novamente a eclusa")
                           
                           saidas.pulso_abre2()
                           
                           saidas.desliga_blq1()

                           status = open("/home/pi/CMM/status_eclusa.cmm","w") 
                           status.write("0")
                           status.close()

                       if fechadura == "motor":

                           log("Portão Eclusa emperrado")
                           
                           os.system("mpg123 /home/pi/CMM/mp3/eclusa_emperrado.mp3")
                                
                           saidas.desliga_blq1() # Libera o social para abrir mesmo com a eclusa aberta

                           status = open("/home/pi/CMM/status_eclusa.cmm","w") 
                           status.write("0")
                           status.close()
                           
                           if eventos == 1:

                               evento.enviar("E","132","009") # Envia portão emperrado

                    if pm2 == "0": # Portão aberto

                        if eventos == 1:

                            evento.enviar("E","133","003") # Envia abertura
                        
                        contador = 200 # Tempo maximo para eclusa ficar aberta 20 segundos
                        
                        log("Esperando por 20 segundos o portão Eclusa fechar...")

                        while contador > 0: # enquanto portão está aberto
                            
                            pm2 = entradas.pm2() 

                            if pm2 == "1": # portão fechou

                                log("Portão Eclusa fechou")

                                if eventos == "1":

                                    evento.enviar("R","133","003") # Envia fechamento
                                
                                contador = 1
                                
                                s = open("/home/pi/CMM/status_eclusa.cmm","w")
                                s.write("0")
                                s.close()

                                saidas.desliga_blq1() # Libera o social para abrir

                                break

                            if (pm2 == "0" and contador == 1): # Portão ainda aberto após 15 segundos de espera

                                log("Portão Eclusa aberto por muito tempo")

                                if eventos == "1":

                                    evento.enviar("E","132","011") # Envia falha no fechamento
                                
                                os.system("mpg123 /home/pi/CMM/mp3/obstrucao.mp3")
                                
                                status = open("/home/pi/CMM/status_eclusa.cmm","w") # Para não disparar o arrombamento
                                status.write("1")
                                status.close()                                

                                saidas.desliga_blq1() # Libera o social para abrir mesmo com a eclusa aberta

                                contador = 0
                            
                            ctw1 = entradas.ctw1()
                            
                            if (ctw1 == "1"): # Alguem esta tentando abrir o social com a eclusa aberta

                                log("Aguarde o fechamento do Social Interno")
                                os.system("mpg123 /home/pi/CMM/mp3/aguarde_fechamento.mp3") # Manter esse audio sempre ativo
                                time.sleep(1)
                                

                            time.sleep(0.1) # 1 segundo
                            contador = contador - 1
def social(mensagem): # Mensagem informa se o evento veio pelo interface web ou do local

    status = open("/home/pi/CMM/status_social.cmm","w") # Para não disparar o arrombamento
    status.write("1")
    status.close()

    fechadura = banco.consulta("config","fechadura")
    audio = banco.consulta("config","audio")

    if mensagem == "0": # local

        log("Abrindo social...")    

    saidas.pulso_abre1() # Pulso para abrir direto o portão sem intertravamento (Social)

    if mensagem == "1": # Via interface web

        log("Abrindo Social pela Central de Monitoramento...")
        os.system("mpg123 /home/pi/CMM/mp3/acionando_pela_central.mp3")    

    if audio == "1":        

        if mensagem == "0":

            if fechadura == "motor":

                os.system("mpg123 /home/pi/CMM/mp3/abrindo_social.mp3")                    

    status = open("/home/pi/CMM/status_social.cmm","w") 
    status.write("0")
    status.close()
    
def eclusa(mensagem):

    status = open("/home/pi/CMM/status_eclusa.cmm","w") # Para não disparar o arrombamento
    status.write("1")
    status.close()

    fechadura = banco.consulta("config","fechadura")
    audio = banco.consulta("config","audio")

    saidas.pulso_abre2() # Pulso para abrir direto o portão sem intertravamento (Eclusa)

    if mensagem == "0": # local

        log("Abrindo eclusa...")

    if mensagem == "1":

        log("Abrindo Eclusa pela Central de Monitoramento...")
        os.system("mpg123 /home/pi/CMM/mp3/acionando_pela_central.mp3")  

    if audio == "1":

        if mensagem == "0":

            if fechadura == "motor":

                os.system("mpg123 /home/pi/CMM/mp3/abrindo_eclusa.mp3")
            
    status = open("/home/pi/CMM/status_eclusa.cmm","w") 
    status.write("0")
    status.close()

def Portoes_sociais(Rele): # Programa
    
    log("Programa Sociais em execução ")

    saida = 0
    qbv_acionado = 0
    banco = cmm.Banco()
    qbv2 = entradas.qbv2()
    print("qbv2",qbv2,type(qbv2))
           
    while(1):

        habilita_intertravamento = banco.consulta("intertravamento","habilitado")
                
        pm1 = entradas.pm1()
        pm2 = entradas.pm2()
       
        ctw1 = entradas.ctw1()
        ctw2 = entradas.ctw2()

        qbv1 = entradas.qbv1()
        
        ihm_soc1 = banco.consulta("comandos","abre_social_externo")
        ihm_soc2 = banco.consulta("comandos","abre_social_interno")
       
        if ctw1 == "1" or ihm_soc1 == "1":                            

            if habilita_intertravamento == "0":

                log("Intertravamento desabilitado\n")
                
                social(ihm_soc1)

                status = open("/home/pi/CMM/status_social.cmm","w") 
                status.write("0")
                status.close()

            else:

                log("Intertravamento habilitado\n")

                status = open("/home/pi/CMM/status_social.cmm","w")
                status.write("1")
                status.close()
         
                Intertravamento("abre_social")

                status = open("/home/pi/CMM/status_social.cmm","w")
                status.write("0")
                status.close()

            banco.atualiza("comandos","abre_social_externo","0")
            
        if ctw2 == "1" or ihm_soc2 == "1":            

            if habilita_intertravamento == "0":

                log("Intertravamento desabilitado\n")
                
                eclusa(ihm_soc2) 
                
            else:
                
                status = open("/home/pi/CMM/status_eclusa.cmm","w")
                status.write("1")
                status.close()

                Intertravamento("abre_eclusa")

                status = open("/home/pi/CMM/status_eclusa.cmm","w")
                status.write("0")
                status.close()

                saida = 1

            banco.atualiza("comandos","abre_social_interno","0")
                   
        if qbv1 == "1" and qbv_acionado == 0:

            time.sleep(0.2)
            qbv1 = entradas.qbv1()   

            if qbv1 == "1":

                saidas.pulso_abre1()
                
                log("Acionado o quebra de vidro da Eclusa")                
                os.system("mpg123 /home/pi/CMM/mp3/emergencia.mp3")

                status = open("/home/pi/CMM/status_social.cmm","w")
                status.write("1")
                status.close()

                status = open("/home/pi/CMM/status_eclusa.cmm","w")
                status.write("1")
                status.close()

                saidas.liga_abre1()
                saidas.liga_abre2()
                
                qbv_acionado = 1

        if qbv1 == "0" and qbv_acionado == 1:

            time.sleep(0.2)
            qbv1 = entradas.qbv1()

            if qbv1 == "0":
                
                log("Restaurou quebra de vidro da Eclusa")
                os.system("mpg123 /home/pi/CMM/mp3/restaurada_emergencia.mp3")

                saidas.desliga_abre1()
                saidas.desliga_abre2()

                fechadura = banco.consulta("config","fechadura")

                if fechadura == "magnetica":
                
                    time.sleep(1)

                if fechadura == "motor":

                    log("Aguardando 5 segundos para fechamento dos portoes sociais")                
                    time.sleep(5)

                os.system("mpg123 /home/pi/CMM/mp3/automatico.mp3")    

                status = open("/home/pi/CMM/status_social.cmm","w")
                status.write("0")
                status.close()

                status = open("/home/pi/CMM/status_eclusa.cmm","w")
                status.write("0")
                status.close()                
                
                
                qbv_acionado = 0
            
        time.sleep(0.1) 

        
################################################ THREADS ROTINAS #################################################
        
def Arrombamento(Rele): # Inicia a thread arrombamento de portões

    time.sleep(2)
    
    log("Programa arrombamento de portões sociais em execução")

    ar1 = 0 # Variavel arrombamento portão 1
    ar2 = 0
    
    reset_ar1 = 0 # Reseta a variavel do portão para 0
    reset_ar2 = 0
    
    segunda_vez1 = 0
    segunda_vez2 = 0
    
    cont1 = 10 # Contador individual para cada reset de arrombamento
    cont2 = 10

    audio = banco.consulta("comandos","audio")
    eventos = banco.consulta("comandos","eventos")

       
    while(1):

        try:
        
            pm1 = entradas.pm1()
            pm2 = entradas.pm2()

            a = open("/home/pi/CMM/status_social.cmm","r")
            abre_social = a.read()
            a.close()

            b = open("/home/pi/CMM/status_eclusa.cmm","r")
            abre_eclusa = b.read()
            b.close()

            if abre_social == "1" or abre_eclusa == "1":

                saidas.desliga_sirene()

            if ar1 == 0 and reset_ar1 == 0 and segunda_vez1 == 1:

                saidas.desliga_sirene()
                segunda_vez1 = 0

            if ar2 == 0 and reset_ar2 == 0 and segunda_vez2 == 1:

                saidas.desliga_sirene()
                segunda_vez2 = 0
                    
            if abre_social == "0" and pm1 == "0" and ar1 == 0:

                time.sleep(1) # Filtra algum possivel ruido de até 500 milissegundos

                a = open("/home/pi/CMM/status_social.cmm","r")
                abre_social = a.read()
                a.close()

                pm1 = entradas.pm1()

                if abre_social == "0" and pm1 == "0": # Se realmente foi um arrombamento liga sirene e notifica o Moni
                    
                    log("Arrombamento do portão social")
                    os.system("mpg123 /home/pi/CMM/mp3/violacao_social.mp3")
                    
                    saidas.liga_sirene()

                    if eventos == "1":

                        evento.enviar("E","132","002")
                    
                    ar1 = 1
                    reset_ar1 = 1

            if ar1 == 1 and reset_ar1 == 1:

                cont1 = cont1 - 1 # A primeira vez que acontece o arrombamento reseta depois de 20 segundos
                time.sleep(1)

                if cont1 == 340:

                    saidas.desliga_sirene()

                if cont1 <= 0:

                    saidas.desliga_sirene()

                    if eventos == "1":

                        evento.enviar("R","132","002")

                    cont1 = 350 # Se apos o reset o portão continuar aberto envia o evento novamente  espera 5 min
                    ar1 = 0
                    reset_ar1 = 0
                    segunda_vez1 = 1

                    saidas.desliga_sirene() # Garantia que esteja desligada
                    
                    

            if abre_eclusa == "0" and pm2 == "0" and ar2 == 0:

                time.sleep(1) # Filtra algum possivel ruido de até 500 milissegundos

                b = open("/home/pi/CMM/status_eclusa.cmm","r")
                abre_eclusa = b.read()
                b.close()

                pm2 = entradas.pm2()

                if abre_eclusa == "0" and pm2 == "0": # Se realmente foi um arrombamento liga sirene e notifica o Moni

                    log("Arrombamento do portão Eclusa")
                    os.system("mpg123 /home/pi/CMM/mp3/violacao_eclusa.mp3")

                    saidas.liga_sirene()

                    if eventos == "1":

                        evento.enviar("E","132","004")
                    
                    ar2 = 1
                    reset_ar2 = 1

            if ar2 == 1 and reset_ar2 == 1:

                cont2 = cont2 - 1 # A primeira vez que acontece o arrombamento reseta depois de 20 segundos
                time.sleep(1)

                if cont2 == 340:

                    saidas.desliga_sirene()

                if cont2 <= 0:

                    saidas.desliga_sirene()

                    if eventos == "1":

                        evento.enviar("R","132","004")

                    cont2 = 350 # Se apos o reset o portão continuar aberto envia o evento novamente e espera 5 min
                    ar2 = 0
                    reset_ar2 = 0
                    segunda_vez2 = 1

                    saidas.desliga_sirene()
            
            time.sleep(1)   

        except Exception as err:

            print("Erro na rotina de alarmes dos sociais")
            log("Erro na rotina de alarmes dos sociais",err)
            
        time.sleep(5)
        
def alarmes_garagem1():
            
        if pmg1 == "0" and mudanca1 == 0 and status_tx1 == "0": # Violação do portão da garagem                              

            cont = 10
            violacao = 1
            
            while cont > 0:

                t = open("/home/pi/CMM/status_garagem_1.cmm","r")
                status_tx1 = t.read()
                t.close() 

                pmg1 = leitor("leitor1_in1")

                if pmg1 == "0" and status_tx1 == "0":

                    violacao = 1
                    
                if pmg1 == "1":
                    
                    violacao = 0
                    break

                time.sleep(0.1)
                cont = cont - 1

            if violacao == 0: # Filtrou ruido

                pass

            if violacao == 1:

                log("violação do portão garagem 1")

                s.desliga_rele3_exp1() # Sinal Vermelho

                s.liga_rele4_exp1() # Sirene
                            
                #evento.enviar("E","132","014")

                cont = 30 # Tempo maximo de espera

                log("Aguardando portão fechar")

                while cont > 0:

                    pmg1 = leitor("leitor1_in1")

                    if(pmg1 == "0"): # Portão ainda aberto                                      

                        time.sleep(1)
                        cont = cont - 1
                            
                    if (pmg1 == "1"): # Portão ja fechou

                        log("Portão fechou")

                        t = open("/home/pi/CMM/status_garagem_1.cmm","w")
                        t.write("0")
                        t.close()


                        
                        cont = 0
                        time.sleep(1)
                        
                        s.desliga_rele4_exp1() # Desliga sirene
                        
                        break            
                
##                s.desliga_rele4_exp1() # Desliga sirene

##                violacao = 0
                
                time.sleep(30)
                
        time.sleep(1)        

def Buffer():

    socket.setdefaulttimeout(3) # limite em segundos para enviar o socket

    host = '172.20.1.5'  # '172.20.1.5' Host servidor  Moni
    port = 4010          # 4010 Porta máquina receptora

    log("Programa buffer de eventos em execução")

    enviado = 0

    while(1):        

        socket.setdefaulttimeout(3)

        b = open("/home/pi/CMM/buffer_eventos.txt","r")
        
        for line in b:

            ln = line
            evento = ln.replace("\n","")
            
            if evento != "": # Se houver alguma coisa para enviar

                # Tentanto enviar o evento",evento...

                try:
        
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect ((host,port))

                    command = (evento + "\r") # ("7000 185808E30500008")  # Envia abriu portão da eclusa para a central de monitormento
                    s.send(str.encode(command))
                    reply = s.recv(1024)
                    log(reply.decode('utf-8'))
                    s.close()

                    enviado = 1                    
                                
                except Exception as err: ## Não conseguiu enviar o evento, sem conexão no momento                    

                    s.close()

                    time.sleep(10)
                    break
                
                if enviado == 1:
                                               
                    txt = ("Evento enviado ",evento)
                    log(txt)

                    # Cria uma lista e adiciona todos as linhas encontradas em buffer.txt

                    lista = []

                    try:

                        txt = open("/home/pi/CMM/buffer_eventos.txt","r")
                        for l in txt:                        
                            l = l.replace("\n","") # Coloca na lista o evento ja editado
                            lista.append(evento)
                        
                        # Exclui o item enviado da lista

                        for i in lista:
                            
                            if i == evento:
                                indice = lista.index(i)
                                txt = ("Excluindo o evento",evento,"posicao",indice)
                                log(txt)
                                del(lista[indice])
                                nova_lista = lista
                                
                        txt.close()

                        # Zera o arquivo buffer

                        tx = open("/home/pi/CMM/buffer_eventos.txt","w") 
                        tx.close()

                        # Reescreve o texto com a nova lista editada

                        txt = open("/home/pi/CMM/buffer_eventos.txt","a")
                        for i in nova_lista:
                            txt.write(i + "\n")
                        txt.close()    
                            
                        enviado = 0

                    except Exception as err:
                        txt = ("Erro",err)
                        log(txt)
            
        b.close() # Fecha o arquivo de texto em modo leitura    
        time.sleep(1)

def Servidor(Rele,Abre): 
    
    log("Programa Servidor em execução")
    socket.setdefaulttimeout(9999) # limite tempo socket
    
    host = '0.0.0.0'
    port = 5510

    time.sleep(0.1)

    log("iniciou o servidor")
    
    txt = ("Servidor: ",host, " porta: ", port)
    log(txt)

    while(1):

        
    ############################################### Thread servidor p/ PHP e MONI #################################################################

            socket.setdefaulttimeout(9999)


            def setupServer():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # "AF_NET" trabalharemos com protocolo ipv4, .SOCK_STREAM USAREMOS TCP
                
                try:
                    s.bind((host, port))
                except socket.error as msg:
                    log (msg)
                
                return s

            def setupConnection():
                s.listen(5)
                conn, address = s.accept()
                txt = ("Conectado com: " + address[0] + ":" + str(address[1]))
                log(txt)
                return conn


            def dataTransfer(conn):  # Loop de transferencia e recepção de dados

                log("Entrou no data transfer")

                while True:
                    
                    rele = Rele()
                                                          
                    data = conn.recv(1024)  # Recebe o dado
                    data = data.decode('utf-8')
                    txt = ("data",data)
                    log(txt)
                    dataMessage = data.split(' ',1)# Separa o comando do resto dos dados
                    command = dataMessage[0]

                    txt = ("command",command)
                    log(txt)

                    (comando,resto) = data.split("\r") # Divide os dados da variavel data e guarda uma parte em comando e eoutra em resto

                    txt = ("comando e resto",comando,resto)
                    log(txt)
                   
                    if(comando == "SET1"):

                        log("Abrindo portão Social pelo Moni")

                        status = open("/home/pi/CMM/status_social.cmm","w") 
                        status.write("1")
                        status.close()
                        
                        rele.liga(4)

                        time.sleep(2)

                        rele.desliga(4)

                        time.sleep(15)

                        status = open("/home/pi/CMM/status_social.cmm","w") # Volta o arquivo para zero para ativar a verificação de arrombamento
                        status.write("0")
                        status.close()

                        conn.close()                        
                                            

                    elif(comando == "SET2"):
                        
                        log("Abrindo portão Eclusa pelo Moni")

                        status = open("/home/pi/CMM/status_eclusa.cmm","w") 
                        status.write("1")
                        status.close()
                        
                        rele.liga(5)

                        time.sleep(2)

                        rele.desliga(5)

                        time.sleep(15)

                        status = open("/home/pi/CMM/status_eclusa.cmm","w") # Volta o arquivo para zero para ativar a verificação de arrombamento
                        status.write("0")
                        status.close()
                        
                        conn.close()
                        
                       
                    elif(comando == "SET3"):
                        
                        log("reconheceu SET 3")                        
    
                        conn.close()                       

                    elif(comando == "SET4"):
                        log("Abrindo garagem")

                        s2 = Expansor()    
    
                        s2.liga_rele1_exp1() # Abre Garagem
                        s2.liga_rele1_exp1() 
                        time.sleep(3)
                        s2.desliga_rele1_exp1() 
                        s2.desliga_rele1_exp1()
                        
                        conn.close()
                        

                    elif(comando == "SET5"):
                        log("Abrindo subsolo")

                        s2 = Expansor()    
    
                        s2.liga_rele1_exp7() # Abre Garagem
                        s2.liga_rele1_exp7() 
                        time.sleep(3)
                        s2.desliga_rele1_exp7() 
                        s2.desliga_rele1_exp7()
                        
                        conn.close()

                    elif(comando == "SET 6"):
                        log("SET 6, RESET SOCIAL")
                        conn.close()

                    elif(comando == "SET 8"):
                        
                        log("SET 8, RESET ECLUSA")
                        conn.close()

                    elif(comando == "SET 9"):
                        
                        log("SET 9, RESET INTERFONES")
                        conn.close()

                    elif(comando == "SET 10"):
                        
                        log("SET 10, AUXILIAR 1 (ON/OFF)")
                        conn.close()

                    elif(comando == "SET 11"):
                        
                        log("SET 11, AUXILIAR 2 (ON/OFF)")
                        conn.close()

                    elif(comando == "SET 12"):
                        
                        log("APRESENTAÇÃO")
                        conn.close()
                                            

                    else:

                        txt = ("Recebido pelo servidor:",comando)
                        log(txt)

                        reply = 'ok'
                        conn.sendall(str.encode(reply))  # Envia o reply de volta para o cliente
                        conn.close()


            s = setupServer()

            while True:
                
              time.sleep(1) 

              txt = ("\nEscutando na porta",port)
              log(txt)
              try:

                  conn = setupConnection()
                  dataTransfer(conn)
                  log("Oiee")


              except Exception as err:

                  log("Encerrou conexão")
                    
        
#################### Instancia as Classes  #############################################

intertravamento = Intertravamento(cmm.Rele)


####################  Declara as threads dos programas disponiveis  ####################

sociais = threading.Thread(target=Portoes_sociais, args=(cmm.Rele,)) # deixar virgula depois do arg 1
##garagem1 = threading.Thread(target=Garagem1, args=(cmm.Rele,))
##garagem2 = threading.Thread(target=Garagem2, args=(cmm.Rele,))
arrombamento = threading.Thread(target=Arrombamento, args=(cmm.Rele,))
servidor = threading.Thread(target=Servidor, args=(cmm.Rele,))
##servidor_qr = threading.Thread(target=Servidor_qr)

buffer = threading.Thread(target=Buffer)


######################################### Start dos Programas  #############################################################

sociais.start() # Inicia o programa dos portões sociais
##garagem1.start() # Inicia o programa do portão de garagem
##garagem2.start() # Inicia o programa do portão de garagem
arrombamento.start() # Inicia o programa de automação
#servidor.start()
##servidor_qr.start() 
##buffer.start() # Inicia o programa Buffer


time.sleep(0.2) # Tempo para colocar as linhas impressas após as linhas de inicio de programa



log("Temperatura processador " + str(temperatura.cpu()) + "°C\n")  # obter temperatura

try:

    log("*")    
    log("O Sistema está conectado a internet")
    tempo = clima.clima_atual()
    tempo = str(tempo)
    log(tempo)
    narrador.falar(tempo)

except:

    os.system("mpg123 /home/pi/CMM/mp3/sem_internet.mp3")
    log("Sistema sem conexão a internet no momento")

while(1):

    reset = banco.consulta("comandos","reset")

    if reset == "1":

        banco.atualiza("comandos","reset","0")
        
        log("Reiniciando o sistema, aguarde...")

        os.system("mpg123 /home/pi/CMM/mp3/reiniciando_sistema.mp3")

        #os.system("sudo reboot now")

    # Colocar aqui o keep alive  
    

    time.sleep(1)

