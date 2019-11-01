import time
from banco import Banco
import wiringpi
import sys
import RPi.GPIO as GPIO
import smbus

bus = smbus.SMBus(1) # esta linha especifica qual dispositivo I2C a ser usado. 1 significa que o dispositivo I2C está localizado em / dev / I2C-1

out_A = 0b11111111 # Todos reles em 0

wiringpi.wiringPiSetup() # configura os 3 PCF8574 da placa de expansao

wiringpi.pcf8574Setup(100,0x25) # Definindo os pinos do rele como saida
for x in range (0, 9):                  

        wiringpi.pinMode(100+x,1)        
        wiringpi.digitalWrite(100+x,1)  # Inicia com o rele desligado


wiringpi.pcf8574Setup(200,0x26) # Definindo os pinos de saida digital como saida
for x in range (0, 9):

        wiringpi.pinMode(200+x,1)
        wiringpi.digitalWrite(200+x,1) 


wiringpi.pcf8574Setup(300, 0x27); # # Definindo os pinos de entrada digital como entradas


class Rele:  # Inicia a classe para acionamento dos reles  (liga / desliga / pulsa)
    
    def __init__(self):

        self.out_A = 0b11111111
        
        self.rele1 =  0b11111110
        self.rele2 =  0b11111101
        self.rele3 =  0b11111011
        self.rele4 =  0b11110111
        self.rele5 =  0b11101111
        self.rele6 =  0b11011111
        self.rele7 =  0b10111111
        self.rele8 =  0b01111111

        self.rele9  =  0b11111110
        self.rele10 =  0b11111101
        self.rele11 =  0b11111011
        self.rele12 =  0b11110111
        self.rele13 =  0b11101111
        self.rele14 =  0b11011111
        self.rele15 =  0b10111111
        self.rele16 =  0b01111111

        self.banco = Banco()

        self.banco.atualiza("status","out1","0")
        self.banco.atualiza("status","out2","0")
        self.banco.atualiza("status","out3","0")
        self.banco.atualiza("status","out4","0")
        self.banco.atualiza("status","out5","0")
        self.banco.atualiza("status","out6","0")
        self.banco.atualiza("status","out7","0")
        self.banco.atualiza("status","out8","0")
        self.banco.atualiza("status","out9","0")
        self.banco.atualiza("status","out10","0")
        self.banco.atualiza("status","out11","0")
        self.banco.atualiza("status","out12","0")
        self.banco.atualiza("status","out13","0")
        self.banco.atualiza("status","out14","0")
        self.banco.atualiza("status","out15","0")
        self.banco.atualiza("status","out16","0")       

 
    def liga(self,out):

        if out == 1 : self.out_A = 100
        if out == 2 : self.out_A = 101
        if out == 3 : self.out_A = 102
        if out == 4 : self.out_A = 103
        if out == 5 : self.out_A = 104
        if out == 6 : self.out_A = 105
        if out == 7 : self.out_A = 106
        if out == 8 : self.out_A = 107
        
        if out == 9  : self.out_A = 200
        if out == 10 : self.out_A = 201
        if out == 11 : self.out_A = 202
        if out == 12 : self.out_A = 203
        if out == 13 : self.out_A = 204
        if out == 14 : self.out_A = 205
        if out == 15 : self.out_A = 206
        if out == 16 : self.out_A = 207


        if out >= 1 and out <=16: # Saidas dos reles
            
            wiringpi.digitalWrite(self.out_A, 0) 
            sys.stdout.write("on" + str(out) + "\n")

            if out == 1:

                self.banco.atualiza("status","out1","1")

            if out == 2:

                self.banco.atualiza("status","out2","1")

            if out == 3:

                self.banco.atualiza("status","out3","1")

            if out == 4:

                self.banco.atualiza("status","out4","1")

            if out == 5:

                self.banco.atualiza("status","out5","1")
                
            if out == 6:

                self.banco.atualiza("status","out6","1")

            if out == 7:

                self.banco.atualiza("status","out7","1")

            if out == 8:

                self.banco.atualiza("status","out8","1")

            if out == 9:

                self.banco.atualiza("status","out9","1")

            if out == 10:

                self.banco.atualiza("status","out10","1")

            if out == 11:

                self.banco.atualiza("status","out11","1")

            if out == 12:

                self.banco.atualiza("status","out12","1")

            if out == 13:

                self.banco.atualiza("status","out13","1")

            if out == 14:

                self.banco.atualiza("status","out14","1")

            if out == 15:

                self.banco.atualiza("status","out15","1")

            if out == 16:

                self.banco.atualiza("status","out16","1")
            
   
    def desliga(self,out):

 
        if out == 1 : self.out_A = 100
        if out == 2 : self.out_A = 101
        if out == 3 : self.out_A = 102
        if out == 4 : self.out_A = 103
        if out == 5 : self.out_A = 104
        if out == 6 : self.out_A = 105
        if out == 7 : self.out_A = 106
        if out == 8 : self.out_A = 107

        if out == 9  : self.out_A = 200
        if out == 10 : self.out_A = 201
        if out == 11 : self.out_A = 202
        if out == 12 : self.out_A = 203
        if out == 13 : self.out_A = 204
        if out == 14 : self.out_A = 205
        if out == 15 : self.out_A = 206
        if out == 16 : self.out_A = 207

        if out >= 1 and out <=16: # Saidas dos reles
            
            wiringpi.digitalWrite(self.out_A, 1)
            sys.stdout.write("off"+ str(out) + "\n")

            if out == 1:

                self.banco.atualiza("status","out1","0")

            if out == 2:

                self.banco.atualiza("status","out2","0")

            if out == 3:

                self.banco.atualiza("status","out3","0")

            if out == 4:

                self.banco.atualiza("status","out4","0")

            if out == 5:

                self.banco.atualiza("status","out5","0")

            if out == 6:

                self.banco.atualiza("status","out6","0")

            if out == 7:

                self.banco.atualiza("status","out7","0")

            if out == 8:

                self.banco.atualiza("status","out8","0")

            if out == 9:

                self.banco.atualiza("status","out9","0")

            if out == 10:

                self.banco.atualiza("status","out10","0")

            if out == 11:

                self.banco.atualiza("status","out11","0")

            if out == 12:

                self.banco.atualiza("status","out12","0")

            if out == 13:

                self.banco.atualiza("status","out13","0")

            if out == 14:

                self.banco.atualiza("status","out14","0")
                
            if out == 15:

                self.banco.atualiza("status","out15","0")

            if out == 16:

                self.banco.atualiza("status","out16","0")
            
     
    def pulso(self,out,tempo):

        def __init__(self):

            Rele.__init__(self) # Inicia o construtor da classe Rele para ser usado aqui
            self.out = out
            self.tempo = out

        rele.liga(out)
        time.sleep(tempo)
        rele.desliga(out)

