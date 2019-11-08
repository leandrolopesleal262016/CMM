#!/usr/bin/env python3
# coding=UTF-8

import time
from expansores import Leitor, Expansor
import os
import threading
from banco import Banco
import cmm_io_entradas as entradas
import cmm_io_saidas as saidas
from biblioteca_CMM_oficial import Evento

s = Expansor()
l = Leitor()

evento = Evento("0054")
banco = Banco()

banco.atualiza("comandos","abre_garagem1","0")
banco.atualiza("comandos","abre_garagem2","0")

       
def Garagem1(): # Inicia a thread do portão da garagem importando a classe Rele

    os.system("sudo chmod 777 /dev/ttyS0")
    os.system("sudo chmod 777 -R /var/www/html/log")

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

    log("Programa Garagem 1 em execução no expansor 1... ")
    
    s = Expansor()
    l = Leitor()
    
    s.desliga_rele4_exp1() # Garante que a sirene esteja desligada
    s.desliga_rele3_exp1() # Garante que sinaleira esteja com sinal vermelho (NF)
    s.desliga_rele2_exp1() # Garante que o Foto esteja desligado
    s.desliga_rele1_exp1() # Garante que o Abre esteja desligado

##    banco = Banco()
    eventos = banco.consulta("comandos","eventos")

    mudanca1 = 0
            
    while(1):
        

        hs = time.strftime("%H:%M:%S")
        s = Expansor()
    
        ihm_gar1 = banco.consulta("comandos","abre_garagem1") # Valor inserido pelo botão da interface       
        tx1 =  l.leitor1_in3()  # Cantato abre vindo do TX (LINEAR HCS)

        mud1 = l.leitor1_in4()  # Chave de mudança

        t = open("/home/pi/CMM/status_garagem_1.cmm","r")
        status_tx1 = t.read()
        t.close()
                   
                    
        if (tx1 == 1 or ihm_gar1 == "1"):   

            time.sleep(0.05)                
            tx1 =  l.leitor1_in3()                                

            if (tx1 == 1 or ihm_gar1 == "1"): # O tx da linear está direto no abre do portão

                time.sleep(0.05)
                tx1 = l.leitor1_in3()

                if tx1 == 1 :

                    log("*")
                    log("Reconheceu tx Garagem 1") # Se reconheceu o tx, é porque o portão ja esta abrindo

                    s.liga_rele3_exp1() # Sinal Verde (Sinaleira)    

                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                    status.write("1")
                    status.close()

                    time.sleep(1)

                if ihm_gar1 == "1": # Abre através do expansor (rele 1)

                    log("*")
                    log("Reconheceu abre Garagem 1 Interface gráfica")

                    s.liga_rele3_exp1() # Sinal Verde (Sinaleira)

                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                    status.write("1")
                    status.close()

                    s.liga_rele1_exp1() # Pulso para abrir a garagem
                    time.sleep(2)
                    s.desliga_rele1_exp1()

                    time.sleep(1)

                banco.atualiza("comandos","abre_garagem1","0")                    

                time.sleep(2) # Tempo para começar a abrir o portão

                pmg1 = l.leitor1_in1()                               
                
                if pmg1 == 1: # Portão não abriu apos o comando

                    time.sleep(0.05)
                    pmg1 = l.leitor1_in1()

                    if pmg1 == 1: # Portão não abriu apos o comando

                        time.sleep(0.05)
                        pmg1 = l.leitor1_in1()

                        if pmg1 == 1:

                            log("Portão Garagem 1 não abriu")

                            s.desliga_rele3_exp1() # Sinal Vermelho                            

                            if eventos == "1":
                            
                                evento.enviar("E","132","015") # Emperrado

                            banco.atualiza("comandos","abre_garagem1","0")
                            
                            status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                            status.write("0")
                            status.close()                                               
                            

                if pmg1 == 0: # Portão abriu

                    time.sleep(0.05)                    
                    pmg1 = l.leitor1_in1()

                    if pmg1 == 0: # Confirmado que o Portão abriu

                        time.sleep(0.05)                    
                        pmg1 = l.leitor1_in1()

                        if pmg1 == 0:                                

                            if eventos == "1":
                                
                                evento.enviar("E","133","013")
                                
                            cont1 = 300     # Tempo maximo para deixar 300 = 30 segundos

                            while cont1 > 0:   # Enquanto o portão esta aberto verifica

                                if cont1 == 300:

                                    log("Portão Garagem abriu")
                                    
                                    s.liga_rele3_exp1() # Sinal verde
                                    
                                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                    status.write("1")
                                    status.close()

                                    time.sleep(2)
                                
                                pmg1 = l.leitor1_in1()
                                
                                if pmg1 == 1: # Se o portão ja fechou

                                    time.sleep(0.05)
                                    pmg1 = l.leitor1_in1()

                                    if pmg1 == 1:

                                        time.sleep(0.05)
                                        pmg1 = l.leitor1_in1()

                                        if pmg1 == 1:

                                            log("Portão Garagem fechou")

                                            s.desliga_rele3_exp1() # Sinal Vermelho

                                            status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                            status.write("0")
                                            status.close()
                                            
                                            if eventos == "1":
                                                
                                                evento.enviar("R","133","013") # Envia o evento de fechamento para a central
                                            
                                            cont1 = 0
                                            break                                            
                                    
                                if pmg1 == 0: # Se o portão ainda esta aberto

                                    time.sleep(0.05)
                                    pmg1 = l.leitor1_in1()

                                    if pmg1 == 0:

                                        time.sleep(0.05)
                                        pmg1 = l.leitor1_in1()

                                        if pmg1 == 0:

                                            cont2 = 300     # Tempo maximo para deixar 300 = 30 segundos

                                            while cont2 > 0:   # Enquanto o portão esta aberto verifica

                                                if cont2 == 300:

                                                    log("Portão Garagem 1 aberto...")
                                            
                                                bar1 = l.leitor1_in2() # Faz a leitura da barreira 1
                                                pmg1 = l.leitor1_in1()

                                                if bar1 == 1: # Se acionou a barreira de entrada

                                                    time.sleep(0.05)
                                                    bar1 = l.leitor1_in2()

                                                    if bar1 == 1:

                                                        time.sleep(0.05)
                                                        bar1 = l.leitor1_in2()

                                                        if bar1 == 1: # Se acionou a barreira de entrada                                                            

                                                            log("Acionou a barreira Garagem 1")

                                                            tempo = 60

                                                            while tempo > 0: # Enquanto esta na frente da barreira

                                                                bar1 = l.leitor1_in2() # Faz a leitura da barreira 1                                                                
                                                                
                                                                if bar1 == 0:

                                                                    time.sleep(0.05)
                                                                    bar1 = l.leitor1_in2()

                                                                    if bar1 == 0:
                                                                        
                                                                        log("Saiu da barreira Garagem 1")
                                                                        s.desliga_rele3_exp1() # Sinal Vermelho
                                                                        tempo = 0
                                                                        break
                                                                    
                                                                if tempo == 1:

                                                                    log("Portão aberto por muito tempo")

                                                                    s.desliga_rele3_exp1() # Sinal Vermelho

                                                                    s.liga_rele4_exp1() # Sirene                                            
                                                                    time.sleep(3)
                                                                    s.desliga_rele4_exp1()

                                                                    if eventos == "1":

                                                                        evento.enviar("E","132","026") # Envia obstruçao

                                                                    if eventos == "0":

                                                                        print("Reconheceu que eventos esta desligado neste nivel")

                                                                    break

                                                                tempo = tempo - 1
                                                                time.sleep(1) 
                                                        
                                                        pmg1 = l.leitor1_in1() # Faz a leitura do ponto magnetico                                    
                                                        
                                                        if pmg1 == 0: # Portão ainda aberto

                                                            time.sleep(0.05)                                                        
                                                            pmg1 = l.leitor1_in1() # Faz a leitura do ponto magnetico                                        

                                                            if pmg1 == 0:

                                                                log("Aguardando 30 segundos portão Garagem fechar")

                                                                temp = 300
                                                                entrada_permitida = 0

                                                                while temp > 0:  # Enquanto o portão ainda está aberto e tempo menor que 30 seg
                                                                    
                                                                    pmg1 = l.leitor1_in1() # Faz a leitura do ponto magnetico
                                                                    bar1 = l.leitor1_in2() # Faz a leitura da barreira 1
                                                                    tx1 =  l.leitor1_in3()  # Cantato abre vindo do TX (LINEAR HCS)

                                                                    if tx1 == 1: # Alguem acionou o controle enquanto o portão fechava

                                                                        time.sleep(0.05)                                                                    
                                                                        tx1 =  l.leitor1_in3()

                                                                        if tx1 == 1:

                                                                            time.sleep(0.05)                                                                    
                                                                            tx1 =  l.leitor1_in3()

                                                                            if tx1 == 1:

                                                                                log("Reconheceu abre Garagem 1 enquanto o portão estava aberto")                                                    
                                                                                s.liga_rele3_exp1() # Sinal Verde

                                                                                entrada_permitida = 1 # Reconhece o segundo acionamento
                                                                                                                                                                                                                                                
