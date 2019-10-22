# Classe para lconfiguração de entradas e saidas do CMM
# Atualizado 19/07/2019

import time
import wiringpi
import RPi.GPIO as GPIO
from banco import Banco
from biblioteca_CMM_oficial import Rele

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

rele = Rele()

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


OUT1 = banco.consulta("saidas","out1")
OUT2 = banco.consulta("saidas","out2")
OUT3 = banco.consulta("saidas","out3")
OUT4 = banco.consulta("saidas","out4")
OUT5 = banco.consulta("saidas","out5")
OUT6 = banco.consulta("saidas","out6")
OUT7 = banco.consulta("saidas","out7")
OUT8 = banco.consulta("saidas","out8")
OUT9 = banco.consulta("saidas","out9")
OUT10 = banco.consulta("saidas","out10")
OUT11 = banco.consulta("saidas","out11")
OUT12 = banco.consulta("saidas","out12")
OUT13 = banco.consulta("saidas","out13")
OUT14 = banco.consulta("saidas","out14")
OUT15 = banco.consulta("saidas","out15")
OUT16 = banco.consulta("saidas","out16")

_abre1 = "Nao definido" 
_abre2 = "Nao definido" 
_abre3 = "Nao definido" 
_abreg = "Nao definido" 
_blq1 = "Nao definido" 
_blq2 = "Nao definido" 
_luz1 = "Nao definido" 
_luz2 = "Nao definido" 
_sinaleira = "Nao definido" 
_sirene = "Nao definido" 
_fot_sociais = "Nao definido" 
_fot_garagem = "Nao definido" 
_exaustor1 = "Nao definido" 
_exaustor2 = "Nao definido" 
_bomba1 = "Nao definido" 
_bomba2 = "Nao definido" 
_aux1 = "Nao definido" 
_aux2 = "Nao definido" 


if OUT1 == "abre_social_externo":           
    _abre1 = "OUT1"    
if OUT1 == "abre_social_interno":            
    _abre2 = "OUT1"
if OUT1 == "abre_social_acesso":          
    _abre3 = "OUT1"
if OUT1 == "abre_garagem":          
    _abreg = "OUT1"    
if OUT1 == "impede_abertura_externo":
    _blq1 = "OUT1"
if OUT1 == "impede_abertura_interno":
    _blq2 = "OUT1"
if OUT1 == "iluminacao_sociais":
    _luz1 = "OUT1"
if OUT1 == "iluminacao_externa":
    _luz2 = "OUT1"
if OUT1 == "sinaleira":
    _sinaleira = "OUT1"
if OUT1 == "sirene":
    _sirene = "OUT1"
if OUT1 == "foto_sociais":
    _fot_sociais = "OUT1"
if OUT1 == "foto_garagem":          
    _fot_garagem = "OUT1"
if OUT1 == "exaustor1":          
    _exaustor1 = "OUT1"
if OUT1 == "exaustor2":          
    _exaustor2 = "OUT1"
if OUT1 == "bomba1":          
    _bomba1 = "OUT1"
if OUT1 == "bomba2":          
    _bomba2 = "OUT1"
if OUT1 == "aux1":          
    _aux1 = "OUT1"
if OUT1 == "aux2":          
    _aux2 = "OUT1"

######################################

if OUT2 == "abre_social_externo":           
    _abre1 = "OUT2"    
if OUT2 == "abre_social_interno":            
    _abre2 = "OUT2"
if OUT2 == "abre_social_acesso":          
    _abre3 = "OUT2"
if OUT2 == "abre_garagem":          
    _abreg = "OUT2"    
if OUT2 == "impede_abertura_externo":
    _blq1 = "OUT2"
if OUT2 == "impede_abertura_interno":
    _blq2 = "OUT2"
if OUT2 == "iluminacao_sociais":
    _luz1 = "OUT2"
if OUT2 == "iluminacao_externa":
    _luz2 = "OUT2"
if OUT2 == "sinaleira":
    _sinaleira = "OUT2"
if OUT2 == "sirene":
    _sirene = "OUT2"
if OUT2 == "foto_sociais":
    _fot_sociais = "OUT2"
if OUT2 == "foto_garagem":          
    _fot_garagem = "OUT2"
if OUT2 == "exaustor1":          
    _exaustor1 = "OUT2"
if OUT2 == "exaustor2":          
    _exaustor2 = "OUT2"
if OUT2 == "bomba1":          
    _bomba1 = "OUT2"
if OUT2 == "bomba2":          
    _bomba2 = "OUT2"
if OUT2 == "aux1":          
    _aux1 = "OUT2"
if OUT2 == "aux2":          
    _aux2 = "OUT2"

######################################
    
if OUT3 == "abre_social_externo":           
    _abre1 = "OUT3"    
if OUT3 == "abre_social_interno":            
    _abre2 = "OUT3"
if OUT3 == "abre_social_acesso":          
    _abre3 = "OUT3"
if OUT3 == "abre_garagem":          
    _abreg = "OUT3"    
if OUT3 == "impede_abertura_externo":
    _blq1 = "OUT3"
if OUT3 == "impede_abertura_interno":
    _blq2 = "OUT3"
if OUT3 == "iluminacao_sociais":
    _luz1 = "OUT3"
if OUT3 == "iluminacao_externa":
    _luz2 = "OUT3"
if OUT3 == "sinaleira":
    _sinaleira = "OUT3"
if OUT3 == "sirene":
    _sirene = "OUT3"
if OUT3 == "foto_sociais":
    _fot_sociais = "OUT3"
if OUT3 == "foto_garagem":          
    _fot_garagem = "OUT3"
if OUT3 == "exaustor1":          
    _exaustor1 = "OUT3"
if OUT3 == "exaustor2":          
    _exaustor2 = "OUT3"
if OUT3 == "bomba1":          
    _bomba1 = "OUT3"
if OUT3 == "bomba2":          
    _bomba2 = "OUT3"
if OUT3 == "aux1":          
    _aux1 = "OUT3"
if OUT3 == "aux2":          
    _aux2 = "OUT3"

######################################
    
if OUT4 == "abre_social_externo":           
    _abre1 = "OUT4"    
if OUT4 == "abre_social_interno":            
    _abre2 = "OUT4"
if OUT4 == "abre_social_acesso":          
    _abre3 = "OUT4"
if OUT4 == "abre_garagem":          
    _abreg = "OUT4"    
if OUT4 == "impede_abertura_externo":
    _blq1 = "OUT4"
if OUT4 == "impede_abertura_interno":
    _blq2 = "OUT4"
if OUT4 == "iluminacao_sociais":
    _luz1 = "OUT4"
if OUT4 == "iluminacao_externa":
    _luz2 = "OUT4"
if OUT4 == "sinaleira":
    _sinaleira = "OUT4"
if OUT4 == "sirene":
    _sirene = "OUT4"
if OUT4 == "foto_sociais":
    _fot_sociais = "OUT4"
if OUT4 == "foto_garagem":          
    _fot_garagem = "OUT4"
if OUT4 == "exaustor1":          
    _exaustor1 = "OUT4"
if OUT4 == "exaustor2":          
    _exaustor2 = "OUT4"
if OUT4 == "bomba1":          
    _bomba1 = "OUT4"
if OUT4 == "bomba2":          
    _bomba2 = "OUT4"
if OUT4 == "aux1":          
    _aux1 = "OUT4"
if OUT4 == "aux2":          
    _aux2 = "OUT4"

######################################
    
if OUT5 == "abre_social_externo":           
    _abre1 = "OUT5"    
if OUT5 == "abre_social_interno":            
    _abre2 = "OUT5"
if OUT5 == "abre_social_acesso":          
    _abre3 = "OUT5"
if OUT5 == "abre_garagem":          
    _abreg = "OUT5"    
if OUT5 == "impede_abertura_externo":
    _blq1 = "OUT5"
if OUT5 == "impede_abertura_interno":
    _blq2 = "OUT5"
if OUT5 == "iluminacao_sociais":
    _luz1 = "OUT5"
if OUT5 == "iluminacao_externa":
    _luz2 = "OUT5"
if OUT5 == "sinaleira":
    _sinaleira = "OUT5"
if OUT5 == "sirene":
    _sirene = "OUT5"
if OUT5 == "foto_sociais":
    _fot_sociais = "OUT5"
if OUT5 == "foto_garagem":          
    _fot_garagem = "OUT5"
if OUT5 == "exaustor1":          
    _exaustor1 = "OUT5"
if OUT5 == "exaustor2":          
    _exaustor2 = "OUT5"
if OUT5 == "bomba1":          
    _bomba1 = "OUT5"
if OUT5 == "bomba2":          
    _bomba2 = "OUT5"
if OUT5 == "aux1":          
    _aux1 = "OUT5"
if OUT5 == "aux2":          
    _aux2 = "OUT5"

######################################
    
if OUT6 == "abre_social_externo":           
    _abre1 = "OUT6"    
if OUT6 == "abre_social_interno":            
    _abre2 = "OUT6"
if OUT6 == "abre_social_acesso":          
    _abre3 = "OUT6"
if OUT6 == "abre_garagem":          
    _abreg = "OUT6"    
