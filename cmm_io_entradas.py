# Classe para lconfiguração de entradas e saidas do CMM
# Atualizado 19/07/2019

import time
import wiringpi
import RPi.GPIO as GPIO
from banco import Banco

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

def log(texto): # Metodo para registro dos eventos no log.txt (exibido na interface grafica)

    hs = time.strftime("%H:%M:%S") 
    data = time.strftime('%d/%m/%y')

    texto = str(texto)

    texto = texto.replace("'","")
    texto = texto.replace(",","")
    texto = texto.replace("(","")
    texto = texto.replace(")","")

    if texto == "*":

        l = open("/var/www/html/log/log.txt","a")
        l.write("\n")
        l.close()

    else:
    

        escrita = ("{} - {}  Evento:  {}\n").format(data, hs, texto)
        escrita = str(escrita)

        l = open("/var/www/html/log/log.txt","a")
        l.write(escrita)
        l.close()

banco = Banco()  # NOME DAS ENTRADAS

IN1 = banco.consulta("entradas","in1")
IN2 = banco.consulta("entradas","in2")
IN3 = banco.consulta("entradas","in3")
IN4 = banco.consulta("entradas","in4")
IN5 = banco.consulta("entradas","in5")
IN6 = banco.consulta("entradas","in6")
IN7 = banco.consulta("entradas","in7")
IN8 = banco.consulta("entradas","in8")
INA = banco.consulta("entradas","a")
INB = banco.consulta("entradas","b")
INC = banco.consulta("entradas","c")
IND = banco.consulta("entradas","d")

exp1 = banco.consulta("entradas","exp1")
exp2 = banco.consulta("entradas","exp2")
exp3 = banco.consulta("entradas","exp3")
exp4 = banco.consulta("entradas","exp4")
exp5 = banco.consulta("entradas","exp5")
exp6 = banco.consulta("entradas","exp6")
exp7 = banco.consulta("entradas","exp7")
exp8 = banco.consulta("entradas","exp8")
exp9 = banco.consulta("entradas","exp9")
exp10 = banco.consulta("entradas","exp10")
exp11 = banco.consulta("entradas","exp11")
exp12 = banco.consulta("entradas","exp12")
exp13 = banco.consulta("entradas","exp13")
exp14 = banco.consulta("entradas","exp14")
exp15 = banco.consulta("entradas","exp15")
exp16 = banco.consulta("entradas","exp16")


_pm1 = "Nao definido"
_pm2 = "Nao definido"
_pm3 = "Nao definido"
_pm_quadro = "Nao definido"
_ctw1 = "Nao definido"
_ctw2 = "Nao definido"
_ctw3 = "Nao definido"
_qbv1 = "Nao definido"
_qbv2 = "Nao definido"
_qde = "Nao definido"
_mudanca_sociais = "Nao definido"
_pmg = "Nao definido"
_barreira = "Nao definido"
_abre_garagem = "Nao definido"
_mudanca_garagem = "Nao definido"


if IN1 == "pm_social_externo":           
    _pm1 = "IN1"    
if IN1 == "pm_social_interno":            
    _pm2 = "IN1"
if IN1 == "pm_social_acesso":          
    _pm3 = "IN1"
if IN1 == "pm_quadro_comando":          
    _pm_quadro = "IN1"    
if IN1 == "abre_social_externo":
    _ctw1 = "IN1"
if IN1 == "abre_social_interno":
    _ctw2 = "IN1"
if IN1 == "abre_social_acesso":
    _ctw3 = "IN1"
if IN1 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN1"
if IN1 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN1"
if IN1 == "queda_energia_eletrica":
    _qde = "IN1"
if IN1 == "mudanca_sociais":
    _mudanca_sociais = "IN1"
if IN1 == "pmg":          
    _pmg = "IN1"
if IN1 == "barreira":          
    _barreira = "IN1"
if IN1 == "abre_garagem":          
    _abre_garagem = "IN1"
if IN1 == "mudanca_garagem":          
    _mudanca_garagem = "IN1"

######################################

if IN2 == "pm_social_externo":           
    _pm1 = "IN2"    
if IN2 == "pm_social_interno":            
    _pm2 = "IN2"
if IN2 == "pm_social_acesso":          
    _pm3 = "IN2"
if IN2 == "pm_quadro_comando":          
    _pm_quadro = "IN2"    
if IN2 == "abre_social_externo":
    _ctw1 = "IN2"
if IN2 == "abre_social_interno":
    _ctw2 = "IN2"
if IN2 == "abre_social_acesso":
    _ctw3 = "IN2"
