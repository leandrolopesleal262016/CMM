# -*- coding:utf-8 -*-

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 06/06/2019

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
##import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import sys
import serial # Para comunicação serial 

ser = serial.Serial("/dev/ttyS0", 115200) # 9600 38400 115200 Configura a serial e a velocidade de transmissao

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

def LeModbus1(ser):

    buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
    time.sleep(0.1)
    buzzer = GPIO.output(11,0)
    
    packet = bytearray()  
    packet.append(0x07) # Endreço do modulo 
    packet.append(0x02) # Modo leitura
    packet.append(0x00) # 
    packet.append(0x00) # Endereço registrador inicial
    packet.append(0x00) # 
    packet.append(0x04) # Registradores a serem lidos
    packet.append(0x79)  
    packet.append(0xaf)
    
    GPIO.output(17, 1)  
    GPIO.output(18, 1)
    
    time.sleep(0.1)
    
    ser.write(packet)
    
    time.sleep(0.002)
    
    GPIO.output(17, 0)  
    GPIO.output(18, 0)
    
    time.sleep(0.02)
    
    bytesToRead = ser.inWaiting()  
    in_bin = ser.read(bytesToRead)

    print("\n",in_bin,type(in_bin))
        
    i = str(in_bin)
    i = i.split('x')

    print("\ndividida",i)
        
    i = (i[4])
    
    b = (i[1])
    print("b",b,type(b))

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
   

    print ("\nin1",in1, "\nin2", in2, "\nin3", in3, "\nin4",in4)
        


        
    
##    b = bytes(b, 'utf-8') 
##    print(bin(int.from_bytes(b, byteorder=sys.byteorder))) # Imprime os bits

while(1):

    a = LeModbus1(ser)

    time.sleep(5)