if OUT6 == "impede_abertura_externo":
    _blq1 = "OUT6"
if OUT6 == "impede_abertura_interno":
    _blq2 = "OUT6"
if OUT6 == "iluminacao_sociais":
    _luz1 = "OUT6"
if OUT6 == "iluminacao_externa":
    _luz2 = "OUT6"
if OUT6 == "sinaleira":
    _sinaleira = "OUT6"
if OUT6 == "sirene":
    _sirene = "OUT6"
if OUT6 == "foto_sociais":
    _fot_sociais = "OUT6"
if OUT6 == "foto_garagem":          
    _fot_garagem = "OUT6"
if OUT6 == "exaustor1":          
    _exaustor1 = "OUT6"
if OUT6 == "exaustor2":          
    _exaustor2 = "OUT6"
if OUT6 == "bomba1":          
    _bomba1 = "OUT6"
if OUT6 == "bomba2":          
    _bomba2 = "OUT6"
if OUT6 == "aux1":          
    _aux1 = "OUT6"
if OUT6 == "aux2":          
    _aux2 = "OUT6"

######################################
    
if OUT7 == "abre_social_externo":           
    _abre1 = "OUT7"    
if OUT7 == "abre_social_interno":            
    _abre2 = "OUT7"
if OUT7 == "abre_social_acesso":          
    _abre3 = "OUT7"
if OUT7 == "abre_garagem":          
    _abreg = "OUT7"    
if OUT7 == "impede_abertura_externo":
    _blq1 = "OUT7"
if OUT7 == "impede_abertura_interno":
    _blq2 = "OUT7"
if OUT7 == "iluminacao_sociais":
    _luz1 = "OUT7"
if OUT7 == "iluminacao_externa":
    _luz2 = "OUT7"
if OUT7 == "sinaleira":
    _sinaleira = "OUT7"
if OUT7 == "sirene":
    _sirene = "OUT7"
if OUT7 == "foto_sociais":
    _fot_sociais = "OUT7"
if OUT7 == "foto_garagem":          
    _fot_garagem = "OUT7"
if OUT7 == "exaustor1":          
    _exaustor1 = "OUT7"
if OUT7 == "exaustor2":          
    _exaustor2 = "OUT7"
if OUT7 == "bomba1":          
    _bomba1 = "OUT7"
if OUT7 == "bomba2":          
    _bomba2 = "OUT7"
if OUT7 == "aux1":          
    _aux1 = "OUT7"
if OUT7 == "aux2":          
    _aux2 = "OUT7"

######################################
    
if OUT8 == "abre_social_externo":           
    _abre1 = "OUT8"    
if OUT8 == "abre_social_interno":            
    _abre2 = "OUT8"
if OUT8 == "abre_social_acesso":          
    _abre3 = "OUT8"
if OUT8 == "abre_garagem":          
    _abreg = "OUT8"    
if OUT8 == "impede_abertura_externo":
    _blq1 = "OUT8"
if OUT8 == "impede_abertura_interno":
    _blq2 = "OUT8"
if OUT8 == "iluminacao_sociais":
    _luz1 = "OUT8"
if OUT8 == "iluminacao_externa":
    _luz2 = "OUT8"
if OUT8 == "sinaleira":
    _sinaleira = "OUT8"
if OUT8 == "sirene":
    _sirene = "OUT8"
if OUT8 == "foto_sociais":
    _fot_sociais = "OUT8"
if OUT8 == "foto_garagem":          
    _fot_garagem = "OUT8"
if OUT8 == "exaustor1":          
    _exaustor1 = "OUT8"
if OUT8 == "exaustor2":          
    _exaustor2 = "OUT8"
if OUT8 == "bomba1":          
    _bomba1 = "OUT8"
if OUT8 == "bomba2":          
    _bomba2 = "OUT8"
if OUT8 == "aux1":          
    _aux1 = "OUT8"
if OUT8 == "aux2":          
    _aux2 = "OUT8"

######################################
    
if OUT9 == "abre_social_externo":           
    _abre1 = "OUT9"    
if OUT9 == "abre_social_interno":            
    _abre2 = "OUT9"
if OUT9 == "abre_social_acesso":          
    _abre3 = "OUT9"
if OUT9 == "abre_garagem":          
    _abreg = "OUT9"    
if OUT9 == "impede_abertura_externo":
    _blq1 = "OUT9"
if OUT9 == "impede_abertura_interno":
    _blq2 = "OUT9"
if OUT9 == "iluminacao_sociais":
    _luz1 = "OUT9"
if OUT9 == "iluminacao_externa":
    _luz2 = "OUT9"
if OUT9 == "sinaleira":
    _sinaleira = "OUT9"
if OUT9 == "sirene":
    _sirene = "OUT9"
if OUT9 == "foto_sociais":
    _fot_sociais = "OUT9"
if OUT9 == "foto_garagem":          
    _fot_garagem = "OUT9"
if OUT9 == "exaustor1":          
    _exaustor1 = "OUT9"
if OUT9 == "exaustor2":          
    _exaustor2 = "OUT9"
if OUT9 == "bomba1":          
    _bomba1 = "OUT9"
if OUT9 == "bomba2":          
    _bomba2 = "OUT9"
if OUT9 == "aux1":          
    _aux1 = "OUT9"
if OUT9 == "aux2":          
    _aux2 = "OUT9"

######################################
    
if OUT10 == "abre_social_externo":           
    _abre1 = "OUT10"    
if OUT10 == "abre_social_interno":            
    _abre2 = "OUT10"
if OUT10 == "abre_social_acesso":          
    _abre3 = "OUT10"
if OUT10 == "abre_garagem":          
    _abreg = "OUT10"    
if OUT10 == "impede_abertura_externo":
    _blq1 = "OUT10"
if OUT10 == "impede_abertura_interno":
    _blq2 = "OUT10"
if OUT10 == "iluminacao_sociais":
    _luz1 = "OUT10"
if OUT10 == "iluminacao_externa":
    _luz2 = "OUT10"
if OUT10 == "sinaleira":
    _sinaleira = "OUT10"
if OUT10 == "sirene":
    _sirene = "OUT10"
if OUT10 == "foto_sociais":
    _fot_sociais = "OUT10"
if OUT10 == "foto_garagem":          
    _fot_garagem = "OUT10"
if OUT10 == "exaustor1":          
    _exaustor1 = "OUT10"
if OUT10 == "exaustor2":          
    _exaustor2 = "OUT10"
if OUT10 == "bomba1":          
    _bomba1 = "OUT10"
if OUT10 == "bomba2":          
    _bomba2 = "OUT10"
if OUT10 == "aux1":          
    _aux1 = "OUT10"
if OUT10 == "aux2":          
    _aux2 = "OUT10"

######################################
    
if OUT11 == "abre_social_externo":           
    _abre1 = "OUT11"    
if OUT11 == "abre_social_interno":            
    _abre2 = "OUT11"
if OUT11 == "abre_social_acesso":          
    _abre3 = "OUT11"
if OUT11 == "abre_garagem":          
    _abreg = "OUT11"    
if OUT11 == "impede_abertura_externo":
    _blq1 = "OUT11"
if OUT11 == "impede_abertura_interno":
    _blq2 = "OUT11"
if OUT11 == "iluminacao_sociais":
    _luz1 = "OUT11"
if OUT11 == "iluminacao_externa":
    _luz2 = "OUT11"
if OUT11 == "sinaleira":
    _sinaleira = "OUT11"
if OUT11 == "sirene":
    _sirene = "OUT11"
if OUT11 == "foto_sociais":
    _fot_sociais = "OUT11"
if OUT11 == "foto_garagem":          
    _fot_garagem = "OUT11"
if OUT11 == "exaustor1":          
    _exaustor1 = "OUT11"
if OUT11 == "exaustor2":          
    _exaustor2 = "OUT11"
if OUT11 == "bomba1":          
    _bomba1 = "OUT11"
if OUT11 == "bomba2":          
    _bomba2 = "OUT11"
if OUT11 == "aux1":          
    _aux1 = "OUT11"
if OUT11 == "aux2":          
    _aux2 = "OUT11"

######################################
    
if OUT12 == "abre_social_externo":           
    _abre1 = "OUT12"    
if OUT12 == "abre_social_interno":            
    _abre2 = "OUT12"
if OUT12 == "abre_social_acesso":          
    _abre3 = "OUT12"
if OUT12 == "abre_garagem":          
    _abreg = "OUT12"    
if OUT12 == "impede_abertura_externo":
    _blq1 = "OUT12"
if OUT12 == "impede_abertura_interno":
    _blq2 = "OUT12"
if OUT12 == "iluminacao_sociais":
    _luz1 = "OUT12"
if OUT12 == "iluminacao_externa":
    _luz2 = "OUT12"
if OUT12 == "sinaleira":
    _sinaleira = "OUT12"
if OUT12 == "sirene":
    _sirene = "OUT12"
if OUT12 == "foto_sociais":
    _fot_sociais = "OUT12"
if OUT12 == "foto_garagem":          
    _fot_garagem = "OUT12"
if OUT12 == "exaustor1":          
    _exaustor1 = "OUT12"
