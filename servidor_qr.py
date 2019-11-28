import time
import socket
import os
import mysql.connector
import json


os.system("sudo chmod 777 -R /var/www/html/log") # Permissão para escrever no log


def Servidor_qr(): ######### Thread servidor Cadastro QR Code ###################
        
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

    ip = os.popen('hostname -I').readline()
    ip = str(ip)
    ip = ip.replace("\n","")
    
    ip1 = (ip.split(" ")[0]) # Sehouverem 2 ips pega o da eth
    ip2 = (ip.split(" ")[1]) # Sehouverem 2 ips pega o da wlan

    time.sleep(1)    

    deletar = 0
    cadastrar = 0

    host_servidor = ip1  # Host servidor 
    port_gerenciador = 5511# porta para receber dados do gerenciador
    

    print("Ouvindo Gerenciador",host_servidor,":",port_gerenciador)
    
    while(1):

        socket.setdefaulttimeout(99999999)

        hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG        
              
        def setupServer():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # "AF_NET" trabalharemos com protocolo ipv4, .SOCK_STREAM USAREMOS TCP
            
            try:
                s.bind((host_servidor, port_gerenciador))
            except socket.error as msg:
                txt = ("Erro servidor gerenciador",msg)
                log(txt)
                
            return s

        def setupConnection():
            
            s.listen(10)
            conn, address = s.accept()           
            
            return conn

        def dataTransfer(conn):  # Loop de transferencia e recepção de dados
            
            while True:

                try:
           
                    data = conn.recv(1024)  # Recebe o dado
                    data = data.decode('utf-8')

                    log("dados recebidos")
                    log(data)
                    print("Dados recebidos:",data)
                    

                    comando = (data.split("&")[0])
                    corpo = (data.split("&")[1])                   

                    reply = "ok"
                    conn.sendall(str.encode(reply))  # Envia o reply de volta para o cliente  
                    conn.close()

                except Exception as err:

                    txt = ("Dados recebidos estao fora do formato",err)
                    log(txt)                    
                    break                
    
                if comando == "deletar_qr":

                    log("Reconheceu deletar")
                    
                    ID = corpo.split(":")[0]
                    txt = ("ID", ID)
                    log(txt)
                    
                    cliente = corpo.split(":")[1]

                    txt =("cliente",cliente)
                    log(txt)                    

                    try:  # Tenta conectar com o banco de dados
                
                        log('Conectando banco de dados...')  
                        cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
                        cursor = cnx.cursor()
                        log('Conectado\n')
                      
                    except Exception as err:
                        
                        log(err)

                    else:

                        log("Vai tentar selecionar na tabela qrcode")

                        query = ("SELECT * FROM qrcode")  # Seleciona a tabela qrcode
                        cursor.execute(query)

                        encontrou = 0
                
                    for i in cursor:

                        if encontrou == 0:
                               
                            ID_recebido = str(i[0]) # Seleciona o primeiro item da lista recebida do banco (ID)
                                                            
                            if (ID_recebido == ID): # Compara se o ID vindo do request e igual ao do banco   

                                log("Achou o id no banco...")
                                encontrou = 1                            

                    if encontrou == 0:

                        log("id inexistente")

                    if encontrou == 1:
                                
                        try:                            
                        
                            query = ("DELETE FROM qrcode WHERE ID = %s")%ID
                            cursor.execute(query)
                            cnx.commit()                               
                            
                        except Exception as err:  # mysql.connector.Error as err:

                            txt = ("Id inexistente",ID,err)
                            log(txt)
                            
                            cnx.close()                            

                        else:

                            txt = ("ID",ID,"deletado do banco")
                            log(txt)                            
                            break
                    break
                    
                if comando == "cadastrar_qr":

                    try:
                       
                        dados = data.replace("cadastrar_qr&","")                        
                        dados = dados.replace("'",'"')

                    except Exception as err:

                        txt = ("Erro ao formatar os dados para converter em json", err)
                        log(txt)
                        print(txt)
                
                  #  Faz o cadastro dos dados recebidos no banco do CMM #

                    try:

                        try:
                            
                            dados_json = json.loads(dados)  # Tranforma a string para formato json (dicionario)

                        except Exception as err:

                            print("Nao conseguiu converter dados json",err)
                            print (dados)

##                            dados.update({'nome':'Nome com emoticons'})                            
##                            print(dados)
##                            dados_json = json.loads(dados)
                            
                           
                        ID = str(dados_json["ID"])
                        
                        nome = (dados_json["nome"])
                        nome = nome.encode('utf-8')
                        
                        ap = str(dados_json["apartamento"])
                        bloco = str(dados_json["bloco"])
                        cond = str(dados_json["condominio"])
                        di = str(dados_json["data_inicio"])
                        df = str(dados_json["data_final"])
                        hi = str(dados_json["hora_inicio"])
                        hf = str(dados_json["hora_final"])
                        ds = str(dados_json["dias_semana"])

                        l = open("/var/www/html/log_qrcode.txt","a") # Pula uma linha no registro de log
                        l.write("\n")
                        l.close()

                        nome_editado = (dados_json["nome"])
                        nome_editado = str(nome_editado)
                        nome_editado = nome_editado.replace("b","")

                        log("*")
                        txt =("Cadastrar:",nome_editado,"Condominio",cond,"Apartamento",ap,"bloco",bloco,"Inicio em",di,"até",df,"das",hi,"até as",hf)
                        txt = str(txt)
                        txt = txt.replace("'","")
                        txt = txt.replace(",","")
                        txt = txt.replace("(","")
                        txt = txt.replace(")","")
                        log(txt)

                    except Exception as err:

                        txt =("Erro na conversao json",err)
                        log(txt)
                                       
                    try:                 
  
                        cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
                        cursor = cnx.cursor()
                      
                    except Exception as err:
                        
                        log(err)
                        
                    try:                        
                    
                        query = ("INSERT INTO qrcode (ID, nome, apartamento, bloco, cond, hora_inicio, hora_final, data_inicio, data_final, dias_semana) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                        query_data = (ID,nome,ap,bloco,cond,hi,hf,di,df,ds)
                        cursor.execute(query, query_data)
                        cnx.commit()
                        
                    except Exception as err:

                        txt = ("Erro na inclusão do banco",err)
                        log(txt)
                            
                    else:

                        txt = ("Cadastrado com sucesso ID",ID)
                        txt = str(txt)
                        txt = txt.replace("'","")
                        txt = txt.replace(",","")
                        txt = txt.replace("(","")
                        txt = txt.replace(")","")
                        log(txt)
                        log("*")

                        cnx.close()
                        break                
                 
        s = setupServer()

        while True:

          time.sleep(0.4)

          txt = ("Aguardando novos cadastros de QRCODE...")
          txt = str(txt)
          txt = txt.replace("'","")
          txt = txt.replace(",","")
          txt = txt.replace("(","")
          txt = txt.replace(")","")
          log(txt)          
                    
          try:

              conn = setupConnection()
              dataTransfer(conn)                                         
                
          except:
            
              log("Encerrou conexão com Gerenciador")


