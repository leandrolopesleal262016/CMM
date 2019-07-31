# -*- coding:utf-8 -*-

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 24/07/2019

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import sys
import serial # Para comunicação serial
import libscrc # biblioteca para calculo do CRC (Controle de Redundancia) - usado no protocolo modbus
import _thread as thread

mutex = thread.allocate_lock() # Trava a thread para que seja executada sozina

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT) # HIGH para enviar LOW para ler dados
GPIO.setup(18,GPIO.OUT) # HIGH para enviar LOW para ler dados


class monta_pacote():

    def __init__(self):

        self = self
        self.ser = serial.Serial("/dev/ttyS0", 115200)
        
    def aciona(self,modulo,rele,funcao): # passar dados como string

        modulo = int(modulo,16)
        rele = int(rele,16)
        funcao = int(funcao,16)

        def crc16(byte):

            byte = bytes(byte)

            self.crc16 = libscrc.modbus(byte) #b'\x07\x05\x00\x00\xFF\x00')  # Estrutura para calculo do CRC

            bin2str = (hex(self.crc16))
            bin2str = str(bin2str)

            p = "0x"

            a1 = bin2str[-2]
            a2 = bin2str[-1]
            if a1 == "x":
                a1 = "0"
            a = p + a1 + a2
            
##            print("a",a)

            b1 = bin2str[-4]
            b2 = bin2str[-3]
            if b1 == "x":
                b1 = "0"
            b = p + b1 + b2
            
##            print("b",b)
            
            return(a,b)   
        
        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
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

##        print(hex(a))
##        print(hex(b))
            
        packet.append(a) # Controle de redundancia 
        packet.append(b) # Controle de redundancia 
        
        mutex.acquire() # Trava para acesso exclusivo
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)
        
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.002)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)

        time.sleep(0.02)  
        bytesToRead = self.ser.inWaiting()  
        in_bin = self.ser.read(bytesToRead)
        
        mutex.release() #Desbloqueia a trava de acesso

        packet_editado = str(packet)
        packet_editado = packet_editado.replace("bytearray(","")
        packet_editado = packet_editado.replace(")","")
        in_bin_editado = str (in_bin)

        cont = 5 # numero de vezes que tenta reenviar

        if packet_editado == in_bin_editado:

            if funcao ==  255:
                funcao = "ON"
            if funcao == 0:
                funcao = "OFF"

            if rele == 0:
                rele = "1"
            if rele == 1:
                rele = "2"
            if rele == 2:
                rele = "3"
            if rele == 3:
                rele = "4"  
                
            print("mod",modulo,"rele",rele,funcao)

        if packet_editado != in_bin_editado:

            while cont > 0:

##                print("Enviado",packet_editado)
##                print("Recebido",in_bin_editado)

                print("Os pacotes são diferentes, reenviando...")

                GPIO.output(17, 1)  
                GPIO.output(18, 1)
                
                time.sleep(0.1)
                
                self.ser.write(packet)
                
                time.sleep(0.002)
                
                GPIO.output(17, 0)  
                GPIO.output(18, 0)

                time.sleep(0.02)  
                bytesToRead = self.ser.inWaiting()  
                in_bin = self.ser.read(bytesToRead)

                packet_editado = str(packet)
                packet_editado = packet_editado.replace("bytearray(","")
                packet_editado = packet_editado.replace(")","")
                in_bin_editado = str (in_bin)

                if packet_editado == in_bin_editado:

                    print("Agora os pacotes são iguais")
                    cont = 0
                    break

                else:

                    print("Opa")
                    cont = cont -1


class Expansor(monta_pacote):

    def __init__(self):

        self.ser = serial.Serial("/dev/ttyS0", 115200) # 9600 38400 115200 
        self.mod = monta_pacote()
        
    
# Acionamentos modulo expansor 1

    def liga_rele1_exp1(self):

        self.mod.aciona('0x01','0x00','0xFF') # Modulo, rele , funcao

    def desliga_rele1_exp1(self):

        self.mod.aciona('0x01','0x00','0x00') 

    def liga_rele2_exp1(self):

        self.mod.aciona('0x01','0x01','0xFF') 

    def desliga_rele2_exp1(self):

        self.mod.aciona('0x01','0x01','0x00') 

    def liga_rele3_exp1(self):

        self.mod.aciona('0x01','0x02','0xFF') 

    def desliga_rele3_exp1(self):

        self.mod.aciona('0x01','0x02','0x00')

        
    def liga_rele4_exp1(self):

        self.mod.aciona('0x01','0x03','0xFF')

    def desliga_rele4_exp1(self):

        self.mod.aciona('0x01','0x03','0x00')        


