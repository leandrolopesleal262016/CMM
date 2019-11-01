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
import binascii
import _thread as thread

mutex = thread.allocate_lock() # Trava a thread para que seja executada sozina

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT) # HIGH para enviar LOW para ler dados
GPIO.setup(18,GPIO.OUT) # HIGH para enviar LOW para ler dados


def log(texto): # Metodo para registro dos eventos no log.txt (exibido na interface grafica)

    hs = time.strftime("%H:%M:%S") 
    data = time.strftime('%d/%m/%y')

    texto = str(texto)

    if texto == "*":

        l = open("/var/www/html/log/log.txt","a")
        l.write("\n")
        l.close()

    else:        

        texto = texto.replace("'","")
        texto = texto.replace(",","")
        texto = texto.replace("(","")
        texto = texto.replace(")","")

        escrita = ("{} - {}  Evento:  {}\n").format(data, hs, texto)
        escrita = str(escrita)

        l = open("/var/www/html/log/log.txt","a")
        l.write(escrita)
        l.close()

def escreve_serial(packet):

    ser = serial.Serial("/dev/ttyS0", 115200)

    try: 

        time.sleep(0.005)
                
        GPIO.output(17, 1)  
        GPIO.output(18, 1)
        
        time.sleep(0.01)
        
        ser.write(packet)
        
        time.sleep(0.002)
        
        GPIO.output(17, 0)  
        GPIO.output(18, 0)

        time.sleep(0.01)
        
        bytesToRead = ser.inWaiting()        
        in_bin = ser.read(bytesToRead)

        verifica = str(in_bin)
                
        return in_bin

    except:        
        
        return ("b''")

class monta_pacote_in():

    def __init__(self):

        self = self
        
    def ler(self,modulo): # passar dados como string

        modulo = int(modulo,16) # Converte para um inteiro de base 16

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
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos

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

                in_bin = escreve_serial(packet)
                in_bin = str(in_bin)
                
                if in_bin != "b''":
                    
                    in_bin = in_bin
                
                    return(in_bin)

                cont = cont - 1
                time.sleep(0.05)
        else:

            return(in_bin)

class retorna:

    def __init__(self):

        self = self

    def entrada(self,b,entrada_requisitada):
            
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

        if entrada_requisitada == 'in1':

            entrada_requisitada = in1
            
        if entrada_requisitada == 'in2':

            entrada_requisitada = in2

        if entrada_requisitada == 'in3':

            entrada_requisitada = in3

        if entrada_requisitada == 'in4':

            entrada_requisitada = in4
       
        return(entrada_requisitada)

class limpa:

    def _init__(self):

        self = self

    def string(self,i):

        try:

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
       
            return(i)

        except:
            
            pass # Erro na classe limpa string

