#!/usr/bin/env python3
# coding=UTF-8

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 15/10/2019

import RPi.GPIO as GPIO
import time
import biblioteca_CMM as cmm
import cmm_io_entradas as entradas
import cmm_io_saidas as saidas

from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import threading # Modulo superior Para executar as threads
import sys
import socket
import _thread as thread

socket.setdefaulttimeout(2) # limite de 2 segundos para enviar o socket


def log(texto): # Metodo para registro dos eventos no log.txt (exibido na interface grafica)

    hs = time.strftime("%H:%M:%S") 
    data = time.strftime('%d/%m/%y')

    texto = str(texto)

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


os.system("mpg123 /home/pi/CMM/mp3/sistema_carregado.mp3") 

# Imprimi o nome e o IP do equipamento no log da interface

nome = os.popen('hostname').readline()
nome = str(nome)
nome = nome.replace("\n","")
ip = os.popen('hostname -I').readline()
ip = str(ip)
ip = ip.replace("\n","")
txt = ("Nome desta maquina",nome,"com IP",ip)
txt = str(txt)
log(txt)

############################ INICIA AS CLASSES DA biblioteca_CMM ###############################################

rele = cmm.Rele() # inicia a classe rele com port A em 0
narrador = cmm.Narrador()
temperatura = cmm.Temperatura()
email = cmm.Email()
clima = cmm.Clima()
evento = cmm.Evento("6639") # Inicia a classe evento com o codigo do cliente
banco = cmm.Banco() # Oprerações CRUD no banco CMM

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

##log ("\nTemperatura",temperatura.cpu(),"°C\n")  # obter temperatura

##email.enviar("O Programa acabou de reiniciar\nPosso enviar qualquer mensagem aqui...") # Não usar nenhum caracter especial na mensagem

##tempo = clima.clima_atual()
##log(tempo)

###evento.enviar_contact_id('E','132','001') # Evento ou Restauração / Evento / Setor


############################## Intertravamento dos portões sociais #############################################

   

status = open("/home/pi/CMM/status_social.cmm","w") 
status.write("0")
status.close()

status = open("/home/pi/CMM/status_eclusa.cmm","w") 
status.write("0")
status.close()

banco.atualiza("comandos","abre_social_externo","0")
banco.atualiza("comandos","abre_social_interno","0")
banco.atualiza("comandos","abre_garagem","0")
banco.atualiza("comandos","abre_subsolo","0")
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

    
        if comando == "abre_social":
            
            pm1 = entradas.pm1()
                                
            if pm1 == "0": # O portão social já esta aberto

                log("O portão social já esta aberto")
                            
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
                    
                    log("Abrindo portão Social")
                   
                    social()

                    if audio == "1": # Ativa as mensagens de abertura e fechamento

                        os.system("mpg123 /home/pi/CMM/mp3/abrindo_social.mp3")                   
                    
                    time.sleep(2) # Tempo minimo para o portão abrir
                   
                    pm1 = entradas.pm1()
                                        
                    if pm1 == "1": # Portão fechado pois não abriu com o comando

                        log("Portão Social emperrado")
                        

                        os.system("mpg123 /home/pi/CMM/mp3/social_emperrado.mp3")
                                                
                        saidas.desliga_blq2() # Fecha o contato e libera a eclusa para ser acionada

                        if eventos == "1":

                            evento.enviar("E","132","008") # Envia portão emperrado                        

                    if pm1 == "0": # Portão abriu

                        if eventos == "1":

                            evento.enviar("E","133","001") # Envia abriu portão
                        
                        contador = 200 # Tempo maximo para o social ficar aberto 30 segundos
                        log("Esperando por 20 segundos o portão social fechar...")

                        while contador > 0: # enquanto portão está aberto
                            
                            pm1 = entradas.pm1()
                            
                            if pm1 == "1": # portão fechou

                                log("Portão social fechou")

                                if eventos == "1":

                                    evento.enviar("R","133","001") # Envia fechamento
                                
                                contador = 1
                                                            
                                s = open("/home/pi/CMM/status_social.cmm","w")
                                s.write("0")
                                s.close()

                                saidas.desliga_blq2() # Fecha o contato e libera a eclusa para ser acionada

                                break

                            if (pm1 == "0" and contador == 1): # Portão ainda aberto após 15 segundos de espera

                                log("Portão social aberto por muito tempo")

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
                    
                    txt = ("Abrindo portão Eclusa")
                    log(txt)
                    eclusa()
                                        

                    if audio == "1":
                        
                        os.system("mpg123 /home/pi/CMM/mp3/abrindo_eclusa.mp3")
                    
                    time.sleep(3) # Tempo de espera para o portão abrir
                    
                    pm2 = entradas.pm2()
                    
                    if pm2 == "1": # Portão fechado não abriu após o comando

                       log("Portão eclusa emperrado")
                       
                       os.system("mpg123 /home/pi/CMM/mp3/eclusa_emperrado.mp3")
                            
                       saidas.desliga_blq1() # Libera o social para abrir mesmo com a eclusa aberta

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
                                
                                s = open("/home/pi/CMM/status_social.cmm","w")
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
                            
                            if ctw1 == "1": # Alguem esta tentando abrir o social com a eclusa aberta

                                log("Aguarde o fechamento do Social Interno")
                                os.system("mpg123 /home/pi/CMM/mp3/aguarde_fechamento.mp3") # Manter esse audio sempre ativo
                                time.sleep(1)
                                

                            time.sleep(0.1) # 1 segundo
                            contador = contador - 1
