import sys
import socket
import time
import os
from biblioteca_CMM_oficial import Rele,Evento

evento = Evento("0054")
rele = Rele()

def Servidor(): # Inicia a thread do portão da garagem importando a classe Rele
    
    sys.stdout.write("\nPrograma Servidor em execução\n")
    socket.setdefaulttimeout(9999) # limite de 2 segundos para enviar o socket
    
    host = '192.168.0.103'
    port = 5510

    time.sleep(0.1)

    msg = ("Servidor: ", host , " porta: ", port)
    msg = str(msg)
        
    sys.stdout.write(msg)

    while(1):

        class Abre(Rele): # Inicia a thread dos portoes sociais importando a classe Rele


            def social(self):

                status = open("status_social.cmm","w") # Para não dispara o arrombamento
                status.write("1")
                status.close()

                rele.pulso(4,2) # Pulso para abrir direto o portão sem intertravamento (Social)
                
                sys.stdout.write("Abrindo portão social")
                evento.enviar("E","133","001") # Envia abertura

            def eclusa(self):

                status = open("status_eclusa.cmm","w") # Para não dispara o arrombamento
                status.write("1")
                status.close()        
            
                rele.pulso(5,2) # Pulso para abrir direto o portão sem intertravamento (Eclusa)

                sys.stdout.write("Abrindo portão eclusa")      
                evento.enviar("E","133","003") # Envia abertura
                

        abre = Abre()
        ############################################### Thread servidor p/ PHP e MONI #################################################################

        while(1):


            def setupServer():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # "AF_NET" trabalharemos com protocolo ipv4, .SOCK_STREAM USAREMOS TCP
                
                try:
                    s.bind((host, port))
                except socket.error as msg:
                    msg = str(msg)
                    sys.stdout.write(msg)
                
                return s

            def setupConnection():
                s.listen(5)
                conn, address = s.accept()
                info = ("Conectado com: " + address[0] + ":" + str(address[1]), "\n")
                info = str(info)
                sys.stdout.write(info)
                return conn


            def dataTransfer(conn):  # Loop de transferencia e recepção de dados

                while True:

                                      
                    data = conn.recv(1024)  # Recebe o dado
                    data = data.decode('utf-8')
                    dataMessage = data.split(' ',1)# Separa o comando do resto dos dados
                    command = dataMessage[0]

                    (comando,resto) = data.split("\r") # Divide os dados da variavel data e guarda uma parte em comando e eoutra em resto


                    if(comando == "SET1"):

                        sys.stdout.write("Abrindo portão Social pelo Moni")
                        
                        abre.social() # Abre sem intertravamento porem fica aguardando o portão fechar

                        time.sleep(1)
                        conn.close()                        
                                            

                    if(comando == "SET2"):
                        
                        sys.stdout.write("Abrindo portão Eclusa pelo Moni")
                        
                        abre.eclusa() # Abre sem intertravamento

                        time.sleep(1)                        
                        conn.close()

                    
                    if(comando == "RESET"):
                        
                        sys.stdout.write("Reiniciando o sistema pelo Moni")
                        time.sleep(1)                        

                        conn.close()

                        os.system("sudo reboot now")
                        
                    
                    else:

                        info = ("Recebido pelo servidor:",comando)
                        info = str(info)
                        sys.stdout.write

                        reply = 'ok'
                        conn.sendall(str.encode(reply))  # Envia o reply de volta para o cliente
                        conn.close()


            s = setupServer()

            while True:
                
              time.sleep(1)

              txt = ("\nEscutando na porta",port, "\n")
              txt = str(txt)
              sys.stdout.write(txt)
              
              try:

                  conn = setupConnection()
                  dataTransfer(conn)
                  sys.stdout.write("Oiee")


              except Exception as err:

                  sys.stdout.write("Encerrou conexão")

Servidor()
