#!/usr/bin/env python3
# coding=UTF-8

from banco import Banco # Classe para inserções, consulta e atualização no banco de dados CMM
import time
import mysql

banco = Banco()

def deleta_qrs_antigos():

        
        try:            
            
            cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
            cursor = cnx.cursor()
            
        except mysql.connector.Error as err:
            
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              
                print("Alguma coisa esta errada com o nome de usuario ou a senha!")
            
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
              
                print("Esta base de dados nao existe")
            
            else:
              
                print(err)
        try:
            
        
            query = ("DELETE FROM qrcode WHERE data_final < DATE_SUB(CURDATE(),INTERVAL 1 DAY)") 
            cursor.execute(query)
            cnx.commit()

            
        except mysql.connector.Error as err:

            print("Erro ao tentar deletar os dados",err)
            
            return ('erro')

            
        else:

            cnx.close()
            print ("Deletado qrcodes com data expirada")
            return("deletado")

deleta_qrs_antigos()