def social():

    status = open("/home/pi/CMM/status_social.cmm","w") # Para não disparar o arrombamento
    status.write("1")
    status.close()

    fechadura = banco.consulta("config","fechadura")
    audio = banco.consulta("config","audio")

    saidas.pulso_abre1() # Pulso para abrir direto o portão sem intertravamento (Social)
    log("Abrindo social...")    

    if audio == "1":

        if fechadura == "magnetica":

            os.system("mpg123 /home/pi/CMM/mp3/empurre.mp3")

        else:

            os.system("mpg123 /home/pi/CMM/mp3/abrindo_social.mp3")
    
def eclusa():

    status = open("/home/pi/CMM/status_eclusa.cmm","w") # Para não disparar o arrombamento
    status.write("1")
    status.close()

    fechadura = banco.consulta("config","fechadura")
    audio = banco.consulta("config","audio")

    saidas.pulso_abre2() # Pulso para abrir direto o portão sem intertravamento (Eclusa)
    log("Abrindo eclusa...")

    if audio == "1":

        if fechadura == "magnetica":

            os.system("mpg123 /home/pi/CMM/mp3/empurre.mp3")

        else:
                        
            os.system("mpg123 /home/pi/CMM/mp3/abrindo_eclusa.mp3")

def Portoes_sociais(Rele): # Programa
    
    log("Programa Sociais em execução ")

    saida = 0
    banco = cmm.Banco()
           
    while(1):

        habilita_intertravamento = banco.consulta("intertravamento","habilitado")
                
        pm1 = entradas.pm1()
        pm2 = entradas.pm2()
       
        ctw1 = entradas.ctw1()
        ctw2 = entradas.ctw2()


        ihm_soc1 = banco.consulta("comandos","abre_social_externo")
        ihm_soc2 = banco.consulta("comandos","abre_social_interno")
       
        if ctw1 == "1" or ihm_soc1 == "1":

            banco.atualiza("comandos","abre_social_externo","0")

            if habilita_intertravamento == "0":

                log("Intertravamento desabilitado\n")
                
                social()

            else:

                log("Intertravamento habilitado\n")

                status = open("/home/pi/CMM/status_social.cmm","w")
                status.write("1")
                status.close()
         
                Intertravamento("abre_social")

                status = open("/home/pi/CMM/status_social.cmm","w")
                status.write("0")
                status.close()

            
        if ctw2 == "1" or ihm_soc2 == "1":

            banco.atualiza("comandos","abre_social_interno","0")

            if habilita_intertravamento == "0":

                log("Intertravamento desabilitado\n")
                
                eclusa()                
               
                
            else:
                
                status = open("/home/pi/CMM/status_eclusa.cmm","w")
                status.write("1")
                status.close()

                Intertravamento("abre_eclusa")

                status = open("/home/pi/CMM/status_eclusa.cmm","w")
                status.write("0")
                status.close()

                saida = 1
                   
                
        time.sleep(0.1) 

        