##                                                                                break # Sai da função e inicia novamente a verificação

                                                                    if bar1 == 1 and entrada_permitida == 1:
                                                                        
                                                                        time.sleep(0.05)                                                                    
                                                                        bar1 = l.leitor1_in2()
                                                                        
                                                                        if bar1 == 1:

                                                                            tempo2 = 60

                                                                            while tempo2 > 0: # Enquanto a barreira esta acionada

                                                                                bar1 = l.leitor1_in2() # Faz a leitura da barreira 1                                                                                                                                                                                                                                                       

                                                                                if bar1 == 0:

                                                                                    time.sleep(0.05)
                                                                                    bar1 = l.leitor1_in2()

                                                                                    if bar1 == 0:

                                                                                        time.sleep(0.05)
                                                                                        bar1 = l.leitor1_in2()

                                                                                        if bar1 == 0:

                                                                                            log("Saiu da barreira")
                                                                                            s.desliga_rele3_exp1() # Sinal Vermelho
                                                                                            log("Entrou segundo veiculo autorizado")

                                                                                            entrada_permitida = 0
                                                                                            
                                                                                            tempo2 = 0
                                                                                            
                                                                                if tempo2 == 1:

                                                                                    log("Portão do segundo veiculo aberto por muito tempo")

                                                                                    s.desliga_rele3_exp1() # Sinal Vermelho

                                                                                    s.liga_rele4_exp1() # Sirene                                            
                                                                                    time.sleep(3)
                                                                                    s.desliga_rele4_exp1()

                                                                                    if eventos == "1":

                                                                                        evento.enviar("E","132","026") # Envia obstruçao

                                                                                    if eventos == "0":

                                                                                        print("Reconheceu que eventos esta desligado neste nivel 2")

                                                                                    tempo2 = 1
                                                                                
                                                                                tempo2 = tempo2 - 1
                                                                                time.sleep(1)                                       

                                                                       
                                                                    if bar1 == 1 and entrada_permitida == 0: # Dupla passagem
                                                                        
                                                                        time.sleep(0.05)                                                                    
                                                                        bar1 = l.leitor1_in2()

                                                                        if bar1 == 1:

                                                                            if bar1 == 1 and entrada_permitida == 0: # Dupla passagem
                                                                        
                                                                                time.sleep(0.05)                                                                    
                                                                                bar1 = l.leitor1_in2()

                                                                                log("Dupla passagem Garagem 1")

                                                                                if eventos == "1":

                                                                                    evento.enviar("E","132","016")

                                                                                s.liga_rele4_exp1() # Sirene                                            
                                                                                time.sleep(10)
                                                                                s.desliga_rele4_exp1()                                            

                                                                                break
                                                                        
                                                             
                                                                    if pmg1 == 1: # portão ja fechou

                                                                        time.sleep(0.05)                                                                    
                                                                        pmg1 = l.leitor1_in1()

                                                                        if pmg1 == 1:

                                                                            time.sleep(0.05)                                                                    
                                                                            pmg1 = l.leitor1_in1()

                                                                            if pmg1 == 1:
                                                                                
                                                                                s.desliga_rele3_exp1() # Sinal Vermelho

                                                                                status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                                                                status.write("0")
                                                                                status.close()

                                                                                if eventos == "1":
                                                                                
                                                                                    evento.enviar("R","133","013") # Envia o evento de fechamento para a central
                                                                                
                                                                                temp = 0
                                                                                break                                                                                                                                                     

                                                                    if temp == 1:

                                                                        log("Portão aberto por muito tempo")

                                                                        s.desliga_rele3_exp1() # Sinal Vermelho

                                                                        s.liga_rele4_exp1() # Sirene                                            
                                                                        time.sleep(3)
                                                                        s.desliga_rele4_exp1()

                                                                        status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                                                        status.write("0")
                                                                        status.close()

                                                                        if eventos == "1":

                                                                            evento.enviar("E","132","026") # Envia obstruçao

                                                                        temp = 0                                                                                                                                   
                                                                        break

                                                                    temp = temp - 1
                                                                    time.sleep(0.2)

                                                if pmg1 == 1:

                                                    time.sleep(0.05)
                                                    pmg1 = l.leitor1_in1()
                                                    
                                                    if pmg1 == 1:

                                                        time.sleep(0.05)
                                                        pmg1 = l.leitor1_in1()
                                                        
                                                        if pmg1 == 1:

                                                            log("Portão Garagem fechou.")

                                                            s.desliga_rele3_exp1() # Sinal Vermelho

                                                            status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                                            status.write("0")
                                                            status.close()

                                                            if eventos == "1":
                                                            
                                                                evento.enviar("R","133","013") # Envia o evento de fechamento para a central
                                                            
                                                            cont2 = 0
                                                            break
                                                                            
                                                if cont2 == 1:

                                                    log("Nao detectou nenhuma entrada ou saida Garagem 1")
                                                    s.liga_rele3_exp1() # Sinal Vermelho
                                                    
                                                    break
                                                
                                                time.sleep(0.1)
                                                cont2 = cont2 - 1
                                                                    
                                                            
                                if cont1 == 1:

                                    log("Atingiu o tempo máximo e o portão da Garagem não fechou")

                                    s.desliga_rele3_exp1() # Sinal Vermelho

                                    s.liga_rele4_exp1() # Sirene                                            
                                    time.sleep(3)
                                    s.desliga_rele4_exp1()

                                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                                    status.write("0")
                                    status.close()

                                    cont1 = 0
                                    break
                                
                                cont1 = cont1 - 1
                                time.sleep(0.1)
                
                if status_tx1 == "1" and pmg1 == 0:

                    log ("Recebeu comando para abrir Garagem 1 mas o portão no abriu")
                    
                    s.desliga_rele3_exp1() # Sinal Vermelho
                    
                    status = open("/home/pi/CMM/status_garagem_1.cmm","w") 
                    status.write("0")
                    status.close()
            if mud1 == 1 and mudanca1 == 0: # Chave de mudança acionada

                time.sleep(0.05)     
                mud1 = l.leitor1_in4()  # Chave de mudança            

                if mud1 == 1:

                    time.sleep(0.05)     
                    mud1 = l.leitor1_in4()  # Chave de mudança            

                    if mud1 == 1:

                        log("*")
                        log("Chave de mudança acionada Garagem")

                        s.liga_rele3_exp1() # Sinal Verde

                        if evento == "1":

                            evento.enviar("E","132","26")                

                        t = open("/home/pi/CMM/status_garagem_1.cmm","w")
                        t.write("1")
                        t.close()

                        s.liga_rele1_exp1() # Aciona o rele 1 do modulo 1 (Abre)
                        time.sleep(2)
                        s.desliga_rele1_exp1()
                        s.liga_rele2_exp1() # Aciona o rele 2 do modulo 1 (Foto)                

                        mudanca1 = 1

        if mud1 == 0 and mudanca1 == 1:

            time.sleep(0.05)
            mud1 = l.leitor1_in4()

            if mud1 == 0:

                time.sleep(0.05)
                mud1 = l.leitor1_in4()

                if mud1 == 0:

                    log("Desligada a chave de mudança")

                    s.desliga_rele3_exp1() # Sinal Vermelho

                    if evento == "1":

                        evento.enviar("R","132","26")
                                    
                    s.desliga_rele1_exp1() # Desliga o rele 1 do modulo 1 (Abre)
                    s.desliga_rele2_exp1() # Desliga o rele 2 do modulo 1 (Foto) 

                    pmg1 = l.leitor1_in1()

                    cont = 60 # Tempo maximo de espera

                    log("Aguardando portão Garagem fechar depois da mudanca")

                    while cont > 0:
                        
                        pmg1 = l.leitor1_in1()                                                               
                                
                        if pmg1 == 1: # Portão ja fechou

                            time.sleep(0.05)
                            pmg1 = l.leitor1_in1()

                            if pmg1 == 1:

                                time.sleep(0.05)
                                pmg1 = l.leitor1_in1()

                                if pmg1 == 1:

                                    log("Portão fechou")

                                    s.desliga_rele3_exp1() # Sinal Vermelho

                                    t = open("/home/pi/CMM/status_garagem_1.cmm","w")
                                    t.write("0")
                                    t.close()
                                    
                                    cont = 0
                                    mudanca1 = 0
                                    time.sleep(1)
                                    break
                                
                        if cont == 1:

                            log("Chave de mudança desligou mas o portão nao fechou após 1 min")

                            s.desliga_rele3_exp1() # Sinal Vermelho

                            t = open("/home/pi/CMM/status_garagem_1.cmm","w")
                            t.write("0")
                            t.close()

                            s.liga_rele4_exp1() # Pulso na Sirene                                            
                            time.sleep(3)
                            s.desliga_rele4_exp1()                                
                            
                            mudanca1 = 0
                            
                            time.sleep(1)

                        time.sleep(1)
                        cont = cont - 1
        time.sleep(0.2)       
    
        
    log("Saiu do loop da lógica da Garagem 1 ")

