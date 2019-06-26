import RPi.GPIO as GPIO
import time
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
from biblioteca_CMM_oficial import Rele

class Monitor:

    def __init__(self):
    
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
                
        self.monitor = Tk()
        menubar = Menu(self.monitor)
        self.monitor.config(menu=menubar)
        self.monitor.title('Monitoramento Entradas / Saídas')
        self.monitor.geometry('400x300')
        self.monitor.maxsize(width=400, height=300) # Limita o tamaho maximo
        self.monitor.minsize(width=400, height=300) # Limita o tamanho minimo

        imagem = PhotoImage(file='/home/pi/img/CASE_CMM.png')
        label = Label(self.monitor, image = imagem)
        label.pack()

        self.ligado =  PhotoImage(file='/home/pi/img/ligado.png') # Led verde

        self.monitor.after(200,self.loop) # Chama a rotina de loop depois 0.2 segundos
                
        self.monitor.mainloop()
        

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

            self.in1 = Label(self.monitor,image = self.ligado)
            self.in1.configure(background = "black")
            self.in1.place(x=348,y=256)
            self.cont1 = 1

        if in1 == 1 and self.cont1 == 1:
            try:
                self.in1.place_forget()
            except Exception as err:
                pass
            finally:
                self.cont1 = 0

        if in2 == 0 and self.cont2 == 0:

            self.in2 = Label(self.monitor,image = self.ligado)
            self.in2.configure(background = "black")
            self.in2.place(x=348,y=242)
            self.cont2 = 1

        if in2 == 1 and self.cont2 == 1:
            try:
                self.in2.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont2 = 0

        if in3 == 0 and self.cont3 == 0:

            self.in3 = Label(self.monitor,image = self.ligado)
            self.in3.configure(background = "black")
            self.in3.place(x=348,y=228)
            self.cont3 = 1

        if in3 == 1 and self.cont3 == 1:
            try:
                self.in3.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont3 = 0

        if in4 == 0 and self.cont4 == 0:

            self.in4 = Label(self.monitor,image = self.ligado)
            self.in4.configure(background = "black")
            self.in4.place(x=348,y=214)
            self.cont4 = 1

        if in4 == 1 and self.cont4 == 1:
            try:
                self.in4.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont4 = 0

        if in5 == 0 and self.cont5 == 0:

            self.in5 = Label(self.monitor,image = self.ligado)
            self.in5.configure(background = "black")
            self.in5.place(x=348,y=200)
            self.cont5 = 1

        if in5 == 1 and self.cont5 == 1:
            try:
                self.in5.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont5 = 0

        if in6 == 0 and self.cont6 == 0:

            self.in6 = Label(self.monitor,image = self.ligado)
            self.in6.configure(background = "black")
            self.in6.place(x=348,y=186)
            self.cont6 = 1

        if in6 == 1 and self.cont6 == 1:
            try:
                self.in6.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont6 = 0

        if in7 == 0 and self.cont7 == 0:

            self.in7 = Label(self.monitor,image = self.ligado)
            self.in7.configure(background = "black")
            self.in7.place(x=348,y=172)
            self.cont7 = 1

        if in7 == 1 and self.cont7 == 1:
            try:
                self.in7.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont7 = 0

        if in8 == 0 and self.cont8 == 0:

            self.in8 = Label(self.monitor,image = self.ligado)
            self.in8.configure(background = "black")
            self.in8.place(x=348,y=158)
            self.cont8 = 1

        if in8 == 1 and self.cont8 == 1:
            try:
                self.in8.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont8 = 0

        if inA == 0 and self.cont9 == 0:

            self.A = Label(self.monitor,image = self.ligado)
            self.A.configure(background = "black")
            self.A.place(x=111,y=251)
            self.cont9 = 1

        if inA == 1 and self.cont9 == 1:
            try:
                self.A.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont9 = 0

        if inB == 0 and self.cont10 == 0:

            self.B = Label(self.monitor,image = self.ligado)
            self.B.configure(background = "black")
            self.B.place(x=140,y=250)
            self.cont10 = 1

        if inB == 1 and self.cont10 == 1:
            try:
                self.B.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont10 = 0

        if inC == 0 and self.cont11 == 0:

            self.C = Label(self.monitor,image = self.ligado)
            self.C.configure(background = "black")
            self.C.place(x=169,y=250)
            self.cont11 = 1

        if inC == 1 and self.cont11 == 1:
            try:
                self.C.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont11 = 0

        if inD == 0 and self.cont12 == 0:

            self.D = Label(self.monitor,image = self.ligado)
            self.D.configure(background = "black")
            self.D.place(x=198,y=250)
            self.cont12 = 1

        if inD == 1 and self.cont12 == 1:
            try:
                self.D.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont12 = 0

        txt = open("out1.cmm","r")
        s1 = txt.read()
        txt.close()

        if s1 == "1" and self.cont13 == 0:

            self.out1 = Label(self.monitor,image = self.ligado)
            self.out1.configure(background = "black")
            self.out1.place(x=48,y=95)
            self.cont13 = 1        

        if s1 == "0" and self.cont13 == 1:
            try:
                self.out1.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont13 = 0

        txt = open("out2.cmm","r")
        s2 = txt.read()
        txt.close()

        if s2 == "1" and self.cont14 == 0:

            self.out2 = Label(self.monitor,image = self.ligado)
            self.out2.configure(background = "black")
            self.out2.place(x=79,y=95)
            self.cont14 = 1

        if s2 == "0" and self.cont14 == 1:
            try:
                self.out2.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont14 = 0

        txt = open("out3.cmm","r")
        s3 = txt.read()
        txt.close()

        if s3 == "1" and self.cont15 == 0:

            self.out3 = Label(self.monitor,image = self.ligado)
            self.out3.configure(background = "black")
            self.out3.place(x=111,y=95)
            self.cont15 = 1

        if s3 == "0" and self.cont15 == 1:
            try:
                self.out3.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont15 = 0

        txt = open("out4.cmm","r")
        s4 = txt.read()
        txt.close()

        if s4 == "1" and self.cont16 == 0:

            self.out4 = Label(self.monitor,image = self.ligado)
            self.out4.configure(background = "black")
            self.out4.place(x=143,y=95)
            self.cont16 = 1

        if s4 == "0" and self.cont16 == 1:
            try:
                self.out4.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont16 = 0

        txt = open("out5.cmm","r")
        s5 = txt.read()
        txt.close()

        if s5 == "1" and self.cont17 == 0:

            self.out5 = Label(self.monitor,image = self.ligado)
            self.out5.configure(background = "black")
            self.out5.place(x=174,y=95)
            self.cont17 = 1

        if s5 == "0" and self.cont17 == 1:
            try:
                self.out5.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont17 = 0


        txt = open("out6.cmm","r")
        s6 = txt.read()
        txt.close()

        if s6 == "1" and self.cont18 == 0:

            self.out6 = Label(self.monitor,image = self.ligado)
            self.out6.configure(background = "black")
            self.out6.place(x=206,y=95)
            self.cont18 = 1

        if s6 == "0" and self.cont18 == 1:
            try:
                self.out6.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont18 = 0

        txt = open("out7.cmm","r")
        s7 = txt.read()
        txt.close()

        if s7 == "1" and self.cont19 == 0:

            self.out7 = Label(self.monitor,image = self.ligado)
            self.out7.configure(background = "black")
            self.out7.place(x=238,y=95)
            self.cont19 = 1

        if s7 == "0" and self.cont19 == 1:
            try:
                self.out7.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont19 = 0

        txt = open("out8.cmm","r")
        s8 = txt.read()
        txt.close()

        if s8 == "1" and self.cont20 == 0:

            self.out8 = Label(self.monitor,image = self.ligado)
            self.out8.configure(background = "black")
            self.out8.place(x=270,y=95)
            self.cont20 = 1

        if s8 == "0" and self.cont20 == 1:
            try:
                self.out8.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont20 = 0
        

        txt = open("out9.cmm","r")
        s9 = txt.read()
        txt.close()

        if s9 == "1" and self.cont21 == 0:

            self.out9 = Label(self.monitor,image = self.ligado)
            self.out9.configure(background = "black")
            self.out9.place(x=348,y=23)
            self.cont21 = 1        

        if s9 == "0" and self.cont21 == 1:
            try:
                self.out9.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont21 = 0

        txt = open("out10.cmm","r")
        s10 = txt.read()
        txt.close()

        if s10 == "1" and self.cont22 == 0:

            self.out10 = Label(self.monitor,image = self.ligado)
            self.out10.configure(background = "black")
            self.out10.place(x=348,y=37)
            self.cont22 = 1

        if s10 == "0" and self.cont22 == 1:
            try:
                self.out10.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont22 = 0

        txt = open("out11.cmm","r")
        s11 = txt.read()
        txt.close()

        if s11 == "1" and self.cont23 == 0:

            self.out11 = Label(self.monitor,image = self.ligado)
            self.out11.configure(background = "black")
            self.out11.place(x=348,y=51)
            self.cont23 = 1

        if s11 == "0" and self.cont23 == 1:
            try:
                self.out11.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont23 = 0

        txt = open("out12.cmm","r")
        s12 = txt.read()
        txt.close()

        if s12 == "1" and self.cont24 == 0:

            self.out12 = Label(self.monitor,image = self.ligado)
            self.out12.configure(background = "black")
            self.out12.place(x=348,y=65)
            self.cont24 = 1

        if s12 == "0" and self.cont24 == 1:
            try:
                self.out12.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont24 = 0

        txt = open("out13.cmm","r")
        s13 = txt.read()
        txt.close()

        if s13 == "1" and self.cont25 == 0:

            self.out13 = Label(self.monitor,image = self.ligado)
            self.out13.configure(background = "black")
            self.out13.place(x=348,y=79)
            self.cont25 = 1

        if s13 == "0" and self.cont25 == 1:
            try:
                self.out13.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont25 = 0


        txt = open("out14.cmm","r")
        s14 = txt.read()
        txt.close()

        if s14 == "1" and self.cont26 == 0:

            self.out14 = Label(self.monitor,image = self.ligado)
            self.out14.configure(background = "black")
            self.out14.place(x=348,y=93)
            self.cont26 = 1

        if s14 == "0" and self.cont26 == 1:
            try:
                self.out14.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont26 = 0

        txt = open("out15.cmm","r")
        s15 = txt.read()
        txt.close()

        if s15 == "1" and self.cont27 == 0:

            self.out15 = Label(self.monitor,image = self.ligado)
            self.out15.configure(background = "black")
            self.out15.place(x=348,y=107)
            self.cont27 = 1

        if s15 == "0" and self.cont27 == 1:
            try:
                self.out15.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont27 = 0

        txt = open("out16.cmm","r")
        s16 = txt.read()
        txt.close()

        if s16 == "1" and self.cont28 == 0:

            self.out16 = Label(self.monitor,image = self.ligado)
            self.out16.configure(background = "black")
            self.out16.place(x=348,y=121)
            self.cont28 = 1

        if s16 == "0" and self.cont28 == 1:
            try:
                self.out16.place_forget()
            except Exception as err:
                pass

            finally:
                self.cont28 = 0

        self.monitor.after(200, self.loop)
        