if OUT12 == "exaustor2":          
    _exaustor2 = "OUT12"
if OUT12 == "bomba1":          
    _bomba1 = "OUT12"
if OUT12 == "bomba2":          
    _bomba2 = "OUT12"
if OUT12 == "aux1":          
    _aux1 = "OUT12"
if OUT12 == "aux2":          
    _aux2 = "OUT12"

######################################
    
if OUT13 == "abre_social_externo":           
    _abre1 = "OUT13"    
if OUT13 == "abre_social_interno":            
    _abre2 = "OUT13"
if OUT13 == "abre_social_acesso":          
    _abre3 = "OUT13"
if OUT13 == "abre_garagem":          
    _abreg = "OUT13"    
if OUT13 == "impede_abertura_externo":
    _blq1 = "OUT13"
if OUT13 == "impede_abertura_interno":
    _blq2 = "OUT13"
if OUT13 == "iluminacao_sociais":
    _luz1 = "OUT13"
if OUT13 == "iluminacao_externa":
    _luz2 = "OUT13"
if OUT13 == "sinaleira":
    _sinaleira = "OUT13"
if OUT13 == "sirene":
    _sirene = "OUT13"
if OUT13 == "foto_sociais":
    _fot_sociais = "OUT13"
if OUT13 == "foto_garagem":          
    _fot_garagem = "OUT13"
if OUT13 == "exaustor1":          
    _exaustor1 = "OUT13"
if OUT13 == "exaustor2":          
    _exaustor2 = "OUT13"
if OUT13 == "bomba1":          
    _bomba1 = "OUT13"
if OUT13 == "bomba2":          
    _bomba2 = "OUT13"
if OUT13 == "aux1":          
    _aux1 = "OUT13"
if OUT13 == "aux2":          
    _aux2 = "OUT13"

######################################
    
if OUT14 == "abre_social_externo":           
    _abre1 = "OUT14"    
if OUT14 == "abre_social_interno":            
    _abre2 = "OUT14"
if OUT14 == "abre_social_acesso":          
    _abre3 = "OUT14"
if OUT14 == "abre_garagem":          
    _abreg = "OUT14"    
if OUT14 == "impede_abertura_externo":
    _blq1 = "OUT14"
if OUT14 == "impede_abertura_interno":
    _blq2 = "OUT14"
if OUT14 == "iluminacao_sociais":
    _luz1 = "OUT14"
if OUT14 == "iluminacao_externa":
    _luz2 = "OUT14"
if OUT14 == "sinaleira":
    _sinaleira = "OUT14"
if OUT14 == "sirene":
    _sirene = "OUT14"
if OUT14 == "foto_sociais":
    _fot_sociais = "OUT14"
if OUT14 == "foto_garagem":          
    _fot_garagem = "OUT14"
if OUT14 == "exaustor1":          
    _exaustor1 = "OUT14"
if OUT14 == "exaustor2":          
    _exaustor2 = "OUT14"
if OUT14 == "bomba1":          
    _bomba1 = "OUT14"
if OUT14 == "bomba2":          
    _bomba2 = "OUT14"
if OUT14 == "aux1":          
    _aux1 = "OUT14"
if OUT14 == "aux2":          
    _aux2 = "OUT14"

######################################
    
if OUT15 == "abre_social_externo":           
    _abre1 = "OUT15"    
if OUT15 == "abre_social_interno":            
    _abre2 = "OUT15"
if OUT15 == "abre_social_acesso":          
    _abre3 = "OUT15"
if OUT15 == "abre_garagem":          
    _abreg = "OUT15"    
if OUT15 == "impede_abertura_externo":
    _blq1 = "OUT15"
if OUT15 == "impede_abertura_interno":
    _blq2 = "OUT15"
if OUT15 == "iluminacao_sociais":
    _luz1 = "OUT15"
if OUT15 == "iluminacao_externa":
    _luz2 = "OUT15"
if OUT15 == "sinaleira":
    _sinaleira = "OUT15"
if OUT15 == "sirene":
    _sirene = "OUT15"
if OUT15 == "foto_sociais":
    _fot_sociais = "OUT15"
if OUT15 == "foto_garagem":          
    _fot_garagem = "OUT15"
if OUT15 == "exaustor1":          
    _exaustor1 = "OUT15"
if OUT15 == "exaustor2":          
    _exaustor2 = "OUT15"
if OUT15 == "bomba1":          
    _bomba1 = "OUT15"
if OUT15 == "bomba2":          
    _bomba2 = "OUT15"
if OUT15 == "aux1":          
    _aux1 = "OUT15"
if OUT15 == "aux2":          
    _aux2 = "OUT15"

######################################
    
if OUT16 == "abre_social_externo":           
    _abre1 = "OUT16"    
if OUT16 == "abre_social_interno":            
    _abre2 = "OUT16"
if OUT16 == "abre_social_acesso":          
    _abre3 = "OUT16"
if OUT16 == "abre_garagem":          
    _abreg = "OUT16"    
if OUT16 == "impede_abertura_externo":
    _blq1 = "OUT16"
if OUT16 == "impede_abertura_interno":
    _blq2 = "OUT16"
if OUT16 == "iluminacao_sociais":
    _luz1 = "OUT16"
if OUT16 == "iluminacao_externa":
    _luz2 = "OUT16"
if OUT16 == "sinaleira":
    _sinaleira = "OUT16"
if OUT16 == "sirene":
    _sirene = "OUT16"
if OUT16 == "foto_sociais":
    _fot_sociais = "OUT16"
if OUT16 == "foto_garagem":          
    _fot_garagem = "OUT16"
if OUT16 == "exaustor1":          
    _exaustor1 = "OUT16"
if OUT16 == "exaustor2":          
    _exaustor2 = "OUT16"
if OUT16 == "bomba1":          
    _bomba1 = "OUT16"
if OUT16 == "bomba2":          
    _bomba2 = "OUT16"
if OUT16 == "aux1":          
    _aux1 = "OUT16"
if OUT16 == "aux2":          
    _aux2 = "OUT16"

######################################