if IN2 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN2"
if IN2 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN2"
if IN2 == "queda_energia_eletrica":
    _qde = "IN2"
if IN2 == "mudanca_sociais":
    _mudanca_sociais = "IN2"
if IN2 == "pmg":          
    _pmg = "IN2"
if IN2 == "barreira":          
    _barreira = "IN2"
if IN2 == "abre_garagem":          
    _abre_garagem = "IN2"
if IN2 == "mudanca_garagem":          
    _mudanca_garagem = "IN2"

######################################

if IN3 == "pm_social_externo":           
    _pm1 = "IN3"    
if IN3 == "pm_social_interno":            
    _pm2 = "IN3"
if IN3 == "pm_social_acesso":          
    _pm3 = "IN3"
if IN3 == "pm_quadro_comando":          
    _pm_quadro = "IN3"    
if IN3 == "abre_social_externo":
    _ctw1 = "IN3"
if IN3 == "abre_social_interno":
    _ctw2 = "IN3"
if IN3 == "abre_social_acesso":
    _ctw3 = "IN3"
if IN3 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN3"
if IN3 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN3"
if IN3 == "queda_energia_eletrica":
    _qde = "IN3"
if IN3 == "mudanca_sociais":
    _mudanca_sociais = "IN3"
if IN3 == "pmg":          
    _pmg = "IN3"
if IN3 == "barreira":          
    _barreira = "IN3"
if IN3 == "abre_garagem":          
    _abre_garagem = "IN3"
if IN3 == "mudanca_garagem":          
    _mudanca_garagem = "IN3"

######################################

if IN4 == "pm_social_externo":           
    _pm1 = "IN4"    
if IN4 == "pm_social_interno":            
    _pm2 = "IN4"
if IN4 == "pm_social_acesso":          
    _pm3 = "IN4"
if IN4 == "pm_quadro_comando":          
    _pm_quadro = "IN4"    
if IN4 == "abre_social_externo":
    _ctw1 = "IN4"
if IN4 == "abre_social_interno":
    _ctw2 = "IN4"
if IN4 == "abre_social_acesso":
    _ctw3 = "IN4"
if IN4 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN4"
if IN4 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN4"
if IN4 == "queda_energia_eletrica":
    _qde = "IN4"
if IN4 == "mudanca_sociais":
    _mudanca_sociais = "IN4"
if IN4 == "pmg":          
    _pmg = "IN4"
if IN4 == "barreira":          
    _barreira = "IN4"
if IN4 == "abre_garagem":          
    _abre_garagem = "IN4"
if IN4 == "mudanca_garagem":          
    _mudanca_garagem = "IN4"

######################################

if IN5 == "pm_social_externo":           
    _pm1 = "IN5"    
if IN5 == "pm_social_interno":            
    _pm2 = "IN5"
if IN5 == "pm_social_acesso":          
    _pm3 = "IN5"
if IN5 == "pm_quadro_comando":    
    _pm_quadro = "IN5"    
if IN5 == "abre_social_externo":   
    _ctw1 = "IN5"
if IN5 == "abre_social_interno":
    _ctw2 = "IN5"
if IN5 == "abre_social_acesso":
    _ctw3 = "IN5"
if IN5 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN5"
if IN5 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN5"
if IN5 == "queda_energia_eletrica":
    _qde = "IN5"
if IN5 == "mudanca_sociais":
    _mudanca_sociais = "IN5"
if IN5 == "pmg":          
    _pmg = "IN5"
if IN5 == "barreira":          
    _barreira = "IN5"
if IN5 == "abre_garagem":          
    _abre_garagem = "IN5"
if IN5 == "mudanca_garagem":          
    _mudanca_garagem = "IN5"

######################################

if IN6 == "pm_social_externo":           
    _pm1 = "IN6"    
if IN6 == "pm_social_interno":            
    _pm2 = "IN6"
if IN6 == "pm_social_acesso":          
    _pm3 = "IN6"
if IN6 == "pm_quadro_comando":          
    _pm_quadro = "IN6"    
if IN6 == "abre_social_externo":
    _ctw1 = "IN6"
if IN6 == "abre_social_interno":
    _ctw2 = "IN6"
if IN6 == "abre_social_acesso":
    _ctw3 = "IN6"
if IN6 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN6"
if IN6 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN6"
if IN6 == "queda_energia_eletrica":
    _qde = "IN6"
if IN6 == "mudanca_sociais":
    _mudanca_sociais = "IN6"
if IN6 == "pmg":          
    _pmg = "IN6"
if IN6 == "barreira":          
    _barreira = "IN6"
if IN6 == "abre_garagem":          
    _abre_garagem = "IN6"