m = Monitor()        

        


##    while (1):
##
##        i1 = wiringpi.digitalRead(300)  # Configuraçoes pinos de entrada necessarios para atualizar as entradas
##        i2 = wiringpi.digitalRead(301)
##        i3 = wiringpi.digitalRead(302)
##        i4 = wiringpi.digitalRead(303)
##        i5 = wiringpi.digitalRead(304)
##        i6 = wiringpi.digitalRead(305)
##        i7 = wiringpi.digitalRead(306)
##        i8 = wiringpi.digitalRead(307)
##
##        iA = GPIO.input(4) # Entrada A 
##        iB = GPIO.input(27) # Entrada B 
##        iC = GPIO.input(22) # Entrada C 
##        iD = GPIO.input(10) # Entrada D 
##
##        pm1 = i1
##        pm2 = i2
##        b1 = iC
##        b2 = iD
##
##        ctw1 = i4
##        ctw2 = i5
##        in3 = i3
##        ctw1 = i4
##        ctw2 = i5
##        qbv = i6
##        qde = i7
##        in8 = i8
##
##
##        if ctw1 == 0:
##
##            print("Reconheceu ctw1")
##
##            in1 = Label(monitor,image = ligado)
##            in1.configure(background = "black")
##            in1.place(x=348,y=256)
##
         