rele = Rele()

rele.liga(1)
time.sleep(1)
rele.desliga(1)

time.sleep(1)

rele.liga(2)
time.sleep(1)
rele.desliga(2)

time.sleep(1)

rele.liga(3)
time.sleep(1)
rele.desliga(3)

time.sleep(1)

rele.liga(4)
time.sleep(1)
rele.desliga(4)

time.sleep(1)

rele.liga(5)
time.sleep(1)
rele.desliga(5)

time.sleep(1)

rele.liga(6)
time.sleep(1)
rele.desliga(6)

time.sleep(1)

rele.liga(7)
time.sleep(1)
rele.desliga(7)

time.sleep(1)

rele.liga(8)
time.sleep(1)
rele.desliga(8)

rele.liga(9)
time.sleep(1)
rele.desliga(9)

time.sleep(1)

rele.liga(10)
time.sleep(1)
rele.desliga(10)

time.sleep(1)

rele.liga(11)
time.sleep(1)
rele.desliga(11)

time.sleep(1)

rele.liga(12)
time.sleep(1)
rele.desliga(12)

rele.liga(13)
time.sleep(1)
rele.desliga(13)

time.sleep(1)

rele.liga(14)
time.sleep(1)
rele.desliga(14)

time.sleep(1)

rele.liga(15)
time.sleep(1)
rele.desliga(15)

time.sleep(1)

rele.liga(16)
time.sleep(1)
rele.desliga(16)