########################################## Métodos de acesso a classe leitor #####################################

def leitor(entrada):

    l = cmm.Leitor()

    if  entrada == ("leitor1_in1"):

        i = l.leitor1_in1()
        return(i)

    if  entrada == ("leitor1_in2"):

        i = l.leitor1_in2()
        return(i)

    if  entrada == ("leitor1_in3"):

        i = l.leitor1_in3()
        return(i)

    if  entrada == ("leitor1_in4"):

        i = l.leitor1_in4()
        return(i)

    if  entrada == ("leitor7_in1"):

        i = l.leitor7_in1()
        return(i)

    if  entrada == ("leitor7_in2"):

        i = l.leitor7_in2()
        return(i)

    if  entrada == ("leitor7_in3"):

        i = l.leitor7_in3()
        return(i)

    if  entrada == ("leitor7_in4"):

        i = l.leitor7_in4()
        return(i)    

################################################ THREADS ROTINAS #################################################


def Garagem1(Rele): # Inicia a thread do portão da garagem importando a classe Rele

    log("Programa Garagem Terreo em execução ")
    
    s = cmm.Expansor()
    
    s.desliga_rele4_exp1() # Garante que a sirene esteja desligada
    s.desliga_rele3_exp1() # Garante que sinaleira esteja com sinal vermelho (NF)
    s.desliga_rele2_exp1() # Garante que o Foto esteja desligado
    s.desliga_rele1_exp1() # Garante que o Abre esteja desligado

