def qr_code():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('172.20.2.134', 5001) # Endereço do QR Code maquete
    
    time.sleep(0.1)
    
    print('Leitor QR CODE {} port {}'.format(*server_address),"\n")
    sock.connect(server_address)

    consulta = 0
    id_valido = 0
    acesso = 0
    fora_do_horario = 0
    consta_no_banco = 0
    item = 0
    ja_encontrou = 0

    while(1):

        consulta = 0
        id_valido = 0
        acesso = 0
        fora_do_horario = 0
        consta_no_banco = 0
        item = 0
        ja_encontrou = 0


        hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
        horario_atual = time.strftime("%H:%M")
        
        try: 

            tamanho = 0

            dados = sock.recv(128)
            tamanho += len(dados)
            
##            print ("Dados recebidos",dados,"tamanho",tamanho) # Dados lidos no cartão de QR Code

            if (tamanho >= 16 or tamanho <8): # Se o QR Code lido não tiver exatamente o mesmo tamanho não consulta o banco de dados

                consulta = 0
                dados = 0

##                print ("colocou consulta = 0")

            if (tamanho >= 8 and tamanho < 16): # Se tiver o tamanho exato, prossegue
                                
                dados = int(dados) # Elimina as '' e o \r
                dados = str(dados)

                dados = dados[3:] # elimina os 3 primeiros digitos da string dados

                
                print("Dados editados",dados,type(dados))

                dados = int(dados)

                consulta = 1
                    
                
                tabela = [601, 403, 820, 417, 217, 162, 684, 895, 797, 413, 577, 527, 921, 203, 565, 620, 369, 471, 316, 988, 387, 418, 643, 987, 297, 108, 396, 880, 436, 465, 899, 671, 422, 253, 765, 992, 259, 286, 932, 627, 474, 378, 894, 216, 594, 289, 258, 490, 647, 487, 409, 888, 221, 805, 535, 713, 363, 925, 964, 327]
                         
                tempo_validade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]

                if (1):

                    
                    for item in tabela:
                             
                        id_raiz = int(dados / item)  # divide o valor lido no QR por cada numero da tabela e consulta no banco

                        # Dividiu o id recebido pelos dados da tabela "item" que resultou no id_raiz

                        #print("\n",id_raiz)
                        
                        try:  # Tenta conectar com o banco de dados

                            signal.alarm(2)
                            cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
                            cursor = cnx.cursor()
                            signal.alarm(0)
                              
                        except mysql.connector.Error as err:
                                
                            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                      
                                print("Alguma coisa esta errada com o nome de usuario ou a senha!")

                                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                                arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: Usuario ou senha invalidos\n")
                                arquivo.close()

                            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                      
                                print("Esta base de dados não existe!")

                                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                                arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: A base de dados não existe\n")
                                arquivo.close()

                            else:
                                              
                                print(err)

                                arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                                arquivo.write("Data: " + data + " " + hs + " Evento: Erro de acesso ao Banco pelo QR Code " + err + "\n")
                                arquivo.close()
                                            
                                time.sleep(0.1)
                                      
                                pass
                        
                        try:                    

                            query = ("SELECT ID FROM qrcode WHERE ID = %s")%id_raiz # procura na coluna ID um código = ao id_raiz
                            cursor.execute(query)

                            for i in cursor: # Se o cursor encontrar o item especificado, prossegue...
                                                                                                
                                id_valido = 1 # Encontrou o ID raiz
                                consulta = 1 # Habilita a consulta de data e horario
                                ja_encontrou = 1 # Depois de encontrar encerra a consulta do ID raiz
                                
                                                   
                        except Exception as e:
                        
                            print("Tipo de erro: " + str(e))
                            
                        if ja_encontrou == 1:
                            
                            ja_encontrou = 0

                            break
                item = item
                        
        except Exception as e:

            print("Não foi possivel ler os dados recebidos ")

            print("Tipo de erro: " + str(e))
            
        if consulta == 0:

            print("\nQR Code em formato invalido")
            print("Texto",dados,"\n")

            pygame.mixer.music.load('mp3/206.mp3') # Formato de QR Code inválido
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de log
            arquivo.write("Data: " + data + " " + hs + " Evento: Tentativa de uso de QR Code invalido\n")
            arquivo.close()
                
            texto_recebido = ("")

            time.sleep(3)


        if consulta == 1 :

            item = item

            try:  # Tenta conectar com o banco de dados

                signal.alarm(2)
                cnx = mysql.connector.connect(user='leandro',database='CMM', password='5510',host='localhost')
                cursor = cnx.cursor()
                signal.alarm(0)
                  
            except mysql.connector.Error as err:
                    
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
          
                    print("Alguma coisa esta errada com o nome de usuario ou a senha!")

                    arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                    arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: Usuario ou senha invalidos\n")
                    arquivo.close()

                elif err.errno == errorcode.ER_BAD_DB_ERROR:
          
                    print("Esta base de dados não existe!")

                    arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                    arquivo.write("Data: " + data + " " + hs + " Evento: Banco de Dados: A base de dados não existe\n")
                    arquivo.close()

                else:
                                  
                    print(err)

                    arquivo = open("log_cmm.txt", "a+") # Escreve o evento no registro de log
                    arquivo.write("Data: " + data + " " + hs + " Evento: Erro de acesso ao Banco pelo QR Code " + err + "\n")
                    arquivo.close()
                                
                    time.sleep(0.1)
                          
                    pass
            

            if id_valido == 1: # Se o cursor encontrou o ID correspondente prossegue...

                hs = time.strftime("%H:%M:%S") # MANTEM ATUALIZADO O HORARIO DO REGISTRO DE LOG
                horario_atual = time.strftime("%H:%M")

                # print("Este ID consta no banco",id_raiz)

                consta_no_banco = 1

                try:                    

                    # Primeiro ve se a data ainda não expirou e se o ID ja está liberado o horario
 
                    query = ("SELECT * FROM qrcode WHERE data_final >= CURDATE() AND ID = %s")%id_raiz # Verifica só id e data
                    cursor.execute(query)
                          
                    for i in cursor: # Se encontrar o item especificado, divide as informações e salva nas variaveis

                                             
                        ID = i[0]
                        nome = i[1]
                        ap = i[2]
                        bloco = i[3]
                        cond = i[4]
                        hora_inicio = i[5]
                        hora_final = i[6]
                        data_inicio = i[7]
                        data_final = i[8]
                        dias_semana = i[9]

                        print("\nID",ID,"\nNome",nome,"valido de",data_inicio.strftime('%d/%m/%Y'),"até",data_final.strftime('%d/%m/%Y'),"das",hora_inicio,"as",hora_final,"hs","dias da semana",dias_semana)

                        hora_i = str(hora_inicio)
                        hora_f = str(hora_final)
                        hs = str(hs)


                        h_i = (hora_i.split(":")[0])
                        m_i = (hora_i.split(":")[1])
                        h_f = (hora_f.split(":")[0])
                        m_f = (hora_f.split(":")[1])

                        hi = int(h_i )  # Hora inicial como um inteiro para comparar com a hora atual
                        mi = int(m_i)  # Minuto inicial como um inteiro para comparar com o minuto atual

                        hf = int(h_f )  # Hora final como um inteiro para comparar com a hora atual
                        mf = int(m_f)  # Minuto final como um inteiro para comparar com o minuto atual

                        h = hs.split(":")[0] # Hora e minutos atuais do sistema
                        m = hs.split(":")[1]
                        h = int(h)
                        m = int(m)

                        consta_no_banco = 1

                    # Calculos para verificar a compatibilidade do código dinamico com o horario

                        tabela = [601, 403, 820, 417, 217, 162, 684, 895, 797, 413, 577, 527, 921, 203, 565, 620, 369, 471, 316, 988, 387, 418, 643, 987, 297, 108, 396, 880, 436, 465, 899, 671, 422, 253, 765, 992, 259, 286, 932, 627, 474, 378, 894, 216, 594, 289, 258, 490, 647, 487, 409, 888, 221, 805, 535, 713, 363, 925, 964, 327]
                        tempo_validade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]

                        #print("Aqui o item vale",item)
                    
                        minutos_equivalentes = (tempo_validade[tabela.index(item)])-10 # minutos equivalentes a mesma posição em que foi encointrado o multiplicador valido
                        posicao_multiplicador = tabela.index(item)

                        print("Posição do multiplicador valido",tabela.index(item))
                        print("Minutos equivalente",minutos_equivalentes)

                        
                        confere_tabela = hora_inicio + timedelta(minutes = minutos_equivalentes) # Horario correspondente ao qr code usado

                        print("\nQr correspondente as",confere_tabela)

                        confere_tabela = str(confere_tabela)
                        confere_tabela_hora = int(confere_tabela.split(":")[0])
                        confere_tabela_minuto = int(confere_tabela.split(":")[1])
                        confere_tabela_segundos = 00