class filtro(limpa):

    def __init__(self):
        
        self.limpa = limpa()

    def mdl1(self,i):
        
        if i != b'':

            i = self.limpa.string(i) 
            
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
                if i == "01H":                    
                    b = "1"
                                             
                return(b)
            
            except:

                pass #log("erro fitro mdl1")
                

    def mdl2(self,i):

        if i != b'':                
            
            i = self.limpa.string(i) 
            
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
                
                return(b)
            
            except:

                pass #log("erro fitro mdl2")                

    def mdl3(self,i):

        if i != "b''":                
            
            i = self.limpa.string(i) 

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
            if i == "01a":
                b = "1"
            if i == "053":
                b = "5"
            if i == "062":
                b = "6"
            if i == "t6":
                b = "9"
            if i == "n7":
                b = "a"
            if i == "ra":
                b = "d"
                                    
            return(b)
        
        except:
            
            pass #log("erro fitro mdl3")            

    def mdl4(self,i):       

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])               
            b = (i[-1])             
                                
            if i == "05aG": 
                b = "5"
            if i == "06F": 
                b = "6"
            if i == "taB": 
                b = "9"
            if i == "nC": 
                b = "a"
            if i == "r": 
                b = "d"
            
                                    
            return(b)
        
        except:            
            
            pass #log("erro fitro mdl4")
            

    def mdl5(self,i):       

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])               
            b = (i[-1])            
                                
            if i == "01a": 
                b = "1"
            if i == "02y": 
                b = "2"
            if i == "t": 
                b = "9"
            if i == "n": 
                b = "a"
            if i == "ra}": 
                b = "d"
            if i == "0e|": 
                b = "e"                        
                                    
            return(b)
        
        except:            
            
            pass #log("erro fitro mdl5")

    def mdl6(self,i):       

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])               
            b = (i[-1])
                                
            if i == "01a<": 
                b = "1"
            if i == "02=": 
                b = "2"
            if i == "t": 
                b = "9"
            if i == "n": 
                b = "a"
            if i == "ra9": 
                b = "d"
            if i == "0e8": 
                b = "e"                        
                                    
            return(b)
        
        except:

            pass #log("erro fitro mdl6")

    def mdl7(self,i):

        if i != "b''":
                    
            i = self.limpa.string(i)

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                
                if i == "05a": 
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
               
                return (b)                            

            except:

                pass #log("erro fitro mdl7")

                
    def mdl8(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])               

                if i == "01c":
                    b = "1"
                if i == "02#":
                    b = "2"                
                if i == "05b": 
                    b = "5"            
                if i == "tb":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "rc":
                    b = "d"
                if i == "0e#":
                    b = "e"
               
                return (b)                            

            except:

                pass #log("erro fitro mdl9")
                

    def mdl9(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01b(":
                    b = "1"
                if i == "02)\\":
                    b = "2"                
                if i == "05c": 
                    b = "5"
                if i == "06#": 
                    b = "6"
                if i == "tc":
                    b = "9"
                if i == "n#":
                    b = "a"
                if i == "rb-":
                    b = "d"
                              
                return (b)                            

            except:

                pass #log("erro fitro mdl9")
                

    def mdl10(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01b(":
                    b = "1"
                if i == "02)\\":
                    b = "2"                
                if i == "05c": 
                    b = "5"
                if i == "06#": 
                    b = "6"
                if i == "tc":
                    b = "9"
                if i == "n#":
                    b = "a"
                if i == "rb-":
                    b = "d"
                              
                return (b)                            

            except:

                pass #log("erro fitro mdl10")
                

    def mdl11(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                if i == "01c":
                    b = "1"                    
                if i == "02#":                    
                    b = "2"                    
                if i == "05bS": 
                    b = "5"                    
                if i == "06R\\": 
                    b = "6"                    
                if i == "tbV":
                    b = "9"                    
                if i == "nW\\":
                    b = "a"                    
                if i == "rc":
                    b = "d"                    
                if i == "0e#":
                    b = "e"
                              
                return (b)                            

            except:

                pass #log("erro fitro mdl11")
                

    def mdl12(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                

                if i == "01b":
                    b = "1"      
                if i == "05c\\": 
                    b = "5"                    
                if i == "06#&": 
                    b = "6"                    
                if i == "tc\\":
                    b = "9"                    
                if i == "n##":
                    b = "a"                    
                if i == "rb":
                    b = "d"                    
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl12")
                

    def mdl13(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                if i == "01c":
                    b = "1"
                if i == "02#":
                    b = "2" 
                if i == "05b": 
                    b = "5"      
                if i == "tb":
                    b = "9"                    
                if i == "n":
                    b = "a"                    
                if i == "rc":
                    b = "d"
                if i == "0e#":
                    b = "e"                
                                              
                return (b)                            

            except:
                
                pass #log("erro fitro mdl13")

    def mdl14(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01c":
                    b = "1"
                if i == "02#":
                    b = "2"
                if i == "04":                    
                    b = "4" 
                if i == "05b": 
                    b = "5"
                if i == "06":
                    b = "6"
                if i == "07":
                    b = "7"
                if i == "06":
                    b = "6" 
                if i == "tb":
                    b = "9"                    
                if i == "n":
                    b = "a"
                if i == "0b":
                    b = "b"
                if i == "0c":
                    b = "c" 
                if i == "rcY":
                    b = "d"
                if i == "0e#X":
                    b = "e"                
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl14")
                

    def mdl15(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])
                
                if i == "01b":
                    b = "1"               
                if i == "05cc": 
                    b = "5"
                if i == "06#b": 
                    b = "6"
                if i == "tcf":
                    b = "9"                    
                if i == "n#g":
                    b = "a"                    
                if i == "rb":
                    b = "d" 
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl15")
                

    def mdl16(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01et":
                    b = "1"               
                if i == "02%u": 
                    b = "2"
                if i == "05d": 
                    b = "5"
                if i == "06$":
                    b = "6"                    
                if i == "td":
                    b = "9"                    
                if i == "n$":
                    b = "a"
                if i == "req":
                    b = "d"                    
                if i == "0e%p":
                    b = "e"
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl16")
                
    
class Leitor(monta_pacote_in,retorna,filtro):

    def __init__(self):
        
        self.mod = monta_pacote_in()
        self.retorna = retorna()
        self.filtro = filtro()
           
# Leitor mdulo expansor 1

    def leitor1_in1(self):

        i = self.mod.ler('0x01') # modulo, entrada
        b = self.filtro.mdl1(i)       
        in1 = self.retorna.entrada(b,'in1')

        return(in1)
    
    def leitor1_in2(self):

        i = self.mod.ler('0x01')        
        b = self.filtro.mdl1(i)
        in2 = self.retorna.entrada(b,'in2')     

        return(in2)
          
    def leitor1_in3(self):
    
        i = self.mod.ler('0x01')      
        b = self.filtro.mdl1(i)
        in3 = self.retorna.entrada(b,'in3')

        return(in3)    
            
    def leitor1_in4(self):
    
        i = self.mod.ler('0x01') 
        b = self.filtro.mdl1(i) 
        in4 = self.retorna.entrada(b,'in4')

        return(in4)
    
# Leitor mdulo expansor 2

    def leitor2_in1(self):

        i = self.mod.ler('0x02') # modulo
        b = self.filtro.mdl2(i) # Limpa e edita os dados recebidos da leitura (i)
        in1 = self.retorna.entrada(b,'in1') 

        return(in1)            
           
    def leitor2_in2(self):

        i = self.mod.ler('0x02')
        b = self.filtro.mdl2(i)        
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
           
    def leitor2_in3(self):
    
        i = self.mod.ler('0x02')   
        b = self.filtro.mdl2(i) 
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor2_in4(self):
    
        i = self.mod.ler('0x02')  
        b = self.filtro.mdl2(i) 
        in4 = self.retorna.entrada(b,'in4') 

        return(in4)
    
# Leitor mdulo expansor 3

    def leitor3_in1(self):

        i = self.mod.ler('0x03') # modulo, entrada
        b = self.filtro.mdl3(i) # Limpa e edita os dados recebidos da leitura (i)
        in1 = self.retorna.entrada(b,'in1') # Confere em uma tabela binaria qual o valor da entrada requisitada 'in1'
        
        return(in1)
    
    def leitor3_in2(self):

        i = self.mod.ler('0x03') 
        b = self.filtro.mdl3(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor3_in3(self):
    
        i = self.mod.ler('0x03') 
        b = self.filtro.mdl3(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor3_in4(self):
    
        i = self.mod.ler('0x03') 
        b = self.filtro.mdl3(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 4
                      
    def leitor4_in1(self):        

        i = self.mod.ler('0x04') # modulo, entrada        
        b = self.filtro.mdl4(i)
        in1 = self.retorna.entrada(b,'in1')

        return (in1)                            
   
    def leitor4_in2(self):

        i = self.mod.ler('0x04') 
        b = self.filtro.mdl4(i)
        in2 = self.retorna.entrada(b,'in2')                

        return(in2)
            
    def leitor4_in3(self):

        i = self.mod.ler('0x04')
        b = self.filtro.mdl4(i)                    
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)
           
    def leitor4_in4(self):
    
        i = self.mod.ler('0x04') 
        b = self.filtro.mdl4(i)
        in4 = self.retorna.entrada(b,'in4') 

        return(in4)

# Leitor mdulo expansor 5
                      
    def leitor5_in1(self):        

        i = self.mod.ler('0x05') # modulo, entrada        
        b = self.filtro.mdl5(i)
        in1 = self.retorna.entrada(b,'in1')

        return (in1)
               
    def leitor5_in2(self):

        i = self.mod.ler('0x05') 
        b = self.filtro.mdl5(i)
        in2 = self.retorna.entrada(b,'in2')                

        return(in2)
            
    def leitor5_in3(self):

        i = self.mod.ler('0x05') 
        b = self.filtro.mdl5(i)                    
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)
           
    def leitor5_in4(self):
    
        i = self.mod.ler('0x05') 
        b = self.filtro.mdl5(i)
        in4 = self.retorna.entrada(b,'in4') 

        return(in4)

# Leitor mdulo expansor 6
                      
    def leitor6_in1(self):        

        i = self.mod.ler('0x06') # modulo, entrada        
        b = self.filtro.mdl6(i)
        in1 = self.retorna.entrada(b,'in1')

        return (in1)
               
    def leitor6_in2(self):

        i = self.mod.ler('0x06') 
        b = self.filtro.mdl6(i)
        in2 = self.retorna.entrada(b,'in2')                

        return(in2)
            
    def leitor6_in3(self):

        i = self.mod.ler('0x06') 
        b = self.filtro.mdl6(i)                    
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)
           
    def leitor6_in4(self):
    
        i = self.mod.ler('0x06') 
        b = self.filtro.mdl6(i)
        in4 = self.retorna.entrada(b,'in4') 

        return(in4)
    
# Leitor mdulo expansor 7

    def leitor7_in1(self):

        i = self.mod.ler('0x07')       
        b = self.filtro.mdl7(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor7_in2(self):

        i = self.mod.ler('0x07') 
        b = self.filtro.mdl7(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor7_in3(self):
    
        i = self.mod.ler('0x07') 
        b = self.filtro.mdl7(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor7_in4(self):
    
        i = self.mod.ler('0x07') 
        b = self.filtro.mdl7(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)
              
# Leitor mdulo expansor 8

    def leitor8_in1(self):

        i = self.mod.ler('0x08')       
        b = self.filtro.mdl8(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor8_in2(self):

        i = self.mod.ler('0x08') 
        b = self.filtro.mdl8(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor8_in3(self):
    
        i = self.mod.ler('0x08') 
        b = self.filtro.mdl8(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor8_in4(self):
    
        i = self.mod.ler('0x08') 
        b = self.filtro.mdl8(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 9

    def leitor9_in1(self):

        i = self.mod.ler('0x09')       
        b = self.filtro.mdl9(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor9_in2(self):

        i = self.mod.ler('0x09') 
        b = self.filtro.mdl9(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor9_in3(self):
    
        i = self.mod.ler('0x09') 
        b = self.filtro.mdl9(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor9_in4(self):
    
        i = self.mod.ler('0x09') 
        b = self.filtro.mdl9(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 10

    def leitor10_in1(self):

        i = self.mod.ler('0x0a')       
        b = self.filtro.mdl10(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor10_in2(self):

        i = self.mod.ler('0x0a') 
        b = self.filtro.mdl10(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor10_in3(self):
    
        i = self.mod.ler('0x0a') 
        b = self.filtro.mdl10(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor10_in4(self):
    
        i = self.mod.ler('0x0b') 
        b = self.filtro.mdl11(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 11

    def leitor11_in1(self):

        i = self.mod.ler('0x0b')        
        b = self.filtro.mdl11(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor11_in2(self):

        i = self.mod.ler('0x0b') 
        b = self.filtro.mdl11(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor11_in3(self):
    
        i = self.mod.ler('0x0b') 
        b = self.filtro.mdl11(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor11_in4(self):
    
        i = self.mod.ler('0x0b') 
        b = self.filtro.mdl11(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 12

    def leitor12_in1(self):

        i = self.mod.ler('0x0c')        
        b = self.filtro.mdl12(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor12_in2(self):

        i = self.mod.ler('0x0c') 
        b = self.filtro.mdl12(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor12_in3(self):
    
        i = self.mod.ler('0x0c') 
        b = self.filtro.mdl12(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor12_in4(self):
    
        i = self.mod.ler('0x0c') 
        b = self.filtro.mdl12(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 13

    def leitor13_in1(self):

        i = self.mod.ler('0x0d')       
        b = self.filtro.mdl13(i) 
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor13_in2(self):

        i = self.mod.ler('0x0d') 
        b = self.filtro.mdl13(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor13_in3(self):
    
        i = self.mod.ler('0x0d') 
        b = self.filtro.mdl13(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor13_in4(self):
    
        i = self.mod.ler('0x0d') 
        b = self.filtro.mdl13(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)
    
# Leitor mdulo expansor 14

    def leitor14_in1(self):

        i = self.mod.ler('0x0e')        
        b = self.filtro.mdl14(i)        
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor14_in2(self):

        i = self.mod.ler('0x0e') 
        b = self.filtro.mdl14(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor14_in3(self):
    
        i = self.mod.ler('0x0e') 
        b = self.filtro.mdl14(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor14_in4(self):
    
        i = self.mod.ler('0x0e') 
        b = self.filtro.mdl14(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)
    
# Leitor mdulo expansor 15

    def leitor15_in1(self):

        i = self.mod.ler('0x0f')        
        b = self.filtro.mdl15(i)        
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor15_in2(self):

        i = self.mod.ler('0x0f') 
        b = self.filtro.mdl15(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor15_in3(self):
    
        i = self.mod.ler('0x0f') 
        b = self.filtro.mdl15(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor15_in4(self):
    
        i = self.mod.ler('0x0f') 
        b = self.filtro.mdl15(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

# Leitor mdulo expansor 16

    def leitor16_in1(self):

        i = self.mod.ler('0x10')        
        b = self.filtro.mdl16(i)        
        in1 = self.retorna.entrada(b,'in1') 
        
        return(in1)
    
    def leitor16_in2(self):

        i = self.mod.ler('0x10') 
        b = self.filtro.mdl16(i)
        in2 = self.retorna.entrada(b,'in2')
        
        return(in2)            
         
    def leitor16_in3(self):
    
        i = self.mod.ler('0x10') 
        b = self.filtro.mdl16(i)
        in3 = self.retorna.entrada(b,'in3') 

        return(in3)            
            
    def leitor16_in4(self):
    
        i = self.mod.ler('0x10') 
        b = self.filtro.mdl16(i)
        in4 = self.retorna.entrada(b,'in4')
        
        return(in4)

#############################################  Acionamento reles Expansores  ##############################

class monta_pacote():

    def __init__(self):

        self = self
        
    def aciona(self,modulo,rele,funcao): # passar dados como string '0x01','0x01','0xFF'

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

        if in_bin == "b''": # reenviando acionamento rele
            
            cont = 5

            while cont > 0:  # rotina de reenvio acionamento

                in_bin = escreve_serial(packet)

                if in_bin == "b''":

                    time.sleep(0.1)
                    cont = cont - 1

                else:

                    return(in_bin)      

        return(in_bin)
        

class Expansor(monta_pacote):

    def __init__(self):

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