if IN6 == "mudanca_garagem":          
    _mudanca_garagem = "IN6"

######################################

if IN7 == "pm_social_externo":           
    _pm1 = "IN7"    
if IN7 == "pm_social_interno":            
    _pm2 = "IN7"
if IN7 == "pm_social_acesso":          
    _pm3 = "IN7"
if IN7 == "pm_quadro_comando":          
    _pm_quadro = "IN7"    
if IN7 == "abre_social_externo":
    _ctw1 = "IN7"
if IN7 == "abre_social_interno":
    _ctw2 = "IN7"
if IN7 == "abre_social_acesso":
    _ctw3 = "IN7"
if IN7 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN7"
if IN7 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN7"
if IN7 == "queda_energia_eletrica":
    _qde = "IN7"
if IN7 == "mudanca_sociais":
    _mudanca_sociais = "IN7"
if IN7 == "pmg":          
    _pmg = "IN7"
if IN7 == "barreira":          
    _barreira = "IN7"
if IN7 == "abre_garagem":          
    _abre_garagem = "IN7"
if IN7 == "mudanca_garagem":          
    _mudanca_garagem = "IN7"

######################################

if IN8 == "pm_social_externo":           
    _pm1 = "IN8"    
if IN8 == "pm_social_interno":            
    _pm2 = "IN8"
if IN8 == "pm_social_acesso":          
    _pm3 = "IN8"
if IN8 == "pm_quadro_comando":          
    _pm_quadro = "IN8"    
if IN8 == "abre_social_externo":
    _ctw1 = "IN8"
if IN8 == "abre_social_interno":
    _ctw2 = "IN8"
if IN8 == "abre_social_acesso":
    _ctw3 = "IN8"
if IN8 == "quebra_vidro_interno_eclusa":
    _qbv1 = "IN8"
if IN8 == "quebra_vidro_dentro_predio":
    _qbv2 = "IN8"
if IN8 == "queda_energia_eletrica":
    _qde = "IN8"
if IN8 == "mudanca_sociais":
    _mudanca_sociais = "IN8"
if IN8 == "pmg":          
    _pmg = "IN8"
if IN8 == "barreira":          
    _barreira = "IN8"
if IN8 == "abre_garagem":          
    _abre_garagem = "IN8"
if IN8 == "mudanca_garagem":          
    _mudanca_garagem = "IN8"

######################################

if INA == "pm_social_externo":           
    _pm1 = "INA"    
if INA == "pm_social_interno":            
    _pm2 = "INA"
if INA == "pm_social_acesso":          
    _pm3 = "INA"
if INA == "pm_quadro_comando":          
    _pm_quadro = "INA"    
if INA == "abre_social_externo":
    _ctw1 = "INA"
if INA == "abre_social_interno":
    _ctw2 = "INA"
if INA == "abre_social_acesso":
    _ctw3 = "INA"
if INA == "quebra_vidro_interno_eclusa":
    _qbv1 = "INA"
if INA == "quebra_vidro_dentro_predio":
    _qbv2 = "INA"
if INA == "queda_energia_eletrica":
    _qde = "INA"
if INA == "mudanca_sociais":
    _mudanca_sociais = "INA"
if INA == "pmg":          
    _pmg = "INA"
if INA == "barreira":          
    _barreira = "INA"
if INA == "abre_garagem":          
    _abre_garagem = "INA"
if INA == "mudanca_garagem":          
    _mudanca_garagem = "INA"

######################################

if INB == "pm_social_externo":           
    _pm1 = "INB"    
if INB == "pm_social_interno":            
    _pm2 = "INB"
if INB == "pm_social_acesso":          
    _pm3 = "INB"
if INB == "pm_quadro_comando":          
    _pm_quadro = "INB"    
if INB == "abre_social_externo":
    _ctw1 = "INB"
if INB == "abre_social_interno":
    _ctw2 = "INB"
if INB == "abre_social_acesso":
    _ctw3 = "INB"
if INB == "quebra_vidro_interno_eclusa":
    _qbv1 = "INB"
if INB == "quebra_vidro_dentro_predio":
    _qbv2 = "INB"
if INB == "queda_energia_eletrica":
    _qde = "INB"
if INB == "mudanca_sociais":
    _mudanca_sociais = "INB"
if INB == "pmg":          
    _pmg = "INB"
if INB == "barreira":          
    _barreira = "INB"
if INB == "abre_garagem":          
    _abre_garagem = "INB"
if INB == "mudanca_garagem":          
    _mudanca_garagem = "INB"

######################################

if INC == "pm_social_externo":           
    _pm1 = "INC"    
if INC == "pm_social_interno":            
    _pm2 = "INC"
