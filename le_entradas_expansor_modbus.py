# -*- coding:utf-8 -*-

# CMM Oficial com placa de expansão da BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 06/06/2019

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))
import sys
import serial # Para comunicação serial
import libscrc # biblioteca para calculo do CRC (Controle de Redundancia) - usado no protocolo modbus

ser = serial.Serial("/dev/ttyS0", 115200) # 9600 38400 115200 Configura a serial e a velocidade de transmissao

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT) # HIGH para enviar LOW para ler dados
GPIO.setup(18,GPIO.OUT) # HIGH para enviar LOW para ler dados

def le_entradas(ser):

    buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
    time.sleep(0.02)
    buzzer = GPIO.output(11,0)
    
    packet = bytearray()  
    packet.append(0x07) # endereço do modulo (dip switch) 
    packet.append(0x02) # modo leitura de rele 
    packet.append(0x00) # 
    packet.append(0x04) # endereço do rele (00,01,02,03) 
    packet.append(0x00) # 
    packet.append(0x04) # desiga rele
    
    packet.append(0x38) # Valor calculado pelo CRC
    packet.append(0x6e) # Valor calculado pelo CRC

    print("Pacote enviado",packet)
    
    GPIO.output(17, 1)  
    GPIO.output(18, 1)  
    time.sleep(0.1)
    
    ser.write(packet)
    
    time.sleep(0.01)
    
    GPIO.output(17, 0)  
    GPIO.output(18, 0)

    time.sleep(0.5)
    
    bytesToRead = ser.inWaiting()  
    in_bin = ser.read(bytesToRead)
    
    tag = ""   
    hexa = []   
    conv = ""
    
    for i in range(len(in_bin)):  
        tag += '%x' % ord(in_bin[i])        
         
    for i in range(6,12,2):  
        hexa.append(tag[i:i+2])
         
    for i in range(len(hexa)):  
        conv += str(hexa[i])
             
    try:
        
        if (int(conv) == 0):  
            return ""
        
        else:
            
            GerarLog("String Conversor: {}".format(tag), "String Tag")  
            return conv  

    except Exception as err:
        
        return ("Erro no metodo",err )
     
    return "Erro no modulo"

l = le_entradas()
print(l)
