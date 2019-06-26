import socket

host = '192.168.0.103' 
port = 5510          

try:
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect ((host,port))

    command = ("SET2\r")#("7000 185808E30500008")  # Envia abriu portão da eclusa para a central de monitormento
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))
    s.close()
    
                
except Exception as err:
    
    print("Não conseguiu enviar o evento ",err)
    s.close()