if INC == "pm_social_acesso":          
    _pm3 = "INC"
if INC == "pm_quadro_comando":          
    _pm_quadro = "INC"    
if INC == "abre_social_externo":
    _ctw1 = "INC"
if INC == "abre_social_interno":
    _ctw2 = "INC"
if INC == "abre_social_acesso":
    _ctw3 = "INC"
if INC == "quebra_vidro_interno_eclusa":
    _qbv1 = "INC"
if INC == "quebra_vidro_dentro_predio":
    _qbv2 = "INC"
if INC == "queda_energia_eletrica":
    _qde = "INC"
if INC == "mudanca_sociais":
    _mudanca_sociais = "INC"
if INC == "pmg":          
    _pmg = "INC"
if INC == "barreira":          
    _barreira = "INC"
if INC == "abre_garagem":          
    _abre_garagem = "INC"
if INC == "mudanca_garagem":          
    _mudanca_garagem = "INC"

######################################

if IND == "pm_social_externo":           
    _pm1 = "IND"    
if IND == "pm_social_interno":            
    _pm2 = "IND"
if IND == "pm_social_acesso":          
    _pm3 = "IND"
if IND == "pm_quadro_comando":          
    _pm_quadro = "IND"    
if IND == "abre_social_externo":
    _ctw1 = "IND"
if IND == "abre_social_interno":
    _ctw2 = "IND"
if IND == "abre_social_acesso":
    _ctw3 = "IND"
if IND == "quebra_vidro_interno_eclusa":
    _qbv1 = "IND"
if IND == "quebra_vidro_dentro_predio":
    _qbv2 = "IND"
if IND == "queda_energia_eletrica":
    _qde = "IND"
if IND == "mudanca_sociais":
    _mudanca_sociais = "IND"
if IND == "pmg":          
    _pmg = "IND"
if IND == "barreira":          
    _barreira = "IND"
if IND == "abre_garagem":          
    _abre_garagem = "IND"
if IND == "mudanca_garagem":          
    _mudanca_garagem = "IND"

log("*") # Deixa uma linha em branco no log
log("Configuração das entradas:")
log("*")
txt1 = ("IN1:",IN1)
log(txt1)
txt2 = ("IN2:",IN2)
log(txt2)
txt3 = ("IN3:",IN3)
log(txt3)
txt4 = ("IN4:",IN4)
log(txt4)
txt5 = ("IN5:",IN5)
log(txt5)
txt6 = ("IN6:",IN6)
log(txt6)
txt7 = ("IN7:",IN7)
log(txt7)
txt8 = ("IN8:",IN8)
log(txt8)
txtA = ("INA:",INA)
log(txtA)
txtB = ("INB:",INB)
log(txtB)
txtC = ("INC:",INC)
log(txtC)
txtD = ("IND:",IND)
log(txtD)
log("*") # Deixa uma linha em branco no log
 
    
def pm1():    

    if _pm1 == "IN1":
        status_pm1 = banco.consulta("status","in1")
        return status_pm1
    if _pm1 == "IN2":
        status_pm1 = banco.consulta("status","in2")
        return status_pm1
    if _pm1 == "IN3":
        status_pm1 = banco.consulta("status","in3")
        return status_pm1
    if _pm1 == "IN4":
        status_pm1 = banco.consulta("status","in4")
        return status_pm1
    if _pm1 == "IN5":
        status_pm1 = banco.consulta("status","in5")
        return status_pm1
    if _pm1 == "IN6":
        status_pm1 = banco.consulta("status","in6")
        return status_pm1
    if _pm1 == "IN7":
        status_pm1 = banco.consulta("status","in7")
        return status_pm1
    if _pm1 == "IN8":
        status_pm1 = banco.consulta("status","in8")
        return status_pm1
    if _pm1 == "INA":
        status_pm1 = banco.consulta("status","ina")
        return status_pm1
    if _pm1 == "INB":
        status_pm1 = banco.consulta("status","inb")
        return status_pm1
    if _pm1 == "INC":
        status_pm1 = banco.consulta("status","inc")
        return status_pm1
    if _pm1 == "IND":
        status_pm1 = banco.consulta("status","ind")
        return status_pm1
       
    


