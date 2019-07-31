#!/bin/bash

cd
sudo apt-get install espeak -y

espeak -v pt-br "Bem vindo a instalação automática do Cê emi emi"

clear

echo '''
Iniciando...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''
sleep 1

sudo apt-get update -y
clear


echo '''
Instalando Reprodutor de audio MPG123...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

# Instala o reprodutor de audio MPG123

sudo apt-get install mpg123 -y


echo '''
Instalando gTTS...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

pip3 install gTTS 
pip3 install gTTS --upgrade 
pip3 install gTTS-token --upgrade

gtts-cli "Olá, ouça uma música durante a instalação." --lang pt --output hello.mp3
sudo mpg123 hello.mp3 
sudo mpg123 /home/pi/musica.mp3 &


echo '''
Instalando supervisor...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

# Instala Suspervisor

sudo apt-get install supervisor 

##echo "Criando o arquivo IHM.conf"
##
##cd /etc/supervisor/conf.d
##sudo rm IHM.conf          # Remove o arquivo se caso ja existir
##sudo touch IHM.conf
##sudo chmod 777 IHM.conf
##
##echo "Editando o arquivo IHM.conf"
##
##echo "[program:IHM]" >> IHM.conf
##echo "command = sudo python3 /home/pi/IHM_CMM.py" >> IHM.conf
##echo "user = pi" >> IHM.conf
##echo "autostart = true" >> IHM.conf
##echo "autorestart = true" >> IHM.conf
##echo "stdout_logfile = /home/pi/IHM.log" >> IHM.conf
##echo "stderr_logfile = /home/pi/IHM.log" >> IHM.conf
##
##echo "Iniciando o IHM pelo supervisor"
##
##sudo supervisorctl stop IHM
##sudo supervisorctl update
##sudo supervisorctl start IHM
##
##cd


echo '''

Instalando Putty...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

sudo apt-get install putty -y

echo '''

Instalando VNC...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

sudo apt-get install vnc4server -y

echo '''

Instalando Apache Mysql e phpmyadmin...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

# Instalando LAMP e phpmyadmin

sudo apt-get install apache2 -y
sudo apt-get install mysql-server php-mysql -y
sudo apt-get install php -y
sudo apt-get install phpmyadmin -y
pip3 install mysql-connector


echo '''

Instalando Team Viewer..
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;


# Instalar teamviewer na rasp

sudo wget http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb
sudo dpkg -i teamviewer-host_armhf.deb 
sudo apt-get -f install -y


echo '''

Criando banco de dados e tabelas...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

# Redefinindo senha e usuario

echo "Redefinindo senha e usuario"

sudo killall mysql
sudo mysqld_safe --skip-grant-tables &
sudo mysql
sudo mysql -u root -p5510 -e "use mysql"
sudo mysql -u root -p5510 -e "update user SET password=password('5510') WHERE user='root'"
sudo mysql -u root -p5510 -e "quit"

#### Cria o banco de dados CMM

    sudo mysql -u root -p5510 -e "CREATE DATABASE CMM"  
    echo "Criou banco CMM"

#### Cria a tabela qrcode dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE qrcode (id VARCHAR(20) NOT NULL PRIMARY KEY,nome VARCHAR(20),\
    apartamento VARCHAR(10), bloco VARCHAR(10), cond VARCHAR(20), hora_inicio TIME(6), hora_final TIME(6), \
    data_inicio DATE, data_final DATE, dias_semana VARCHAR(10))" CMM
  
    echo "Criou a tabela qrcode no banco"

#### Cria a tabela status dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE qrcode (in1 VARCHAR(1) NOT NULL PRIMARY KEY,in2 VARCHAR(1),\
    in3 VARCHAR(1), in4 VARCHAR(1), in5 VARCHAR(1), in6 VARCHAR(1), in7 VARCHAR(1), in8 VARCHAR(1),\
    inA VARCHAR(1), inB VARCHAR(1), inC VARCHAR(1), inD VARCHAR(1), out1 VARCHAR(1), out2 VARCHAR(1),\
    out3 VARCHAR(1), out4 VARCHAR(1), out5 VARCHAR(1), out6 VARCHAR(1), out7 VARCHAR(1), out8 VARCHAR(1),\
    out9 VARCHAR(1), out10 VARCHAR(1), out11 VARCHAR(1), out12 VARCHAR(1), out13 VARCHAR(1), out14 VARCHAR(1),\
    out15 VARCHAR(1), out16 VARCHAR(1))" CMM
      
    echo "Criou a tabela status no banco"

#### Cria a tabela qrcode dentro do banco CMM

    sudo mysql -u root -p5510 -e "USE CMM"
    sudo mysql -u root -p5510 -e "CREATE TABLE moradores LIKE qrcode" CMM

    echo "Criou uma tabela maoradores"

#### Criando novo usuario

    sudo mysql -u root -p5510 -e "CREATE USER 'leandro' IDENTIFIED BY '5510'"

    echo "Criou usuario leandro"

#### Dando todos os priviegios ao usuario

    sudo mysql -u root -p5510 -e "GRANT ALL PRIVILEGES ON CMM.* TO leandro"



echo '''

Instalando bibliotecas para o Python 3...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

echo '''

pip3 install RPi.GPIO
pip3 install smbus
pip3 install spidev
pip3 install serial
pip3 install libscrc 


Agora vamos abrir a interface de controle...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  ''';

sleep 1

nohup python3 /home/pi/IHM_CMM.py 

kill -9 $PPID # Fecha o terminal





