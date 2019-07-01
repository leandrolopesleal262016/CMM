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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT) # HIGH para enviar LOW para ler dados
GPIO.setup(18,GPIO.OUT) # HIGH para enviar LOW para ler dados

class Expansor:

    def __init__(self):

        self.ser = serial.Serial("/dev/ttyS0", 115200) # 9600 38400 115200 Configura a serial e a velocidade de transmissao

    
    def liga_rele1_exp1(self):
        
        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x00) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0x8c) # Controle de redundancia 
        packet.append(0x5c) # Controle de redundancia

        print("mod1 on1")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele1_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x00) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0xcd) # Valor calculado pelo CRC
        packet.append(0xac) # Valor calculado pelo CRC

        print("mod1 off1")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)


    def liga_rele2_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x01) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0xdd) # Controle de redundancia 
        packet.append(0x9c) # Controle de redundancia

        print("mod1 on2")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele2_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x01) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0x9c) # Valor calculado pelo CRC
        packet.append(0x6c) # Valor calculado pelo CRC

        print("mod1 off2")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)


    def liga_rele3_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x02) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0x2d) # Controle de redundancia 
        packet.append(0x9c) # Controle de redundancia

        print("mod1 on3")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele3_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x02) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0x6c) # Valor calculado pelo CRC
        packet.append(0x6c) # Valor calculado pelo CRC

        print("mod1 off3")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)


    def liga_rele4_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x03) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0x7c) # Controle de redundancia 
        packet.append(0x5c) # Controle de redundancia

        print("mod1 on4")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)

    def desliga_rele4_exp1(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x07) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x03) # endereço do rele (00,01,02,03) 
        packet.append(0x00) #
        packet.append(0x00) # desliga rele 
            
        packet.append(0x3d) # Controle de redundancia 
        packet.append(0xac) # Controle de redundancia

        print("mod1 off4")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def liga_rele1_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x00) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0x8c) # Controle de redundancia 
        packet.append(0x3a) # Controle de redundancia

        print("mod2 on1")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele1_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x00) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0xcd) # Valor calculado pelo CRC
        packet.append(0xca) # Valor calculado pelo CRC

        print("mod2 off1")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)

    def liga_rele2_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x01) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0xdd) # Controle de redundancia 
        packet.append(0xfa) # Controle de redundancia

        print("mod2 on2")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele2_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x01) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0x9c) # Valor calculado pelo CRC
        packet.append(0x0a) # Valor calculado pelo CRC

        print("mod2 off2")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)

    def liga_rele3_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x02) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0x2d) # Controle de redundancia 
        packet.append(0xfa) # Controle de redundancia

        print("mod2 on3")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele3_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x02) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0x6c) # Valor calculado pelo CRC
        packet.append(0x0a) # Valor calculado pelo CRC

        print("mod2 off3")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)


    def liga_rele4_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) #            
        packet.append(0x03) # endereço do rele (00,01,02,03) 
        packet.append(0xFF) #
        packet.append(0x00) # Liga rele 
            
        packet.append(0x7c) # Controle de redundancia 
        packet.append(0x3a) # Controle de redundancia

        print("mod2 on4")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)    


    def desliga_rele4_exp2(self):

        buzzer = GPIO.output(11,1) # Sinal De buzzer informando ligou
        time.sleep(0.02)
        buzzer = GPIO.output(11,0)
        
        packet = bytearray()  
        packet.append(0x01) # endereço do modulo (dip switch) 
        packet.append(0x05) # modo acionamento de rele 
        packet.append(0x00) # 
        packet.append(0x03) # endereço do rele (00,01,02,03) 
        packet.append(0x00) # 
        packet.append(0x00) # desiga rele
        
        packet.append(0x3d) # Valor calculado pelo CRC
        packet.append(0xca) # Valor calculado pelo CRC

        print("mod2 off4")
        
        GPIO.output(17, 1)  
        GPIO.output(18, 1)  
        time.sleep(0.1)
        
        self.ser.write(packet)
        
        time.sleep(0.01)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)


##liga_rele1(self)
##time.sleep(1)
##desliga_rele1(self)
##
##time.sleep(1)
##
##liga_rele2(self)
##time.sleep(1)
##desliga_rele2(self)
##
##time.sleep(1)
##
##liga_rele3(self)
##time.sleep(1)
##desliga_rele3(self)
##
##time.sleep(1)
##
##liga_rele4(self)
##time.sleep(1)
##desliga_rele4(self)
##
##time.sleep(1)
##
##i = liga_rele1_exp2(self)
##time.sleep(1)
##i = desliga_rele1_exp2(self)
##
##time.sleep(1)
##
##i = liga_rele2_exp2(self)
##time.sleep(1)
##i = desliga_rele2_exp2(self)
##
##time.sleep(1)
##
##i = liga_rele3_exp2(self)
##time.sleep(1)
##i = desliga_rele3_exp2(self)
##
##time.sleep(1)
##
##i = liga_rele4_exp2(self)
##time.sleep(1)
##i = desliga_rele4_exp2(self)