##                        print("Horario correspondente",confere_tabela_hora, confere_tabela_minuto, confere_tabela_segundos)
                                                                       
                        now = datetime.now()

                        horario_atual_hora = now.hour  # Estes valores são do tipo inteiro
                        horario_atual_minuto = now.minute
                        horario_atual_segundo = now.second

                        print("Horario atual no CMM ",hs)

                        if (hi > h): # se o horario inicial é menor do que a hora atual, ainda não foi liberado

                            print("Ainda não liberado\n")

                            pygame.mixer.music.load('mp3/207.mp3') # Fora do horario
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                time.sleep(0.1)

                            #acesso = 0
                            fora_do_horario = 1
                            consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                        # Aqui se compara o horario atual com o horario correspondente

                        if confere_tabela_hora == horario_atual_hora :

                            ja_mudou = 0

                            #print ("A hora correspondente ao QR code lido é igual a hora atual")

                            for i in range(1,11):

                                if confere_tabela_minuto == horario_atual_minuto:

                                    print ("Qr Code dentro dos 10 minutos validos")

                                    ja_mudou = 1

                                    fora_do_horario = 0
                                                                        
                                    break
                                
                                horario_atual_minuto = horario_atual_minuto - 1 # Verifica se esta dentro dos 10 minutos atuais

                            if ja_mudou == 0 and fora_do_horario == 0:

                                print("Este QRCode ja mudou")

                                pygame.mixer.music.load('mp3/212.mp3') # Este QRCode ja mudou 
                                pygame.mixer.music.play()
                                while pygame.mixer.music.get_busy():
                                    time.sleep(0.1)

                                fora_do_horario = 1

                                #time.sleep(1)
                        if confere_tabela_hora != horario_atual_hora and fora_do_horario == 0:

                            pygame.mixer.music.load('mp3/212.mp3') # Este QRCode ja mudou 
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                time.sleep(0.1)

                            fora_do_horario = 1

                                                   
                        
                        if (hf < h): # se o horario final é menor que o horario atual já expirou

                            print("Horario do QR Code já Expirou\n")

                            pygame.mixer.music.load('mp3/208.mp3') # Expirou
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                time.sleep(0.1)

                            time.sleep(3)

                            #acesso = 0
                            consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                        if (hf > h and fora_do_horario == 0): # se o horario final for maior que o horario atual, QR Code ainda válido

                            #print("Dentro do horario permitido\n")

                            pygame.mixer.music.load('mp3/188.mp3') # Acesso por QR Code
                            pygame.mixer.music.play()

                            
                            arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                            arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                            arquivo.close()
            
                            acesso = 1
                            consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                             
                            
                        if (hf == h): # se a hora final for a mesma da hora atual, verifica os minutos

                            if mf == 0:

                                print("Expirou a alguns minutos\n")

                                pygame.mixer.music.load('mp3/211.mp3') # Expirou
                                pygame.mixer.music.play()
                                while pygame.mixer.music.get_busy():
                                    time.sleep(0.1)

                                time.sleep(3)

                                #acesso = 0
                                consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final

                            if (mf != 0 and mf >= m): # se minutos finais forem menores do que minutos atuais, ainda válido

                                print("Dentro do horario, faltando",mf - m, "minutos")

                                pygame.mixer.music.load('mp3/188.mp3') # Acesso por QR Code
                                pygame.mixer.music.play()

                                arquivo = open("acesso_de_moradores.txt", "a+") # Escreve o evento no registro de acesso de moradores
                                arquivo.write("Data: " + data + " " + hs + " Evento: Acesso por QR Code " + nome + " Ap " + ap + " bloco " + bloco + "\n")
                                arquivo.close()
                
                                acesso = 1
                                consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                                              

                            if (mf != 0 and mf <= m):
                        
                                 print("Expirou\n")

                                 pygame.mixer.music.load('mp3/208.mp3') # Expirou
                                 pygame.mixer.music.play()
                                 while pygame.mixer.music.get_busy():
                                    time.sleep(0.1)

                                 time.sleep(3)

                                 #acesso = 0
                                 consta_no_banco = 0  # zera a variavel para não narrar a mensagem no final
                                 

                    if acesso == 1:

                        intertravamento(saidaA,saidaB,hs,data,"QR",nome)

                    if acesso == 0 and consta_no_banco == 1 and fora_do_horario == 0:

                        print("QR Code com data expirada")

                        pygame.mixer.music.load('mp3/210.mp3') # Data Expirada
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)

                        consulta = 1


                    # Aqui será necessário verificar se ja passou do horario final e avisar
                
                except Exception as e:
                    
                    print("Tipo de erro: " + str(e))

                
            if id_valido == 0:

                print("QR Code não cadastrado")

                pygame.mixer.music.load('mp3/189.mp3') # Não cadastrado
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)

            
            fora_do_horario = 0