log("*") # Deixa uma linha em branco no log
log("Configuração das saídas:")
log("*")
txt1 = ("OUT1:",OUT1)
log(txt1)
txt2 = ("OUT2:",OUT2)
log(txt2)
txt3 = ("OUT3:",OUT3)
log(txt3)
txt4 = ("OUT4:",OUT4)
log(txt4)
txt5 = ("OUT5:",OUT5)
log(txt5)
txt6 = ("OUT6:",OUT6)
log(txt6)
txt7 = ("OUT7:",OUT7)
log(txt7)
txt8 = ("OUT8:",OUT8)
log(txt8)
txt9 = ("OUT9:",OUT9)
log(txt9)
txt10 = ("OUT10:",OUT10)
log(txt10)
txt11 = ("OUT11:",OUT11)
log(txt11)
txt12 = ("OUT12:",OUT12)
log(txt12)
txt13 = ("OUT13:",OUT13)
log(txt13)
txt14 = ("OUT14:",OUT14)
log(txt14)
txt15 = ("OUT15:",OUT15)
log(txt15)
txt16 = ("OUT16:",OUT16)
log(txt16)
log("*") # Deixa uma linha em branco no log   

    
def liga_abre1():    

    if _abre1 == "OUT1":
        rele.liga(1)
        return        
    if _abre1 == "OUT2":
        rele.liga(2)
        return
    if _abre1 == "OUT3":
        rele.liga(3)
        return
    if _abre1 == "OUT4":
        rele.liga(4)
        return
    if _abre1 == "OUT5":
        rele.liga(5)
        return
    if _abre1 == "OUT6":
        rele.liga(6)
        return
    if _abre1 == "OUT7":
        rele.liga(7)
        return
    if _abre1 == "OUT8":
        rele.liga(8)
        return
    if _abre1 == "OUT9":
        rele.liga(9)
        return
    if _abre1 == "OUT10":
        rele.liga(10)
        return
    if _abre1 == "OUT11":
        rele.liga(11)
        return
    if _abre1 == "OUT12":
        rele.liga(12)
        return
    if _abre1 == "OUT13":
        rele.liga(13)
        return
    if _abre1 == "OUT14":
        rele.liga(14)
        return
    if _abre1 == "OUT15":
        rele.liga(15)
        return
    if _abre1 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_abre1():    

    if _abre1 == "OUT1":
        rele.desliga(1)
        return
    if _abre1 == "OUT2":
        rele.desliga(2)
        return
    if _abre1 == "OUT3":
        rele.desliga(3)
        return
    if _abre1 == "OUT4":
        rele.desliga(4)
        return
    if _abre1 == "OUT5":
        rele.desliga(5)
        return
    if _abre1 == "OUT6":
        rele.desliga(6)
        return
    if _abre1 == "OUT7":
        rele.desliga(7)
        return
    if _abre1 == "OUT8":
        rele.desliga(8)
        return
    if _abre1 == "OUT9":
        rele.desliga(9)
        return
    if _abre1 == "OUT10":
        rele.desliga(10)
        return
    if _abre1 == "OUT11":
        rele.desliga(11)
        return
    if _abre1 == "OUT12":
        rele.desliga(12)
        return
    if _abre1 == "OUT13":
        rele.desliga(13)
        return
    if _abre1 == "OUT14":
        rele.desliga(14)
        return
    if _abre1 == "OUT15":
        rele.desliga(15)
        return
    if _abre1 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_abre1():
   
    if _abre1 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _abre1 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _abre1 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _abre1 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _abre1 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _abre1 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _abre1 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _abre1 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _abre1 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _abre1 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _abre1 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _abre1 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _abre1 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _abre1 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _abre1 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _abre1 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_abre2():    

    if _abre2 == "OUT1":
        rele.liga(1)
        return
    if _abre2 == "OUT2":
        rele.liga(2)
        return
    if _abre2 == "OUT3":
        rele.liga(3)
        return
    if _abre2 == "OUT4":
        rele.liga(4)
        return
    if _abre2 == "OUT5":
        rele.liga(5)
        return
    if _abre2 == "OUT6":
        rele.liga(6)
        return
    if _abre2 == "OUT7":
        rele.liga(7)
        return
    if _abre2 == "OUT8":
        rele.liga(8)
        return
    if _abre2 == "OUT9":
        rele.liga(9)
        return
    if _abre2 == "OUT10":
        rele.liga(10)
        return
    if _abre2 == "OUT11":
        rele.liga(11)
        return
    if _abre2 == "OUT12":
        rele.liga(12)
        return
    if _abre2 == "OUT13":
        rele.liga(13)
        return
    if _abre2 == "OUT14":
        rele.liga(14)
        return
    if _abre2 == "OUT15":
        rele.liga(15)
        return
    if _abre2 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_abre2():    

    if _abre2 == "OUT1":
        rele.desliga(1)
        return
    if _abre2 == "OUT2":
        rele.desliga(2)
        return
    if _abre2 == "OUT3":
        rele.desliga(3)
        return
    if _abre2 == "OUT4":
        rele.desliga(4)
        return
    if _abre2 == "OUT5":
        rele.desliga(5)
        return
    if _abre2 == "OUT6":
        rele.desliga(6)
        return
    if _abre2 == "OUT7":
        rele.desliga(7)
        return
    if _abre2 == "OUT8":
        rele.desliga(8)
        return
    if _abre2 == "OUT9":
        rele.desliga(9)
        return
    if _abre2 == "OUT10":
        rele.desliga(10)
        return
    if _abre2 == "OUT11":
        rele.desliga(11)
        return
    if _abre2 == "OUT12":
        rele.desliga(12)
        return
    if _abre2 == "OUT13":
        rele.desliga(13)
        return
    if _abre2 == "OUT14":
        rele.desliga(14)
        return
    if _abre2 == "OUT15":
        rele.desliga(15)
        return
    if _abre2 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_abre2():    

    if _abre2 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _abre2 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _abre2 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _abre2 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _abre2 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _abre2 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _abre2 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _abre2 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _abre2 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _abre2 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _abre2 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _abre2 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _abre2 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _abre2 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _abre2 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _abre2 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_abre3():    

    if _abre3 == "OUT1":
        rele.liga(1)
        return        
    if _abre3 == "OUT2":
        rele.liga(2)
        return
    if _abre3 == "OUT3":
        rele.liga(3)
        return
    if _abre3 == "OUT4":
        rele.liga(4)
        return
    if _abre3 == "OUT5":
        rele.liga(5)
        return
    if _abre3 == "OUT6":
        rele.liga(6)
        return
    if _abre3 == "OUT7":
        rele.liga(7)
        return
    if _abre3 == "OUT8":
        rele.liga(8)
        return
    if _abre3 == "OUT9":
        rele.liga(9)
        return
    if _abre3 == "OUT10":
        rele.liga(10)
        return
    if _abre3 == "OUT11":
        rele.liga(11)
        return
    if _abre3 == "OUT12":
        rele.liga(12)
        return
    if _abre3 == "OUT13":
        rele.liga(13)
        return
    if _abre3 == "OUT14":
        rele.liga(14)
        return
    if _abre3 == "OUT15":
        rele.liga(15)
        return
    if _abre3 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_abre3():    

    if _abre3 == "OUT1":
        rele.desliga(1)
        return
    if _abre3 == "OUT2":
        rele.desliga(2)
        return
    if _abre3 == "OUT3":
        rele.desliga(3)
        return
    if _abre3 == "OUT4":
        rele.desliga(4)
        return
    if _abre3 == "OUT5":
        rele.desliga(5)
        return
    if _abre3 == "OUT6":
        rele.desliga(6)
        return
    if _abre3 == "OUT7":
        rele.desliga(7)
        return
    if _abre3 == "OUT8":
        rele.desliga(8)
        return
    if _abre3 == "OUT9":
        rele.desliga(9)
        return
    if _abre3 == "OUT10":
        rele.desliga(10)
        return
    if _abre3 == "OUT11":
        rele.desliga(11)
        return
    if _abre3 == "OUT12":
        rele.desliga(12)
        return
    if _abre3 == "OUT13":
        rele.desliga(13)
        return
    if _abre3 == "OUT14":
        rele.desliga(14)
        return
    if _abre3 == "OUT15":
        rele.desliga(15)
        return
    if _abre3 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_abre3():    

    if _abre3 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _abre3 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _abre3 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _abre3 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _abre3 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _abre3 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _abre3 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _abre3 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _abre3 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _abre3 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _abre3 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _abre3 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _abre3 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _abre3 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _abre3 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _abre3 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None
   