def pm2():

    if _pm2 == "IN1":
        status_pm2 = banco.consulta("status","in1")
        return status_pm2
    if _pm2 == "IN2":
        status_pm2 = banco.consulta("status","in2")
        return status_pm2
    if _pm2 == "IN3":
        status_pm2 = banco.consulta("status","in3")
        return status_pm2
    if _pm2 == "IN4":
        status_pm2 = banco.consulta("status","in4")
        return status_pm2
    if _pm2 == "IN5":
        status_pm2 = banco.consulta("status","in5")
        return status_pm2
    if _pm2 == "IN6":
        status_pm2 = banco.consulta("status","in6")
        return status_pm2
    if _pm2 == "IN7":
        status_pm2 = banco.consulta("status","in7")
        return status_pm2
    if _pm2 == "IN8":
        status_pm2 = banco.consulta("status","in8")
        return status_pm2
    if _pm2 == "INA":
        status_pm2 = banco.consulta("status","ina")
        return status_pm2
    if _pm2 == "INB":
        status_pm2 = banco.consulta("status","inb")
        return status_pm2
    if _pm2 == "INC":
        status_pm2 = banco.consulta("status","inc")
        return status_pm2
    if _pm2 == "IND":
        status_pm2 = banco.consulta("status","ind")
        return status_pm2        
      

def pm3():

    if _pm3 == "IN1":
        status_pm3 = banco.consulta("status","in1")
        return status_pm3
    if _pm3 == "IN2":
        status_pm3 = banco.consulta("status","in2")
        return status_pm3
    if _pm3 == "IN3":
        status_pm3 = banco.consulta("status","in3")
        return status_pm3
    if _pm3 == "IN4":
        status_pm3 = banco.consulta("status","in4")
        return status_pm3
    if _pm3 == "IN5":
        status_pm3 = banco.consulta("status","in5")
        return status_pm3
    if _pm3 == "IN6":
        status_pm3 = banco.consulta("status","in6")
        return status_pm3
    if _pm3 == "IN7":
        status_pm3 = banco.consulta("status","in7")
        return status_pm3
    if _pm3 == "IN8":
        status_pm3 = banco.consulta("status","in8")
        return status_pm3
    if _pm3 == "INA":
        status_pm3 = banco.consulta("status","ina")
        return status_pm3
    if _pm3 == "INB":
        status_pm3 = banco.consulta("status","inb")
        return status_pm3
    if _pm3 == "INC":
        status_pm3 = banco.consulta("status","inc")
        return status_pm3
    if _pm3 == "IND":
        status_pm3 = banco.consulta("status","ind")
        return status_pm3        
    

def pm_quadro():

    
    if _pm_quadro == "IN1":
        status_pm_quadro = banco.consulta("status","in1")
        return status_pm_quadro
    if _pm_quadro == "IN2":
        status_pm_quadro = banco.consulta("status","in2")
        return status_pm_quadro
    if _pm_quadro == "IN3":
        status_pm_quadro = banco.consulta("status","in3")
        return status_pm_quadro
    if _pm_quadro == "IN4":
        status_pm_quadro = banco.consulta("status","in4")
        return status_pm_quadro
    if _pm_quadro == "IN5":        
        status_pm_quadro = banco.consulta("status","in5")
        return status_pm_quadro
    if _pm_quadro == "IN6":
        status_pm_quadro = banco.consulta("status","in6")
        return status_pm_quadro
    if _pm_quadro == "IN7":
        status_pm_quadro = banco.consulta("status","in7")
        return status_pm_quadro
    if _pm_quadro == "IN8":        
        status_pm_quadro = banco.consulta("status","in8")
        return status_pm_quadro        
    if _pm_quadro == "INA":
        status_pm_quadro = banco.consulta("status","ina")
        return status_pm_quadro
    if _pm_quadro == "INB":
        status_pm_quadro = banco.consulta("status","inb")
        return status_pm_quadro
    if _pm_quadro == "INC":
        status_pm_quadro = banco.consulta("status","inc")
        return status_pm_quadro
    if _pm_quadro == "IND":
        status_pm_quadro = banco.consulta("status","ind")
        return status_pm_quadro
        
    

def ctw1():


    if _ctw1 == "IN1":
        status_ctw1 = banco.consulta("status","in1")
        return status_ctw1
    if _ctw1 == "IN2":
        status_ctw1 = banco.consulta("status","in2")
        return status_ctw1
    if _ctw1 == "IN3":
        status_ctw1 = banco.consulta("status","in3")
        return status_ctw1
    if _ctw1 == "IN4":
        status_ctw1 = banco.consulta("status","in4")
        return status_ctw1
    if _ctw1 == "IN5":
        status_ctw1 = banco.consulta("status","in5")
        return status_ctw1
    if _ctw1 == "IN6":
        status_ctw1 = banco.consulta("status","in6")
        return status_ctw1
    if _ctw1 == "IN7":
        status_ctw1 = banco.consulta("status","in7")
        return status_ctw1
    if _ctw1 == "IN8":
        status_ctw1 = banco.consulta("status","in8")
        return status_ctw1
    if _ctw1 == "INA":
        status_ctw1 = banco.consulta("status","ina")
        return status_ctw1
    if _ctw1 == "INB":
        status_ctw1 = banco.consulta("status","inb")
        return status_ctw1
    if _ctw1 == "INC":
        status_ctw1 = banco.consulta("status","inc")
        return status_ctw1
    if _ctw1 == "IND":
        status_ctw1 = banco.consulta("status","ind")
        return status_ctw1

