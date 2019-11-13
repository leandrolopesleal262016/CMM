##!/usr/bin/env python3
# coding=UTF-8

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 01/11/2019

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import sys
import serial
import libscrc # biblioteca para calculo do CRC (Controle de Redundancia) - usado no protocolo modbus
import threading
import _thread as thread
from filtro import Filtro
from retorna import Retorna

mutex = thread.allocate_lock()

f = Filtro()
r = Retorna()

mutex = thread.allocate_lock() # Trava a thread para que seja executada sozina

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT) # HIGH para enviar LOW para ler dados
GPIO.setup(18,GPIO.OUT) # HIGH para enviar LOW para ler dados

os.system("sudo chmod 777 /dev/ttyS0") # Altera a permissão do acesso a serial

def escreve_serial(packet):    

    try:

        mutex.acquire() 

        time.sleep(0.005) # 004

        ser = serial.Serial("/dev/ttyS0", 115200)        
                
        GPIO.output(17, 1)  
        GPIO.output(18, 1)
        
        time.sleep(0.005) # 004
        
        ser.write(packet)
        
        time.sleep(0.002) # nao alterar este valor
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)

        time.sleep(0.005) # 004
        
        bytesToRead = ser.inWaiting()        
        in_bin = ser.read(bytesToRead)

        mutex.release() 
                        
        return in_bin

    except Exception as err:

        print("\nErro na leitura da serial",err)
        return ("b''")

def ler(modulo): # passar dados como string

    modulo = int(modulo,16) # Converte para um inteiro de base 16

    def crc16(byte):

        byte = bytes(byte)

        crc16 = libscrc.modbus(byte) #b'\x07\x05\x00\x00\xFF\x00')  # Estrutura para calculo do CRC

        bin2str = (hex(crc16))
        bin2str = str(bin2str)

        p = "0x"

        a1 = bin2str[-2]
        a2 = bin2str[-1]
        if a1 == "x":
            a1 = "0"
        a = p + a1 + a2            

        b1 = bin2str[-4]
        b2 = bin2str[-3]
        if b1 == "x":
            b1 = "0"
        b = p + b1 + b2
        
        return(a,b) 
           
    packet = bytearray()  
    packet.append(modulo) # Endreço do modulo 
    packet.append(0x02) # Modo leitura
    packet.append(0x00) # 
    packet.append(0x04) # Endereço registrador inicial
    packet.append(0x00) # 
    packet.append(0x04) # Registradores a serem lidos

    crc = crc16(packet)

    a = int(crc[0],16)
    b = int(crc[1],16)
        
    packet.append(a) # Controle de redundancia
    packet.append(b) # Controle de redundancia
                   
    in_bin1 = escreve_serial(packet)        

    in_bin1 = str(in_bin1)

    cont = 5

    if in_bin1 == "b''": # reenviando leitura            

        while cont > 0:  # reenviando leitura

            time.sleep(0.05)
            
            in_bin1 = escreve_serial(packet)
            in_bin1 = str(in_bin1)                
            
            if in_bin1 != "b''":
                
                in_bin1 = in_bin1                
                return(in_bin1)

            cont = cont - 1
            
    else:

        return(in_bin1)

def aciona(modulo,rele,funcao): # passar dados como string '0x01','0x01','0xFF'

    modulo = int(modulo,16)
    rele = int(rele,16)
    funcao = int(funcao,16)

    def crc16(byte):

        byte = bytes(byte)

        crc16 = libscrc.modbus(byte) #b'\x07\x05\x00\x00\xFF\x00')  # Estrutura para calculo do CRC

        bin2str = (hex(crc16))
        bin2str = str(bin2str)

        p = "0x"

        a1 = bin2str[-2]
        a2 = bin2str[-1]
        if a1 == "x":
            a1 = "0"
        a = p + a1 + a2            

        b1 = bin2str[-4]
        b2 = bin2str[-3]
        if b1 == "x":
            b1 = "0"
        b = p + b1 + b2 
        
        return(a,b) 
            
    packet = bytearray()  
    packet.append(modulo) # endereço do modulo (dip switch) 
    packet.append(0x05) # modo acionamento de rele 
    packet.append(0x00) #            
    packet.append(rele) # endereço do rele (00,01,02,03) 
    packet.append(funcao) # Liga / Desliga rele
    packet.append(0x00) #
   
    crc = crc16(packet)

    a = int(crc[0],16)
    b = int(crc[1],16)

    packet.append(a) # Controle de redundancia 
    packet.append(b) # Controle de redundancia        
    
    in_bin = escreve_serial(packet)              

    in_bin = str(in_bin)

    cont = 5

    if in_bin == "b''": # reenviando leitura            

        while cont > 0:  # reenviando leitura

            time.sleep(0.05)
            
            in_bin = escreve_serial(packet)
            in_bin = str(in_bin)
            
            if in_bin != "b''":                    
                               
                return(in_bin)

            cont = cont - 1
            
    else:

        return(in_bin)

