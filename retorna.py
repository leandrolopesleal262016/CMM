class Retorna:

    def __init__(self):

        self = self

    def entrada(self,b,entrada_requisitada):
            
        in1 = 0
        in2 = 0
        in3 = 0
        in4 = 0

        if (b == "1" or b =="3" or b =="5" or b =="7" or b =="9" or b =="b" or b =="d" or b =="f"):
            in1 = 1
        
        if (b == "2" or b =="3" or b =="6" or b =="7" or b =="a" or b =="b" or b =="e" or b =="f"):
            in2 = 1
        
        if (b == "4" or b =="5" or b =="6" or b =="7" or b =="c" or b =="d" or b =="e" or b =="f"):
            in3 = 1
        
        if (b == "8" or b =="9" or b =="a" or b =="b" or b =="c" or b =="d" or b =="e" or b =="f"):
            in4 = 1

        if entrada_requisitada == 'in1':

            entrada_requisitada = in1
            
        if entrada_requisitada == 'in2':

            entrada_requisitada = in2

        if entrada_requisitada == 'in3':

            entrada_requisitada = in3

        if entrada_requisitada == 'in4':

            entrada_requisitada = in4
       
        return(entrada_requisitada)