def ctw2():


    if _ctw2 == "IN1":
        status_ctw2 = banco.consulta("status","in1")
        return status_ctw2
    if _ctw2 == "IN2":
        status_ctw2 = banco.consulta("status","in2")
        return status_ctw2
    if _ctw2 == "IN3":
        status_ctw2 = banco.consulta("status","in3")
        return status_ctw2
    if _ctw2 == "IN4":
        status_ctw2 = banco.consulta("status","in4")
        return status_ctw2
    if _ctw2 == "IN5":
        status_ctw2 = banco.consulta("status","in5")
        return status_ctw2
    if _ctw2 == "IN6":
        status_ctw2 = banco.consulta("status","in6")
        return status_ctw2
    if _ctw2 == "IN7":
        status_ctw2 = banco.consulta("status","in7")
        return status_ctw2
    if _ctw2 == "IN8":
        status_ctw2 = banco.consulta("status","in8")
        return status_ctw2
    if _ctw2 == "INA":
        status_ctw2 = banco.consulta("status","ina")
        return status_ctw2
    if _ctw2 == "INB":
        status_ctw2 = banco.consulta("status","inb")
        return status_ctw2
    if _ctw2 == "INC":
        status_ctw2 = banco.consulta("status","inc")
        return status_ctw2
    if _ctw2 == "IND":
        status_ctw2 = banco.consulta("status","ind")
        return status_ctw2


def ctw3():


    if _ctw3 == "IN1":
        status_ctw3 = banco.consulta("status","in1")
        return status_ctw3
    if _ctw3 == "IN2":
        status_ctw3 = banco.consulta("status","in2")
        return status_ctw3
    if _ctw3 == "IN3":
        status_ctw3 = banco.consulta("status","in3")
        return status_ctw3
    if _ctw3 == "IN4":
        status_ctw3 = banco.consulta("status","in4")
        return status_ctw3
    if _ctw3 == "IN5":
        status_ctw3 = banco.consulta("status","in5")
        return status_ctw3
    if _ctw3 == "IN6":
        status_ctw3 = banco.consulta("status","in6")
        return status_ctw3
    if _ctw3 == "IN7":
        status_ctw3 = banco.consulta("status","in7")
        return status_ctw3
    if _ctw3 == "IN8":
        status_ctw3 = banco.consulta("status","in8")
        return status_ctw3
    if _ctw3 == "INA":
        status_ctw3 = banco.consulta("status","ina")
        return status_ctw3
    if _ctw3 == "INB":
        status_ctw3 = banco.consulta("status","inb")
        return status_ctw3
    if _ctw3 == "INC":
        status_ctw3 = banco.consulta("status","inc")
        return status_ctw3
    if _ctw3 == "IND":
        status_ctw3 = banco.consulta("status","ind")
        return status_ctw3

def qbv1():


    if _qbv1 == "IN1":
        status_qbv1 = banco.consulta("status","in1")
        return status_qbv1
    if _qbv1 == "IN2":
        status_qbv1 = banco.consulta("status","in2")
        return status_qbv1
    if _qbv1 == "IN3":
        status_qbv1 = banco.consulta("status","in3")
        return status_qbv1
    if _qbv1 == "IN4":
        status_qbv1 = banco.consulta("status","in4")
        return status_qbv1
    if _qbv1 == "IN5":
        status_qbv1 = banco.consulta("status","in5")
        return status_qbv1
    if _qbv1 == "IN6":
        status_qbv1 = banco.consulta("status","in6")
        return status_qbv1
    if _qbv1 == "IN7":
        status_qbv1 = banco.consulta("status","in7")
        return status_qbv1
    if _qbv1 == "IN8":
        status_qbv1 = banco.consulta("status","in8")
        return status_qbv1
    if _qbv1 == "INA":
        status_qbv1 = banco.consulta("status","ina")
        return status_qbv1
    if _qbv1 == "INB":
        status_qbv1 = banco.consulta("status","inb")
        return status_qbv1
    if _qbv1 == "INC":
        status_qbv1 = banco.consulta("status","inc")
        return status_qbv1
    if _qbv1 == "IND":
        status_qbv1 = banco.consulta("status","ind")
        return status_qbv1