def liga_abreg():    

    if _abreg == "OUT1":
        rele.liga(1)
        return        
    if _abreg == "OUT2":
        rele.liga(2)
        return
    if _abreg == "OUT3":
        rele.liga(3)
        return
    if _abreg == "OUT4":
        rele.liga(4)
        return
    if _abreg == "OUT5":
        rele.liga(5)
        return
    if _abreg == "OUT6":
        rele.liga(6)
        return
    if _abreg == "OUT7":
        rele.liga(7)
        return
    if _abreg == "OUT8":
        rele.liga(8)
        return
    if _abreg == "OUT9":
        rele.liga(9)
        return
    if _abreg == "OUT10":
        rele.liga(10)
        return
    if _abreg == "OUT11":
        rele.liga(11)
        return
    if _abreg == "OUT12":
        rele.liga(12)
        return
    if _abreg == "OUT13":
        rele.liga(13)
        return
    if _abreg == "OUT14":
        rele.liga(14)
        return
    if _abreg == "OUT15":
        rele.liga(15)
        return
    if _abreg == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_abreg():    

    if _abreg == "OUT1":
        rele.desliga(1)
        return
    if _abreg == "OUT2":
        rele.desliga(2)
        return
    if _abreg == "OUT3":
        rele.desliga(3)
        return
    if _abreg == "OUT4":
        rele.desliga(4)
        return
    if _abreg == "OUT5":
        rele.desliga(5)
        return
    if _abreg == "OUT6":
        rele.desliga(6)
        return
    if _abreg == "OUT7":
        rele.desliga(7)
        return
    if _abreg == "OUT8":
        rele.desliga(8)
        return
    if _abreg == "OUT9":
        rele.desliga(9)
        return
    if _abreg == "OUT10":
        rele.desliga(10)
        return
    if _abreg == "OUT11":
        rele.desliga(11)
        return
    if _abreg == "OUT12":
        rele.desliga(12)
        return
    if _abreg == "OUT13":
        rele.desliga(13)
        return
    if _abreg == "OUT14":
        rele.desliga(14)
        return
    if _abreg == "OUT15":
        rele.desliga(15)
        return
    if _abreg == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_abreg():
   
    if _abreg == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _abreg == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _abreg == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _abreg == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _abreg == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _abreg == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _abreg == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _abreg == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _abreg == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _abreg == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _abreg == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _abreg == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _abreg == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _abreg == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _abreg == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _abreg == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_blq1():    

    if _blq1 == "OUT1":
        rele.liga(1)
        return        
    if _blq1 == "OUT2":
        rele.liga(2)
        return
    if _blq1 == "OUT3":
        rele.liga(3)
        return
    if _blq1 == "OUT4":
        rele.liga(4)
        return
    if _blq1 == "OUT5":
        rele.liga(5)
        return
    if _blq1 == "OUT6":
        rele.liga(6)
        return
    if _blq1 == "OUT7":
        rele.liga(7)
        return
    if _blq1 == "OUT8":
        rele.liga(8)
        return
    if _blq1 == "OUT9":
        rele.liga(9)
        return
    if _blq1 == "OUT10":
        rele.liga(10)
        return
    if _blq1 == "OUT11":
        rele.liga(11)
        return
    if _blq1 == "OUT12":
        rele.liga(12)
        return
    if _blq1 == "OUT13":
        rele.liga(13)
        return
    if _blq1 == "OUT14":
        rele.liga(14)
        return
    if _blq1 == "OUT15":
        rele.liga(15)
        return
    if _blq1 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_blq1():    

    if _blq1 == "OUT1":
        rele.desliga(1)
        return
    if _blq1 == "OUT2":
        rele.desliga(2)
        return
    if _blq1 == "OUT3":
        rele.desliga(3)
        return
    if _blq1 == "OUT4":
        rele.desliga(4)
        return
    if _blq1 == "OUT5":
        rele.desliga(5)
        return
    if _blq1 == "OUT6":
        rele.desliga(6)
        return
    if _blq1 == "OUT7":
        rele.desliga(7)
        return
    if _blq1 == "OUT8":
        rele.desliga(8)
        return
    if _blq1 == "OUT9":
        rele.desliga(9)
        return
    if _blq1 == "OUT10":
        rele.desliga(10)
        return
    if _blq1 == "OUT11":
        rele.desliga(11)
        return
    if _blq1 == "OUT12":
        rele.desliga(12)
        return
    if _blq1 == "OUT13":
        rele.desliga(13)
        return
    if _blq1 == "OUT14":
        rele.desliga(14)
        return
    if _blq1 == "OUT15":
        rele.desliga(15)
        return
    if _blq1 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_blq1():
   
    if _blq1 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _blq1 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _blq1 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _blq1 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _blq1 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _blq1 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _blq1 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _blq1 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _blq1 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _blq1 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _blq1 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _blq1 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _blq1 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _blq1 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _blq1 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _blq1 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_blq2():    

    if _blq2 == "OUT1":
        rele.liga(1)
        return        
    if _blq2 == "OUT2":
        rele.liga(2)
        return
    if _blq2 == "OUT3":
        rele.liga(3)
        return
    if _blq2 == "OUT4":
        rele.liga(4)
        return
    if _blq2 == "OUT5":
        rele.liga(5)
        return
    if _blq2 == "OUT6":
        rele.liga(6)
        return
    if _blq2 == "OUT7":
        rele.liga(7)
        return
    if _blq2 == "OUT8":
        rele.liga(8)
        return
    if _blq2 == "OUT9":
        rele.liga(9)
        return
    if _blq2 == "OUT10":
        rele.liga(10)
        return
    if _blq2 == "OUT11":
        rele.liga(11)
        return
    if _blq2 == "OUT12":
        rele.liga(12)
        return
    if _blq2 == "OUT13":
        rele.liga(13)
        return
    if _blq2 == "OUT14":
        rele.liga(14)
        return
    if _blq2 == "OUT15":
        rele.liga(15)
        return
    if _blq2 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_blq2():    

    if _blq2 == "OUT1":
        rele.desliga(1)
        return
    if _blq2 == "OUT2":
        rele.desliga(2)
        return
    if _blq2 == "OUT3":
        rele.desliga(3)
        return
    if _blq2 == "OUT4":
        rele.desliga(4)
        return
    if _blq2 == "OUT5":
        rele.desliga(5)
        return
    if _blq2 == "OUT6":
        rele.desliga(6)
        return
    if _blq2 == "OUT7":
        rele.desliga(7)
        return
    if _blq2 == "OUT8":
        rele.desliga(8)
        return
    if _blq2 == "OUT9":
        rele.desliga(9)
        return
    if _blq2 == "OUT10":
        rele.desliga(10)
        return
    if _blq2 == "OUT11":
        rele.desliga(11)
        return
    if _blq2 == "OUT12":
        rele.desliga(12)
        return
    if _blq2 == "OUT13":
        rele.desliga(13)
        return
    if _blq2 == "OUT14":
        rele.desliga(14)
        return
    if _blq2 == "OUT15":
        rele.desliga(15)
        return
    if _blq2 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_blq2():
   
    if _blq2 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _blq2 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _blq2 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _blq2 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _blq2 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _blq2 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _blq2 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _blq2 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _blq2 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _blq2 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _blq2 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _blq2 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _blq2 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _blq2 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _blq2 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _blq2 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_luz1():    

    if _luz1 == "OUT1":
        rele.liga(1)
        return        
    if _luz1 == "OUT2":
        rele.liga(2)
        return
    if _luz1 == "OUT3":
        rele.liga(3)
        return
    if _luz1 == "OUT4":
        rele.liga(4)
        return
    if _luz1 == "OUT5":
        rele.liga(5)
        return
    if _luz1 == "OUT6":
        rele.liga(6)
        return
    if _luz1 == "OUT7":
        rele.liga(7)
        return
    if _luz1 == "OUT8":
        rele.liga(8)
        return
    if _luz1 == "OUT9":
        rele.liga(9)
        return
    if _luz1 == "OUT10":
        rele.liga(10)
        return
    if _luz1 == "OUT11":
        rele.liga(11)
        return
    if _luz1 == "OUT12":
        rele.liga(12)
        return
    if _luz1 == "OUT13":
        rele.liga(13)
        return
    if _luz1 == "OUT14":
        rele.liga(14)
        return
    if _luz1 == "OUT15":
        rele.liga(15)
        return
    if _luz1 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_luz1():    

    if _luz1 == "OUT1":
        rele.desliga(1)
        return
    if _luz1 == "OUT2":
        rele.desliga(2)
        return
    if _luz1 == "OUT3":
        rele.desliga(3)
        return
    if _luz1 == "OUT4":
        rele.desliga(4)
        return
    if _luz1 == "OUT5":
        rele.desliga(5)
        return
    if _luz1 == "OUT6":
        rele.desliga(6)
        return
    if _luz1 == "OUT7":
        rele.desliga(7)
        return
    if _luz1 == "OUT8":
        rele.desliga(8)
        return
    if _luz1 == "OUT9":
        rele.desliga(9)
        return
    if _luz1 == "OUT10":
        rele.desliga(10)
        return
    if _luz1 == "OUT11":
        rele.desliga(11)
        return
    if _luz1 == "OUT12":
        rele.desliga(12)
        return
    if _luz1 == "OUT13":
        rele.desliga(13)
        return
    if _luz1 == "OUT14":
        rele.desliga(14)
        return
    if _luz1 == "OUT15":
        rele.desliga(15)
        return
    if _luz1 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_luz1():
   
    if _luz1 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _luz1 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _luz1 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _luz1 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _luz1 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _luz1 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _luz1 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _luz1 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _luz1 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _luz1 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _luz1 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _luz1 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _luz1 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _luz1 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _luz1 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _luz1 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_luz2():    

    if _luz2 == "OUT1":
        rele.liga(1)
        return        
    if _luz2 == "OUT2":
        rele.liga(2)
        return
    if _luz2 == "OUT3":
        rele.liga(3)
        return
    if _luz2 == "OUT4":
        rele.liga(4)
        return
    if _luz2 == "OUT5":
        rele.liga(5)
        return
    if _luz2 == "OUT6":
        rele.liga(6)
        return
    if _luz2 == "OUT7":
        rele.liga(7)
        return
    if _luz2 == "OUT8":
        rele.liga(8)
        return
    if _luz2 == "OUT9":
        rele.liga(9)
        return
    if _luz2 == "OUT10":
        rele.liga(10)
        return
    if _luz2 == "OUT11":
        rele.liga(11)
        return
    if _luz2 == "OUT12":
        rele.liga(12)
        return
    if _luz2 == "OUT13":
        rele.liga(13)
        return
    if _luz2 == "OUT14":
        rele.liga(14)
        return
    if _luz2 == "OUT15":
        rele.liga(15)
        return
    if _luz2 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_luz2():    

    if _luz2 == "OUT1":
        rele.desliga(1)
        return
    if _luz2 == "OUT2":
        rele.desliga(2)
        return
    if _luz2 == "OUT3":
        rele.desliga(3)
        return
    if _luz2 == "OUT4":
        rele.desliga(4)
        return
    if _luz2 == "OUT5":
        rele.desliga(5)
        return
    if _luz2 == "OUT6":
        rele.desliga(6)
        return
    if _luz2 == "OUT7":
        rele.desliga(7)
        return
    if _luz2 == "OUT8":
        rele.desliga(8)
        return
    if _luz2 == "OUT9":
        rele.desliga(9)
        return
    if _luz2 == "OUT10":
        rele.desliga(10)
        return
    if _luz2 == "OUT11":
        rele.desliga(11)
        return
    if _luz2 == "OUT12":
        rele.desliga(12)
        return
    if _luz2 == "OUT13":
        rele.desliga(13)
        return
    if _luz2 == "OUT14":
        rele.desliga(14)
        return
    if _luz2 == "OUT15":
        rele.desliga(15)
        return
    if _luz2 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_luz2():
   
    if _luz2 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _luz2 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _luz2 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _luz2 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _luz2 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _luz2 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _luz2 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _luz2 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _luz2 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _luz2 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _luz2 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _luz2 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _luz2 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _luz2 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _luz2 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _luz2 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_sinaleira():    

    if _sinaleira == "OUT1":
        rele.liga(1)
        return        
    if _sinaleira == "OUT2":
        rele.liga(2)
        return
    if _sinaleira == "OUT3":
        rele.liga(3)
        return
    if _sinaleira == "OUT4":
        rele.liga(4)
        return
    if _sinaleira == "OUT5":
        rele.liga(5)
        return
    if _sinaleira == "OUT6":
        rele.liga(6)
        return
    if _sinaleira == "OUT7":
        rele.liga(7)
        return
    if _sinaleira == "OUT8":
        rele.liga(8)
        return
    if _sinaleira == "OUT9":
        rele.liga(9)
        return
    if _sinaleira == "OUT10":
        rele.liga(10)
        return
    if _sinaleira == "OUT11":
        rele.liga(11)
        return
    if _sinaleira == "OUT12":
        rele.liga(12)
        return
    if _sinaleira == "OUT13":
        rele.liga(13)
        return
    if _sinaleira == "OUT14":
        rele.liga(14)
        return
    if _sinaleira == "OUT15":
        rele.liga(15)
        return
    if _sinaleira == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_sinaleira():    

    if _sinaleira == "OUT1":
        rele.desliga(1)
        return
    if _sinaleira == "OUT2":
        rele.desliga(2)
        return
    if _sinaleira == "OUT3":
        rele.desliga(3)
        return
    if _sinaleira == "OUT4":
        rele.desliga(4)
        return
    if _sinaleira == "OUT5":
        rele.desliga(5)
        return
    if _sinaleira == "OUT6":
        rele.desliga(6)
        return
    if _sinaleira == "OUT7":
        rele.desliga(7)
        return
    if _sinaleira == "OUT8":
        rele.desliga(8)
        return
    if _sinaleira == "OUT9":
        rele.desliga(9)
        return
    if _sinaleira == "OUT10":
        rele.desliga(10)
        return
    if _sinaleira == "OUT11":
        rele.desliga(11)
        return
    if _sinaleira == "OUT12":
        rele.desliga(12)
        return
    if _sinaleira == "OUT13":
        rele.desliga(13)
        return
    if _sinaleira == "OUT14":
        rele.desliga(14)
        return
    if _sinaleira == "OUT15":
        rele.desliga(15)
        return
    if _sinaleira == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_sinaleira():
   
    if _sinaleira == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _sinaleira == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _sinaleira == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _sinaleira == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _sinaleira == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _sinaleira == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _sinaleira == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _sinaleira == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _sinaleira == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _sinaleira == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _sinaleira == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _sinaleira == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _sinaleira == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _sinaleira == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _sinaleira == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _sinaleira == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_sirene():    

    if _sirene == "OUT1":
        rele.liga(1)
        return        
    if _sirene == "OUT2":
        rele.liga(2)
        return
    if _sirene == "OUT3":
        rele.liga(3)
        return
    if _sirene == "OUT4":
        rele.liga(4)
        return
    if _sirene == "OUT5":
        rele.liga(5)
        return
    if _sirene == "OUT6":
        rele.liga(6)
        return
    if _sirene == "OUT7":
        rele.liga(7)
        return
    if _sirene == "OUT8":
        rele.liga(8)
        return
    if _sirene == "OUT9":
        rele.liga(9)
        return
    if _sirene == "OUT10":
        rele.liga(10)
        return
    if _sirene == "OUT11":
        rele.liga(11)
        return
    if _sirene == "OUT12":
        rele.liga(12)
        return
    if _sirene == "OUT13":
        rele.liga(13)
        return
    if _sirene == "OUT14":
        rele.liga(14)
        return
    if _sirene == "OUT15":
        rele.liga(15)
        return
    if _sirene == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_sirene():    

    if _sirene == "OUT1":
        rele.desliga(1)
        return
    if _sirene == "OUT2":
        rele.desliga(2)
        return
    if _sirene == "OUT3":
        rele.desliga(3)
        return
    if _sirene == "OUT4":
        rele.desliga(4)
        return
    if _sirene == "OUT5":
        rele.desliga(5)
        return
    if _sirene == "OUT6":
        rele.desliga(6)
        return
    if _sirene == "OUT7":
        rele.desliga(7)
        return
    if _sirene == "OUT8":
        rele.desliga(8)
        return
    if _sirene == "OUT9":
        rele.desliga(9)
        return
    if _sirene == "OUT10":
        rele.desliga(10)
        return
    if _sirene == "OUT11":
        rele.desliga(11)
        return
    if _sirene == "OUT12":
        rele.desliga(12)
        return
    if _sirene == "OUT13":
        rele.desliga(13)
        return
    if _sirene == "OUT14":
        rele.desliga(14)
        return
    if _sirene == "OUT15":
        rele.desliga(15)
        return
    if _sirene == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_sirene():
   
    if _sirene == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _sirene == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _sirene == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _sirene == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _sirene == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _sirene == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _sirene == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _sirene == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _sirene == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _sirene == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _sirene == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _sirene == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _sirene == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _sirene == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _sirene == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _sirene == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_exaustor1():    

    if _exaustor1 == "OUT1":
        rele.liga(1)
        return        
    if _exaustor1 == "OUT2":
        rele.liga(2)
        return
    if _exaustor1 == "OUT3":
        rele.liga(3)
        return
    if _exaustor1 == "OUT4":
        rele.liga(4)
        return
    if _exaustor1 == "OUT5":
        rele.liga(5)
        return
    if _exaustor1 == "OUT6":
        rele.liga(6)
        return
    if _exaustor1 == "OUT7":
        rele.liga(7)
        return
    if _exaustor1 == "OUT8":
        rele.liga(8)
        return
    if _exaustor1 == "OUT9":
        rele.liga(9)
        return
    if _exaustor1 == "OUT10":
        rele.liga(10)
        return
    if _exaustor1 == "OUT11":
        rele.liga(11)
        return
    if _exaustor1 == "OUT12":
        rele.liga(12)
        return
    if _exaustor1 == "OUT13":
        rele.liga(13)
        return
    if _exaustor1 == "OUT14":
        rele.liga(14)
        return
    if _exaustor1 == "OUT15":
        rele.liga(15)
        return
    if _exaustor1 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_exaustor1():    

    if _exaustor1 == "OUT1":
        rele.desliga(1)
        return
    if _exaustor1 == "OUT2":
        rele.desliga(2)
        return
    if _exaustor1 == "OUT3":
        rele.desliga(3)
        return
    if _exaustor1 == "OUT4":
        rele.desliga(4)
        return
    if _exaustor1 == "OUT5":
        rele.desliga(5)
        return
    if _exaustor1 == "OUT6":
        rele.desliga(6)
        return
    if _exaustor1 == "OUT7":
        rele.desliga(7)
        return
    if _exaustor1 == "OUT8":
        rele.desliga(8)
        return
    if _exaustor1 == "OUT9":
        rele.desliga(9)
        return
    if _exaustor1 == "OUT10":
        rele.desliga(10)
        return
    if _exaustor1 == "OUT11":
        rele.desliga(11)
        return
    if _exaustor1 == "OUT12":
        rele.desliga(12)
        return
    if _exaustor1 == "OUT13":
        rele.desliga(13)
        return
    if _exaustor1 == "OUT14":
        rele.desliga(14)
        return
    if _exaustor1 == "OUT15":
        rele.desliga(15)
        return
    if _exaustor1 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_exaustor1():
   
    if _exaustor1 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _exaustor1 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _exaustor1 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _exaustor1 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _exaustor1 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _exaustor1 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _exaustor1 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _exaustor1 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _exaustor1 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _exaustor1 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _exaustor1 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _exaustor1 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _exaustor1 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _exaustor1 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _exaustor1 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _exaustor1 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_exaustor2():    

    if _exaustor2 == "OUT1":
        rele.liga(1)
        return        
    if _exaustor2 == "OUT2":
        rele.liga(2)
        return
    if _exaustor2 == "OUT3":
        rele.liga(3)
        return
    if _exaustor2 == "OUT4":
        rele.liga(4)
        return
    if _exaustor2 == "OUT5":
        rele.liga(5)
        return
    if _exaustor2 == "OUT6":
        rele.liga(6)
        return
    if _exaustor2 == "OUT7":
        rele.liga(7)
        return
    if _exaustor2 == "OUT8":
        rele.liga(8)
        return
    if _exaustor2 == "OUT9":
        rele.liga(9)
        return
    if _exaustor2 == "OUT10":
        rele.liga(10)
        return
    if _exaustor2 == "OUT11":
        rele.liga(11)
        return
    if _exaustor2 == "OUT12":
        rele.liga(12)
        return
    if _exaustor2 == "OUT13":
        rele.liga(13)
        return
    if _exaustor2 == "OUT14":
        rele.liga(14)
        return
    if _exaustor2 == "OUT15":
        rele.liga(15)
        return
    if _exaustor2 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_exaustor2():    

    if _exaustor2 == "OUT1":
        rele.desliga(1)
        return
    if _exaustor2 == "OUT2":
        rele.desliga(2)
        return
    if _exaustor2 == "OUT3":
        rele.desliga(3)
        return
    if _exaustor2 == "OUT4":
        rele.desliga(4)
        return
    if _exaustor2 == "OUT5":
        rele.desliga(5)
        return
    if _exaustor2 == "OUT6":
        rele.desliga(6)
        return
    if _exaustor2 == "OUT7":
        rele.desliga(7)
        return
    if _exaustor2 == "OUT8":
        rele.desliga(8)
        return
    if _exaustor2 == "OUT9":
        rele.desliga(9)
        return
    if _exaustor2 == "OUT10":
        rele.desliga(10)
        return
    if _exaustor2 == "OUT11":
        rele.desliga(11)
        return
    if _exaustor2 == "OUT12":
        rele.desliga(12)
        return
    if _exaustor2 == "OUT13":
        rele.desliga(13)
        return
    if _exaustor2 == "OUT14":
        rele.desliga(14)
        return
    if _exaustor2 == "OUT15":
        rele.desliga(15)
        return
    if _exaustor2 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_exaustor2():
   
    if _exaustor2 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _exaustor2 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _exaustor2 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _exaustor2 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _exaustor2 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _exaustor2 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _exaustor2 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _exaustor2 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _exaustor2 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _exaustor2 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _exaustor2 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _exaustor2 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _exaustor2 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _exaustor2 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _exaustor2 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _exaustor2 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_bomba1():    

    if _bomba1 == "OUT1":
        rele.liga(1)
        return        
    if _bomba1 == "OUT2":
        rele.liga(2)
        return
    if _bomba1 == "OUT3":
        rele.liga(3)
        return
    if _bomba1 == "OUT4":
        rele.liga(4)
        return
    if _bomba1 == "OUT5":
        rele.liga(5)
        return
    if _bomba1 == "OUT6":
        rele.liga(6)
        return
    if _bomba1 == "OUT7":
        rele.liga(7)
        return
    if _bomba1 == "OUT8":
        rele.liga(8)
        return
    if _bomba1 == "OUT9":
        rele.liga(9)
        return
    if _bomba1 == "OUT10":
        rele.liga(10)
        return
    if _bomba1 == "OUT11":
        rele.liga(11)
        return
    if _bomba1 == "OUT12":
        rele.liga(12)
        return
    if _bomba1 == "OUT13":
        rele.liga(13)
        return
    if _bomba1 == "OUT14":
        rele.liga(14)
        return
    if _bomba1 == "OUT15":
        rele.liga(15)
        return
    if _bomba1 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_bomba1():    

    if _bomba1 == "OUT1":
        rele.desliga(1)
        return
    if _bomba1 == "OUT2":
        rele.desliga(2)
        return
    if _bomba1 == "OUT3":
        rele.desliga(3)
        return
    if _bomba1 == "OUT4":
        rele.desliga(4)
        return
    if _bomba1 == "OUT5":
        rele.desliga(5)
        return
    if _bomba1 == "OUT6":
        rele.desliga(6)
        return
    if _bomba1 == "OUT7":
        rele.desliga(7)
        return
    if _bomba1 == "OUT8":
        rele.desliga(8)
        return
    if _bomba1 == "OUT9":
        rele.desliga(9)
        return
    if _bomba1 == "OUT10":
        rele.desliga(10)
        return
    if _bomba1 == "OUT11":
        rele.desliga(11)
        return
    if _bomba1 == "OUT12":
        rele.desliga(12)
        return
    if _bomba1 == "OUT13":
        rele.desliga(13)
        return
    if _bomba1 == "OUT14":
        rele.desliga(14)
        return
    if _bomba1 == "OUT15":
        rele.desliga(15)
        return
    if _bomba1 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_bomba1():
   
    if _bomba1 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _bomba1 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _bomba1 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _bomba1 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _bomba1 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _bomba1 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _bomba1 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _bomba1 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _bomba1 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _bomba1 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _bomba1 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _bomba1 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _bomba1 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _bomba1 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _bomba1 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _bomba1 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_bomba2():    

    if _bomba2 == "OUT1":
        rele.liga(1)
        return        
    if _bomba2 == "OUT2":
        rele.liga(2)
        return
    if _bomba2 == "OUT3":
        rele.liga(3)
        return
    if _bomba2 == "OUT4":
        rele.liga(4)
        return
    if _bomba2 == "OUT5":
        rele.liga(5)
        return
    if _bomba2 == "OUT6":
        rele.liga(6)
        return
    if _bomba2 == "OUT7":
        rele.liga(7)
        return
    if _bomba2 == "OUT8":
        rele.liga(8)
        return
    if _bomba2 == "OUT9":
        rele.liga(9)
        return
    if _bomba2 == "OUT10":
        rele.liga(10)
        return
    if _bomba2 == "OUT11":
        rele.liga(11)
        return
    if _bomba2 == "OUT12":
        rele.liga(12)
        return
    if _bomba2 == "OUT13":
        rele.liga(13)
        return
    if _bomba2 == "OUT14":
        rele.liga(14)
        return
    if _bomba2 == "OUT15":
        rele.liga(15)
        return
    if _bomba2 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_bomba2():    

    if _bomba2 == "OUT1":
        rele.desliga(1)
        return
    if _bomba2 == "OUT2":
        rele.desliga(2)
        return
    if _bomba2 == "OUT3":
        rele.desliga(3)
        return
    if _bomba2 == "OUT4":
        rele.desliga(4)
        return
    if _bomba2 == "OUT5":
        rele.desliga(5)
        return
    if _bomba2 == "OUT6":
        rele.desliga(6)
        return
    if _bomba2 == "OUT7":
        rele.desliga(7)
        return
    if _bomba2 == "OUT8":
        rele.desliga(8)
        return
    if _bomba2 == "OUT9":
        rele.desliga(9)
        return
    if _bomba2 == "OUT10":
        rele.desliga(10)
        return
    if _bomba2 == "OUT11":
        rele.desliga(11)
        return
    if _bomba2 == "OUT12":
        rele.desliga(12)
        return
    if _bomba2 == "OUT13":
        rele.desliga(13)
        return
    if _bomba2 == "OUT14":
        rele.desliga(14)
        return
    if _bomba2 == "OUT15":
        rele.desliga(15)
        return
    if _bomba2 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_bomba2():
   
    if _bomba2 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _bomba2 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _bomba2 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _bomba2 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _bomba2 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _bomba2 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _bomba2 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _bomba2 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _bomba2 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _bomba2 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _bomba2 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _bomba2 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _bomba2 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _bomba2 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _bomba2 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _bomba2 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_aux1():    

    if _aux1 == "OUT1":
        rele.liga(1)
        return        
    if _aux1 == "OUT2":
        rele.liga(2)
        return
    if _aux1 == "OUT3":
        rele.liga(3)
        return
    if _aux1 == "OUT4":
        rele.liga(4)
        return
    if _aux1 == "OUT5":
        rele.liga(5)
        return
    if _aux1 == "OUT6":
        rele.liga(6)
        return
    if _aux1 == "OUT7":
        rele.liga(7)
        return
    if _aux1 == "OUT8":
        rele.liga(8)
        return
    if _aux1 == "OUT9":
        rele.liga(9)
        return
    if _aux1 == "OUT10":
        rele.liga(10)
        return
    if _aux1 == "OUT11":
        rele.liga(11)
        return
    if _aux1 == "OUT12":
        rele.liga(12)
        return
    if _aux1 == "OUT13":
        rele.liga(13)
        return
    if _aux1 == "OUT14":
        rele.liga(14)
        return
    if _aux1 == "OUT15":
        rele.liga(15)
        return
    if _aux1 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_aux1():    

    if _aux1 == "OUT1":
        rele.desliga(1)
        return
    if _aux1 == "OUT2":
        rele.desliga(2)
        return
    if _aux1 == "OUT3":
        rele.desliga(3)
        return
    if _aux1 == "OUT4":
        rele.desliga(4)
        return
    if _aux1 == "OUT5":
        rele.desliga(5)
        return
    if _aux1 == "OUT6":
        rele.desliga(6)
        return
    if _aux1 == "OUT7":
        rele.desliga(7)
        return
    if _aux1 == "OUT8":
        rele.desliga(8)
        return
    if _aux1 == "OUT9":
        rele.desliga(9)
        return
    if _aux1 == "OUT10":
        rele.desliga(10)
        return
    if _aux1 == "OUT11":
        rele.desliga(11)
        return
    if _aux1 == "OUT12":
        rele.desliga(12)
        return
    if _aux1 == "OUT13":
        rele.desliga(13)
        return
    if _aux1 == "OUT14":
        rele.desliga(14)
        return
    if _aux1 == "OUT15":
        rele.desliga(15)
        return
    if _aux1 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_aux1():
   
    if _aux1 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _aux1 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _aux1 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _aux1 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _aux1 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _aux1 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _aux1 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _aux1 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _aux1 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _aux1 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _aux1 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _aux1 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _aux1 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _aux1 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _aux1 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _aux1 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_aux2():    

    if _aux2 == "OUT1":
        rele.liga(1)
        return        
    if _aux2 == "OUT2":
        rele.liga(2)
        return
    if _aux2 == "OUT3":
        rele.liga(3)
        return
    if _aux2 == "OUT4":
        rele.liga(4)
        return
    if _aux2 == "OUT5":
        rele.liga(5)
        return
    if _aux2 == "OUT6":
        rele.liga(6)
        return
    if _aux2 == "OUT7":
        rele.liga(7)
        return
    if _aux2 == "OUT8":
        rele.liga(8)
        return
    if _aux2 == "OUT9":
        rele.liga(9)
        return
    if _aux2 == "OUT10":
        rele.liga(10)
        return
    if _aux2 == "OUT11":
        rele.liga(11)
        return
    if _aux2 == "OUT12":
        rele.liga(12)
        return
    if _aux2 == "OUT13":
        rele.liga(13)
        return
    if _aux2 == "OUT14":
        rele.liga(14)
        return
    if _aux2 == "OUT15":
        rele.liga(15)
        return
    if _aux2 == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_aux2():    

    if _aux2 == "OUT1":
        rele.desliga(1)
        return
    if _aux2 == "OUT2":
        rele.desliga(2)
        return
    if _aux2 == "OUT3":
        rele.desliga(3)
        return
    if _aux2 == "OUT4":
        rele.desliga(4)
        return
    if _aux2 == "OUT5":
        rele.desliga(5)
        return
    if _aux2 == "OUT6":
        rele.desliga(6)
        return
    if _aux2 == "OUT7":
        rele.desliga(7)
        return
    if _aux2 == "OUT8":
        rele.desliga(8)
        return
    if _aux2 == "OUT9":
        rele.desliga(9)
        return
    if _aux2 == "OUT10":
        rele.desliga(10)
        return
    if _aux2 == "OUT11":
        rele.desliga(11)
        return
    if _aux2 == "OUT12":
        rele.desliga(12)
        return
    if _aux2 == "OUT13":
        rele.desliga(13)
        return
    if _aux2 == "OUT14":
        rele.desliga(14)
        return
    if _aux2 == "OUT15":
        rele.desliga(15)
        return
    if _aux2 == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_aux2():
   
    if _aux2 == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _aux2 == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _aux2 == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _aux2 == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _aux2 == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _aux2 == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _aux2 == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _aux2 == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _aux2 == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _aux2 == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _aux2 == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _aux2 == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _aux2 == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _aux2 == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _aux2 == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _aux2 == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None