##    s.liga_rele3_exp1() # Sinal Verde (Sinaleira)
##    s.desliga_rele3_exp1() # Sinal Vermelho (Sinaleira)
    

    banco = cmm.Banco()
            
    while(1):

        hs = time.strftime("%H:%M:%S")
        s = cmm.Expansor()
    
        ihm_gar1 = banco.consulta("comandos","abre_garagem") # Valor inserido pelo botão da interface       
        tx1 =  leitor("leitor1_in3")  # Cantato abre vindo do TX (LINEAR HCS)
                
        if (tx1 == "1" or ihm_gar1 == "1"):    # Se o tx ou o botão da interface mandou abrir o portão

            time.sleep(0.1)

            tx1 =  leitor("leitor1_in3")
            ihm_gar1 = banco.consulta("comandos","abre_garagem")

            if (tx1 == "1" or ihm_gar1 == "1"): # O tx da linear está direto no abre do portão

                time.sleep(0.1)
                tx1 =  leitor("leitor1_in3")

                if tx1 == "1":

                    log("Reconheceu tx Garagem") # Se reconheceu o tx, é porque o portão ja esta abrindo

                    s.liga_rele3_exp1() # Sinal Verde (Sinaleira)    

                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                    status.write("1")
                    status.close()

                if ihm_gar1 == "1": # Abre através do expansor (rele 1)

                    log("Reconheceu abre Garagem Interface pela gráfica")

                    s.liga_rele3_exp1() # Sinal Verde (Sinaleira)

                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                    status.write("1")
                    status.close()

                    s.liga_rele1_exp1()
                    time.sleep(2)
                    s.desliga_rele1_exp1()
                    

                banco.atualiza("comandos","abre_garagem","0")                

                time.sleep(3) # Tempo para começar a abrir o portão

                pmg1 = leitor("leitor1_in1")

                cont = 150     # Tempo maximo para deixar o portão aberto (150 = 30 segundos)
                
                if pmg1 == "1": # Portão não abriu apos o comando

                    time.sleep(0.1)
                    pmg1 = leitor("leitor1_in1")

                    if pmg1 == "1": # Portão não abriu apos o comando

                        log("Portão garagem não abriu")

                        s.desliga_rele3_exp1() # Sinal Vermelho
                        
                        #evento.enviar("E","132","015") # Emperrado
                        
                        status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                        status.write("0")
                        status.close()
                                            
                        cont = 0

                if pmg1 == "0": # Portão abriu

                    time.sleep(0.1)                    
                    pmg1 = leitor("leitor1_in1")

                    if pmg1 == "0": # Confirmado que o Portão abriu

        ##                    #evento.enviar("E","133","013")

                        while cont > 0:   # Enquanto o portão esta aberto verifica

                            if cont == 150:

                                log("Portão Garagem abriu")
                            
                            pmg1 = leitor("leitor1_in1")
                            
                            if pmg1 == "1": # Se o portão ja fechou

                                log("Portão Garagem fechou")

                                s.desliga_rele3_exp1() # Sinal Vermelho

                                status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                status.write("0")
                                status.close()

                                time.sleep(2)

        ##                            #evento.enviar("R","133","013") # Envia o evento de fechamento para a central

                                
                                cont = 0
                                break
                                
                            if pmg1 == "0":     # Se o portão ainda esta aberto

                                bar1 = leitor("leitor1_in2") # Faz a leitura da barreira 1

                                if bar1 == "1": # Se acionou a barreira de entrada

                                    log("Acionou a barreira Garagem")

                                    while bar1 == "1": # Enquanto a barreira esta acionada

                                        bar1 = leitor("leitor1_in2") # Faz a leitura da barreira 1

                                        # Alguem esta na frente da barreira

                                        time.sleep(0.1)
                                        
        ##                                log("Passou alguem, verificando dupla passagem...")

                                    s.desliga_rele3_exp1() # Sinal Vermelho
                                    
                                    pmg1 = leitor("leitor1_in1") # Faz a leitura do ponto magnetico
                                    
                                    if pmg1 == "0": # Portão ainda aberto

                                        pmg1 = leitor("leitor1_in1") # Faz a leitura do ponto magnetico

                                        log("Aguardando portão Garagem fechar")

                                        temp = 300

                                        while temp > 30:  # Enquanto o portão ainda está aberto e tempo menor que 30 seg                         

                                            pmg1 = leitor("leitor1_in1") # Faz a leitura do ponto magnetico
                                            bar1 = leitor("leitor1_in2") # Faz a leitura da barreira 1
                                            tx1 =  leitor("leitor1_in3")  # Cantato abre vindo do TX (LINEAR HCS)  

                                            if bar1 == "1": # Dupla passagem

                                                time.sleep(0.2)
                                                bar1 = leitor("leitor1_in2")

                                                if bar1 == "1":

                                                    log("Dupla passagem Garagem")                                                

                                                    #evento.enviar("E","132","019")

                                                    s.liga_rele4_exp1() # Sirene                                            
                                                    time.sleep(10)
                                                    s.desliga_rele4_exp1()                                            

                                                    break

                                            if tx1 == "1": # Alguem acionou o controle enquanto o portão fechava

                                                log("Reconheceu abre Garagem enquanto o portão estava aberto")
                                                
                                                s.liga_rele3_exp1() # Sinal Verde

                                                temp = 0
                                                
                                                break # Sai da função e inicia novamente a verificação

##                                            
                                     
                                            if pmg1 == "1": # portão ja fechou

                                                log("Portão Garagem fechou")
                                                s.desliga_rele3_exp1() # Sinal vermelho
                                                break

                                            temp = temp - 1
                                            time.sleep(0.1)

##                                    time.sleep(1)                                

                            cont = cont - 1
                            time.sleep(0.2)

                    if cont == 1: # Passaram se 29 segundos e o portão não fechou

                        log("Portão Garagem aberto muito tempo")

                        s.desliga_rele3_exp1() # Sinal Vermelho

                        status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                        status.write("0")
                        status.close()

                        #evento.enviar("E","132","019") # Envia evento de portão aberto
                        
                        cont = 0
                        break
        time.sleep(0.1)
        
