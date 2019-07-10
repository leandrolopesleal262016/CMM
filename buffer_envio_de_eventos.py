def Buffer():

    socket.setdefaulttimeout(3) # limite em segundos para enviar o socket

    host = '172.20.1.5'  # '172.20.1.5' Host servidor  Moni
    port = 4010          # 4010 Porta máquina receptora

    print("Iniciou o programa buffer")

    enviado = 0

    while(1):

        b = open("/home/pi/CMM/buffer_eventos.txt","r")
        
        for line in b:

            ln = line
            evento = ln.replace("\n","")
            
            if evento != "": # Se houver alguma coisa para enviar

                print("Tentanto enviar o evento",evento)

                try:
        
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect ((host,port))

                    command = (evento + "\r") # ("7000 185808E30500008")  # Envia abriu portão da eclusa para a central de monitormento
                    s.send(str.encode(command))
                    reply = s.recv(1024)
                    print(reply.decode('utf-8'))
                    s.close()

                    enviado = 1                    
                                
                except Exception as err:
                    
                    print("Não conseguiu enviar o evento, sem conexão no momento")
                    s.close()

                    time.sleep(10)
                    break
                
                if enviado == 1:
                                               
                    print("Evento enviado ",evento)           

                    # Cria uma lista e adiciona todos as linhas encontradas em buffer.txt

                    lista = []

                    try:

                        txt = open("/home/pi/CMM/buffer_eventos.txt","r")
                        for l in txt:                        
                            l = l.replace("\n","") # Coloca na lista o evento ja editado
                            lista.append(evento)
                        
                        # Exclui o item enviado da lista

                        for i in lista:
                            if i == evento:
                                indice = lista.index(i)
                                print("Excluindo o evento",evento,"posicao",indice)
                                del(lista[indice])
                                nova_lista = lista
                        txt.close()

                        # Zera o arquivo buffer

                        tx = open("/home/pi/CMM/buffer_eventos.txt","w") 
                        tx.close()

                        # Reescreve o texto com a nova lista editada

                        txt = open("/home/pi/CMM/buffer_eventos.txt","a")
                        for i in nova_lista:
                            txt.write(i + "\n")
                        txt.close()    
                            
                        enviado = 0

                    except Exception as err:
                        print("Erro",err)
            
        b.close() # Fecha o arquivo de texto em modo leitura    
        time.sleep(1)
