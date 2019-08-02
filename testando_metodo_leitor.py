import metodo_leitor_modbus as l
import time
import threading


def thread_1():
    
    while(1):
        
        in1 = l.leitor16_in1()
        in2 = l.leitor16_in2()    
        in3 = l.leitor16_in3()
        in4 = l.leitor16_in4()
        print("expansor 16:",in1,in2,in3,in4)
        time.sleep(0.2)
        

def thread_2():
    
    while(1):
        
        in1 = l.leitor1_in1()
        in2 = l.leitor1_in2()    
        in3 = l.leitor1_in3()
        in4 = l.leitor1_in4()
        print("expansor 1:",in1,in2,in3,in4)
        time.sleep(0.2)

        

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

   