def Garagem2(Rele): # Inicia a thread do portão da garagem importando a classe Rele

    log("Programa Garagem Subsolo em execução ")

    s2 = Expansor()    
    
    s2.desliga_rele4_exp7() # Garante que a sirene esteja desligada
    s2.desliga_rele1_exp7() # Garante que o Abre esteja desligado
    s2.desliga_rele2_exp7() # Garante que o Foto esteja desligado

    banco = cmm.Banco()
            
    while(1):

        hs = time.strftime("%H:%M:%S")        
        s2 = Expansor()

        ihm_gar2 = banco.consulta("comandos","abre_subsolo")        
        tx2 =  leitor("leitor7_in3")  # Cantato abre vindo do TX (LINEAR HCS)               
        
        if (tx2 == "1" or ihm_gar2 == "1"):    # Se o tx mandou abrir o portão

            time.sleep(0.1)

            tx2 =  leitor("leitor7_in3")

            if (tx2 == "1" or ihm_gar2 == "1"):

                log("reconheceu tx Subsolo")

                if ihm_gar2 == "1":

                    s2.liga_rele1_exp7()
                    time.sleep(2)
                    s2.desliga_rele1_exp7()
                    

                banco.atualiza("comandos","abre_subsolo","0")

                status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                status.write("1")
                status.close()

                time.sleep(3) # Tempo para começar a abrir o portão

                pmg2 = leitor("leitor7_in1")

                cont = 150     # Tempo maximo para deixar o portão aberto (150 = 30 segundos)
                
                if pmg2 == "1": # Portão não abriu apos o comando

                    log("Portão Subsolo não abriu")
                    
                    #evento.enviar("E","132","018")
                    
                    status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                    status.write("0")
                    status.close()
                                    
                    cont = 0

                if pmg2 == "0": # Portão abriu

                    while cont > 0:   # Enquanto o portão esta aberto verifica

                        if cont == 150:

                            log("Portão Subsolo abriu")
                        
                        pmg2 = leitor("leitor7_in1")
                        
                        if pmg2 == "1": # Se o portão ja fechou

                            log("Portão Subsolo fechou\n")

                            status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                            status.write("0")
                            status.close()

                            time.sleep(2)
                            
                            cont = 0
                            break
                            
                        if pmg2 == "0":     # Se o portão ainda esta aberto

                            bar2 = leitor("leitor7_in2") # Faz a leitura da barreira 1

                            if bar2 == "1": # Se acionou a barreira de entrada

                                log("Acionou a barreira Subsolo")

                                while bar2 == "1": # Enquanto a barreira esta acionada

                                    bar2 = leitor("leitor7_in2") # Faz a leitura da barreira 1

                                    # Alguem esta na frente da barreira

                                    time.sleep(0.1)
                                    
                                # Passou alguem Subsolo, verificando dupla passagem...

                                pmg2 = leitor("leitor7_in1") # Faz a leitura do ponto magnetico
                                
                                if pmg2 == "0":

                                    pmg2 = leitor("leitor7_in1") # Faz a leitura do ponto magnetico

                                    log("Aguardando portão Subsolo fechar")

                                    while pmg2 == "0":  # Enquanto o portão ainda não fechou                                

                                        pmg2 = leitor("leitor7_in1") # Faz a leitura do ponto magnetico
                                        bar2 = leitor("leitor7_in2") # Faz a leitura da barreira 1
                                        tx2 =  leitor("leitor7_in3")  # Cantato abre vindo do TX (LINEAR HCS)  

                                        if bar2 == "1": # Dupla passagem

                                            time.sleep(0.2)
                                            bar2 = leitor("leitor7_in2")

                                            if bar2 == "1":

                                                log("Dupla passagem Subsolo")

                                                #evento.enviar("E","132","019")

                                                s2.liga_rele4_exp7() # Sirene
                                                time.sleep(10)
                                                s2.desliga_rele4_exp7()

                                                break

                                        if tx2 == "1": # Alguem acionou o controle enquanto o portão fechava

                                            cont = 0
                                            
                                            break # Sai da função e inicia novamente a verificação

                                        time.sleep(0.1)
                                        
                                # Fim do cilo Subsolo

                                time.sleep(1)

                        cont = cont - 1
                        time.sleep(0.2)

                    if cont == 1: # Passaram se 29 segundos e o portão não fechou

                        log("Portão Subsolo aberto muito tempo")

                        status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                        status.write("0")
                        status.close()

                        #evento.enviar("E","132","019")# Envia evento de portão aberto
                        cont = 0
                        break     
        time.sleep(0.1)
        