def liga_fot_sociais():    

    if _fot_sociais == "OUT1":
        rele.liga(1)
        return        
    if _fot_sociais == "OUT2":
        rele.liga(2)
        return
    if _fot_sociais == "OUT3":
        rele.liga(3)
        return
    if _fot_sociais == "OUT4":
        rele.liga(4)
        return
    if _fot_sociais == "OUT5":
        rele.liga(5)
        return
    if _fot_sociais == "OUT6":
        rele.liga(6)
        return
    if _fot_sociais == "OUT7":
        rele.liga(7)
        return
    if _fot_sociais == "OUT8":
        rele.liga(8)
        return
    if _fot_sociais == "OUT9":
        rele.liga(9)
        return
    if _fot_sociais == "OUT10":
        rele.liga(10)
        return
    if _fot_sociais == "OUT11":
        rele.liga(11)
        return
    if _fot_sociais == "OUT12":
        rele.liga(12)
        return
    if _fot_sociais == "OUT13":
        rele.liga(13)
        return
    if _fot_sociais == "OUT14":
        rele.liga(14)
        return
    if _fot_sociais == "OUT15":
        rele.liga(15)
        return
    if _fot_sociais == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_fot_sociais():    

    if _fot_sociais == "OUT1":
        rele.desliga(1)
        return
    if _fot_sociais == "OUT2":
        rele.desliga(2)
        return
    if _fot_sociais == "OUT3":
        rele.desliga(3)
        return
    if _fot_sociais == "OUT4":
        rele.desliga(4)
        return
    if _fot_sociais == "OUT5":
        rele.desliga(5)
        return
    if _fot_sociais == "OUT6":
        rele.desliga(6)
        return
    if _fot_sociais == "OUT7":
        rele.desliga(7)
        return
    if _fot_sociais == "OUT8":
        rele.desliga(8)
        return
    if _fot_sociais == "OUT9":
        rele.desliga(9)
        return
    if _fot_sociais == "OUT10":
        rele.desliga(10)
        return
    if _fot_sociais == "OUT11":
        rele.desliga(11)
        return
    if _fot_sociais == "OUT12":
        rele.desliga(12)
        return
    if _fot_sociais == "OUT13":
        rele.desliga(13)
        return
    if _fot_sociais == "OUT14":
        rele.desliga(14)
        return
    if _fot_sociais == "OUT15":
        rele.desliga(15)
        return
    if _fot_sociais == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_fot_sociais():
   
    if _fot_sociais == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _fot_sociais == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _fot_sociais == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _fot_sociais == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _fot_sociais == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _fot_sociais == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _fot_sociais == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _fot_sociais == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _fot_sociais == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _fot_sociais == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _fot_sociais == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _fot_sociais == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _fot_sociais == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _fot_sociais == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _fot_sociais == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _fot_sociais == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None

