#!/usr/bin/env python3
# coding=UTF-8

import time
from expansores import Leitor, Expansor

s = Expansor()
l = Leitor()

while(1):


    s.liga_rele1_exp1()
    time.sleep(0.1)
    s.liga_rele2_exp1()
    time.sleep(0.1)
    s.liga_rele3_exp1()
    time.sleep(0.1)
    s.liga_rele4_exp1()

    time.sleep(2)

    s.desliga_rele1_exp1()
    time.sleep(0.1)
    s.desliga_rele2_exp1()
    time.sleep(0.1)
    s.desliga_rele3_exp1()
    time.sleep(0.1)
    s.desliga_rele4_exp1()

    

    print(l.leitor1_in1())
    time.sleep(0.1)
    print(l.leitor1_in2())
    time.sleep(0.1)
    print(l.leitor1_in3())
    time.sleep(0.1)
    print(l.leitor1_in4())
    time.sleep(0.1)


##    s.liga_rele1_exp2() 
##    s.liga_rele2_exp2()
##    s.liga_rele3_exp2()
##    s.liga_rele4_exp2()
##
##    time.sleep(2)
##
##    s.desliga_rele1_exp2() 
##    s.desliga_rele2_exp2()
##    s.desliga_rele3_exp2()
##    s.desliga_rele4_exp2()
##
    time.sleep(2)
