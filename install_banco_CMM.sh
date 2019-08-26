#!/bin/bash

# Instalando Apache Mysql e phpmyadmin...

echo '''
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

# Instalando LAMP e phpmyadmin

sudo apt-get install apache2 -y
sudo apt-get install mariadb-server php-mysql -y
sudo apt-get install php -y
sudo apt-get install phpmyadmin -y
pip3 install mysql-connector


echo '''

# Criando banco de dados e tabelas...
    _____  ___ __  __ ___    
   / ___/ /  /  / /  /  /   
  / /    / , , / / , , /    
 / /___ /_/_/_/ /_/_/_/     
 \____/ v1.4 for Linux (Python 3)
 
  '''; sleep 1;

# Criando base de dados CMM

sudo mysql -u root -p5510 -e "CREATE DATABASE CMM"

#sudo mysql -u root -p5510 -e "use CMM"
#sudo mysql -u root -p5510 -e "update user SET password=password('5510') WHERE user='root'"
#sudo mysql -u root -p5510 -e "quit"

#### Cria o banco de dados CMM
      
    echo "Criou banco CMM"

#### Cria a tabela qrcode dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE qrcode (id VARCHAR(20) NOT NULL PRIMARY KEY,nome VARCHAR(20),\
    apartamento VARCHAR(10), bloco VARCHAR(10), cond VARCHAR(20), hora_inicio TIME(6), hora_final TIME(6), \
    data_inicio DATE, data_final DATE, dias_semana VARCHAR(10))" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO qrcode (id,nome) VALUES('12345678','Leandro')" CMM;
  
    echo "Criou a tabela qrcode no banco"

#### Cria a tabela status dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE status (in1 VARCHAR(1) NOT NULL PRIMARY KEY,in2 VARCHAR(1),\
    in3 VARCHAR(1), in4 VARCHAR(1), in5 VARCHAR(1), in6 VARCHAR(1), in7 VARCHAR(1), in8 VARCHAR(1),\
    inA VARCHAR(1), inB VARCHAR(1), inC VARCHAR(1), inD VARCHAR(1), out1 VARCHAR(1), out2 VARCHAR(1),\
    out3 VARCHAR(1), out4 VARCHAR(1), out5 VARCHAR(1), out6 VARCHAR(1), out7 VARCHAR(1), out8 VARCHAR(1),\
    out9 VARCHAR(1), out10 VARCHAR(1), out11 VARCHAR(1), out12 VARCHAR(1), out13 VARCHAR(1), out14 VARCHAR(1),\
    out15 VARCHAR(1), out16 VARCHAR(1))" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO status (in1,in2,in3,in4,in5,in6,in7,in8,inA,inB,inC,inD,\
    out1,out2,out3,out4,out5,out6,out7,out8,out9,out10,out11,out12,out13,out14,out15,out16)\
    VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)" CMM;
      
    echo "Criou a tabela status no banco"

#### Cria a tabela leitores_qrcode dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE leitores_qrcode (id INT(11) NOT NULL PRIMARY KEY,\
    leitor_1 VARCHAR(100) NULL, leitor_2 VARCHAR(100) NULL, leitor_3 VARCHAR(100) NULL,leitor_4 VARCHAR(100) NULL,\
    leitor_5 VARCHAR(100) NULL, leitor_6 VARCHAR(100) NULL,leitor_7 VARCHAR(100) NULL, leitor_8 VARCHAR(100)  NULL,\
    leitor_9 VARCHAR(100) NULL, leitor_10 VARCHAR(100) NULL, leitor_11 VARCHAR(100) NULL, leitor_12 VARCHAR(100) NULL,\
    leitor_13 VARCHAR(100) NULL, leitor_14 VARCHAR(100) NULL, leitor_15 VARCHAR(100) NULL, leitor_16 VARCHAR(100) NULL,\
    portao_1 VARCHAR(100) NULL, portao_2 VARCHAR(100) NULL, portao_3 VARCHAR(100) NULL, portao_4 VARCHAR(100) NULL,\
    portao_5 VARCHAR(100) NULL, portao_6 VARCHAR(100) NULL, portao_7 VARCHAR(100) NULL, portao_8 VARCHAR(100) NULL,\
    portao_9 VARCHAR(100) NULL, portao_10 VARCHAR(100) NULL, portao_11 VARCHAR(100) NULL, portao_12 VARCHAR(100) NULL,\
    portao_13 VARCHAR(100) NULL, portao_14 VARCHAR(100) NULL, portao_15 VARCHAR(100) NULL, portao_16 VARCHAR(100) NULL,\
    mensagem_1 VARCHAR(100) NULL, mensagem_2 VARCHAR(100) NULL, mensagem_3 VARCHAR(100) NULL, mensagem_4 VARCHAR(100) NULL,\
    mensagem_5 VARCHAR(100) NULL, mensagem_6 VARCHAR(100) NULL, mensagem_7 VARCHAR(100) NULL, mensagem_8 VARCHAR(100) NULL,\
    mensagem_9 VARCHAR(100) NULL, mensagem_10 VARCHAR(100) NULL, mensagem_11 VARCHAR(100) NULL, mensagem_12 VARCHAR(100) NULL,\
    mensagem_13 VARCHAR(100) NULL, mensagem_14 VARCHAR(100) NULL, mensagem_15 VARCHAR(100) NULL, mensagem_16 VARCHAR(100) NULL)" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO leitores_qrcode (id) VALUES (1)" CMM;

    echo "Criou a tabela leitores_qrcode no banco"

#### Cria a tabela comandos dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE comandos (id INT(11) NOT NULL PRIMARY KEY,\
    abre_social_externo int(11) DEFAULT NULL,abre_social_interno int(11) DEFAULT NULL,abre_garagem int(11) DEFAULT NULL,\
    abre_subsolo int(11) DEFAULT NULL)" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO comandos (id) VALUES (1)" CMM;

    echo "Criou a tabela comandos no banco"

#### Cria a tabela entradas dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE entradas (id INT(11) DEFAULT '1' PRIMARY KEY,\
    in1 varchar(100) DEFAULT NULL,in2 varchar(100) DEFAULT NULL,in3 varchar(100) DEFAULT NULL,in4 varchar(100) DEFAULT NULL,\
    in5 varchar(100) DEFAULT NULL,in6 varchar(100) DEFAULT NULL,in7 varchar(100) DEFAULT NULL,in8 varchar(100) DEFAULT NULL,\
    a varchar(100) DEFAULT NULL,b varchar(100) DEFAULT NULL,c varchar(100) DEFAULT NULL,d varchar(100) DEFAULT NULL,\
    exp1 varchar(100) DEFAULT NULL,exp2 varchar(100) DEFAULT NULL,exp3 varchar(100) DEFAULT NULL,exp4 varchar(100) DEFAULT NULL,\
    exp5 varchar(100) DEFAULT NULL,exp6 varchar(100) DEFAULT NULL,exp7 varchar(100) DEFAULT NULL,exp8 varchar(100) DEFAULT NULL,\
    exp9 varchar(100) DEFAULT NULL,exp10 varchar(100) DEFAULT NULL,exp11 varchar(100) DEFAULT NULL,exp12 varchar(100) DEFAULT NULL,\
    exp13 varchar(100) DEFAULT NULL,exp14 varchar(100) DEFAULT NULL,exp15 varchar(100) DEFAULT NULL,exp16 varchar(100) DEFAULT NULL)" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO entradas (id) VALUES (1)" CMM;

    echo "Criou a tabela entradas no banco"

#### Cria a tabela saidas dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE saidas (id INT(11) NOT NULL PRIMARY KEY,\
    out1 varchar(100) DEFAULT NULL,out2 varchar(100) DEFAULT NULL,out3 varchar(100) DEFAULT NULL,out4 varchar(100) DEFAULT NULL,\
    out5 varchar(100) DEFAULT NULL,out6 varchar(100) DEFAULT NULL,out7 varchar(100) DEFAULT NULL,out8 varchar(100) DEFAULT NULL,\
    out9 varchar(100) DEFAULT NULL,out10 varchar(100) DEFAULT NULL,out11 varchar(100) DEFAULT NULL,out12 varchar(100) DEFAULT NULL,\
    out13 varchar(100) DEFAULT NULL,out14 varchar(100) DEFAULT NULL,out15 varchar(100) DEFAULT NULL,out16 varchar(100) DEFAULT NULL)" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO saidas (id) VALUES (1)" CMM;

    echo "Criou a tabela saidas no banco"

#### Cria a tabela intertravamento dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE intertravamento (id INT(11) NOT NULL PRIMARY KEY,\
    habilitado int(11) DEFAULT NULL)" CMM

    sudo mysql -u root -p5510 -e "INSERT INTO intertravamento (id,habilitado) VALUES (1,0)" CMM;

    echo "Criou a tabela intertravamento no banco"

#### Cria a tabela qr_utilizado dentro do banco CMM

    sudo mysql -u root -p5510 -e "CREATE TABLE qr_utilizado (id INT(11) NOT NULL PRIMARY KEY)" CMM
    
    sudo mysql -u root -p5510 -e "INSERT INTO qr_utilizado (id) VALUES ('12345678')" CMM;

    echo "Criou a tabela qr_utilizado no banco"

#### Criando novo usuario e concedendo todos os priviegios ao usuario

    sudo mysql -u root -p5510 -e "CREATE USER 'leandro' IDENTIFIED BY '5510'"
    sudo mysql -u root -p5510 -e "GRANT ALL PRIVILEGES ON CMM.* TO leandro"