def liga_rele1_exp1():

    aciona('0x01','0x00','0xFF') # Modulo, rele , funcao

def desliga_rele1_exp1():

    aciona('0x01','0x00','0x00') 

def liga_rele2_exp1():

    aciona('0x01','0x01','0xFF') 

def desliga_rele2_exp1():

    aciona('0x01','0x01','0x00') 

def liga_rele3_exp1():

    aciona('0x01','0x02','0xFF') 

def desliga_rele3_exp1():
    
    aciona('0x01','0x02','0x00')
    
def liga_rele4_exp1():

    aciona('0x01','0x03','0xFF')

def desliga_rele4_exp1():

    aciona('0x01','0x03','0x00')        


# Acionamentos modulo expansor 2

def liga_rele1_exp2():

    aciona('0x02','0x00','0xFF') # Modulo, rele , funcao

def desliga_rele1_exp2():

    aciona('0x02','0x00','0x00')        

def liga_rele2_exp2():

    aciona('0x02','0x01','0xFF') 

def desliga_rele2_exp2():

    aciona('0x02','0x01','0x00')        

def liga_rele3_exp2():

    aciona('0x02','0x02','0xFF') 

def desliga_rele3_exp2():

    aciona('0x02','0x02','0x00')        

def liga_rele4_exp2():

    aciona('0x02','0x03','0xFF') 

def desliga_rele4_exp2():

    aciona('0x02','0x03','0x00')    
           
# Leitor mdulo expansor 1

def leitor1_in1():

    i = ler('0x01') # modulo, entrada
    b = f.mdl1(i)       
    in1 = r.entrada(b,'in1')

    return(in1)
    
def leitor1_in2():

    i = ler('0x01')
    b = f.mdl1(i)
    in2 = r.entrada(b,'in2')        

    return(in2)
      
def leitor1_in3():

    i = ler('0x01')      
    b = f.mdl1(i)
    in3 = r.entrada(b,'in3')

    return(in3)    
        
def leitor1_in4():

    i = ler('0x01') 
    b = f.mdl1(i) 
    in4 = r.entrada(b,'in4')

    return(in4)




def leitor2_in1():

    i = ler('0x02') # modulo
    b = f.mdl2(i) # Limpa e edita os dados recebidos da leitura (i)
    in1 = r.entrada(b,'in1') 

    return(in1)

def leitor2_in2():

    i = ler('0x02')
    b = f.mdl2(i)        
    in2 = r.entrada(b,'in2')
    
    return(in2)            
       
def leitor2_in3():

    i = ler('0x02')   
    b = f.mdl2(i) 
    in3 = r.entrada(b,'in3') 

    return(in3)            
        
def leitor2_in4():

    i = ler('0x02')  
    b = f.mdl2(i) 
    in4 = r.entrada(b,'in4') 

    return(in4)

def printa(texto):

    mutex.acquire() 

    print(texto)

    mutex.release() 

def thread1():
    
    while(1):

        time.sleep(0.1)
               
        a = (leitor1_in1())            
        b = (leitor1_in2())                           
        c = (leitor1_in3())
        d = (leitor1_in4())

        txt = ("leitor 1",a,b,c,d)
        printa(txt)

        liga_rele1_exp1()
        time.sleep(1)
        desliga_rele1_exp1()

        time.sleep(1)
        
        liga_rele2_exp1()
        time.sleep(1)
        desliga_rele2_exp1()

        time.sleep(1)
        
        liga_rele3_exp1()
        time.sleep(1)
        desliga_rele3_exp1()

        time.sleep(1)
        
        liga_rele4_exp1()
        time.sleep(1)
        desliga_rele4_exp1()
        
        
            