# Acionamentos modulo expansor 2
    
    def liga_rele1_exp2(self):

        self.mod.aciona('0x02','0x00','0xFF') # Modulo, rele , funcao

    def desliga_rele1_exp2(self):

        self.mod.aciona('0x02','0x00','0x00')        

    def liga_rele2_exp2(self):

        self.mod.aciona('0x02','0x01','0xFF') 

    def desliga_rele2_exp2(self):

        self.mod.aciona('0x02','0x01','0x00')        

    def liga_rele3_exp2(self):

        self.mod.aciona('0x02','0x02','0xFF') 

    def desliga_rele3_exp2(self):

        self.mod.aciona('0x02','0x02','0x00')        

    def liga_rele4_exp2(self):

        self.mod.aciona('0x02','0x03','0xFF') 

    def desliga_rele4_exp2(self):

        self.mod.aciona('0x02','0x03','0x00')
        

# Acionamentos modulo expansor 3
    
    def liga_rele1_exp3(self):

        self.mod.aciona('0x03','0x00','0xFF') # Modulo, rele , funcao

    def desliga_rele1_exp3(self):

        self.mod.aciona('0x03','0x00','0x00')        

    def liga_rele2_exp3(self):

        self.mod.aciona('0x03','0x01','0xFF') 

    def desliga_rele2_exp3(self):

        self.mod.aciona('0x03','0x01','0x00')        

    def liga_rele3_exp3(self):

        self.mod.aciona('0x03','0x02','0xFF') 

    def desliga_rele3_exp3(self):

        self.mod.aciona('0x03','0x02','0x00')        

    def liga_rele4_exp3(self):

        self.mod.aciona('0x03','0x03','0xFF') 

    def desliga_rele4_exp3(self):

        self.mod.aciona('0x03','0x03','0x00') 


# Acionamentos modulo expansor 4
    
    def liga_rele1_exp4(self):

        self.mod.aciona('0x04','0x00','0xFF') # Modulo, rele , funcao

    def desliga_rele1_exp4(self):

        self.mod.aciona('0x04','0x00','0x00')        

    def liga_rele2_exp4(self):

        self.mod.aciona('0x04','0x01','0xFF') 

    def desliga_rele2_exp4(self):

        self.mod.aciona('0x04','0x01','0x00')        

    def liga_rele3_exp4(self):

        self.mod.aciona('0x04','0x02','0xFF') 

    def desliga_rele3_exp4(self):

        self.mod.aciona('0x04','0x02','0x00')        

    def liga_rele4_exp4(self):

        self.mod.aciona('0x04','0x03','0xFF') 

    def desliga_rele4_exp4(self):

        self.mod.aciona('0x04','0x03','0x00')

# Acionamentos modulo expansor 5
    
    def liga_rele1_exp5(self):

        self.mod.aciona('0x05','0x00','0xFF') # Modulo, rele , funcao

    def desliga_rele1_exp5(self):

        self.mod.aciona('0x05','0x00','0x00')        

    def liga_rele2_exp5(self):

        self.mod.aciona('0x05','0x01','0xFF') 

    def desliga_rele2_exp5(self):

        self.mod.aciona('0x05','0x01','0x00')        

    def liga_rele3_exp5(self):

        self.mod.aciona('0x05','0x02','0xFF') 

    def desliga_rele3_exp5(self):

        self.mod.aciona('0x05','0x02','0x00')        

    def liga_rele4_exp5(self):

        self.mod.aciona('0x05','0x03','0xFF') 

    def desliga_rele4_exp5(self):

        self.mod.aciona('0x05','0x03','0x00')

# Acionamentos modulo expansor 6
    
    def liga_rele1_exp6(self):

        self.mod.aciona('0x06','0x00','0xFF') # Modulo, rele , funcao

    def desliga_rele1_exp6(self):

        self.mod.aciona('0x06','0x00','0x00')        

    def liga_rele2_exp6(self):

        self.mod.aciona('0x06','0x01','0xFF') 

    def desliga_rele2_exp6(self):

        self.mod.aciona('0x06','0x01','0x00')        

    def liga_rele3_exp6(self):

        self.mod.aciona('0x06','0x02','0xFF') 

    def desliga_rele3_exp6(self):

        self.mod.aciona('0x06','0x02','0x00')        

    def liga_rele4_exp6(self):

        self.mod.aciona('0x06','0x03','0xFF') 

    def desliga_rele4_exp6(self):

        self.mod.aciona('0x06','0x03','0x00') 