def Arrombamento(Rele): # Inicia a thread arrombamento de portões
    
    log("Programa arrombamento de portões em execução")

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

            if abre_social == "0": # Se realmente foi um arrombamento liga sirene e notifica o Moni
                
                log("Arrombamento do portão social")
                os.system("mpg123 /home/pi/CMM/mp3/violacao_social.mp3")
                
                saidas.liga_sirene()

                if evento == "1":

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

                if evento == "1":

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

            if abre_eclusa == "0": # Se realmente foi um arrombamento liga sirene e notifica o Moni

                log("Arrombamento do portão Eclusa")
                os.system("mpg123 /home/pi/CMM/mp3/violacao_eclusa.mp3")

                saidas.liga_sirene()

                if evento == "1":

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

                if evento == "1":

                    evento.enviar("R","132","004")

                cont2 = 350 # Se apos o reset o portão continuar aberto envia o evento novamente e espera 5 min
                ar2 = 0
                reset_ar2 = 0
                segunda_vez2 = 1

                saidas.desliga_sirene()
        
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

        
def Alarmes_garagem_1(Rele):
    
    log("Programa Alarmes Garagem em execução")

    mudanca1 = 0
    
    while(1):         

        s = cmm.Expansor()

        pmg1 = leitor("leitor1_in1") # Ponto magnetico portão leitor 1 entrada 1      
        mud1 = leitor("leitor1_in4")  # Chave de mudança

        t = open("/home/pi/CMM/status_garagem_1.cmm","r")
        status_tx1 = t.read()
        t.close()
                

        if mud1 == "1" and mudanca1 == 0: # Chave de mudança acionada

            time.sleep(0.1)

            pmg1 = leitor("leitor1_in1") # Ponto magnetico portão leitor 1 entrada 1      
            mud1 = leitor("leitor1_in4")  # Chave de mudança            

            if mud1 == "1" and mudanca1 == 0:    

                log("Chave de mudança acionada Garagem")

                s.liga_rele3_exp1() # Sinal Verde

                #evento.enviar("E","132","26")                

                t = open("/home/pi/CMM/status_garagem_1.cmm","w")
                t.write("1")
                t.close()

                s.liga_rele1_exp1() # Aciona o rele 1 do modulo 1 (Abre)
                time.sleep(2)
                s.desliga_rele1_exp1()
                s.liga_rele2_exp1() # Aciona o rele 2 do modulo 1 (Foto)                

                mudanca1 = 1

        if mud1 == "0" and mudanca1 == 1:

            time.sleep(0.1)
            mud1 = leitor("leitor1_in4")

            if mud1 == "0":

                log("Desligada a chave de mudança")

                s.desliga_rele3_exp1() # Sinal Vermelho

                #evento.enviar("R","132","26")
                                
                s.desliga_rele1_exp1() # Desliga o rele 1 do modulo 1 (Abre)
                s.desliga_rele2_exp1() # Desliga o rele 2 do modulo 1 (Foto) 

                pmg1 = leitor("leitor1_in1")

                cont = 30 # Tempo maximo de espera

                log("Aguardando portão Garagem fechar depois da mudanca")

                while cont > 0:

                    pmg1 = leitor("leitor1_in1")

                    if(pmg1 == "0"): # Portão ainda aberto                                      

                        time.sleep(1)
                        cont = cont - 1
                            
                    if (pmg1 == "1"): # Portão ja fechou

                        log("Portão fechou")

                        s.desliga_rele3_exp1() # Sinal Vermelho

                        t = open("/home/pi/CMM/status_garagem_1.cmm","w")
                        t.write("0")
                        t.close()
                        
                        cont = 0
                        mudanca1 = 0
                        time.sleep(1)
                        break
            
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
                
                s.desliga_rele4_exp1() # Desliga sirene