def qbv2():


    if _qbv2 == "IN1":
        status_qbv2 = banco.consulta("status","in1")
        return status_qbv2
    if _qbv2 == "IN2":
        status_qbv2 = banco.consulta("status","in2")
        return status_qbv2
    if _qbv2 == "IN3":
        status_qbv2 = banco.consulta("status","in3")
        return status_qbv2
    if _qbv2 == "IN4":
        status_qbv2 = banco.consulta("status","in4")
        return status_qbv2
    if _qbv2 == "IN5":
        status_qbv2 = banco.consulta("status","in5")
        return status_qbv2
    if _qbv2 == "IN6":
        status_qbv2 = banco.consulta("status","in6")
        return status_qbv2
    if _qbv2 == "IN7":
        status_qbv2 = banco.consulta("status","in7")
        return status_qbv2
    if _qbv2 == "IN8":
        status_qbv2 = banco.consulta("status","in8")
        return status_qbv2
    if _qbv2 == "INA":
        status_qbv2 = banco.consulta("status","ina")
        return status_qbv2
    if _qbv2 == "INB":
        status_qbv2 = banco.consulta("status","inb")
        return status_qbv2
    if _qbv2 == "INC":
        status_qbv2 = banco.consulta("status","inc")
        return status_qbv2
    if _qbv2 == "IND":
        status_qbv2 = banco.consulta("status","ind")
        return status_qbv2

def qde():


    if _qde == "IN1":
        status_qde = banco.consulta("status","in1")
        return status_qde
    if _qde == "IN2":
        status_qde = banco.consulta("status","in2")
        return status_qde
    if _qde == "IN3":
        status_qde = banco.consulta("status","in3")
        return status_qde
    if _qde == "IN4":
        status_qde = banco.consulta("status","in4")
        return status_qde
    if _qde == "IN5":
        status_qde = banco.consulta("status","in5")
        return status_qde
    if _qde == "IN6":
        status_qde = banco.consulta("status","in6")
        return status_qde
    if _qde == "IN7":
        status_qde = banco.consulta("status","in7")
        return status_qde
    if _qde == "IN8":
        status_qde = banco.consulta("status","in8")
        return status_qde
    if _qde == "INA":
        status_qde = banco.consulta("status","ina")
        return status_qde
    if _qde == "INB":
        status_qde = banco.consulta("status","inb")
        return status_qde
    if _qde == "INC":
        status_qde = banco.consulta("status","inc")
        return status_qde
    if _qde == "IND":
        status_qde = banco.consulta("status","ind")
        return status_qde

def mudanca_sociais():

    
    if _mudanca_sociais == "IN1":
        status_mudanca_sociais = banco.consulta("status","in1")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN2":
        status_mudanca_sociais = banco.consulta("status","in2")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN3":
        status_mudanca_sociais = banco.consulta("status","in3")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN4":
        status_mudanca_sociais = banco.consulta("status","in4")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN5":
        status_mudanca_sociais = banco.consulta("status","in5")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN6":
        status_mudanca_sociais = banco.consulta("status","in6")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN7":
        status_mudanca_sociais = banco.consulta("status","in7")
        return status_mudanca_sociais
    if _mudanca_sociais == "IN8":
        status_mudanca_sociais = banco.consulta("status","in8")
        return status_mudanca_sociais
    if _mudanca_sociais == "INA":
        status_mudanca_sociais = banco.consulta("status","ina")
        return status_mudanca_sociais
    if _mudanca_sociais == "INB":
        status_mudanca_sociais = banco.consulta("status","inb")
        return status_mudanca_sociais
    if _mudanca_sociais == "INC":
        status_mudanca_sociais = banco.consulta("status","inc")
        return status_mudanca_sociais
    if _mudanca_sociais == "IND":
        status_mudanca_sociais = banco.consulta("status","ind")
        return status_mudanca_sociais

def pmg():


    if _pmg == "IN1":
        status_pmg = banco.consulta("status","in1")
        return status_pmg
    if _pmg == "IN2":
        status_pmg = banco.consulta("status","in2")
        return status_pmg
    if _pmg == "IN3":
        status_pmg = banco.consulta("status","in3")
        return status_pmg
    if _pmg == "IN4":
        status_pmg = banco.consulta("status","in4")
        return status_pmg
    if _pmg == "IN5":
        status_pmg = banco.consulta("status","in5")
        return status_pmg
    if _pmg == "IN6":
        status_pmg = banco.consulta("status","in6")
        return status_pmg
    if _pmg == "IN7":
        status_pmg = banco.consulta("status","in7")
        return status_pmg
    if _pmg == "IN8":
        status_pmg = banco.consulta("status","in8")
        return status_pmg
    if _pmg == "INA":
        status_pmg = banco.consulta("status","ina")
        return status_pmg
    if _pmg == "INB":
        status_pmg = banco.consulta("status","inb")
        return status_pmg
    if _pmg == "INC":
        status_pmg = banco.consulta("status","inc")
        return status_pmg
    if _pmg == "IND":
        status_pmg = banco.consulta("status","ind")
        return status_pmg

