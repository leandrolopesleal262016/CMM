# Classe para leitura de entradas e acionamento de saidas do CMM
# Atualizado 08/07/2019

import time
import wiringpi
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

A = GPIO.input(4) # ENTRADAS NÃO FOTOACOPLADAS (As entradas A B C D então normalmente em nivel lógico HIGH (1))
B = GPIO.input(27)
C = GPIO.input(22)
D = GPIO.input(10)


hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
h = int(time.strftime('%H'))
data = time.strftime('%d/%m/%y')

class Entradas(object): # Inicia a thread leitura das entradas do CLP
    
    def __init__(self):            
    
        self.IN1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
        self.IN2 = wiringpi.digitalRead(301)  # entradas constantes
        self.IN3 = wiringpi.digitalRead(302)
        self.IN4 = wiringpi.digitalRead(303)
        self.IN5 = wiringpi.digitalRead(304)
        self.IN6 = wiringpi.digitalRead(305)
        self.IN7 = wiringpi.digitalRead(306)
        self.IN8 = wiringpi.digitalRead(307)

        self.A = GPIO.input(4) # Entrada A  # entradas constantes
        self.B = GPIO.input(27) # Entrada B 
        self.C = GPIO.input(22) # Entrada C 
        self.D = GPIO.input(10) # Entrada D

        entradas = []    
        txt = open("/home/pi/CMM/config.txt",'r')    
        for line in txt: 
            entradas.append(line)
        txt.close()
        
        line1 = (entradas[0])         # Coloca na variavel line1 o texto encontrado na linha 1
        line1 = line1.replace("\n","")  # Retira o \n do texto
        line2 = (entradas[1])         
        line2 = line2.replace("\n","")
        line3 = (entradas[2])
        line3 = line3.replace("\n","")
        line4 = (entradas[3])
        line4 = line4.replace("\n","")
        line5 = (entradas[4])
        line5 = line5.replace("\n","")  
        line6 = (entradas[5])
        line6 = line6.replace("\n","")  
        line7 = (entradas[6])
        line7 = line7.replace("\n","")
        line8 = (entradas[7])
        line8 = line8.replace("\n","")
        line9 = (entradas[8])
        line9 = (line9.replace("\n",""))
        line10 = (entradas[9])
        line10 = (line10.replace("\n",""))
        line11 = (entradas[10])
        line11 = (line11.replace("\n",""))
        line12 = (entradas[11])
        line12 = (line12.replace("\n",""))

            
        if line1 == "IN1":            
            self.pm1 = self.IN1
        if line1 == "IN2":
            self.pm1 = self.IN2
        if line1 == "IN3":
            self.pm1 = self.IN3
        if line1 == "IN4":
            self.pm1 = self.IN4
        if line1 == "IN5":
            self.pm1 = self.IN5
        if line1 == "IN6":
            self.pm1 = self.IN6
        if line1 == "IN7":
            self.pm1 = self.IN7
        if line1 == "IN8":
            self.pm1 = self.IN8
        if line1 == "A":
            self.pm1 = self.A
        if line1 == "B":
            self.pm1 = self.B
        if line1 == "C":
            self.pm1 = self.C
        if line1 == "D":
            self.pm1 = self.D
        if line1 == " --- ":
            self.pm1 == None

        if line2 == "IN1":            
            self.pm2 = self.IN1
        if line2 == "IN2":
            self.pm2 = self.IN2
        if line2 == "IN3":
            self.pm2 = self.IN3
        if line2 == "IN4":
            self.pm2 = self.IN4
        if line2 == "IN5":
            self.pm2 = self.IN5
        if line2 == "IN6":
            self.pm2 = self.IN6
        if line2 == "IN7":
            self.pm2 = self.IN7
        if line2 == "IN8":
            self.pm2 = self.IN8
        if line2 == "A":
            self.pm2 = self.A
        if line2 == "B":
            self.pm2 = self.B
        if line2 == "C":
            self.pm2 = self.C
        if line2 == "D":
            self.pm2 = self.D
        if line2 == " --- ":
            self.pm2 = None

        if line3 == "IN1":            
            self.pm3 = self.IN1
        if line3 == "IN2":
            self.pm3 = self.IN2
        if line3 == "IN3":
            self.pm3 = self.IN3
        if line3 == "IN4":
            self.pm3 = self.IN4
        if line3 == "IN5":
            self.pm3 = self.IN5
        if line3 == "IN6":
            self.pm3 = self.IN6
        if line3 == "IN7":
            self.pm3 = self.IN7
        if line3 == "IN8":
            self.pm3 = self.IN8
        if line3 == "A":
            self.pm3 = self.A
        if line3 == "B":
            self.pm3 = self.B
        if line3 == "C":
            self.pm3 = self.C
        if line3 == "D":
            self.pm3 = self.D
        if line3 == " --- ":
            self.pm3 = None

            
        if line4 == "IN1":            
            self.pm4 = self.IN1
        if line4 == "IN2":
            self.pm4 = self.IN2
        if line4 == "IN3":
            self.pm4 = self.IN3
        if line4 == "IN4":
            self.pm4 = self.IN4
        if line4 == "IN5":
            self.pm4 = self.IN5
        if line4 == "IN6":
            self.pm4 = self.IN6
        if line4 == "IN7":
            self.pm4 = self.IN7
        if line4 == "IN8":
            self.pm4 = self.IN8
        if line4 == "A":
            self.pm4 = self.A
        if line4 == "B":
            self.pm4 = self.B
        if line4 == "C":
            self.pm4 = self.C
        if line4 == "D":
            self.pm4 = self.D
        if line4 == " --- ":
            self.pm4 = None
            
        if line5 == "IN1":            
            self.pm5 = self.IN1
        if line5 == "IN2":
            self.pm5 = self.IN2
        if line5 == "IN3":
            self.pm5 = self.IN3
        if line5 == "IN4":
            self.pm5 = self.IN4
        if line5 == "IN5":
            self.pm5 = self.IN5
        if line5 == "IN6":
            self.pm5 = self.IN6
        if line5 == "IN7":
            self.pm5 = self.IN7
        if line5 == "IN8":
            self.pm5 = self.IN8
        if line5 == "A":
            self.pm5 = self.A
        if line5 == "B":
            self.pm5 = self.B
        if line5 == "C":
            self.pm5 = self.C
        if line5 == "D":
            self.pm5 = self.D
        if line5 == " --- ":
            self.pm5 = None

        if line6 == "IN1":            
            self.qbv = self.IN1
        if line6 == "IN2":
            self.qbv = self.IN2
        if line6 == "IN3":
            self.qbv = self.IN3
        if line6 == "IN4":
            self.qbv = self.IN4
        if line6 == "IN5":
            self.qbv = self.IN5
        if line6 == "IN6":
            self.qbv = self.IN6
        if line6 == "IN7":
            self.qbv = self.IN7
        if line6 == "IN8":
            self.qbv = self.IN8
        if line6 == "A":
            self.qbv = self.A
        if line6 == "B":
            self.qbv = self.B
        if line6 == "C":
            self.qbv = self.C
        if line6 == "D":
            self.qbv = self.D
        if line6 == " --- ":
            self.qbv = None

        if line7 == "IN1":            
            self.mud = self.IN1
        if line7 == "IN2":
            self.mud = self.IN2
        if line7 == "IN3":
            self.mud = self.IN3
        if line7 == "IN4":
            self.mud = self.IN4
        if line7 == "IN5":
            self.mud = self.IN5
        if line7 == "IN6":
            self.mud = self.IN6
        if line7 == "IN7":
            self.mud = self.IN7
        if line7 == "IN8":
            self.mud = self.IN8
        if line7 == "A":
            self.mud = self.A
        if line7 == "B":
            self.mud = self.B
        if line7 == "C":
            self.mud = self.C
        if line7 == "D":
            self.mud = self.D
        if line7 == " --- ":
            self.mud = None

        if line8 == "IN1":            
            self.qde = self.IN1
        if line8 == "IN2":
            self.qde = self.IN2
        if line8 == "IN3":
            self.qde = self.IN3
        if line8 == "IN4":
            self.qde = self.IN4
        if line8 == "IN5":
            self.qde = self.IN5
        if line8 == "IN6":
            self.qde = self.IN6
        if line8 == "IN7":
            self.qde = self.IN7
        if line8 == "IN8":
            self.qde = self.IN8
        if line8 == "A":
            self.qde = self.A
        if line8 == "B":
            self.qde = self.B
        if line8 == "C":
            self.qde = self.C
        if line8 == "D":
            self.qde = self.D
        if line8 == " --- ":
            self.qde = None

        if line9 == "IN1":            
            self.ctw4 = self.IN1
        if line9 == "IN2":
            self.ctw4 = self.IN2
        if line9 == "IN3":
            self.ctw4 = self.IN3
        if line9 == "IN4":
            self.ctw4 = self.IN4
        if line9 == "IN5":
            self.ctw4 = self.IN5
        if line9 == "IN6":
            self.ctw4 = self.IN6
        if line9 == "IN7":
            self.ctw4 = self.IN7
        if line9 == "IN8":
            self.ctw4 = self.IN8
        if line9 == "A":
            self.ctw4 = self.A
        if line9 == "B":
            self.ctw4 = self.B
        if line9 == "C":
            self.ctw4 = self.C
        if line9 == "D":
            self.ctw4 = self.D
        if line9 == " --- ":
            self.ctw4 = None

        if line10 == "IN1":            
            self.ctw3 = self.IN1
        if line10 == "IN2":
            self.ctw3 = self.IN2
        if line10 == "IN3":
            self.ctw3 = self.IN3
        if line10 == "IN4":
            self.ctw3 = self.IN4
        if line10 == "IN5":
            self.ctw3 = self.IN5
        if line10 == "IN6":
            self.ctw3 = self.IN6
        if line10 == "IN7":
            self.ctw3 = self.IN7
        if line10 == "IN8":
            self.ctw3 = self.IN8
        if line10 == "A":
            self.ctw3 = self.A
        if line10 == "B":
            self.ctw3 = self.B
        if line10 == "C":
            self.ctw3 = self.C
        if line10 == "D":
            self.ctw3 = self.D
        if line10 == " --- ":
            self.ctw3 = None

        if line11 == "IN1":            
            self.ctw2 = self.IN1
        if line11 == "IN2":
            self.ctw2 = self.IN2
        if line11 == "IN3":
            self.ctw2 = self.IN3
        if line11 == "IN4":
            self.ctw2 = self.IN4
        if line11 == "IN5":
            self.ctw2 = self.IN5
        if line11 == "IN6":
            self.ctw2 = self.IN6
        if line11 == "IN7":
            self.ctw2 = self.IN7
        if line11 == "IN8":
            self.ctw2 = self.IN8
        if line11 == "A":
            self.ctw2 = self.A
        if line11 == "B":
            self.ctw2 = self.B
        if line11 == "C":
            self.ctw2 = self.C
        if line11 == "D":
            self.ctw2 = self.D
        if line11 == " --- ":
            self.ctw2 = None

        if line12 == "IN1":            
            self.ctw1 = self.IN1
        if line12 == "IN2":
            self.ctw1 = self.IN2
        if line12 == "IN3":
            self.ctw1 = self.IN3
        if line12 == "IN4":
            self.ctw1 = self.IN4
        if line12 == "IN5":
            self.ctw1 = self.IN5
        if line12 == "IN6":
            self.ctw1 = self.IN6
        if line12 == "IN7":
            self.ctw1 = self.IN7
        if line12 == "IN8":
            self.ctw1 = self.IN8
        if line12 == "A":
            self.ctw1 = self.A
        if line12 == "B":
            self.ctw1 = self.B
        if line12 == "C":
            self.ctw1 = self.C
        if line12 == "D":
            self.ctw1 = self.D
        if line12 == " --- ":
            self.ctw1 = None  

    def pm1(self):
        return self.pm1

    def pm2(self):
        return self.pm2    

    def pm3(self):
        return self.pm3

    def pm4(self):
        return self.pm4

    def pm5(self):
        return self.pm5

    def qbv(self):
        return self.qbv

    def mud(self):
        return self.mud

    def qde(self):
        return self.qde

    def ctw1(self):
        return self.ctw1

    def ctw2(self):
        return self.ctw2

    def ctw3(self):
        return self.ctw3

    def ctw4(self):
        return self.ctw4

