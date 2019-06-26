
def LeModbus(port):  
    packet = bytearray()  
    packet.append(0x01) # Endereço dip switch 
    packet.append(0x03) # Comando (entrada ou saida) 
    packet.append(0x01)  
    packet.append(0x90)  
    packet.append(0x00)  
    packet.append(0x0D)  
    packet.append(0x85)  
    packet.append(0xDE)  
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    time.sleep(0.1)  
    port.write(packet)  
    time.sleep(0.01)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    time.sleep(0.5)  
    bytesToRead = port.inWaiting()  
    in_bin = port.read(bytesToRead)

    print(packet)

    tag = ""   
    hexa = []   
    conv = ""   
    for i in range(len(in_bin)):  
        tag += '%x' % ord(in_bin[i])  
     
    for i in range(6,12,2):  
        hexa.append(tag[i:i+2])  
     
    for i in range(len(hexa)):  
        conv += str(hexa[i])  
         
    try:  
        if (int(conv) == 0):  
            return ""   
        else:  
            GerarLog("String Conversor: {}".format(tag), "String Tag")  
            return conv  

    except:  
        return "" 

    print("tag",tag)
    print("hexa",hexa)
    print("conv",conv)
    
    return ""