##monitor = threading.Thread(target=Monitor)
##monitor.start()

##self.in8 = Label(self,image = ligado)
##self.in8.configure(background = "black")
##self.in8.place(x=348,y=158)
##
##self.in7 = Label(self,image = ligado)
##self.in7.configure(background = "black")
##self.in7.place(x=348,y=172)
##
##self.in6 = Label(self,image = ligado)
##self.in6.configure(background = "black")
##self.in6.place(x=348,y=186)
##
##self.in5 = Label(self,image = ligado)
##self.in5.configure(background = "black")
##self.in5.place(x=348,y=200)
##
##self.in4 = Label(self,image = ligado)
##self.in4.configure(background = "black")
##self.in4.place(x=348,y=214)
##
##self.in3 = Label(self,image = ligado)
##self.in3.configure(background = "black")
##self.in3.place(x=348,y=228)
##
##self.in2 = Label(self,image = ligado)
##self.in2.configure(background = "black")
##self.in2.place(x=348,y=242)
##
##self.in1 = Label(self,image = ligado)
##self.in1.configure(background = "black")
##self.in1.place(x=348,y=256)


    
##    D = Label(self,image = ligado)
##    D.configure(background = "black")
##    D.place(x=198,y=250)
##
##    C = Label(self,image = ligado)
##    C.configure(background = "black")
##    C.place(x=169,y=250)
##
##    B = Label(self,image = ligado)
##    B.configure(background = "black")
##    B.place(x=140,y=250)
##
##    A = Label(self,image = ligado)
##    A.configure(background = "black")
##    A.place(x=111,y=250)

    
   
    

        
        