def thread2():
    
    while(1):

        time.sleep(0.1)
               
        a = (leitor2_in1())            
        b = (leitor2_in2())                           
        c = (leitor2_in3())
        d = (leitor2_in4())

        txt = ("leitor 2",a,b,c,d)
        printa(txt)

        liga_rele1_exp2()
        time.sleep(1)
        desliga_rele1_exp2()

        time.sleep(1)
        
        liga_rele2_exp2()
        time.sleep(1)
        desliga_rele2_exp2()

        time.sleep(1)
        
        liga_rele3_exp2()
        time.sleep(1)
        desliga_rele3_exp2()

        time.sleep(1)
        
        liga_rele4_exp2()
        time.sleep(1)
        desliga_rele4_exp2()

            

t1 = threading.Thread(target=thread1)
t1.start()

t2 = threading.Thread(target=thread2)
t2.start()
##    
### Leitor mdulo expansor 2
##
##    def leitor2_in1():
##
##        i = ler('0x02') # modulo
##        b = filtro.mdl2(i) # Limpa e edita os dados recebidos da leitura (i)
##        in1 = retorna.entrada(b,'in1') 
##
##        return(in1)            
##           
##    def leitor2_in2():
##
##        i = ler('0x02')
##        b = filtro.mdl2(i)        
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##           
##    def leitor2_in3():
##    
##        i = ler('0x02')   
##        b = filtro.mdl2(i) 
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor2_in4():
##    
##        i = ler('0x02')  
##        b = filtro.mdl2(i) 
##        in4 = retorna.entrada(b,'in4') 
##
##        return(in4)
##    
### Leitor mdulo expansor 3
##
##    def leitor3_in1():
##
##        i = ler('0x03') # modulo, entrada
##        b = filtro.mdl3(i) # Limpa e edita os dados recebidos da leitura (i)
##        in1 = retorna.entrada(b,'in1') # Confere em uma tabela binaria qual o valor da entrada requisitada 'in1'
##        
##        return(in1)
##    
##    def leitor3_in2():
##
##        i = ler('0x03') 
##        b = filtro.mdl3(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor3_in3():
##    
##        i = ler('0x03') 
##        b = filtro.mdl3(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor3_in4():
##    
##        i = ler('0x03') 
##        b = filtro.mdl3(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 4
##                      
##    def leitor4_in1():        
##
##        i = ler('0x04') # modulo, entrada        
##        b = filtro.mdl4(i)
##        in1 = retorna.entrada(b,'in1')
##
##        return (in1)                            
##   
##    def leitor4_in2():
##
##        i = ler('0x04') 
##        b = filtro.mdl4(i)
##        in2 = retorna.entrada(b,'in2')                
##
##        return(in2)
##            
##    def leitor4_in3():
##
##        i = ler('0x04')
##        b = filtro.mdl4(i)                    
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)
##           
##    def leitor4_in4():
##    
##        i = ler('0x04') 
##        b = filtro.mdl4(i)
##        in4 = retorna.entrada(b,'in4') 
##
##        return(in4)
##
### Leitor mdulo expansor 5
##                      
##    def leitor5_in1():        
##
##        i = ler('0x05') # modulo, entrada        
##        b = filtro.mdl5(i)
##        in1 = retorna.entrada(b,'in1')
##
##        return (in1)
##               
##    def leitor5_in2():
##
##        i = ler('0x05') 
##        b = filtro.mdl5(i)
##        in2 = retorna.entrada(b,'in2')                
##
##        return(in2)
##            
##    def leitor5_in3():
##
##        i = ler('0x05') 
##        b = filtro.mdl5(i)                    
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)
##           
##    def leitor5_in4():
##    
##        i = ler('0x05') 
##        b = filtro.mdl5(i)
##        in4 = retorna.entrada(b,'in4') 
##
##        return(in4)
##
### Leitor mdulo expansor 6
##                      
##    def leitor6_in1():        
##
##        i = ler('0x06') # modulo, entrada        
##        b = filtro.mdl6(i)
##        in1 = retorna.entrada(b,'in1')
##
##        return (in1)
##               
##    def leitor6_in2():
##
##        i = ler('0x06') 
##        b = filtro.mdl6(i)
##        in2 = retorna.entrada(b,'in2')                
##
##        return(in2)
##            
##    def leitor6_in3():
##
##        i = ler('0x06') 
##        b = filtro.mdl6(i)                    
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)
##           
##    def leitor6_in4():
##    
##        i = ler('0x06') 
##        b = filtro.mdl6(i)
##        in4 = retorna.entrada(b,'in4') 
##
##        return(in4)
##    
### Leitor mdulo expansor 7
##
##    def leitor7_in1():
##
##        i = ler('0x07')       
##        b = filtro.mdl7(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor7_in2():
##
##        i = ler('0x07') 
##        b = filtro.mdl7(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor7_in3():
##    
##        i = ler('0x07') 
##        b = filtro.mdl7(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor7_in4():
##    
##        i = ler('0x07') 
##        b = filtro.mdl7(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##              
### Leitor mdulo expansor 8
##
##    def leitor8_in1():
##
##        i = ler('0x08')       
##        b = filtro.mdl8(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor8_in2():
##
##        i = ler('0x08') 
##        b = filtro.mdl8(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor8_in3():
##    
##        i = ler('0x08') 
##        b = filtro.mdl8(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor8_in4():
##    
##        i = ler('0x08') 
##        b = filtro.mdl8(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 9
##
##    def leitor9_in1():
##
##        i = ler('0x09')       
##        b = filtro.mdl9(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor9_in2():
##
##        i = ler('0x09') 
##        b = filtro.mdl9(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor9_in3():
##    
##        i = ler('0x09') 
##        b = filtro.mdl9(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor9_in4():
##    
##        i = ler('0x09') 
##        b = filtro.mdl9(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 10
##
##    def leitor10_in1():
##
##        i = ler('0x0a')       
##        b = filtro.mdl10(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor10_in2():
##
##        i = ler('0x0a') 
##        b = filtro.mdl10(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor10_in3():
##    
##        i = ler('0x0a') 
##        b = filtro.mdl10(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor10_in4():
##    
##        i = ler('0x0b') 
##        b = filtro.mdl11(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 11
##
##    def leitor11_in1():
##
##        i = ler('0x0b')        
##        b = filtro.mdl11(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor11_in2():
##
##        i = ler('0x0b') 
##        b = filtro.mdl11(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor11_in3():
##    
##        i = ler('0x0b') 
##        b = filtro.mdl11(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor11_in4():
##    
##        i = ler('0x0b') 
##        b = filtro.mdl11(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 12
##
##    def leitor12_in1():
##
##        i = ler('0x0c')        
##        b = filtro.mdl12(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor12_in2():
##
##        i = ler('0x0c') 
##        b = filtro.mdl12(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor12_in3():
##    
##        i = ler('0x0c') 
##        b = filtro.mdl12(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor12_in4():
##    
##        i = ler('0x0c') 
##        b = filtro.mdl12(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 13
##
##    def leitor13_in1():
##
##        i = ler('0x0d')       
##        b = filtro.mdl13(i) 
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor13_in2():
##
##        i = ler('0x0d') 
##        b = filtro.mdl13(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor13_in3():
##    
##        i = ler('0x0d') 
##        b = filtro.mdl13(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor13_in4():
##    
##        i = ler('0x0d') 
##        b = filtro.mdl13(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##    
### Leitor mdulo expansor 14
##
##    def leitor14_in1():
##
##        i = ler('0x0e')        
##        b = filtro.mdl14(i)        
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor14_in2():
##
##        i = ler('0x0e') 
##        b = filtro.mdl14(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor14_in3():
##    
##        i = ler('0x0e') 
##        b = filtro.mdl14(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor14_in4():
##    
##        i = ler('0x0e') 
##        b = filtro.mdl14(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##    
### Leitor mdulo expansor 15
##
##    def leitor15_in1():
##
##        i = ler('0x0f')        
##        b = filtro.mdl15(i)        
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor15_in2():
##
##        i = ler('0x0f') 
##        b = filtro.mdl15(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor15_in3():
##    
##        i = ler('0x0f') 
##        b = filtro.mdl15(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor15_in4():
##    
##        i = ler('0x0f') 
##        b = filtro.mdl15(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
### Leitor mdulo expansor 16
##
##    def leitor16_in1():
##
##        i = ler('0x10')        
##        b = filtro.mdl16(i)        
##        in1 = retorna.entrada(b,'in1') 
##        
##        return(in1)
##    
##    def leitor16_in2():
##
##        i = ler('0x10') 
##        b = filtro.mdl16(i)
##        in2 = retorna.entrada(b,'in2')
##        
##        return(in2)            
##         
##    def leitor16_in3():
##    
##        i = ler('0x10') 
##        b = filtro.mdl16(i)
##        in3 = retorna.entrada(b,'in3') 
##
##        return(in3)            
##            
##    def leitor16_in4():
##    
##        i = ler('0x10') 
##        b = filtro.mdl16(i)
##        in4 = retorna.entrada(b,'in4')
##        
##        return(in4)
##