# Acionamentos modulo expansor 7    
    
    def liga_rele1_exp7(self):

        self.mod.aciona('0x07','0x00','0xFF') 

    def desliga_rele1_exp7(self):

        self.mod.aciona('0x07','0x00','0x00') 

    def liga_rele2_exp7(self):

        self.mod.aciona('0x07','0x01','0xFF') 

    def desliga_rele2_exp7(self):

        self.mod.aciona('0x07','0x01','0x00') 

    def liga_rele3_exp7(self):

        self.mod.aciona('0x07','0x02','0xFF') 

    def desliga_rele3_exp7(self):

        self.mod.aciona('0x07','0x02','0x00') 
  
    def liga_rele4_exp7(self):

        self.mod.aciona('0x07','0x03','0xFF')        
    def desliga_rele4_exp7(self):

        self.mod.aciona('0x07','0x03','0x00')

# Acionamentos modulo expansor 8   
    
    def liga_rele1_exp8(self):

        self.mod.aciona('0x08','0x00','0xFF') 

    def desliga_rele1_exp8(self):

        self.mod.aciona('0x08','0x00','0x00') 

    def liga_rele2_exp8(self):

        self.mod.aciona('0x08','0x01','0xFF') 

    def desliga_rele2_exp8(self):

        self.mod.aciona('0x08','0x01','0x00') 

    def liga_rele3_exp8(self):

        self.mod.aciona('0x08','0x02','0xFF') 

    def desliga_rele3_exp8(self):

        self.mod.aciona('0x08','0x02','0x00') 
  
    def liga_rele4_exp8(self):

        self.mod.aciona('0x08','0x03','0xFF')        
    def desliga_rele4_exp8(self):

        self.mod.aciona('0x08','0x03','0x00')

# Acionamentos modulo expansor 9    
    
    def liga_rele1_exp9(self):

        self.mod.aciona('0x09','0x00','0xFF') 

    def desliga_rele1_exp9(self):

        self.mod.aciona('0x09','0x00','0x00') 

    def liga_rele2_exp9(self):

        self.mod.aciona('0x09','0x01','0xFF') 

    def desliga_rele2_exp9(self):

        self.mod.aciona('0x09','0x01','0x00') 

    def liga_rele3_exp9(self):

        self.mod.aciona('0x09','0x02','0xFF') 

    def desliga_rele3_exp9(self):

        self.mod.aciona('0x09','0x02','0x00') 
  
    def liga_rele4_exp9(self):

        self.mod.aciona('0x09','0x03','0xFF')        
    def desliga_rele4_exp9(self):

        self.mod.aciona('0x09','0x03','0x00')

# Acionamentos modulo expansor 10    
    
    def liga_rele1_exp10(self):

        self.mod.aciona('0xa','0x00','0xFF') 

    def desliga_rele1_exp10(self):

        self.mod.aciona('0xa','0x00','0x00') 

    def liga_rele2_exp10(self):

        self.mod.aciona('0xa','0x01','0xFF') 

    def desliga_rele2_exp10(self):

        self.mod.aciona('0xa','0x01','0x00') 

    def liga_rele3_exp10(self):

        self.mod.aciona('0xa','0x02','0xFF') 

    def desliga_rele3_exp10(self):

        self.mod.aciona('0xa','0x02','0x00') 
  
    def liga_rele4_exp10(self):

        self.mod.aciona('0xa','0x03','0xFF')        
    def desliga_rele4_exp10(self):

        self.mod.aciona('0xa','0x03','0x00')

# Acionamentos modulo expansor 11    
    
    def liga_rele1_exp11(self):

        self.mod.aciona('0xb','0x00','0xFF') 

    def desliga_rele1_exp11(self):

        self.mod.aciona('0xb','0x00','0x00') 

    def liga_rele2_exp11(self):

        self.mod.aciona('0xb','0x01','0xFF') 

    def desliga_rele2_exp11(self):

        self.mod.aciona('0xb','0x01','0x00') 

    def liga_rele3_exp11(self):

        self.mod.aciona('0xb','0x02','0xFF') 

    def desliga_rele3_exp11(self):

        self.mod.aciona('0xb','0x02','0x00') 
  
    def liga_rele4_exp11(self):

        self.mod.aciona('0xb','0x03','0xFF')        
    def desliga_rele4_exp11(self):

        self.mod.aciona('0xb','0x03','0x00')