##        out1 = Label(self,image = ligado)
##        out1.configure(background = "black")
##        out1.place(x=48,y=95)
##        
##        out2 = Label(self,image = ligado)
##        out2.configure(background = "black")
##        out2.place(x=79,y=95)
##
##        out3 = Label(self,image = ligado)
##        out3.configure(background = "black")
##        out3.place(x=111,y=95)
##
##        out4 = Label(self,image = ligado)
##        out4.configure(background = "black")
##        out4.place(x=143,y=95)
##
##        out5 = Label(self,image = ligado)
##        out5.configure(background = "black")
##        out5.place(x=174,y=95)
##
##        out6 = Label(self,image = ligado)
##        out6.configure(background = "black")
##        out6.place(x=206,y=95)
##
##        out7 = Label(self,image = ligado)
##        out7.configure(background = "black")
##        out7.place(x=238,y=95)
##
##        out8 = Label(self,image = ligado)
##        out8.configure(background = "black")
##        out8.place(x=270,y=95)
##
##        out9 = Label(self,image = ligado)
##        out9.configure(background = "black")
##        out9.place(x=348,y=23)
##        
##        out10 = Label(self,image = ligado)
##        out10.configure(background = "black")
##        out10.place(x=348,y=37)
##        
##        out11 = Label(self,image = ligado)
##        out11.configure(background = "black")
##        out11.place(x=348,y=51)
##        
##        out12 = Label(self,image = ligado)
##        out12.configure(background = "black")
##        out12.place(x=348,y=65)
##        
##        out13 = Label(self,image = ligado)
##        out13.configure(background = "black")
##        out13.place(x=348,y=79)
##
##        out14 = Label(self,image = ligado)
##        out14.configure(background = "black")
##        out14.place(x=348,y=93)
##
##        out15 = Label(self,image = ligado)
##        out15.configure(background = "black")
##        out15.place(x=348,y=107)
##
##        out16 = Label(self,image = ligado)
##        out16.configure(background = "black")
##        out16.place(x=348,y=121)
##
##        in8 = Label(self,image = ligado)
##        in8.configure(background = "black")
##        in8.place(x=348,y=158)
##
##        in7 = Label(self,image = ligado)
##        in7.configure(background = "black")
##        in7.place(x=348,y=172)
##
##        in6 = Label(self,image = ligado)
##        in6.configure(background = "black")
##        in6.place(x=348,y=186)
##
##        in5 = Label(self,image = ligado)
##        in5.configure(background = "black")
##        in5.place(x=348,y=200)
##
##        in4 = Label(self,image = ligado)
##        in4.configure(background = "black")
##        in4.place(x=348,y=214)
##
##        in3 = Label(self,image = ligado)
##        in3.configure(background = "black")
##        in3.place(x=348,y=228)
##
##        in2 = Label(self,image = ligado)
##        in2.configure(background = "black")
##        in2.place(x=348,y=242)
##
##        in1 = Label(self,image = ligado)
##        in1.configure(background = "black")
##        in1.place(x=348,y=256)

        
