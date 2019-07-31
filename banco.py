import mysql.connector # faz a comunicação com o mysql no python 3.6

class Banco:

    def __init__(self):

        self = self

    def consulta(self,tabela,coluna):
    
        try:  # Tenta conectar com o banco de dados
            
            cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
            cursor = cnx.cursor()
                  
        except mysql.connector.Error as err:
                
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:

                print("Alguma coisa esta errada com o nome de usuario ou a senha!")
                
            elif err.errno == errorcode.ER_BAD_DB_ERROR:

                print("Esta base de dados não existe!")

            elif err.errno == errorcode.ER_DUP_ENTRY:

                print("ID duplicado")
               
            else:
                              
                print(err)

        else:    
            
            query = ("SELECT {} FROM {}").format (coluna,tabela) # SELECT campo FROM tabela
            cursor.execute(query)
                      
            for (i) in cursor: # Para cada item da coluna nome faz a comparação

                i = str(i)
                i = i.replace("'","")
                i = i.replace("(","")
                i = i.replace(")","")
                i = i.replace(",","")

                return (i)
        cnx.close()

    def atualiza(self,tabela,coluna,valor):
        

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
            
        
            query = ("UPDATE {} SET {} = {}").format (tabela,coluna,valor)
            cursor.execute(query)
            cnx.commit()

            
        except mysql.connector.Error as err:

            print("Erro na atualização dos dados",err)
            
            return ('erro')

            
        else:

            cnx.close()
            return ("Atualizado valor",valor,"na coluna",coluna,"da tabela",tabela)
            

    def insere(self,tabela,coluna,valor):

        
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
            
        
            query = ("INSERT INTO {}({}) VALUES ({})").format (tabela,coluna,valor)
            cursor.execute(query)
            cnx.commit()

            
        except mysql.connector.Error as err:

            print("Erro na atualização dos dados",err)
            
            return ('erro')

            
        else:

            cnx.close()
            print ("Inserido valor",valor,"na coluna",coluna,"da tabela",tabela)
            return("inserido")
      

    