def liga_fot_garagem():    

    if _fot_garagem == "OUT1":
        rele.liga(1)
        return        
    if _fot_garagem == "OUT2":
        rele.liga(2)
        return
    if _fot_garagem == "OUT3":
        rele.liga(3)
        return
    if _fot_garagem == "OUT4":
        rele.liga(4)
        return
    if _fot_garagem == "OUT5":
        rele.liga(5)
        return
    if _fot_garagem == "OUT6":
        rele.liga(6)
        return
    if _fot_garagem == "OUT7":
        rele.liga(7)
        return
    if _fot_garagem == "OUT8":
        rele.liga(8)
        return
    if _fot_garagem == "OUT9":
        rele.liga(9)
        return
    if _fot_garagem == "OUT10":
        rele.liga(10)
        return
    if _fot_garagem == "OUT11":
        rele.liga(11)
        return
    if _fot_garagem == "OUT12":
        rele.liga(12)
        return
    if _fot_garagem == "OUT13":
        rele.liga(13)
        return
    if _fot_garagem == "OUT14":
        rele.liga(14)
        return
    if _fot_garagem == "OUT15":
        rele.liga(15)
        return
    if _fot_garagem == "OUT16":
        rele.liga(16)
        return
    else:
        return None

def desliga_fot_garagem():    

    if _fot_garagem == "OUT1":
        rele.desliga(1)
        return
    if _fot_garagem == "OUT2":
        rele.desliga(2)
        return
    if _fot_garagem == "OUT3":
        rele.desliga(3)
        return
    if _fot_garagem == "OUT4":
        rele.desliga(4)
        return
    if _fot_garagem == "OUT5":
        rele.desliga(5)
        return
    if _fot_garagem == "OUT6":
        rele.desliga(6)
        return
    if _fot_garagem == "OUT7":
        rele.desliga(7)
        return
    if _fot_garagem == "OUT8":
        rele.desliga(8)
        return
    if _fot_garagem == "OUT9":
        rele.desliga(9)
        return
    if _fot_garagem == "OUT10":
        rele.desliga(10)
        return
    if _fot_garagem == "OUT11":
        rele.desliga(11)
        return
    if _fot_garagem == "OUT12":
        rele.desliga(12)
        return
    if _fot_garagem == "OUT13":
        rele.desliga(13)
        return
    if _fot_garagem == "OUT14":
        rele.desliga(14)
        return
    if _fot_garagem == "OUT15":
        rele.desliga(15)
        return
    if _fot_garagem == "OUT16":
        rele.desliga(16)
        return
    else:
        return None

