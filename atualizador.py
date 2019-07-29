from atualiza_monitor import Monitor
import threading
import time

def thread_monitor(): # Programa que mantem a conexão com o QR Code

    print("\nPrograma Monitor em execução\n")

    monitor = Monitor()

    while(1):        

        monitor.loop()
        time.sleep(0.4)
    
monitor = threading.Thread(target=thread_monitor)
monitor.start()   