def barreira():

    print("barreira",_barreira)


    if _barreira == "IN1":
        status_barreira = banco.consulta("status","in1")
        return status_barreira
    if _barreira == "IN2":
        status_barreira = banco.consulta("status","in2")
        return status_barreira
    if _barreira == "IN3":
        status_barreira = banco.consulta("status","in3")
        return status_barreira
    if _barreira == "IN4":
        status_barreira = banco.consulta("status","in4")
        return status_barreira
    if _barreira == "IN5":
        status_barreira = banco.consulta("status","in5")
        return status_barreira
    if _barreira == "IN6":
        status_barreira = banco.consulta("status","in6")
        return status_barreira
    if _barreira == "IN7":
        status_barreira = banco.consulta("status","in7")
        return status_barreira
    if _barreira == "IN8":
        status_barreira = banco.consulta("status","in8")
        return status_barreira
    if _barreira == "INA":
        status_barreira = banco.consulta("status","ina")
        return status_barreira
    if _barreira == "INB":
        status_barreira = banco.consulta("status","inb")
        return status_barreira
    if _barreira == "INC":
        status_barreira = banco.consulta("status","inc")
        return status_barreira
    if _barreira == "IND":
        status_barreira = banco.consulta("status","ind")
        return status_barreira

def abre_garagem():


    if _abre_garagem == "IN1":
        status_abre_garagem = banco.consulta("status","in1")
        return status_abre_garagem
    if _abre_garagem == "IN2":
        status_abre_garagem = banco.consulta("status","in2")
        return status_abre_garagem
    if _abre_garagem == "IN3":
        status_abre_garagem = banco.consulta("status","in3")
        return status_abre_garagem
    if _abre_garagem == "IN4":
        status_abre_garagem = banco.consulta("status","in4")
        return status_abre_garagem
    if _abre_garagem == "IN5":
        status_abre_garagem = banco.consulta("status","in5")
        return status_abre_garagem
    if _abre_garagem == "IN6":
        status_abre_garagem = banco.consulta("status","in6")
        return status_abre_garagem
    if _abre_garagem == "IN7":
        status_abre_garagem = banco.consulta("status","in7")
        return status_abre_garagem
    if _abre_garagem == "IN8":
        status_abre_garagem = banco.consulta("status","in8")
        return status_abre_garagem
    if _abre_garagem == "INA":
        status_abre_garagem = banco.consulta("status","ina")
        return status_abre_garagem
    if _abre_garagem == "INB":
        status_abre_garagem = banco.consulta("status","inb")
        return status_abre_garagem
    if _abre_garagem == "INC":
        status_abre_garagem = banco.consulta("status","inc")
        return status_abre_garagem
    if _abre_garagem == "IND":
        status_abre_garagem = banco.consulta("status","ind")
        return status_abre_garagem

def mudanca_garagem():


    if _mudanca_garagem == "IN1":
        status_mudanca_garagem = banco.consulta("status","in1")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN2":
        status_mudanca_garagem = banco.consulta("status","in2")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN3":
        status_mudanca_garagem = banco.consulta("status","in3")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN4":
        status_mudanca_garagem = banco.consulta("status","in4")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN5":
        status_mudanca_garagem = banco.consulta("status","in5")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN6":
        status_mudanca_garagem = banco.consulta("status","in6")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN7":
        status_mudanca_garagem = banco.consulta("status","in7")
        return status_mudanca_garagem
    if _mudanca_garagem == "IN8":
        status_mudanca_garagem = banco.consulta("status","in8")
        return status_mudanca_garagem
    if _mudanca_garagem == "INA":
        status_mudanca_garagem = banco.consulta("status","ina")
        return status_mudanca_garagem
    if _mudanca_garagem == "INB":
        status_mudanca_garagem = banco.consulta("status","inb")
        return status_mudanca_garagem
    if _mudanca_garagem == "INC":
        status_mudanca_garagem = banco.consulta("status","inc")
        return status_mudanca_garagem
    if _mudanca_garagem == "IND":
        status_mudanca_garagem = banco.consulta("status","ind")
        return status_mudanca_garagem

