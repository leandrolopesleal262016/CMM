import time
import os
import glob
import shutil

# Data atual formatada com"_"

data = time.strftime('%d_%m_%Y')
mes = time.strftime('%m')
dia = time.strftime('%d')

hs = time.strftime("%H:%M:%S")

##print(data)

if mes == "1":
    mes = "Janeiro"
    
    fazer_backup = 31

if mes == "2":
    mes = "Fevereiro"

    fazer_backup = 28

if mes == "3":
    mes = "Marco"

    fazer_backup = 31

if mes == "4":
    mes = "Abril"

    fazer_backup = 30

if mes == "5":
    mes = "Maio"

    fazer_backup = 31

if mes == "6":
    mes = "Junho"

    fazer_backup = 30

if mes == "7":
    mes = "Julho"

    fazer_backup = 31

if mes == "8":
    mes = "Agosto"

    fazer_backup = 31

if mes == "9":
    mes = "Setembro"

    fazer_backup = 30

if mes == "10":
    mes = "Outubro"

    fazer_backup = 31

if mes == "11":
    mes = "Novembro"

    fazer_backup = 30

if mes == "12":
    mes = "Dezembro"

    fazer_backup = 31

# Cria uma lista com os nomes contidos na oasta log em formato .txt

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
    
    print("Limpando a pasta que ja contem o limite de arquivos do mes...")

    diretorio = ("/var/www/html/log/{}").format(mes)

    shutil.rmtree(diretorio)
    os.mkdir(diretorio)
    msg = ("A pasta atual de {}, substituiu a pasta do ano passado").format(mes)
    print(msg) 

# Salvando o log do dia no arquivo e pasta correspondente

fonte = "/var/www/html/log/log.txt"
destino = ("/var/www/html/log/{}/{}.txt").format(mes,data)

try:        

    shutil.copyfile(fonte,destino) # Tenta salvar o log.txt como um novo arquivo
    txt = open("/var/www/html/log/log.txt","w")    
    txt.write("\n")
    txt.close()

except : # Se for a primeira vez e nao existir pasta, cria uma.
    
    print("Criando a pasta do mes que ainda nao existia...")
    diretorio = ("/var/www/html/log/{}").format(mes)
    os.mkdir(diretorio)
    
    shutil.copyfile(fonte,destino)
    txt = open("/var/www/html/log/log.txt","w")    
    txt.write("\n")
    txt.close()


print("Salvo o log do dia na pasta correspondente")    



    