def Garagem2(): # Inicia a thread do portão da garagem importando a classe Rele

    os.system("sudo chmod 777 /dev/ttyS0")
    os.system("sudo chmod 777 -R /var/www/html/log")

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

    log("Programa Garagem 2 em execução no expansor 2... ")
    
    s = Expansor()
    l = Leitor()
    
    s.desliga_rele4_exp2() # Garante que a sirene esteja desligada
    s.desliga_rele3_exp2() # Garante que sinaleira esteja com sinal vermelho (NF)
    s.desliga_rele2_exp2() # Garante que o Foto esteja desligado
    s.desliga_rele1_exp2() # Garante que o Abre esteja desligado

##    banco = Banco()
    eventos = banco.consulta("comandos","eventos2")

    mudanca2 = 0
            
    while(1):        

        hs = time.strftime("%H:%M:%S")
        s = Expansor()
    
        ihm_gar2 = banco.consulta("comandos","abre_garagem2") # Valor inserido pelo botão da interface       
        tx2 =  l.leitor2_in3()  # Cantato abre vindo do TX (LINEAR HCS)

        mud2 = l.leitor2_in4()  # Chave de mudança

        t = open("/home/pi/CMM/status_garagem_2.cmm","r")
        status_tx2 = t.read()
        t.close()
                   
                    
        if (tx2 == 1 or ihm_gar2 == "1"):   

            time.sleep(0.05)                
            tx2 =  l.leitor2_in3()                                

            if (tx2 == 1 or ihm_gar2 == "1"): # O tx da linear está direto no abre do portão

                time.sleep(0.05)
                tx2 = l.leitor2_in3()

                if tx2 == 1 :

                    log("*")
                    log("Reconheceu tx Garagem 2") # Se reconheceu o tx, é porque o portão ja esta abrindo

                    s.liga_rele3_exp2() # Sinal Verde (Sinaleira)    

                    status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                    status.write("1")
                    status.close()

                    time.sleep(1)

                if ihm_gar2 == "1": # Abre através do expansor (rele 1)

                    log("*")
                    log("Reconheceu abre Garagem 2 Interface gráfica")

                    s.liga_rele3_exp2() # Sinal Verde (Sinaleira)

                    status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                    status.write("1")
                    status.close()

                    s.liga_rele1_exp2() # Pulso para abrir a garagem
                    time.sleep(2)
                    s.desliga_rele1_exp2()

                    time.sleep(1)

                banco.atualiza("comandos","abre_garagem2","0")                    

                time.sleep(2) # Tempo para começar a abrir o portão

                pmg2 = l.leitor2_in1()                               
                
                if pmg2 == 1: # Portão não abriu apos o comando

                    time.sleep(0.05)
                    pmg2 = l.leitor2_in1()

                    if pmg2 == 1: # Portão não abriu apos o comando

                        time.sleep(0.05)
                        pmg2 = l.leitor2_in1()

                        if pmg2 == 1:

                            log("Portão Garagem 2 não abriu")

                            s.desliga_rele3_exp2() # Sinal Vermelho                            

                            if eventos == "1":
                            
                                evento.enviar("E","132","019") # Emperrado

                            banco.atualiza("comandos","abre_garagem2","0")
                            
                            status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                            status.write("0")
                            status.close()                                               
                            

                if pmg2 == 0: # Portão abriu

                    time.sleep(0.05)                    
                    pmg2 = l.leitor2_in1()

                    if pmg2 == 0: # Confirmado que o Portão abriu

                        time.sleep(0.05)                    
                        pmg2 = l.leitor2_in1()

                        if pmg2 == 0:                                

                            if eventos == "1":
                                
                                evento.enviar("E","133","017")
                                
                            cont1 = 300     # Tempo maximo para deixar 300 = 30 segundos

                            while cont1 > 0:   # Enquanto o portão esta aberto verifica

                                if cont1 == 300:

                                    log("Portão Garagem 2 abriu")
                                    
                                    s.liga_rele3_exp2() # Sinal verde
                                    
                                    status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                                    status.write("1")
                                    status.close()

                                    time.sleep(2)
                                
                                pmg2 = l.leitor2_in1()
                                
                                if pmg2 == 1: # Se o portão ja fechou

                                    time.sleep(0.05)
                                    pmg2 = l.leitor2_in1()

                                    if pmg2 == 1:

                                        time.sleep(0.05)
                                        pmg2 = l.leitor2_in1()

                                        if pmg2 == 1:

                                            log("Portão Garagem 2 fechou")

                                            s.desliga_rele3_exp2() # Sinal Vermelho

                                            status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                                            status.write("0")
                                            status.close()
                                            
                                            if eventos == "1":
                                                
                                                evento.enviar("R","133","017") # Envia o evento de fechamento para a central
                                            
                                            cont1 = 0
                                            break                                            
                                    
                                if pmg2 == 0: # Se o portão ainda esta aberto

                                    time.sleep(0.05)
                                    pmg2 = l.leitor2_in1()

                                    if pmg2 == 0:

                                        time.sleep(0.05)
                                        pmg2 = l.leitor2_in1()

                                        if pmg2 == 0:

                                            cont2 = 300     # Tempo maximo para deixar 300 = 30 segundos

                                            while cont2 > 0:   # Enquanto o portão esta aberto verifica

                                                if cont2 == 300:

                                                    log("Portão Garagem 2 aberto...")
                                            
                                                bar2 = l.leitor2_in2() # Faz a leitura da barreira 1
                                                pmg2 = l.leitor2_in1()

                                                if bar2 == 1: # Se acionou a barreira de entrada

                                                    time.sleep(0.05)
                                                    bar2 = l.leitor2_in2()

                                                    if bar2 == 1:

                                                        time.sleep(0.05)
                                                        bar2 = l.leitor2_in2()

                                                        if bar2 == 1: # Se acionou a barreira de entrada                                                            

                                                            log("Acionou a barreira Garagem 2")

                                                            tempo = 60

                                                            while tempo > 0: # Enquanto esta na frente da barreira

                                                                bar2 = l.leitor2_in2() # Faz a leitura da barreira 1                                                                
                                                                
                                                                if bar2 == 0:

                                                                    time.sleep(0.05)
                                                                    bar2 = l.leitor2_in2()

                                                                    if bar2 == 0:
                                                                        
                                                                        log("Saiu da barreira Garagem 2")
                                                                        s.desliga_rele3_exp2() # Sinal Vermelho
                                                                        tempo = 0
                                                                        break
                                                                    
                                                                if tempo == 1:

                                                                    log("Portão Garagem 2 aberto por muito tempo")

                                                                    s.desliga_rele3_exp2() # Sinal Vermelho

                                                                    s.liga_rele4_exp2() # Sirene                                            
                                                                    time.sleep(3)
                                                                    s.desliga_rele4_exp2()

                                                                    if eventos == "1":

                                                                        evento.enviar("E","132","027") # Envia obstruçao

                                                                    if eventos == "0":

                                                                        print("Reconheceu que eventos esta desligado neste nivel g2")

                                                                    break

                                                                tempo = tempo - 1
                                                                time.sleep(1) 
                                                        
                                                        pmg2 = l.leitor2_in1() # Faz a leitura do ponto magnetico                                    
                                                        
                                                        if pmg2 == 0: # Portão ainda aberto

                                                            time.sleep(0.05)                                                        
                                                            pmg2 = l.leitor2_in1() # Faz a leitura do ponto magnetico                                        

                                                            if pmg2 == 0:

                                                                log("Aguardando 30 segundos portão Garagem 2 fechar")

                                                                temp = 300
                                                                entrada_permitida = 0

                                                                while temp > 0:  # Enquanto o portão ainda está aberto e tempo menor que 30 seg
                                                                    
                                                                    pmg2 = l.leitor2_in1() # Faz a leitura do ponto magnetico
                                                                    bar2 = l.leitor2_in2() # Faz a leitura da barreira 1
                                                                    tx2 =  l.leitor2_in3()  # Cantato abre vindo do TX (LINEAR HCS)

                                                                    if tx2 == 1: # Alguem acionou o controle enquanto o portão fechava

                                                                        time.sleep(0.05)                                                                    
                                                                        tx2 =  l.leitor2_in3()

                                                                        if tx2 == 1:

                                                                            time.sleep(0.05)                                                                    
                                                                            tx2 =  l.leitor2_in3()

                                                                            if tx2 == 1:

                                                                                log("Reconheceu abre Garagem 2 enquanto o portão estava aberto")                                                    
                                                                                s.liga_rele3_exp2() # Sinal Verde

                                                                                entrada_permitida = 1 # Reconhece o segundo acionamento
                                                                                                                                                                                                                                                
