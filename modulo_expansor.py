def LeModbus(port):  
    packet = bytearray()  
    packet.append(0x01)  
    packet.append(0x03)  
    packet.append(0x01)  
    packet.append(0x90)  
    packet.append(0x00)  
    packet.append(0x0D)  
    packet.append(0x85)  
    packet.append(0xDE)  
    gpio.output(11, gpio.HIGH)  
    gpio.output(12, gpio.HIGH)  
    time.sleep(0.1)  
    port.write(packet)  
    time.sleep(0.01)  
    gpio.output(11, gpio.LOW)  
    gpio.output(12, gpio.LOW)  
    time.sleep(0.5)  
    bytesToRead = port.inWaiting()  
    in_bin = port.read(bytesToRead)  

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
     
    return "" 
