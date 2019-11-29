#!/usr/bin/env python3
# coding=UTF-8

import time
from expansores import Leitor#, Expansor
import os


l = Leitor()

print("Teste Periodico dos expansores")


try:    

    
    print("\n")
    print("leitor 1 - in1",l.leitor1_in1())
    time.sleep(0.1)
    print("leitor 1 - in2",l.leitor1_in2())
    time.sleep(0.1)
    print("leitor 1 - in3",l.leitor1_in3())
    time.sleep(0.1)
    print("leitor 1 - in4",l.leitor1_in4())
    time.sleep(0.1)
    print("\n")
    
    time.sleep(0.1)

##    l.liga_rele3_exp1()
##    time.sleep(2)
##    l.desliga_rele3_exp1()

except Exception as err:

    print(err)


try:

    print("\n")
    
    print("leitor 2 - in1",l.leitor2_in1())
    time.sleep(0.1)
    print("leitor 2 - in2",l.leitor2_in2())
    time.sleep(0.1)
    print("leitor 2 - in3",l.leitor2_in3())
    time.sleep(0.1)
    print("leitor 2 - in4",l.leitor2_in4())

    time.sleep(0.1)        

##    l.liga_rele3_exp2()
##    time.sleep(2)
##    l.desliga_rele3_exp2()

        
##    time.sleep(0.1)


except Exception as err:

    print(err)

