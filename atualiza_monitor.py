import RPi.GPIO as GPIO
import time
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
##from functools import partial
from biblioteca_CMM_oficial import Rele
from banco import Banco
##import biblioteca_CMM as cmm

class Monitor:

    def __init__(self):

        self.banco = Banco()
    
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.IN)
        GPIO.setup(27,GPIO.IN)
        GPIO.setup(22,GPIO.IN)
        GPIO.setup(10,GPIO.IN)

        A = GPIO.input(4) # ENTRADAS NÃO FOTOACOPLADAS (As entradas A B C D então normalmente em nivel lógico HIGH (1))
        B = GPIO.input(27)
        C = GPIO.input(22)
        D = GPIO.input(10)

        self.cont1 = 0
        self.cont2 = 0
        self.cont3 = 0
        self.cont4 = 0
        self.cont5 = 0
        self.cont6 = 0
        self.cont7 = 0
        self.cont8 = 0
        self.cont9 = 0
        self.cont10 = 0
        self.cont11 = 0
        self.cont12 = 0
        self.cont13 = 0
        self.cont14 = 0
        self.cont15 = 0
        self.cont16 = 0
        self.cont17 = 0
        self.cont18 = 0
        self.cont19 = 0
        self.cont20 = 0
        self.cont21 = 0
        self.cont22 = 0
        self.cont23 = 0
        self.cont24 = 0
        self.cont25 = 0
        self.cont26 = 0
        self.cont27 = 0
        self.cont28 = 0
        
        self.banco.atualiza("status","in1","0")
        self.banco.atualiza("status","in2","0")
        self.banco.atualiza("status","in3","0")
        self.banco.atualiza("status","in4","0")
        self.banco.atualiza("status","in5","0")
        self.banco.atualiza("status","in6","0")
        self.banco.atualiza("status","in7","0")
        self.banco.atualiza("status","in8","0")
        
        self.banco.atualiza("status","inA","0")
        self.banco.atualiza("status","inB","0")
        self.banco.atualiza("status","inC","0")
        self.banco.atualiza("status","inD","0")
        
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
        
               

    def loop(self): # Loop para fazer leituras das entradas e acender os 'leds'

        self.i1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
        self.i2 = wiringpi.digitalRead(301)
        self.i3 = wiringpi.digitalRead(302)
        self.i4 = wiringpi.digitalRead(303)
        self.i5 = wiringpi.digitalRead(304)
        self.i6 = wiringpi.digitalRead(305)
        self.i7 = wiringpi.digitalRead(306)
        self.i8 = wiringpi.digitalRead(307)

        self.iA = GPIO.input(4) # Entrada A 
        self.iB = GPIO.input(27) # Entrada B 
        self.iC = GPIO.input(22) # Entrada C 
        self.iD = GPIO.input(10) # Entrada D

        in1 = self.i1
        in2 = self.i2
        in3 = self.i3
        in4 = self.i4
        in5 = self.i5
        in6 = self.i6
        in7 = self.i7
        in8 = self.i8
        inA = self.iA
        inB = self.iB
        inC = self.iC
        inD = self.iD

        if in1 == 0 and self.cont1 == 0:            
                                    
            self.banco.atualiza("status","in1","1") 
            self.cont1 = 1

        if in1 == 1 and self.cont1 == 1: 
                
            self.banco.atualiza("status","in1","0") 
            self.cont1 = 0

        if in2 == 0 and self.cont2 == 0:

            self.banco.atualiza("status","in2","1")
            self.cont2 = 1

        if in2 == 1 and self.cont2 == 1:
            
            self.banco.atualiza("status","in2","0")
            self.cont2 = 0

        if in3 == 0 and self.cont3 == 0:

            self.banco.atualiza("status","in3","1")
            self.cont3 = 1

        if in3 == 1 and self.cont3 == 1:
            
            self.banco.atualiza("status","in3","0")
            self.cont3 = 0

        if in4 == 0 and self.cont4 == 0:

            self.banco.atualiza("status","in4","1")
            self.cont4 = 1

        if in4 == 1 and self.cont4 == 1:
            
            self.banco.atualiza("status","in4","0")
            self.cont4 = 0
            
        if in5 == 0 and self.cont5 == 0:            
                                    
            self.banco.atualiza("status","in5","1") 
            self.cont5 = 1

        if in5 == 1 and self.cont5 == 1: 
                
            self.banco.atualiza("status","in5","0") 
            self.cont5 = 0

        if in6 == 0 and self.cont6 == 0:

            self.banco.atualiza("status","in6","1")
            self.cont6 = 1

        if in6 == 1 and self.cont6 == 1:
            
            self.banco.atualiza("status","in6","0")
            self.cont6 = 0

        if in7 == 0 and self.cont7 == 0:

            self.banco.atualiza("status","in7","1")
            self.cont7 = 1

        if in7 == 1 and self.cont7 == 1:
            
            self.banco.atualiza("status","in7","0")
            self.cont7 = 0

        if in8 == 0 and self.cont8 == 0:

            self.banco.atualiza("status","in8","1")
            self.cont8 = 1

        if in8 == 1 and self.cont8 == 1:
            
            self.banco.atualiza("status","in8","0")
            self.cont8 = 0

        if inA == 0 and self.cont9 == 0:

            self.banco.atualiza("status","inA","1")
            self.cont9 = 1

        if inA == 1 and self.cont9 == 1:
            
            self.banco.atualiza("status","inA","0")
            self.cont9 = 0

        if inB == 0 and self.cont10 == 0:

            self.banco.atualiza("status","inB","1")
            self.cont10 = 1

        if inB == 1 and self.cont10 == 1:
            
            self.banco.atualiza("status","inB","0")
            self.cont10 = 0

        if inC == 0 and self.cont11 == 0:

            self.banco.atualiza("status","inC","1")
            self.cont11 = 1

        if inC == 1 and self.cont11== 1:
            
            self.banco.atualiza("status","inC","0")
            self.cont11 = 0

        if inD == 0 and self.cont12 == 0:

            self.banco.atualiza("status","inD","1")
            self.cont12 = 1

        if inD == 1 and self.cont12 == 1:
            
            self.banco.atualiza("status","inD","0")
            self.cont12 = 0