class Saidas(object): # Inicia a thread para acionamento das saidas do CLP (8 reles + 8 saidas a transistor) 
    
    def __init__(self):            
    
        saidas = []    
        txt = open("/home/pi/CMM/config.txt",'r')  # Obtem o endereço das saidas do arquivo config.tx  
        for line in txt: 
            saidas.append(line)
        txt.close()        
        
        line12 = (saidas[12])
        line12 = (line12.replace("\n",""))
        line13 = (saidas[13])
        line13 = (line13.replace("\n",""))
        line14 = (saidas[14])
        line14 = (line14.replace("\n",""))        
        line15 = (saidas[15])
        line15 = (line15.replace("\n",""))
        line16 = (saidas[16])
        line16 = (line16.replace("\n",""))
        line17 = (saidas[16])
        line17 = (line17.replace("\n",""))
        line18 = (saidas[17])
        line18 = (line18.replace("\n",""))
        line19 = (saidas[17])
        line19 = (line19.replace("\n",""))
        line20 = (saidas[18])
        line20 = (line20.replace("\n",""))
        line21 = (saidas[18])
        line21 = (line21.replace("\n",""))
        line22 = (saidas[19])
        line22 = (line22.replace("\n",""))
        line23 = (saidas[19])
        line23 = (line23.replace("\n",""))

            
        if line12 == "IN1":            
            self.rua = self.IN1
        if line12 == "IN2":
            self.rua = self.IN2
        if line12 == "IN3":
            self.rua = self.IN3
        if line12 == "IN4":
            self.rua = self.IN4
        if line12 == "IN5":
            self.rua = self.IN5
        if line12 == "IN6":
            self.rua = self.IN6
        if line12 == "IN7":
            self.rua = self.IN7
        if line12 == "IN8":
            self.rua = self.IN8
        if line12 == "A":
            self.rua = self.A
        if line12 == "B":
            self.rua = self.B
        if line12 == "C":
            self.rua = self.C
        if line12 == "D":
            self.rua = self.D
        if line12 == " --- ":
            self.rua == None

        if line13 == "IN1":            
            self.eclusa = self.IN1
        if line13 == "IN2":
            self.eclusa = self.IN2
        if line13 == "IN3":
            self.eclusa = self.IN3
        if line13 == "IN4":
            self.eclusa = self.IN4
        if line13 == "IN5":
            self.eclusa = self.IN5
        if line13 == "IN6":
            self.eclusa = self.IN6
        if line13 == "IN7":
            self.eclusa = self.IN7
        if line13 == "IN8":
            self.eclusa = self.IN8
        if line13 == "A":
            self.eclusa = self.A
        if line13 == "B":
            self.eclusa = self.B
        if line13 == "C":
            self.eclusa = self.C
        if line13 == "D":
            self.eclusa = self.D
        if line13 == " --- ":
            self.eclusa = None

        if line14 == "IN1":            
            self.pm3 = self.IN1
        if line14 == "IN2":
            self.pm3 = self.IN2
        if line14 == "IN3":
            self.pm3 = self.IN3
        if line14 == "IN4":
            self.pm3 = self.IN4
        if line14 == "IN5":
            self.pm3 = self.IN5
        if line14 == "IN6":
            self.pm3 = self.IN6
        if line14 == "IN7":
            self.pm3 = self.IN7
        if line14 == "IN8":
            self.pm3 = self.IN8
        if line14 == "A":
            self.pm3 = self.A
        if line14 == "B":
            self.pm3 = self.B
        if line14 == "C":
            self.pm3 = self.C
        if line14 == "D":
            self.pm3 = self.D
        if line14 == " --- ":
            self.pm3 = None

            
        if line15 == "IN1":            
            self.pm4 = self.IN1
        if line15 == "IN2":
            self.pm4 = self.IN2
        if line15 == "IN3":
            self.pm4 = self.IN3
        if line15 == "IN4":
            self.pm4 = self.IN4
        if line15 == "IN5":
            self.pm4 = self.IN5
        if line15 == "IN6":
            self.pm4 = self.IN6
        if line15 == "IN7":
            self.pm4 = self.IN7
        if line15 == "IN8":
            self.pm4 = self.IN8
        if line15 == "A":
            self.pm4 = self.A
        if line15 == "B":
            self.pm4 = self.B
        if line15 == "C":
            self.pm4 = self.C
        if line15 == "D":
            self.pm4 = self.D
        if line15 == " --- ":
            self.pm4 = None
            
        if line16 == "IN1":            
            self.pm5 = self.IN1
        if line16 == "IN2":
            self.pm5 = self.IN2
        if line16 == "IN3":
            self.pm5 = self.IN3
        if line16 == "IN4":
            self.pm5 = self.IN4
        if line16 == "IN5":
            self.pm5 = self.IN5
        if line16 == "IN6":
            self.pm5 = self.IN6
        if line16 == "IN7":
            self.pm5 = self.IN7
        if line16 == "IN8":
            self.pm5 = self.IN8
        if line16 == "A":
            self.pm5 = self.A
        if line16 == "B":
            self.pm5 = self.B
        if line16 == "C":
            self.pm5 = self.C
        if line16 == "D":
            self.pm5 = self.D
        if line16 == " --- ":
            self.pm5 = None

        if line17 == "IN1":            
            self.qbv = self.IN1
        if line17 == "IN2":
            self.qbv = self.IN2
        if line17 == "IN3":
            self.qbv = self.IN3
        if line17 == "IN4":
            self.qbv = self.IN4
        if line17 == "IN5":
            self.qbv = self.IN5
        if line17 == "IN6":
            self.qbv = self.IN6
        if line17 == "IN7":
            self.qbv = self.IN7
        if line17 == "IN8":
            self.qbv = self.IN8
        if line17 == "A":
            self.qbv = self.A
        if line17 == "B":
            self.qbv = self.B
        if line17 == "C":
            self.qbv = self.C
        if line17 == "D":
            self.qbv = self.D
        if line17 == " --- ":
            self.qbv = None

        if line18 == "IN1":            
            self.mud = self.IN1
        if line18 == "IN2":
            self.mud = self.IN2
        if line18 == "IN3":
            self.mud = self.IN3
        if line18 == "IN4":
            self.mud = self.IN4
        if line18 == "IN5":
            self.mud = self.IN5
        if line18 == "IN6":
            self.mud = self.IN6
        if line18 == "IN7":
            self.mud = self.IN7
        if line18 == "IN8":
            self.mud = self.IN8
        if line18 == "A":
            self.mud = self.A
        if line18 == "B":
            self.mud = self.B
        if line18 == "C":
            self.mud = self.C
        if line18 == "D":
            self.mud = self.D
        if line18 == " --- ":
            self.mud = None

        if line19 == "IN1":            
            self.qde = self.IN1
        if line19 == "IN2":
            self.qde = self.IN2
        if line19 == "IN3":
            self.qde = self.IN3
        if line19 == "IN4":
            self.qde = self.IN4
        if line19 == "IN5":
            self.qde = self.IN5
        if line19 == "IN6":
            self.qde = self.IN6
        if line19 == "IN7":
            self.qde = self.IN7
        if line19 == "IN8":
            self.qde = self.IN8
        if line19 == "A":
            self.qde = self.A
        if line19 == "B":
            self.qde = self.B
        if line19 == "C":
            self.qde = self.C
        if line19 == "D":
            self.qde = self.D
        if line19 == " --- ":
            self.qde = None

        if line20 == "IN1":            
            self.ctw4 = self.IN1
        if line20 == "IN2":
            self.ctw4 = self.IN2
        if line20 == "IN3":
            self.ctw4 = self.IN3
        if line20 == "IN4":
            self.ctw4 = self.IN4
        if line20 == "IN5":
            self.ctw4 = self.IN5
        if line20 == "IN6":
            self.ctw4 = self.IN6
        if line20 == "IN7":
            self.ctw4 = self.IN7
        if line20 == "IN8":
            self.ctw4 = self.IN8
        if line20 == "A":
            self.ctw4 = self.A
        if line20 == "B":
            self.ctw4 = self.B
        if line20 == "C":
            self.ctw4 = self.C
        if line20 == "D":
            self.ctw4 = self.D
        if line20 == " --- ":
            self.ctw4 = None

        if line21 == "IN1":            
            self.ctw3 = self.IN1
        if line21 == "IN2":
            self.ctw3 = self.IN2
        if line21 == "IN3":
            self.ctw3 = self.IN3
        if line21 == "IN4":
            self.ctw3 = self.IN4
        if line21 == "IN5":
            self.ctw3 = self.IN5
        if line21 == "IN6":
            self.ctw3 = self.IN6
        if line21 == "IN7":
            self.ctw3 = self.IN7
        if line21 == "IN8":
            self.ctw3 = self.IN8
        if line21 == "A":
            self.ctw3 = self.A
        if line21 == "B":
            self.ctw3 = self.B
        if line21 == "C":
            self.ctw3 = self.C
        if line21 == "D":
            self.ctw3 = self.D
        if line21 == " --- ":
            self.ctw3 = None

        if line22 == "IN1":            
            self.ctw2 = self.IN1
        if line22 == "IN2":
            self.ctw2 = self.IN2
        if line22 == "IN3":
            self.ctw2 = self.IN3
        if line22 == "IN4":
            self.ctw2 = self.IN4
        if line22 == "IN5":
            self.ctw2 = self.IN5
        if line22 == "IN6":
            self.ctw2 = self.IN6
        if line22 == "IN7":
            self.ctw2 = self.IN7
        if line22 == "IN8":
            self.ctw2 = self.IN8
        if line22 == "A":
            self.ctw2 = self.A
        if line22 == "B":
            self.ctw2 = self.B
        if line22 == "C":
            self.ctw2 = self.C
        if line22 == "D":
            self.ctw2 = self.D
        if line22 == " --- ":
            self.ctw2 = None

        if line23 == "IN1":            
            self.ctw1 = self.IN1
        if line23 == "IN2":
            self.ctw1 = self.IN2
        if line23 == "IN3":
            self.ctw1 = self.IN3
        if line23 == "IN4":
            self.ctw1 = self.IN4
        if line23 == "IN5":
            self.ctw1 = self.IN5
        if line23 == "IN6":
            self.ctw1 = self.IN6
        if line23 == "IN7":
            self.ctw1 = self.IN7
        if line23 == "IN8":
            self.ctw1 = self.IN8
        if line23 == "A":
            self.ctw1 = self.A
        if line23 == "B":
            self.ctw1 = self.B
        if line23 == "C":
            self.ctw1 = self.C
        if line23 == "D":
            self.ctw1 = self.D
        if line23 == " --- ":
            self.ctw1 = None  

    def rua(self):
        return self.rua

    def eclusa(self):
        return self.eclusa    

    def pm3(self):
        return self.pm3

    def pm4(self):
        return self.pm4

    def pm5(self):
        return self.pm5

    def qbv(self):
        return self.qbv

    def mud(self):
        return self.mud

    def qde(self):
        return self.qde

    def ctw1(self):
        return self.ctw1

    def ctw2(self):
        return self.ctw2

    def ctw3(self):
        return self.ctw3

    def ctw4(self):
        return self.ctw4