##                                                                                break # Sai da função e inicia novamente a verificação

                                                                    if bar2 == 1 and entrada_permitida == 1:
                                                                        
                                                                        time.sleep(0.05)                                                                    
                                                                        bar2 = l.leitor2_in2()
                                                                        
                                                                        if bar2 == 1:

                                                                            tempo2 = 60

                                                                            while tempo2 > 0: # Enquanto a barreira esta acionada

                                                                                bar2 = l.leitor2_in2() # Faz a leitura da barreira 1                                                                                                                                                                                                                                                       

                                                                                if bar2 == 0:

                                                                                    time.sleep(0.05)
                                                                                    bar2 = l.leitor2_in2()

                                                                                    if bar2 == 0:

                                                                                        time.sleep(0.05)
                                                                                        bar2 = l.leitor2_in2()

                                                                                        if bar2 == 0:

                                                                                            log("Saiu da barreira Garagem 2")
                                                                                            s.desliga_rele3_exp2() # Sinal Vermelho
                                                                                            log("Entrou segundo veiculo autorizado Garagem 2")

                                                                                            entrada_permitida = 0
                                                                                            
                                                                                            tempo2 = 0
                                                                                            
                                                                                if tempo2 == 1:

                                                                                    log("Portão do segundo veiculo aberto por muito tempo Garagem 2 ")

                                                                                    s.desliga_rele3_exp2() # Sinal Vermelho

                                                                                    s.liga_rele4_exp2() # Sirene                                            
                                                                                    time.sleep(3)
                                                                                    s.desliga_rele4_exp2()

                                                                                    if eventos == "1":

                                                                                        evento.enviar("E","132","027") # Envia obstruçao

                                                                                    if eventos == "0":

                                                                                        print("Reconheceu que eventos esta desligado neste nivel 2 g2")

                                                                                    tempo2 = 1
                                                                                
                                                                                tempo2 = tempo2 - 1
                                                                                time.sleep(1)                                       

                                                                       
                                                                    if bar2 == 1 and entrada_permitida == 0: # Dupla passagem
                                                                        
                                                                        time.sleep(0.05)                                                                    
                                                                        bar2 = l.leitor2_in2()

                                                                        if bar2 == 1:

                                                                            if bar2 == 1 and entrada_permitida == 0: # Dupla passagem
                                                                        
                                                                                time.sleep(0.05)                                                                    
                                                                                bar2 = l.leitor2_in2()

                                                                                log("Dupla passagem Garagem 2")

                                                                                if eventos == "1":

                                                                                    evento.enviar("E","132","020")

                                                                                s.liga_rele4_exp2() # Sirene                                            
                                                                                time.sleep(10)
                                                                                s.desliga_rele4_exp2()                                            

                                                                                break
                                                                        
                                                             
                                                                    if pmg2 == 1: # portão ja fechou

                                                                        time.sleep(0.05)                                                                    
                                                                        pmg2 = l.leitor2_in1()

                                                                        if pmg2 == 1:

                                                                            time.sleep(0.05)                                                                    
                                                                            pmg2 = l.leitor2_in1()

                                                                            if pmg2 == 1:
                                                                                
                                                                                s.desliga_rele3_exp2() # Sinal Vermelho

                                                                                status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                                                                                status.write("0")
                                                                                status.close()

                                                                                if eventos == "1":
                                                                                
                                                                                    evento.enviar("R","133","017") # Envia o evento de fechamento para a central
                                                                                
                                                                                temp = 0
                                                                                break                                                                                                                                                     

                                                                    if temp == 1:

                                                                        log("Portão Garagem 2 aberto por muito tempo")

                                                                        s.desliga_rele3_exp2() # Sinal Vermelho

                                                                        s.liga_rele4_exp2() # Sirene                                            
                                                                        time.sleep(3)
                                                                        s.desliga_rele4_exp2()

                                                                        status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                                                                        status.write("0")
                                                                        status.close()

                                                                        if eventos == "1":

                                                                            evento.enviar("E","132","027") # Envia obstruçao

                                                                        temp = 0                                                                                                                                   
                                                                        break

                                                                    temp = temp - 1
                                                                    time.sleep(0.2)

                                                if pmg2 == 1:

                                                    time.sleep(0.05)
                                                    pmg2 = l.leitor2_in1()
                                                    
                                                    if pmg2 == 1:

                                                        time.sleep(0.05)
                                                        pmg2 = l.leitor2_in1()
                                                        
                                                        if pmg2 == 1:

                                                            log("Portão Garagem 2 fechou.")

                                                            s.desliga_rele3_exp2() # Sinal Vermelho

                                                            status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                                                            status.write("0")
                                                            status.close()

                                                            if eventos == "1":
                                                            
                                                                evento.enviar("R","133","017") # Envia o evento de fechamento para a central
                                                            
                                                            cont2 = 0
                                                            break
                                                                            
                                                if cont2 == 1:

                                                    log("Nao detectou nenhuma entrada ou saida Garagem 2")
                                                    s.desliga_rele3_exp2() # Sinal Vermelho
                                                    
                                                    break
                                                
                                                time.sleep(0.1)
                                                cont2 = cont2 - 1
                                                                    
                                                            
                                if cont1 == 1:

                                    log("Atingiu o tempo máximo e o portão da Garagem 2 não fechou")

                                    s.desliga_rele3_exp2() # Sinal Vermelho

                                    s.liga_rele4_exp2() # Sirene                                            
                                    time.sleep(3)
                                    s.desliga_rele4_exp2()

                                    status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                                    status.write("0")
                                    status.close()

                                    cont1 = 0
                                    break
                                
                                cont1 = cont1 - 1
                                time.sleep(0.1)

                if status_tx2 == "1" and pmg2 == 0:

                    log ("Recebeu comando para abrir Garagem 2 mas o portão no abriu")
                    
                    s.desliga_rele3_exp2() # Sinal Vermelho
                    
                    status = open("/home/pi/CMM/status_garagem_2.cmm","w") 
                    status.write("0")
                    status.close()