# Acionamentos modulo expansor 12    
    
    def liga_rele1_exp12(self):

        self.mod.aciona('0xc','0x00','0xFF') 

    def desliga_rele1_exp12(self):

        self.mod.aciona('0xc','0x00','0x00') 

    def liga_rele2_exp12(self):

        self.mod.aciona('0xc','0x01','0xFF') 

    def desliga_rele2_exp12(self):

        self.mod.aciona('0xc','0x01','0x00') 

    def liga_rele3_exp12(self):

        self.mod.aciona('0xc','0x02','0xFF') 

    def desliga_rele3_exp12(self):

        self.mod.aciona('0xc','0x02','0x00') 
  
    def liga_rele4_exp12(self):

        self.mod.aciona('0xc','0x03','0xFF')        
    def desliga_rele4_exp12(self):

        self.mod.aciona('0xc','0x03','0x00')

# Acionamentos modulo expansor 13    
    
    def liga_rele1_exp13(self):

        self.mod.aciona('0xd','0x00','0xFF') 

    def desliga_rele1_exp13(self):

        self.mod.aciona('0xd','0x00','0x00') 

    def liga_rele2_exp13(self):

        self.mod.aciona('0xd','0x01','0xFF') 

    def desliga_rele2_exp13(self):

        self.mod.aciona('0xd','0x01','0x00') 

    def liga_rele3_exp13(self):

        self.mod.aciona('0xd','0x02','0xFF') 

    def desliga_rele3_exp13(self):

        self.mod.aciona('0xd','0x02','0x00') 
  
    def liga_rele4_exp13(self):

        self.mod.aciona('0xd','0x03','0xFF')        
    def desliga_rele4_exp13(self):

        self.mod.aciona('0xd','0x03','0x00')

# Acionamentos modulo expansor 14    
    
    def liga_rele1_exp14(self):

        self.mod.aciona('0xe','0x00','0xFF') 

    def desliga_rele1_exp14(self):

        self.mod.aciona('0xe','0x00','0x00') 

    def liga_rele2_exp14(self):

        self.mod.aciona('0xe','0x01','0xFF') 

    def desliga_rele2_exp14(self):

        self.mod.aciona('0xe','0x01','0x00') 

    def liga_rele3_exp14(self):

        self.mod.aciona('0xe','0x02','0xFF') 

    def desliga_rele3_exp14(self):

        self.mod.aciona('0xe','0x02','0x00') 
  
    def liga_rele4_exp14(self):

        self.mod.aciona('0xe','0x03','0xFF')        
    def desliga_rele4_exp14(self):

        self.mod.aciona('0xe','0x03','0x00')

# Acionamentos modulo expansor 15    
    
    def liga_rele1_exp15(self):

        self.mod.aciona('0xf','0x00','0xFF') 

    def desliga_rele1_exp15(self):

        self.mod.aciona('0xf','0x00','0x00') 

    def liga_rele2_exp15(self):

        self.mod.aciona('0xf','0x01','0xFF') 

    def desliga_rele2_exp15(self):

        self.mod.aciona('0xf','0x01','0x00') 

    def liga_rele3_exp15(self):

        self.mod.aciona('0xf','0x02','0xFF') 

    def desliga_rele3_exp15(self):

        self.mod.aciona('0xf','0x02','0x00') 
  
    def liga_rele4_exp15(self):

        self.mod.aciona('0xf','0x03','0xFF')        
    def desliga_rele4_exp15(self):

        self.mod.aciona('0xf','0x03','0x00')

# Acionamentos modulo expansor 16    
    
    def liga_rele1_exp16(self):

        self.mod.aciona('0x10','0x00','0xFF') 

    def desliga_rele1_exp16(self):

        self.mod.aciona('0x10','0x00','0x00') 

    def liga_rele2_exp16(self):

        self.mod.aciona('0x10','0x01','0xFF') 

    def desliga_rele2_exp16(self):

        self.mod.aciona('0x10','0x01','0x00') 

    def liga_rele3_exp16(self):

        self.mod.aciona('0x10','0x02','0xFF') 

    def desliga_rele3_exp16(self):

        self.mod.aciona('0x10','0x02','0x00') 
  
    def liga_rele4_exp16(self):

        self.mod.aciona('0x10','0x03','0xFF')        
    def desliga_rele4_exp16(self):

        self.mod.aciona('0x10','0x03','0x00')
        
    

       
