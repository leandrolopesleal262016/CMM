#!/home/pi/CMM/bin/python3
# -*- coding:utf-8 -*-

# Leitor de entradas do Modulo expansorda BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 02/07/2019

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import sys
import serial # Para comunicação serial
import binascii

class Leitor:

    def __init__(self):        

        self.ser = serial.Serial("/dev/ttyS0", 115200) # 9600 38400 115200 Configura a serial e a velocidade de transmissao

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
                
    def leitor1_in1(self):

        ser = self.ser

##        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
##        time.sleep(0.1)
##        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xaf) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.02)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))           
                
        i = str(in_bin)    # Formata os dados recebidos
        i = str(i.split('\\'))
        i = i.replace("x","")
        i = i.replace("'","")
        i = i.replace("`","")
        i = i.replace(" ","")
        i = i.replace("!","")
        i= i.split(",")

        try:
                
            i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
              
            b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
            
            if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                b = "5"            
            if i == "ta":
                b = "9"
            if i == "n":
                b = "a"
            if i == "r":
                b = "d"
                        
            in1 = 0
            in2 = 0
            in3 = 0
            in4 = 0

            if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                in1 = 1
            
            if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                in2 = 1
            
            if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                in3 = 1
            
            if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                in4 = 1
           
            return(in1)

        except:
            pass
    
    def leitor1_in2(self):

        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x07) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xaf) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.02)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))           
                       
        i = str(in_bin)    # Formata os dados recebidos
        i = str(i.split('\\'))
        i = i.replace("x","")
        i = i.replace("'","")
        i = i.replace("`","")
        i = i.replace(" ","")
        i = i.replace("!","")
        i= i.split(",")

        try:
                
            i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
              
            b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
            
            if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                b = "5"            
            if i == "ta":
                b = "9"
            if i == "n":
                b = "a"
            if i == "r":
                b = "d"
                        
            in1 = 0
            in2 = 0
            in3 = 0
            in4 = 0

            if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                in1 = 1
            
            if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                in2 = 1
            
            if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                in3 = 1
            
            if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                in4 = 1       
            
            return(in2)

        except:
            pass

    def leitor1_in3(self):
    
        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x07) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xaf) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.02)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))           
                        
        i = str(in_bin)    # Formata os dados recebidos
        i = str(i.split('\\'))
        i = i.replace("x","")
        i = i.replace("'","")
        i = i.replace("`","")
        i = i.replace(" ","")
        i = i.replace("!","")
        i= i.split(",")

        try:
                        
            i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
              
            b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
            
            if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                b = "5"            
            if i == "ta":
                b = "9"
            if i == "n":
                b = "a"
            if i == "r":
                b = "d"
                        
            in1 = 0
            in2 = 0
            in3 = 0
            in4 = 0

            if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                in1 = 1
            
            if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                in2 = 1
            
            if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                in3 = 1
            
            if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                in4 = 1
           
            return(in3)

        except:

            pass

    def leitor1_in4(self):
    
        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x07) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xaf) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.02)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))           
                       
        i = str(in_bin)    # Formata os dados recebidos
        i = str(i.split('\\'))
        i = i.replace("x","")
        i = i.replace("'","")
        i = i.replace("`","")
        i = i.replace(" ","")
        i = i.replace("!","")
        i= i.split(",")

        try:
                     
            i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
              
            b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
            
            if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                b = "5"            
            if i == "ta":
                b = "9"
            if i == "n":
                b = "a"
            if i == "r":
                b = "d"
                        
            in1 = 0
            in2 = 0
            in3 = 0
            in4 = 0

            if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                in1 = 1
            
            if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                in2 = 1
            
            if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                in3 = 1
            
            if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                in4 = 1
           
            return(in4)

        except:
            pass

    def leitor2_in1(self):

        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x01) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xc9) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.01)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))

        if in_bin != b'':
                
            i = str(in_bin)    # Formata os dados recebidos
            i = str(i.split('\\'))
            i = i.replace("x","")
            i = i.replace("'","")
            i = i.replace("`","")
            i = i.replace(" ","")
            i = i.replace("!","")
            i = i.replace("I","")
            i = i.replace('"',"")
            i = i.replace("[","")
            i = i.replace("]","")
            i = i.replace("H","")
           
            try:
                i= i.split(",")
                                
                i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
                  
                b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                        
                if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
                if i == "":
                    b = "d"
                if i == "0eL":
                    b = "e"
                if i == "rM":
                    b = "d"
                            
                in1 = 0
                in2 = 0
                in3 = 0
                in4 = 0

                if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                    in1 = 1
                
                if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                    in2 = 1
                
                if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in3 = 1
                
                if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in4 = 1
               
                return(in1)
            
            except:
                pass
            
    
    def leitor2_in2(self):

        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x01) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xc9) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.01)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))

        if in_bin != b'':
                
            i = str(in_bin)    # Formata os dados recebidos
            i = str(i.split('\\'))
            i = i.replace("x","")
            i = i.replace("'","")
            i = i.replace("`","")
            i = i.replace(" ","")
            i = i.replace("!","")
            i = i.replace("I","")
            i = i.replace('"',"")
            i = i.replace("[","")
            i = i.replace("]","")
           
            try:
                i= i.split(",")
                                
                i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
                  
                b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                        
                if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
                if i == "":
                    b = "d"
                if i == "0eL":
                    b = "7"
                            
                in1 = 0
                in2 = 0
                in3 = 0
                in4 = 0

                if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                    in1 = 1
                
                if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                    in2 = 1
                
                if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in3 = 1
                
                if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in4 = 1
               
                return(in2)
            except:
                pass

    def leitor2_in3(self):
    
        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x01) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xc9) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.02)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead))           
                        
        if in_bin != b'':
                
            i = str(in_bin)    # Formata os dados recebidos
            i = str(i.split('\\'))
            i = i.replace("x","")
            i = i.replace("'","")
            i = i.replace("`","")
            i = i.replace(" ","")
            i = i.replace("!","")
            i = i.replace("I","")
            i = i.replace('"',"")
            i = i.replace("[","")
            i = i.replace("]","")
            
            try:
                i= i.split(",")
                                
                i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
                  
                b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                        
                if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
                if i == "":
                    b = "d"
                if i == "0eL":
                    b = "7"
                if i == "rM":
                    b = "d"
                            
                in1 = 0
                in2 = 0
                in3 = 0
                in4 = 0

                if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                    in1 = 1
                
                if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                    in2 = 1
                
                if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in3 = 1
                
                if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in4 = 1
               
                return(in3)
            
            except:
                pass
        

    def leitor2_in4(self):
    
        ser = self.ser
        
        packet = bytearray()  
        packet.append(0x01) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos
        packet.append(0x79) # crc16 
        packet.append(0xc9) # crc16
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)        
        time.sleep(0.1)
        
        ser.write(packet)
        
        time.sleep(0.002)        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)
        
        time.sleep(0.02)    
        
        bytesToRead = ser.inWaiting()        
        in_bin = (ser.read(bytesToRead)) 

        if in_bin != b'':
                
            i = str(in_bin)    # Formata os dados recebidos
            i = str(i.split('\\'))
            i = i.replace("x","")
            i = i.replace("'","")
            i = i.replace("`","")
            i = i.replace(" ","")
            i = i.replace("!","")
            i = i.replace("I","")
            i = i.replace('"',"")
            i = i.replace("[","")
            i = i.replace("]","")
            
            try:
                i= i.split(",")
                                
                i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
                  
                b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                        
                if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
                if i == "":
                    b = "d"
                if i == "0eL":
                    b = "e"
                if i == "rM":
                    b = "d"
                            
                in1 = 0
                in2 = 0
                in3 = 0
                in4 = 0

                if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
                    in1 = 1
                
                if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
                    in2 = 1
                
                if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in3 = 1
                
                if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
                    in4 = 1
               
                return(in4)
            
            except:
                pass
       
        
    
       