##                violacao = 0
                
                time.sleep(30)
                
        time.sleep(1)
        
def Alarmes_garagem_2(Rele):

    log("Programa Alarmes Garagem Subsolo em execução")

    mudanca2 = 0
    
    while(1):        

        s2 = Expansor()
        
        pmg2 = leitor("leitor7_in1") # Ponto magnetico portão leitor 1 entrada 1        

        t = open("/home/pi/CMM/status_garagem_2.cmm","r")
        status_tx2 = t.read()
        t.close()
                                
        if pmg2 == "0" and status_tx2 == "0": # Violação do portão da garagem
            
            cont = 10
            violacao = 1
            
            while cont > 0: # Filtro

                t = open("/home/pi/CMM/status_garagem_2.cmm","r")
                status_tx2 = t.read()
                t.close() 

                pmg2 = leitor("leitor7_in1")

                if pmg2 == "0" and status_tx2 == "0":
                    
                    violacao = 1

                if pmg2 == "1":
                    
                    violacao = 0
                    break

                time.sleep(0.1)
                cont = cont - 1

            if violacao == 0: # Filtrou ruido

                pass

            if violacao == 1:

                log("violação do portão Subsolo")

                s2.liga_rele4_exp7() # Sirene
                                            
                #evento.enviar("E","132","016")

                cont = 30 # Tempo maximo de espera

                log("Aguardando portão Subsolo fechar apos violação")

                while cont > 0:

                    pmg2 = leitor("leitor7_in1")

                    if(pmg2 == "0"): # Portão ainda aberto                                      

                        time.sleep(1)
                        cont = cont - 1
                            
                    if (pmg2 == "1"): # Portão ja fechou

                        log("Portão Subsolo fechou")

                        t = open("/home/pi/CMM/status_garagem_2.cmm","w")
                        t.write("0")
                        t.close()
                        
                        cont = 0
                        time.sleep(1)
                        
                        s2.desliga_rele4_exp7() # Desliga sirene
                        
                        break
                    
                s2.desliga_rele4_exp7() # Desliga sirene
                
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
                    
        
#################### Instancia as Classes  #############################################

intertravamento = Intertravamento(cmm.Rele)


####################  Declara as threads dos programas disponiveis  ####################

sociais = threading.Thread(target=Portoes_sociais, args=(cmm.Rele,)) # deixar virgula depois do arg 1
garagem1 = threading.Thread(target=Garagem1, args=(cmm.Rele,))
garagem2 = threading.Thread(target=Garagem2, args=(cmm.Rele,))
arrombamento = threading.Thread(target=Arrombamento, args=(cmm.Rele,))
servidor = threading.Thread(target=Servidor, args=(cmm.Rele,))
buffer = threading.Thread(target=Buffer)

alarmes1 = threading.Thread(target=Alarmes_garagem_1, args=(cmm.Rele,))
alarmes2 = threading.Thread(target=Alarmes_garagem_1, args=(cmm.Rele,))


######################################### Start dos Programas  #############################################################

sociais.start() # Inicia o programa dos portões sociais
garagem1.start() # Inicia o programa do portão de garagem
##garagem2.start() # Inicia o programa do portão de garagem
arrombamento.start() # Inicia o programa de automação
#servidor.start() 
buffer.start() # Inicia o programa Buffer

alarmes1.start() # Inicia a leitura de "interrupções" (chave de mudança garagem1 e arrombamento de portões)
##alarmes2.start()
##qrcode.start()
##wiegand.start()

time.sleep(0.2) # Tempo para colocar as linhas impressas após as linhas de inicio de programa



log("Temperatura processador " + str(temperatura.cpu()) + "°C\n")  # obter temperatura

try:

    log("*")    
    log("Sistema conectado a internet")
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

