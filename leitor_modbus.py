#!/home/pi/CMM/bin/python3
# -*- coding:utf-8 -*-

# Leitor de entradas do Modulo expansorda BRAVAS Technololgy
# Desenvolvido por Leandro Leal  rev. 23/07/2019

import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import wiringpi # Biblioteca para usar as GPIO da rasp como saidas ou entradas
import sys
import serial # Para comunicação serial
import binascii
import libscrc
import _thread as thread

mutex = thread.allocate_lock() # Trava a thread para que seja executada sozina

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(11,GPIO.OUT)  # Sinal De buzzer

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

class monta_pacote():

    def __init__(self):

        self = self
        self.ser = serial.Serial("/dev/ttyS0", 115200)
        
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
            
##            print("a",a)

            b1 = bin2str[-4]
            b2 = bin2str[-3]
            if b1 == "x":
                b1 = "0"
            b = p + b1 + b2
            
##            print("b",b)
            
            return(a,b) 
               
        packet = bytearray()  
        packet.append(modulo) # Endreço do modulo 
        packet.append(0x02) # Modo leitura
        packet.append(0x00) # 
        packet.append(0x00) # Endereço registrador inicial
        packet.append(0x00) # 
        packet.append(0x04) # Registradores a serem lidos

##        print("pacote montado sem o crc",packet)
       
        crc = crc16(packet)

        a = int(crc[0],16)
        b = int(crc[1],16)

##        print("a",hex(a))
##        print("b",hex(b))
            
        packet.append(a) # Controle de redundancia
        packet.append(b) # Controle de redundancia
        
        try:
            
            mutex.acquire() # Trava para acesso exclusivo

            time.sleep(0.15)
                    
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

            mutex.release() # Desbloqueia trava de acesso

        except:

            print("\nErro na leitura da serial\n")
            return("0")

        

        in_bin = str(in_bin)

        return(in_bin)

##        packet_editado = str(packet)
##        packet_editado = packet_editado.replace("bytearray(","")
##        packet_editado = packet_editado.replace(")","")
##        in_bin_editado = str (in_bin)
##
##        cont = 5 # numero de vezes que tenta reenviar
##
##        if in_bin_editado != "b''":
##
####            print(in_bin_editado)
####            print("recebeu retorno do modulo")
##            
##            return(in_bin)
##
##        if in_bin_editado == "b''":            
##
##            while cont > 0:                
##
####                print("Lendo novamente")                
##
##                GPIO.output(17, 1)  
##                GPIO.output(18, 1)
##                
##                time.sleep(0.1)
##                
##                self.ser.write(packet)
##                
##                time.sleep(0.002)
##                
##                GPIO.output(17, 0)  
##                GPIO.output(18, 0)
##
##                time.sleep(0.02)  
##                bytesToRead = self.ser.inWaiting()  
##                in_bin = self.ser.read(bytesToRead)
##
##                packet_editado = str(packet)
##                packet_editado = packet_editado.replace("bytearray(","")
##                packet_editado = packet_editado.replace(")","")
##                in_bin_editado = str (in_bin)
##
##                if in_bin_editado != "b''":            
##
####                    print("Agora recebeu algo do modulo")
##                    return(in_bin)
##                    
##
##                else:
##
####                    print("Opa")
##                    cont = cont -1


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
            pass

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

                #print("erro fitro mdl1")
                pass


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

                #print("erro fitro mdl2")
                pass

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
            
            #print("erro fitro mdl3")
            pass

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

            pass
            
            #print("erro fitro mdl4")
        


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

            pass
            
            #print("erro fitro mdl5")

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

            pass
            
            #print("erro fitro mdl6")

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

                #print("erro fitro mdl7")
                pass

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

                #print("erro fitro mdl9")
                pass

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

                #print("erro fitro mdl9")
                pass

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

                #print("erro fitro mdl10")
                pass

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

                #print("erro fitro mdl11")
                pass

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

                #print("erro fitro mdl12")
                pass

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

                pass
##                print("erro fitro mdl13")

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

                #print("erro fitro mdl14")
                pass

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

                #print("erro fitro mdl15")
                pass

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

                #print("erro fitro mdl16")
                pass


    
class Leitor(monta_pacote,retorna,filtro):

    def __init__(self):
        
        self.ser = serial.Serial("/dev/ttyS0", 115200) # 9600 38400 115200 Configura a serial e a velocidade de transmissao
        self.mod = monta_pacote()
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

            ##    
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