# SAIDAS DE OUT1 ATé OUT16
        
        s1 = self.banco.consulta("status","out1")        

        if s1 == "1" and self.cont13 == 0:

            self.banco.atualiza("status","out1","1")
            self.cont13 = 1        

        if s1 == "0" and self.cont13 == 1:
            
            self.banco.atualiza("status","out1","0")
            self.cont13 = 0

            

        s2 = self.banco.consulta("status","out2")        

        if s2 == "1" and self.cont14 == 0:

            self.banco.atualiza("status","out2","1")
            self.cont14 = 1        

        if s2 == "0" and self.cont14 == 1:
            
            self.banco.atualiza("status","out2","0")
            self.cont14 = 0

            

        s3 = self.banco.consulta("status","out3")        

        if s3 == "1" and self.cont15 == 0:

            self.banco.atualiza("status","out3","1")
            self.cont15 = 1        

        if s3 == "0" and self.cont15 == 1:
            
            self.banco.atualiza("status","out3","0")
            self.cont15 = 0

            

        s4 = self.banco.consulta("status","out4")        

        if s4 == "1" and self.cont16 == 0:

            self.banco.atualiza("status","out4","1")
            self.cont16 = 1        

        if s4 == "0" and self.cont16 == 1:
            
            self.banco.atualiza("status","out4","0")
            self.cont16 = 0

            

        s5 = self.banco.consulta("status","out5")        

        if s5 == "1" and self.cont17 == 0:

            self.banco.atualiza("status","out5","1")
            self.cont17 = 1        

        if s5 == "0" and self.cont17 == 1:
            
            self.banco.atualiza("status","out5","0")
            self.cont17 = 0

            

        s6 = self.banco.consulta("status","out6")        

        if s6 == "1" and self.cont18 == 0:

            self.banco.atualiza("status","out6","1")
            self.cont18 = 1        

        if s6 == "0" and self.cont18 == 1:
            
            self.banco.atualiza("status","out6","0")
            self.cont18 = 0

            

        s7 = self.banco.consulta("status","out7")        

        if s7 == "1" and self.cont19 == 0:

            self.banco.atualiza("status","out7","1")
            self.cont19 = 1        

        if s7 == "0" and self.cont19 == 1:
            
            self.banco.atualiza("status","out7","0")
            self.cont19 = 0

            

        s8 = self.banco.consulta("status","out8")        

        if s8 == "1" and self.cont20 == 0:

            self.banco.atualiza("status","out8","1")
            self.cont20 = 1        

        if s8 == "0" and self.cont20 == 1:
            
            self.banco.atualiza("status","out8","0")
            self.cont20 = 0

            

        s9 = self.banco.consulta("status","out9")        

        if s9 == "1" and self.cont21 == 0:

            self.banco.atualiza("status","out9","1")
            self.cont21 = 1        

        if s9 == "0" and self.cont21 == 1:
            
            self.banco.atualiza("status","out9","0")
            self.cont21 = 0

            

        s10 = self.banco.consulta("status","out10")        

        if s10 == "1" and self.cont22 == 0:

            self.banco.atualiza("status","out10","1")
            self.cont22 = 1        

        if s10 == "0" and self.cont22 == 1:
            
            self.banco.atualiza("status","out10","0")
            self.cont22 = 0

            

        s11 = self.banco.consulta("status","out11")        

        if s11 == "1" and self.cont23 == 0:

            self.banco.atualiza("status","out11","1")
            self.cont23 = 1        

        if s11 == "0" and self.cont23 == 1:
            
            self.banco.atualiza("status","out11","0")
            self.cont23 = 0

            

        s12 = self.banco.consulta("status","out12")        

        if s12 == "1" and self.cont24 == 0:

            self.banco.atualiza("status","out12","1")
            self.cont24 = 1        

        if s12 == "0" and self.cont24 == 1:
            
            self.banco.atualiza("status","out12","0")
            self.cont24 = 0

            

        s13 = self.banco.consulta("status","out13")        

        if s13 == "1" and self.cont25 == 0:

            self.banco.atualiza("status","out13","1")
            self.cont25 = 1        

        if s13 == "0" and self.cont25 == 1:
            
            self.banco.atualiza("status","out13","0")
            self.cont25 = 0

            

        s14 = self.banco.consulta("status","out14")        

        if s14 == "1" and self.cont26 == 0:

            self.banco.atualiza("status","out14","1")
            self.cont26 = 1        

        if s14 == "0" and self.cont26 == 1:
            
            self.banco.atualiza("status","out14","0")
            self.cont26 = 0

            

        s15 = self.banco.consulta("status","out15")        

        if s15 == "1" and self.cont27 == 0:

            self.banco.atualiza("status","out15","1")
            self.cont27 = 1        

        if s15 == "0" and self.cont27 == 1:
            
            self.banco.atualiza("status","out15","0")
            self.cont27 = 0

            

        s16 = self.banco.consulta("status","out16")        

        if s16 == "1" and self.cont27 == 0:

            self.banco.atualiza("status","out16","1")
            self.cont27 = 1        

        if s16 == "0" and self.cont27 == 1:
            
            self.banco.atualiza("status","out16","0")
            self.cont27 = 0

            
        


        
