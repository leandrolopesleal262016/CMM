import time
import os
import glob
import shutil

os.system("sudo chmod 777 -R /var/www/html/log") # Permissão para escrever no log

# Data atual formatada com"_"

data = time.strftime('%d_%m_%Y')
mes = time.strftime('%m')
dia = time.strftime('%d')

hs = time.strftime("%H:%M:%S")

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
    

##print(data)
mes = int(mes)

if mes == 1:
    mes = "Janeiro"
    
    fazer_backup = 31

if mes == 2:
    mes = "Fevereiro"

    fazer_backup = 28

if mes == 3:
    mes = "Marco"

    fazer_backup = 31

if mes == 4:
    mes = "Abril"

    fazer_backup = 30

if mes == 5:
    mes = "Maio"

    fazer_backup = 31

if mes == 6:
    mes = "Junho"

    fazer_backup = 30

if mes == 7:
    mes = "Julho"

    fazer_backup = 31

if mes == 8:
    mes = "Agosto"

    fazer_backup = 31

if mes == 9:
    mes = "Setembro"

    fazer_backup = 30

if mes == 10:
    mes = "Outubro"

    fazer_backup = 31

if mes == 11:
    mes = "Novembro"

    fazer_backup = 30

if mes == 12:
    mes = "Dezembro"

    fazer_backup = 31

# Cria uma lista com os nomes contidos na pasta log em formato .txt

path = '/var/www/html/log'
folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.txt')): #, '.png', '.gif') ): # poderia listar outros tipos tambem
        filenames.append(filename)
                        
quantidade = (len(filenames)) # Quantidade de arquivos na pasta
##print(filenames) # imprime a lista

##print("Temos",quantidade, "arquivos na pasta")

# Limpando a pasta caso ja tenha a quantidade maxima de arquivos

if quantidade >= fazer_backup:
    
    log("Limpando a pasta que ja contem o limite de arquivos do mes...")

    diretorio = ("/var/www/html/log/{}").format(mes)

    shutil.rmtree(diretorio)
    os.mkdir(diretorio)
    msg = ("A pasta atual de {}, substituiu a pasta do ano passado").format(mes)
    print(msg) 

# Salvando o log do dia no arquivo e pasta correspondente

fonte = "/var/www/html/log/log.txt"
destino = ("/var/www/html/log/{}/{}.txt").format(mes,data)

ok = 0

try:        

    shutil.copyfile(fonte,destino) # Tenta salvar o log.txt como um novo arquivo
    txt = open("/var/www/html/log/log.txt","w")    
    txt.write("\n")
    txt.close()
    ok = 0

except : # Se nao existir pasta, cria uma.

    msg = ("Não encontrou a pasta de {} para salvar o log de hoje").format(mes)
    log(msg)
    ok = 1

if ok == 0:

    print("Salvo o log do dia na pasta correspondente")



   



    