##            if mud1 == 1 and mudanca1 == 0: # Chave de mudança acionada
##
##                time.sleep(0.05)     
##                mud1 = l.leitor1_in4()  # Chave de mudança            
##
##                if mud1 == 1:
##
##                    time.sleep(0.05)     
##                    mud1 = l.leitor1_in4()  # Chave de mudança            
##
##                    if mud1 == 1:
##
##                        log("*")
##                        log("Chave de mudança acionada Garagem")
##
##                        s.liga_rele3_exp1() # Sinal Verde
##
##                        if evento == "1":
##
##                            evento.enviar("E","132","26")                
##
##                        t = open("/home/pi/CMM/status_garagem_1.cmm","w")
##                        t.write("1")
##                        t.close()
##
##                        s.liga_rele1_exp1() # Aciona o rele 1 do modulo 1 (Abre)
##                        time.sleep(2)
##                        s.desliga_rele1_exp1()
##                        s.liga_rele2_exp1() # Aciona o rele 2 do modulo 1 (Foto)                
##
##                        mudanca1 = 1
##
##            if mud1 == 0 and mudanca1 == 1:
##
##                time.sleep(0.05)
##                mud1 = l.leitor1_in4()
##
##                if mud1 == 0:
##
##                    time.sleep(0.05)
##                    mud1 = l.leitor1_in4()
##
##                    if mud1 == 0:
##
##                        log("Desligada a chave de mudança")
##
##                        s.desliga_rele3_exp1() # Sinal Vermelho
##
##                        if evento == "1":
##
##                            evento.enviar("R","132","26")
##                                        
##                        s.desliga_rele1_exp1() # Desliga o rele 1 do modulo 1 (Abre)
##                        s.desliga_rele2_exp1() # Desliga o rele 2 do modulo 1 (Foto) 
##
##                        pmg1 = l.leitor1_in1()
##
##                        cont = 60 # Tempo maximo de espera
##
##                        log("Aguardando portão Garagem fechar depois da mudanca")
##
##                        while cont > 0:
##                            
##                            pmg1 = l.leitor1_in1()                                                               
##                                    
##                            if pmg1 == 1: # Portão ja fechou
##
##                                time.sleep(0.05)
##                                pmg1 = l.leitor1_in1()
##
##                                if pmg1 == 1:
##
##                                    time.sleep(0.05)
##                                    pmg1 = l.leitor1_in1()
##
##                                    if pmg1 == 1:
##
##                                        log("Portão fechou")
##
##                                        s.desliga_rele3_exp1() # Sinal Vermelho
##
##                                        t = open("/home/pi/CMM/status_garagem_1.cmm","w")
##                                        t.write("0")
##                                        t.close()
##                                        
##                                        cont = 0
##                                        mudanca1 = 0
##                                        time.sleep(1)
##                                        break
##                                    
##                            if cont == 1:
##
##                                log("Chave de mudança desligou mas o portão no fechou após 1 min")
##
##                                s.desliga_rele3_exp1() # Sinal Vermelho
##
##                                t = open("/home/pi/CMM/status_garagem_1.cmm","w")
##                                t.write("0")
##                                t.close()
##
##                                s.liga_rele4_exp1() # Pulso na Sirene                                            
##                                time.sleep(3)
##                                s.desliga_rele4_exp1()                                
##                                
##                                mudanca1 = 0
##                                
##                                time.sleep(1)
##
##                            time.sleep(1)
##                            cont = cont - 1
##            time.sleep(0.2)
##            
##        except Exception as err:
##
##            print(err)
##            log(err)
##        
##    log("Saiu do loop da lógica do portão")