def pulso_fot_garagem():
   
    if _fot_garagem == "OUT1":
        rele.liga(1)
        time.sleep(3)
        rele.desliga(1)
        return        
    if _fot_garagem == "OUT2":
        rele.liga(2)
        time.sleep(3)
        rele.desliga(2)
        return
    if _fot_garagem == "OUT3":
        rele.liga(3)
        time.sleep(3)
        rele.desliga(3)
        return
    if _fot_garagem == "OUT4":
        rele.liga(4)
        time.sleep(3)
        rele.desliga(4)
        return
    if _fot_garagem == "OUT5":
        rele.liga(5)
        time.sleep(3)
        rele.desliga(5)
        return
    if _fot_garagem == "OUT6":
        rele.liga(6)
        time.sleep(3)
        rele.desliga(6)
        return
    if _fot_garagem == "OUT7":
        rele.liga(7)
        time.sleep(3)
        rele.desliga(7)
        return
    if _fot_garagem == "OUT8":
        rele.liga(8)
        time.sleep(3)
        rele.desliga(8)
        return
    if _fot_garagem == "OUT9":
        rele.liga(9)
        time.sleep(3)
        rele.desliga(9)
        return
    if _fot_garagem == "OUT10":
        rele.liga(10)
        time.sleep(3)
        rele.desliga(10)
        return
    if _fot_garagem == "OUT11":
        rele.liga(11)
        time.sleep(3)
        rele.desliga(11)
        return
    if _fot_garagem == "OUT12":
        rele.liga(12)
        time.sleep(3)
        rele.desliga(12)
        return
    if _fot_garagem == "OUT13":
        rele.liga(13)
        time.sleep(3)
        rele.desliga(13)
        return
    if _fot_garagem == "OUT14":
        rele.liga(14)
        time.sleep(3)
        rele.desliga(14)
        return
    if _fot_garagem == "OUT15":
        rele.liga(15)
        time.sleep(3)
        rele.desliga(15)
        return
    if _fot_garagem == "OUT16":
        rele.liga(16)
        time.sleep(3)
        rele.desliga(16)
        return
    else:
        return None
    

