class limpa:

    def _init__(self):

        self = self

    def string(self,i):

        try:

            i = str(i.split('\\')) 
            i = i.replace("x","")
            i = i.replace("y","")
            i = i.replace("'","")
            i = i.replace("`","")
            i = i.replace(" ","")
            i = i.replace("!","")
            i = i.replace("I","")
            i = i.replace('"',"")
            i = i.replace("[","")
            i = i.replace("]","")
            i = i.replace(";","")
            i = i.replace(":","")
            i = i.replace("-","")
       
            return(i)

        except:
            
            pass # Erro na classe limpa string

class Filtro(limpa):

    def __init__(self):
        
        self.limpa = limpa()

    def mdl1(self,i):
        
        if i != b'':

            i = self.limpa.string(i) 
            
            try:
                
                i= i.split(",")
                                
                i = (i[4])  # Obtem da lista o byte referente ao estado das entradas                    
                b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                                        
                if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                    b = "5"
                if i == "04y": # Formatações devido ao retorno do byte com representação em ascii
                    b = "4"
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
                if i == "":
                    b = "d"
                if i == "0eL":
                    b = "e"
                if i == "rM":
                    b = "d"
                if i == "01H":                    
                    b = "1"
                                             
                return(b)
            
            except:

                pass #log("erro fitro mdl1")
                

    def mdl2(self,i):

        if i != b'':                
            
            i = self.limpa.string(i) 
            
            try:
                
                i= i.split(",")
                                
                i = (i[4])  # Obtem da lista o byte referente ao estado das entradas  
                  
                b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                        
                if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
                if i == "":
                    b = "d"
                if i == "0eL":
                    b = "e"
                if i == "rM":
                    b = "d"                            
                
                return(b)
            
            except:

                pass #log("erro fitro mdl2")                

    def mdl3(self,i):

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])  # Obtem da lista o byte referente ao estado das entradas                    
            b = (i[-1]) # Obtem do byte a metade que contem os bits que representa as entradas
                                
            if i == "05a": # Formatações devido ao retorno do byte com representação em ascii
                b = "5"            
            if i == "ta":
                b = "9"
            if i == "n":
                b = "a"
            if i == "r":
                b = "d"
            if i == "":
                b = "d"
            if i == "0eL":
                b = "e"
            if i == "rM":
                b = "d"
            if i == "01a":
                b = "1"
            if i == "053":
                b = "5"
            if i == "062":
                b = "6"
            if i == "t6":
                b = "9"
            if i == "n7":
                b = "a"
            if i == "ra":
                b = "d"
                                    
            return(b)
        
        except:
            
            pass #log("erro fitro mdl3")            

    def mdl4(self,i):       

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])               
            b = (i[-1])             
                                
            if i == "05aG": 
                b = "5"
            if i == "06F": 
                b = "6"
            if i == "taB": 
                b = "9"
            if i == "nC": 
                b = "a"
            if i == "r": 
                b = "d"
            
                                    
            return(b)
        
        except:            
            
            pass #log("erro fitro mdl4")
            

    def mdl5(self,i):       

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])               
            b = (i[-1])            
                                
            if i == "01a": 
                b = "1"
            if i == "02y": 
                b = "2"
            if i == "t": 
                b = "9"
            if i == "n": 
                b = "a"
            if i == "ra}": 
                b = "d"
            if i == "0e|": 
                b = "e"                        
                                    
            return(b)
        
        except:            
            
            pass #log("erro fitro mdl5")

    def mdl6(self,i):       

        if i != "b''":                
            
            i = self.limpa.string(i) 

        try:
            
            i= i.split(",")
                            
            i = (i[4])               
            b = (i[-1])
                                
            if i == "01a<": 
                b = "1"
            if i == "02=": 
                b = "2"
            if i == "t": 
                b = "9"
            if i == "n": 
                b = "a"
            if i == "ra9": 
                b = "d"
            if i == "0e8": 
                b = "e"                        
                                    
            return(b)
        
        except:

            pass #log("erro fitro mdl6")

    def mdl7(self,i):

        if i != "b''":
                    
            i = self.limpa.string(i)

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                
                if i == "05a": 
                    b = "5"            
                if i == "ta":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "r":
                    b = "d"
               
                return (b)                            

            except:

                pass #log("erro fitro mdl7")

                
    def mdl8(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])               

                if i == "01c":
                    b = "1"
                if i == "02#":
                    b = "2"                
                if i == "05b": 
                    b = "5"            
                if i == "tb":
                    b = "9"
                if i == "n":
                    b = "a"
                if i == "rc":
                    b = "d"
                if i == "0e#":
                    b = "e"
               
                return (b)                            

            except:

                pass #log("erro fitro mdl9")
                

    def mdl9(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01b(":
                    b = "1"
                if i == "02)\\":
                    b = "2"                
                if i == "05c": 
                    b = "5"
                if i == "06#": 
                    b = "6"
                if i == "tc":
                    b = "9"
                if i == "n#":
                    b = "a"
                if i == "rb-":
                    b = "d"
                              
                return (b)                            

            except:

                pass #log("erro fitro mdl9")
                

    def mdl10(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01b(":
                    b = "1"
                if i == "02)\\":
                    b = "2"                
                if i == "05c": 
                    b = "5"
                if i == "06#": 
                    b = "6"
                if i == "tc":
                    b = "9"
                if i == "n#":
                    b = "a"
                if i == "rb-":
                    b = "d"
                              
                return (b)                            

            except:

                pass #log("erro fitro mdl10")
                

    def mdl11(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                if i == "01c":
                    b = "1"                    
                if i == "02#":                    
                    b = "2"                    
                if i == "05bS": 
                    b = "5"                    
                if i == "06R\\": 
                    b = "6"                    
                if i == "tbV":
                    b = "9"                    
                if i == "nW\\":
                    b = "a"                    
                if i == "rc":
                    b = "d"                    
                if i == "0e#":
                    b = "e"
                              
                return (b)                            

            except:

                pass #log("erro fitro mdl11")
                

    def mdl12(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                

                if i == "01b":
                    b = "1"      
                if i == "05c\\": 
                    b = "5"                    
                if i == "06#&": 
                    b = "6"                    
                if i == "tc\\":
                    b = "9"                    
                if i == "n##":
                    b = "a"                    
                if i == "rb":
                    b = "d"                    
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl12")
                

    def mdl13(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])

                if i == "01c":
                    b = "1"
                if i == "02#":
                    b = "2" 
                if i == "05b": 
                    b = "5"      
                if i == "tb":
                    b = "9"                    
                if i == "n":
                    b = "a"                    
                if i == "rc":
                    b = "d"
                if i == "0e#":
                    b = "e"                
                                              
                return (b)                            

            except:
                
                pass #log("erro fitro mdl13")

    def mdl14(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01c":
                    b = "1"
                if i == "02#":
                    b = "2"
                if i == "04":                    
                    b = "4" 
                if i == "05b": 
                    b = "5"
                if i == "06":
                    b = "6"
                if i == "07":
                    b = "7"
                if i == "06":
                    b = "6" 
                if i == "tb":
                    b = "9"                    
                if i == "n":
                    b = "a"
                if i == "0b":
                    b = "b"
                if i == "0c":
                    b = "c" 
                if i == "rcY":
                    b = "d"
                if i == "0e#X":
                    b = "e"                
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl14")
                

    def mdl15(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])
                
                if i == "01b":
                    b = "1"               
                if i == "05cc": 
                    b = "5"
                if i == "06#b": 
                    b = "6"
                if i == "tcf":
                    b = "9"                    
                if i == "n#g":
                    b = "a"                    
                if i == "rb":
                    b = "d" 
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl15")
                

    def mdl16(self,i):

        if i != "b''":
        
            i = self.limpa.string(i) 

            try:

                i= i.split(",")
                    
                i = (i[4])  
                b = (i[-1])                

                if i == "01et":
                    b = "1"               
                if i == "02%u": 
                    b = "2"
                if i == "05d": 
                    b = "5"
                if i == "06$":
                    b = "6"                    
                if i == "td":
                    b = "9"                    
                if i == "n$":
                    b = "a"
                if i == "req":
                    b = "d"                    
                if i == "0e%p":
                    b = "e"
                                              
                return (b)                            

            except:

                pass #log("erro fitro mdl16")
