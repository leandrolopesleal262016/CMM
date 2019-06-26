from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
from biblioteca_CMM_oficial import Rele,Narrador,Temperatura,Email,Clima
import time
import RPi.GPIO as GPIO
import threading # Modulo superior Para executar as threads
import os     # Executa comandos do sistema operacional Ex.: os.system('sudo reboot now'))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)

A = GPIO.input(4) # ENTRADAS NÃO FOTOACOPLADAS (As entradas A B C D então normalmente em nivel lógico HIGH (1))
B = GPIO.input(27)
C = GPIO.input(22)
D = GPIO.input(10)

hs = time.strftime("%H:%M:%S") # Hora completa para registro de Log
h = int(time.strftime('%H'))
data = time.strftime('%d/%m/%y')

global entradas
entradas = [" --- ","A", "B", "C", "D", "IN1", "IN2", "IN3", "IN4", "IN5", "IN6", "IN7", "IN8"]
global mp3
                    

def qr_code():        

    print("Chama a rotina do qr code aqui")

    file = open("start_qrcode.txt","w")
    file.write("1")
    file.close()

    
def thread_start_qr():

    while(1):

        file = open("start_qrcode.txt","r")
        texto = file.read()
        file.close

        if texto == "0":
            
            pass
        
        if texto == "1":
            
            file = open("start_qrcode.txt","w")
            file.write("0")
            file.close()

            os.system("python3 /home/pi/IHM/IHM_qrcode.py")

        time.sleep(1)
    


############################ INICIA AS CLASSES DA Biblioteca_CMM_Bravas  ########################################

rele = Rele() # inicia a classe rele com port A em 0
narrador = Narrador()
temperatura = Temperatura()
email = Email()
clima = Clima()
##    
##    qrcode = Qrcode() # Instancia a classe do leitor de qrcode
##wiegand = Wiegand()
##rele_qr = Rele_qr() # Instanciar loclamente com o IP do leitor para acionamento do rele do equipamento
## Ex. rele_qr = Rele_qr("172.20.9.5",5000) # Conecta com o Qrcode deste endereço para acionamento do rele e leitura da entrada auxiliar
verifica = threading.Thread(target=thread_start_qr)
verifica.start()

################################  GUI (Graphic User Interface) ####################################

# Configurações da janela

janela = Tk()
janela.title("CMM Controladora Multi Módulos")
janela.geometry("700x520+20+50")
janela.maxsize(width=700, height=530) # Limita o tamaho maximo
janela.minsize(width=700, height=530) # Limita o tamanho minimo

############################# Saida do programa ###############################

def on_closing():
        
        if messagebox.askokcancel("Sair", "Você gostaria de sair da aplicação?"):

            try:

                sock.close()

            except:

                print("Não havia nenhuma conexão estabelecida")

            finally:
                janela.destroy()

temperatura = Temperatura()

class Monitoramento(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        menubar = Menu(master)
        self.config(menu=menubar)
        self.title('Monitoramento Entradas / Saídas')
        self.geometry('400x300')
        self.maxsize(width=400, height=300) # Limita o tamaho maximo
        self.minsize(width=400, height=300) # Limita o tamanho minimo

        imagem = PhotoImage(file='/home/pi/img/CASE_CMM.png')
        label = Label(self, image = imagem)
        label.pack()#fill = BOTH, expand = 1)

        ligado =  PhotoImage(file='/home/pi/img/ligado.png')
        
        out1 = Label(self,image = ligado)
        out1.configure(background = "black")
        out1.place(x=48,y=95)
        
        out2 = Label(self,image = ligado)
        out2.configure(background = "black")
        out2.place(x=79,y=95)

        out3 = Label(self,image = ligado)
        out3.configure(background = "black")
        out3.place(x=111,y=95)

        out4 = Label(self,image = ligado)
        out4.configure(background = "black")
        out4.place(x=143,y=95)

        out5 = Label(self,image = ligado)
        out5.configure(background = "black")
        out5.place(x=174,y=95)

        out6 = Label(self,image = ligado)
        out6.configure(background = "black")
        out6.place(x=206,y=95)

        out7 = Label(self,image = ligado)
        out7.configure(background = "black")
        out7.place(x=238,y=95)

        out8 = Label(self,image = ligado)
        out8.configure(background = "black")
        out8.place(x=270,y=95)

        out9 = Label(self,image = ligado)
        out9.configure(background = "black")
        out9.place(x=348,y=23)
        
        out10 = Label(self,image = ligado)
        out10.configure(background = "black")
        out10.place(x=348,y=37)
        
        out11 = Label(self,image = ligado)
        out11.configure(background = "black")
        out11.place(x=348,y=51)
        
        out12 = Label(self,image = ligado)
        out12.configure(background = "black")
        out12.place(x=348,y=65)
        
        out13 = Label(self,image = ligado)
        out13.configure(background = "black")
        out13.place(x=348,y=79)

        out14 = Label(self,image = ligado)
        out14.configure(background = "black")
        out14.place(x=348,y=93)

        out15 = Label(self,image = ligado)
        out15.configure(background = "black")
        out15.place(x=348,y=107)

        out16 = Label(self,image = ligado)
        out16.configure(background = "black")
        out16.place(x=348,y=121)

        in8 = Label(self,image = ligado)
        in8.configure(background = "black")
        in8.place(x=348,y=158)

        in7 = Label(self,image = ligado)
        in7.configure(background = "black")
        in7.place(x=348,y=172)

        in6 = Label(self,image = ligado)
        in6.configure(background = "black")
        in6.place(x=348,y=186)

        in5 = Label(self,image = ligado)
        in5.configure(background = "black")
        in5.place(x=348,y=200)

        in4 = Label(self,image = ligado)
        in4.configure(background = "black")
        in4.place(x=348,y=214)

        in3 = Label(self,image = ligado)
        in3.configure(background = "black")
        in3.place(x=348,y=228)

        in2 = Label(self,image = ligado)
        in2.configure(background = "black")
        in2.place(x=348,y=242)

        in1 = Label(self,image = ligado)
        in1.configure(background = "black")
        in1.place(x=348,y=256)

        D = Label(self,image = ligado)
        D.configure(background = "black")
        D.place(x=198,y=250)

        C = Label(self,image = ligado)
        C.configure(background = "black")
        C.place(x=169,y=250)

        B = Label(self,image = ligado)
        B.configure(background = "black")
        B.place(x=140,y=250)

        A = Label(self,image = ligado)
        A.configure(background = "black")
        A.place(x=111,y=250)
 
        self.mainloop()



class Setup(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.title("CMM Controladora Multi Módulos")
        self.geometry("700x520+400+50")
        self.maxsize(width=700, height=530) # Limita o tamaho maximo
        self.minsize(width=700, height=530) # Limita o tamanho minimo

        # Configurações do menu superior

        menubar = Menu(master)
        self.config(menu=menubar)

        filemenu1 = Menu(menubar,tearoff=0) # tearoff=0 para os menus não serem "flutuantes"
        filemenu2 = Menu(menubar,tearoff=0)
        filemenu3 = Menu(menubar,tearoff=0)

        menubar.add_cascade(label='Arquivo', menu=filemenu1) # Associa o menu a barra
        menubar.add_cascade(label='QR Code', menu=filemenu2)
        menubar.add_cascade(label='Sobre', menu=filemenu3)

        filemenu1.add_command(label='Abrir...', accelerator="Teste+A")#,command=Open)
        filemenu1.add_command(label='Salvar como...')#, command=Save)
        filemenu1.add_separator() # Adiciona um separador entre as opções
        filemenu1.add_command(label='Sair')#, command=Quit)
        filemenu2.add_command(label='Conectar com QR Code', command=qr_code)
        filemenu3.add_command(label='Ajuda')#, command=Help)

        ############################# Background ######################################

        imagem = PhotoImage(file='/home/pi/img/SEA.png')
        label = Label(self, image = imagem)
        label.pack()#fill = BOTH, expand = 1)

        #############################  Labels  ########################################

        Font_label = ("Arial",10,"bold italic")
        font1 = ("Arial", 8, "bold")
        font2 = ("Helvetica", 10,"italic")
        font3 = ("Helvetica", 8,"italic")

        # Labels pontos magneticos

        lb_saida = Label(self,bg="black",fg="white",font=font3, text = "SAIDA")
        lb_saida.place(x=125, y=80)

        lb_pm1 = Label(self,bg="black",fg="white", font=font3, text = "PM")
        lb_pm1.place(x=200, y=80)

        lb_qbv = Label(self,bg="black",fg="white",font=font3, text = "Quebra de vidro")
        lb_qbv.place(x=265, y=80)

        lb_cx = Label(self,bg="black",fg="white",font=font3, text = "PM Quadro")
        lb_cx.place(x=275, y=135)

        lb_qd = Label(self,bg="black",fg="white",font=font3, text = "Queda de Energia")
        lb_qd.place(x=263, y=195)


        # Labels dos portões

        lb_pm1 = Label(self, bg="black",fg="white",text = "Portão da Rua")
        lb_pm1.place(x=10, y=100)

        lb_pm1 = Label(self, bg="black",fg="white",text = "Portão Eclusa")
        lb_pm1.place(x=10, y=130)

        lb_pm1 = Label(self, bg="black",fg="white",text = "Portão Acesso")
        lb_pm1.place(x=10, y=160)

        lb_pm1 = Label(self,bg="black",fg="white", text = " Hall Entrada")
        lb_pm1.place(x=10, y=190)

        lb_pm1 = Label(self, bg="black",fg="white",text = " Hall  Saída")
        lb_pm1.place(x=10, y=220)

        # Label Pulso

        lb_pulso = Label(self ,bg="black",fg="white",font=font3, text = "Pulso")
        lb_pulso.place(x=488, y=80)

        lb_pulso1 = Label(self, bg="black",fg="white", font=font3, text = "Pulso")
        lb_pulso1.place(x=653, y=80)

        # Gravador de voz

        lb1 = Label (self, text = "Insira o texto a ser gravado",bg="black",fg="white",font = Font_label)
        lb1.place(x=10, y=5)

        lb_nome = Label (self, text = "Nome",bg="black",fg="white",font=font2)
        lb_nome.place(x=200, y=57)

        # Temperatura CPU
        
##        temp = str(temperatura.cpu())
##        lb_temp_cpu = Label (self, text = ("Temp CPU " + temp + "°C") ,bg="black",fg="white",font = font2)
##        lb_temp_cpu.place(x=585,y=18)

        def temp_cpu():

            temp = str(temperatura.cpu())
            lb_temp_cpu = Label (self, text = ("Temp CPU " + temp + "°C") ,bg="black",fg="white",font = font2)
            lb_temp_cpu.place(x=585,y=18)

            self.after(2000,temp_cpu)

        temp_cpu()

        # Label Entrada acionamentos dos portões

        lb_social = Label (self, text = "Abre Social" ,bg="black",fg="white")
        lb_social.place(x=370, y=222)

        lb_social = Label (self, text = "Abre Eclusa" ,bg="black",fg="white")
        lb_social.place(x=370, y=256)

        lb_social = Label (self, text = "Abre Hall 1" ,bg="black",fg="white")
        lb_social.place(x=370, y=293)

        lb_social = Label (self, text = "Abre Hall 2" ,bg="black",fg="white")
        lb_social.place(x=370, y=330)    

        # Label Feed back do programa (rodapé da self)

        lb_log = Label (self, text = "Feed back do programa",width=96,font = font2,padx=5,relief = RIDGE, bd=1, anchor = W) # GROOVE, RIDGE, FLAT
        lb_log.place(x=5, y=475)

        ####################################  Caixa de entrada #######################################

        ed1 = Entry(self, width=54)  # Caixa de texto
        ed1.place(x=10, y=30)

        ed_nome = Entry(self, width=15)  # Caixa de texto
        ed_nome.place(x=248, y=58)

        cb1 = StringVar()
        cb2 = StringVar()
        cb3 = StringVar()
        cb4 = StringVar()
        cb5 = StringVar()
        cb_qbv = StringVar()
        cb_cx = StringVar()
        cb_qd = StringVar()

        # Combobox Entradas (IN1, IN2, ...)

        def verifica_disponibilidade_entrada():

            i1 = cb1.get()
            i2 = cb2.get()
            i3 = cb3.get()
            i4 = cb4.get()
            i5 = cb5.get()
            i6 = cb_qbv.get()
            i7 = cb_cx.get()
            i8 = cb_qd.get()

            select(i1,i2,i3,i4,i5,i6,i7,i8)
            
            for i in select: # Verfica se este item esta disponivel 

                if item == i:
                    print("disponivel para uso")
                    pos = entradas.index(i)
                    del(entradas[pos])
                    print(entradas)
                    
                else:
                    print ("Entada já foi usada") 
                    messagebox.showerror("Não disponível","Entrada ja está sendo usada")
                    
                

        def atualiza_entradas(c):

            i1 = cb1.get()
            i2 = cb2.get()
            i3 = cb3.get()
            i4 = cb4.get()
            i5 = cb5.get()
            i6 = cb_qbv.get()
            i7 = cb_cx.get()
            i8 = cb_qd.get()

    ##        if c == 1:
    ##            cadastra("entrada","in1",i1)
    ##        if c == 2:
    ##            cadastra("entrada","in2",i2)
    ##        if c == 3:
    ##            cadastra("entrada","in3",i3)
    ##        if c == 4:
    ##            cadastra("entrada","in4",i4)
    ##        if c == 5:
    ##            cadastra("entrada","in5",i5)
    ##        if c == 6:
    ##            cadastra("entrada","in6",i6)
    ##        if c == 7:
    ##            cadastra("entrada","in7",i7)
    ##        if c == 8:
    ##            cadastra("entrada","in8",i8)
    ##       
            
        # Combobox das entradas Ponto Magnético

        cbox1 = ttk.Combobox(self, width=4 ,values= entradas,state='readonly',textvariable=cb1,)
        cbox1.place(x=190, y=100)
        cbox1.set("A")
        cbox1.bind('<<ComboSelected>>',atualiza_entradas(1))

        cbox2 = ttk.Combobox(self, width=4 ,values= entradas,state='readonly',textvariable=cb2)
        cbox2.place(x=190, y=130)
        cbox2.set("B")
        cbox2.bind('<<ComboSelected>>',atualiza_entradas(2))

        cbox3 = ttk.Combobox(self, width=4 ,values= entradas,state='readonly',textvariable=cb3)
        cbox3.place(x=190, y=160)
        cbox3.set("   ")
        cbox3.bind('<<ComboSelected>>',atualiza_entradas(3)) 

        cbox4 = ttk.Combobox(self, width=4 ,values= entradas,state='readonly',textvariable=cb4)
        cbox4.place(x=190, y=190)
        cbox4.set("   ")
        cbox4.bind('<<ComboSelected>>',atualiza_entradas(4)) 

        cbox5 = ttk.Combobox(self, width=4 ,values= entradas,state='readonly',textvariable=cb5)
        cbox5.place(x=190, y=220)
        cbox5.set("   ")
        cbox5.bind('<<ComboSelected>>',atualiza_entradas(5)) 

        cbox_qbv = ttk.Combobox(self, width=5 ,values= entradas,state='readonly',textvariable=cb_qbv)
        cbox_qbv.place(x=280, y=100)
        cbox_qbv.set("   ")
        cbox_qbv.bind('<<ComboSelected>>',atualiza_entradas(6)) 

        cbox_cx = ttk.Combobox(self, width=5 ,values= entradas,state='readonly',textvariable=cb_cx)
        cbox_cx.place(x=280, y=160)
        cbox_cx.set("   ")
        cbox_cx.bind('<<ComboSelected>>',atualiza_entradas(7)) 

        cbox_qd = ttk.Combobox(self, width=5 ,values= entradas,state='readonly',textvariable=cb_qd)
        cbox_qd.place(x=280, y=220)
        cbox_qd.set("   ")
        cbox_qd.bind('<<ComboSelected>>',atualiza_entradas(8))

        # Combobox Saidas Portões (OUT1, OUT2, ...)

        c10 = StringVar()
        c20 = StringVar()
        c30 = StringVar()
        c40 = StringVar()
        c50 = StringVar()

        global saidas
        saidas=[" --- ","OUT1", "OUT2", "OUT3", "OUT4", "OUT5", "OUT6", "OUT7", "OUT8", "OUT9", "OUT 10", "OUT 11", "OUT 12", "OUT 13", "OUT 14", "OUT 15", "OUT 16"]

        cbox10 = ttk.Combobox(self, width=6 , values = saidas,state='readonly',textvariable=c10)
        cbox10.set(" --- ")
        cbox10.place(x=115, y=100)

        cbox20 = ttk.Combobox(self, width=6 ,values = saidas,state='readonly',textvariable=c20)
        cbox20.set(" --- ")
        cbox20.place(x=115, y=130)

        cbox30 = ttk.Combobox(self, width=6 ,values = saidas,state='readonly',textvariable=c30)
        cbox30.set(" --- ")
        cbox30.place(x=115, y=160)

        cbox40 = ttk.Combobox(self, width=6 ,values = saidas,state='readonly',textvariable=c40)
        cbox40.set(" --- ")
        cbox40.place(x=115, y=190)

        cbox50 = ttk.Combobox(self, width=6 ,values = saidas,state='readonly',textvariable=c50)
        cbox50.set(" --- ")
        cbox50.place(x=115, y=220)

        # Combobox LIGA Saidas especificadas

        c60 = StringVar()
        c70 = StringVar()
        c80 = StringVar()
        c100 = StringVar()
        c110 = StringVar()
        c120 = StringVar()

        cbox60 = ttk.Combobox(self,textvariable=c60, state='readonly', width=6 ,values=saidas)
        cbox60.set(" --- ")
        cbox60.place(x=420, y=105)

        cbox70 = ttk.Combobox(self,textvariable=c70, state='readonly', width=6 ,values=saidas)
        cbox70.set(" --- ")
        cbox70.place(x=420, y=140)

        cbox80 = ttk.Combobox(self,textvariable=c80, state='readonly', width=6 ,values=saidas)
        cbox80.set(" --- ")
        cbox80.place(x=420, y=180)


        cbox100 = ttk.Combobox(self,textvariable=c100, state='readonly', width=6 ,values=saidas)
        cbox100.set(" --- ")
        cbox100.place(x=590, y=105)

        cbox110 = ttk.Combobox(self,textvariable=c110, state='readonly', width=6 ,values=saidas)
        cbox110.set(" --- ")
        cbox110.place(x=590, y=140)

        cbox120 = ttk.Combobox(self,textvariable=c120, state='readonly', width=6 ,values=saidas)
        cbox120.set(" --- ")
        cbox120.place(x=590, y=180)


        # Luz Eclusa

        cbox60 = ttk.Combobox(self, width=6 ,values=saidas ,state='readonly')
        cbox60.set(" --- ")
        cbox60.place(x=260, y=331)

        # Combobox dos players MP3 (play1, play2, ...)

        mp3 = os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3
        
        

        self.play1 = StringVar()
        self.play2 = StringVar()
        self.play3 = StringVar()
        self.play4 = StringVar()
        self.play5 = StringVar()
        self.play6 = StringVar()
        self.play7 = StringVar()
        self.play8 = StringVar()

        self.mp3= os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3        
        
        self.cbbox_play4 = ttk.Combobox(self,textvariable=self.play4, width=6 ,state='readonly',values=entradas)
        self.cbbox_play4.set(" --- ")
        self.cbbox_play4.place(x=455,y=331)

        self.cbbox_play3 = ttk.Combobox(self,textvariable=self.play3, width=6 ,state='readonly',values=entradas)
        self.cbbox_play3.set(" --- ")
        self.cbbox_play3.place(x=455,y=294)

        self.cbbox_play2 = ttk.Combobox(self,textvariable=self.play2, width=6 ,state='readonly',values=entradas)
        self.cbbox_play2.set(" --- ")
        self.cbbox_play2.place(x=455,y=257)

        self.cbbox_play1 = ttk.Combobox(self,textvariable=self.play1, width=6 ,state='readonly',values=entradas)
        self.cbbox_play1.set(" --- ")
        self.cbbox_play1.place(x=455,y=220)

        self.cbbox_play8 = ttk.Combobox(self,textvariable=self.play8, width=11 ,state='readonly',values=self.mp3)
        self.cbbox_play8.place(x=590,y=331)

        self.cbbox_play7 = ttk.Combobox(self,textvariable=self.play7, width=11 ,state='readonly',values=self.mp3)
        self.cbbox_play7.place(x=590,y=294)

        self.cbbox_play6 = ttk.Combobox(self,textvariable=self.play6, width=11 ,state='readonly',values=self.mp3)
        self.cbbox_play6.place(x=590,y=257)

        self.cbbox_play5 = ttk.Combobox(self,textvariable=self.play5, width=11 ,state='readonly',values=self.mp3)
        self.cbbox_play5.place(x=590,y=220)
           
        mp3 = os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3

        #################### Metodos e funções usadas dentro da interface ###########################

        def gravar():

            lb_log["text"] = "Gravando o texto..."
            self.update() # Atualiza a self principal
            msg = ed1.get()
            nome = ed_nome.get()

            if nome != "":
            
                try:

                    lb_log["text"] = "Ouça como ficou..."
                    narrador.gravar(msg,nome)
                    lb_log["text"] = ("Terminou de narrar o texto gravado em " + nome + '.mp3')
                    mp3 = os.listdir('/home/pi/MP3') # Coloca na variavel mp3 o nome dos arquivos da pasta MP3
                    self.update()
                    #cbox.plays(mp3)
    ##                cbox = Cbox()
                    
                except Exception as err:
                    
                    lb_log["text"] = ("Não conseguiu gravar o texto",err)
                    print(err)

            else:

                messagebox.showinfo("Nome do arquivo","Insira o nome que terá o seu\n         arquivo mp3")
                lb_log["text"] = "Insira o nome que tera sua mensagem mp3"

                
        def tocar(a):            
                    
            print(a)

            if a == 1:
                 p1 = cbox.get_cbox(1)
                 print("p1 ",p1)
            if a == 2:
                 p1 = cbox.get_cbox(2)
                 print("p1 ",p1)
            if a == 3:
                 p1 = cbox.get_cbox(3)
                 print("p1 ",p1)
            if a == 4:
                 p1 = cbox.get_cbox(4)
                 print("p1 ",p1)
            if a == 5:
                 p1 = cbox.get_cbox(5)
                 print("p1 ",p1)
            if a == 6:
                 p1 = cbox.get_cbox(6)
                 print("p1 ",p1)
            if a == 7:
                 p1 = cbox.get_cbox(7)
                 print("p1 ",p1)
            if a == 8:
                 p1 = cbox.get_cbox(8)
                 print("p1 ",p1)    
           
            print(os.system("mpg123 /home/pi/MP3/" + p1 ))        
       
        ################################# GIFS ######################################

    ##    class AnimatedGif(object):
    ##        
    ##        """ Animated GIF Image Container. """
    ##        def __init__(self, image_file_path):
    ##            # Read in all the frames of a multi-frame gif image.
    ##            self._frames = []
    ##
    ##            frame_num = 0  # Number of next frame to read.
    ##            while True:
    ##                try:
    ##                    frame = PhotoImage(file=image_file_path,
    ##                                       format="gif -index {}".format(frame_num))
    ##                except TclError:
    ##                    break
    ##                self._frames.append(frame)
    ##                frame_num += 1
    ##
    ##        def __len__(self):
    ##            return len(self._frames)
    ##
    ##        def __getitem__(self, frame_num):
    ##            return self._frames[frame_num]
    ##
    ##
    ##    def update_label_image(label, ani, ms_delay, frame_num):
    ##        global cancel_id
    ##        label.configure(image=ani[frame_num])
    ##        frame_num = (frame_num+1) % len(ani)
    ##        cancel_id = self.after(
    ##            ms_delay, update_label_image, label, ani, ms_delay, frame_num)
    ##
    ##    def enable_animation():
    ##
    ##        bt_start["text"] = "Stop"
    ##        global cancel_id
    ##        if cancel_id is None:  # Animation not started?
    ##            ms_delay = 6000 // len(ani)  # Show all frames in 1000 ms.
    ##            cancel_id = self.after(
    ##                ms_delay, update_label_image, animation, ani, ms_delay, 0)
    ##
    ##        
    ##    def cancel_animation():
    ##
    ##        bt_start["text"] = "Start"
    ##        global cancel_id
    ##        if cancel_id is not None:  # Animation started?
    ##            self.after_cancel(cancel_id)
    ##            cancel_id = None
    ##
    ##    global cancel_id
    ##    cancel_id = None
    ##    
    ##    ani = AnimatedGif("/home/pi/gifs/globo.gif")    
    ##
    ##    animation = Label(image=ani[0],bg='black')  # Display first frame initially.
    ##    animation.place(x=603,y=360)

        #############################################################################

        
        def atualiza(): # Atualiza informações a cada 2 segundos
                
            temp = str(temperatura.cpu())

            text = ("Temp CPU " + temp + "°C")
            lb_temp_cpu["text"] = text
            
            self.after(2000,atualiza)
                        

        ############### Metodos para iniciar funções no tkinter  ######################

        def start_stop():

            bt = bt_start["text"]

            if bt == "Start":  # aqui se chama todas as rotinas que iniciam com start

                lb_log["text"] = "Programa em execução..."

                self.after(100, enable_animation) # Chama a rotina animação da gif depois de 0.1 segundo
                self.after(200, atualiza)         # Chama a rotina atualiza depois de 0.2 segundos

            if bt == "Stop": # aqui se chama todas as rotinas que iniciam com stop

                lb_log["text"] = "Parou a execução do programa"

                self.after(100, cancel_animation)


        def liga(p): # Muda a função do botão de liga para pulso

            if p == 1: # De qual checkbox veio       
                p1 = pulso1.get() # obtem o valor da variavel referente ao checkbox
                if p1 == 1: # Se o valor for 1 escreve PULSO no botão se for 0 esvreve ON
                    bt_rl1["text"] = "PULSO"            
                else:
                    bt_rl1["text"] = "ON"

            if p == 2:        
                p2 = pulso2.get()
                if p2 == 1:
                    bt_rl2["text"] = "PULSO"            
                else:
                    bt_rl2["text"] = "ON"    
            
            if p == 3:        
                p3 = pulso3.get()
                if p3 == 1:
                    bt_rl3["text"] = "PULSO"            
                else:
                    bt_rl3["text"] = "ON"

            if p == 4:        
                p4 = pulso4.get()
                if p4 == 1:
                    bt_rl4["text"] = "PULSO"            
                else:
                    bt_rl4["text"] = "ON"

            if p == 5:        
                p5 = pulso5.get()
                if p5 == 1:
                    bt_rl5["text"] = "PULSO"            
                else:
                    bt_rl5["text"] = "ON"

            if p == 6:        
                p6 = pulso6.get()
                if p6 == 1:
                    bt_rl6["text"] = "PULSO"            
                else:
                    bt_rl6["text"] = "ON"

           
        def aciona(r): # LISTA COM TODAS AS POSSIVEIS SAIDAS SELECIONADAS (16)

            lista = [" --- ","OUT1","OUT2","OUT3","OUT4","OUT5","OUT6","OUT7","OUT8","OUT9","OUT 10","OUT 11","OUT 12","OUT 13","OUT 14","OUT 15","OUT 16"]

            
            if r == 1:
                out1 = c60.get()
                if out1 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:
                    for i in lista:
                        if out1 == i:
                            r1 = (lista.index(i))                        
                    rl1 = bt_rl1["text"]
                    if rl1 == "ON":            
                        rele.liga(r1)
                        bt_rl1["text"] = "OFF"
                    if rl1 == "OFF":            
                        rele.desliga(r1)
                        bt_rl1["text"] = "ON"
                    if rl1 == "PULSO":
                        rele.pulso(r1,2)
                    

            if r == 2:
                out2 = c70.get()
                if out2 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:
                    for i in lista:
                        if out2 == i:
                            r2 = (lista.index(i))
                    rl2 = bt_rl2["text"]
                    if rl2 == "ON":
                        rele.liga(r2)
                        bt_rl2["text"] = "OFF"
                    if rl2 == "OFF":
                        rele.desliga(r2)
                        bt_rl2["text"] = "ON"
                    if rl2 == "PULSO":
                        rele.pulso(r2,2)
                    

            if r == 3:
                out3 = c80.get()
                if out3 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:           
                    for i in lista:
                        if out3 == i:
                            r3 = (lista.index(i))       
                    rl3 = bt_rl3["text"]
                    if rl3 == "ON":
                        rele.liga(r3)
                        bt_rl3["text"] = "OFF"
                    if rl3 == "OFF":
                        rele.desliga(r3)
                        bt_rl3["text"] = "ON"            
                    if rl3 == "PULSO":
                        rele.pulso(r3,2)

            if r == 4:
                out4 = c100.get()
                if out4 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:
                    for i in lista:
                        if out4 == i:
                            r4 = (lista.index(i))        
                    rl4 = bt_rl4["text"]
                    if rl4 == "ON":
                        rele.liga(r4)
                        bt_rl4["text"] = "OFF"
                    if rl4 == "OFF":
                        rele.desliga(r4)
                        bt_rl4["text"] = "ON"
                    if rl4 == "PULSO":
                        rele.pulso(r4,2)

            if r == 5:
                out5 = c110.get()
                if out5 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:
                    for i in lista:
                        if out5 == i:
                            r5 = (lista.index(i)) 
                    rl5 = bt_rl5["text"]
                    if rl5 == "ON":
                        rele.liga(r5)
                        bt_rl5["text"] = "OFF"
                    if rl5 == "OFF":
                        rele.desliga(r5)
                        bt_rl5["text"] = "ON"
                    if rl5 == "PULSO":
                        rele.pulso(r5,2)

            if r == 6:
                out6 = c120.get()
                if out6 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:
                    for i in lista:
                        if out6 == i:
                            r6 = (lista.index(i)) 
                    rl6 = bt_rl6["text"]
                    if rl6 == "ON":
                        rele.liga(r6)
                        bt_rl6["text"] = "OFF"
                    if rl6 == "OFF":
                        rele.desliga(r6)
                        bt_rl6["text"] = "ON"
                    if rl6 == "PULSO":
                        rele.pulso(r6,2)

            if r == 7:
                out7 = c10.get()
                if out7 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:            
                    for i in lista:
                        if out7 == i:
                            r7 = (lista.index(i))
                    rele.pulso(r7,2)

                        
            if r == 8:
                out8 = c20.get()
                if out8 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:            
                    for i in lista:
                        if out8 == i:
                            r8 = (lista.index(i))
                    rele.pulso(r8,2)

            if r == 9:
                out9 = c30.get()
                if out9 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:            
                    for i in lista:
                        if out9 == i:
                            r9 = (lista.index(i))
                    rele.pulso(r9,2)

            if r == 10:
                out10 = c40.get()
                if out10 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:            
                    for i in lista:
                        if out10 == i:
                            r10 = (lista.index(i))
                    rele.pulso(r10,2)

            if r == 11:
                out11 = c50.get()
                if out11 == " --- ":
                    messagebox.showerror('Erro','Escolha um rele\n para acionar')
                else:            
                    for i in lista:
                        if out11 == i:
                            r11 = (lista.index(i))
                    rele.pulso(r11,2)

            
        #############################  Botões  ########################################

        bt_n = Button(self, text="Gravar",width=5, command = gravar) # Botão narrar
        #bt_n["command"] = partial (gravar,1) # reescreve uma função
        bt_n.place(x=380, y=55)

        # Botões acionamento reles

        bt1 = Button(self, text="Rua",width=4) # Botão rele Rua
        bt1["command"] = partial (aciona,7) # reescreve uma função
        bt1.place(x=10, y=255)

        bt2 = Button(self, text="Eclusa",width=4) # Botão rele Eclusa
        bt2["command"] = partial (aciona,8) # reescreve uma função
        bt2.place(x=75, y=255)

        bt3 = Button(self, text="Acesso",width=4) # Botão rele Acesso
        bt3["command"] = partial (aciona,9) # reescreve uma função
        bt3.place(x=140, y=255)

        bt4 = Button(self, text="Hall 1",width=4) # Botão rele Hall 1
        bt4["command"] = partial (aciona,10) # reescreve uma função
        bt4.place(x=205, y=255)

        bt5 = Button(self, text="Hall 2",width=4) # Botão rele Hall 2
        bt5["command"] = partial (aciona,11) # reescreve uma função
        bt5.place(x=270, y=255)

        # Acionamento de saida selecionada

        bt_rl1 = Button(self, text="ON",width=2, height=1, command=aciona) # Botão rele 
        bt_rl1["command"] = partial (aciona,1) # reescreve uma função
        bt_rl1.place(x=370, y=100)

        bt_rl2 = Button(self, text="ON",width=2, height=1, command=aciona) # Botão rele 
        bt_rl2["command"] = partial (aciona,2) # reescreve uma função
        bt_rl2.place(x=370, y=137)

        bt_rl3 = Button(self, text="ON",width=2, height=1, command=aciona) # Botão rele 
        bt_rl3["command"] = partial (aciona,3) # reescreve uma função
        bt_rl3.place(x=370, y=174)


        bt_rl4 = Button(self, text="ON",width=2, height=1, command=aciona) # Botão rele 
        bt_rl4["command"] = partial (aciona,4) # reescreve uma função
        bt_rl4.place(x=540, y=100)

        bt_rl5 = Button(self, text="ON",width=2, height=1, command=aciona) # Botão rele 
        bt_rl5["command"] = partial (aciona,5) # reescreve uma função
        bt_rl5.place(x=540, y=137)

        bt_rl6 = Button(self, text="ON",width=2, height=1, command=aciona) # Botão rele 
        bt_rl6["command"] = partial (aciona,6) # reescreve uma função
        bt_rl6.place(x=540, y=174)


    ##    bt_play1 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
    ##    bt_play1["command"] = partial (tocar,1,) # reescreve uma função
    ##    bt_play1.place(x=370, y=217)
    ##
    ##    bt_play2 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
    ##    bt_play2["command"] = partial (tocar,2) # reescreve uma função
    ##    bt_play2.place(x=370, y=251)
    ##
    ##    bt_play3 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
    ##    bt_play3["command"] = partial (tocar,3) # reescreve uma função
    ##    bt_play3.place(x=370, y=288)
    ##
    ##    bt_play4 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
    ##    bt_play4["command"] = partial (tocar,4) # reescreve uma função
    ##    bt_play4.place(x=370, y=325)


        bt_play5 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
        bt_play5["command"] = partial (tocar,5) # reescreve uma função
        bt_play5.place(x=540, y=217)

        bt_play6 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
        bt_play6["command"] = partial (tocar,6) # reescreve uma função
        bt_play6.place(x=540, y=251)

        bt_play7 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
        bt_play7["command"] = partial (tocar,7) # reescreve uma função
        bt_play7.place(x=540, y=288)

        bt_play8 = Button(self, text="Play",width=1, height=1, command = tocar) # Botão rele 7
        bt_play8["command"] = partial (tocar,8) # reescreve uma função
        bt_play8.place(x=540, y=325)

        # Botão Start

        bt_start = Button(self, text="Start",width=6,command = start_stop)
        bt_start.place(x=610, y=430)


        # Check box Programas Intertravamento, Saudação, Iluminação Automática

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()

        pulso1 = IntVar()
        pulso2 = IntVar()
        pulso3 = IntVar()
        pulso4 = IntVar()
        pulso5 = IntVar()
        pulso6 = IntVar()

        check1 = Checkbutton(self, text="Intertravamento Sociais",variable = CheckVar1)
        check1.place(x=10,y=300)

        check1 = Checkbutton(self, text="Saudação Sociais",variable = CheckVar2)
        check1.place(x=194,y=300)

        check1 = Checkbutton(self, text=" Iluminação Automática da Eclusa ",variable = CheckVar3)
        check1.place(x=10,y=330)

        # cHECK BOX PARA HAHILITAR PULSO DO RELE

        check30 = Checkbutton(self,variable = pulso3)
        check30["command"] = partial (liga,3) # reescreve uma função
        check30.place(x=495, y=180)

        check20 = Checkbutton(self,variable = pulso2)
        check20["command"] = partial (liga,2) # reescreve uma função
        check20.place(x=495, y=140)

        check10 = Checkbutton(self,variable = pulso1)
        check10["command"] = partial (liga,1) # reescreve uma função
        check10.place(x=495, y=105)


        check60 = Checkbutton(self,variable = pulso6)
        check60["command"] = partial (liga,6) # reescreve uma função
        check60.place(x=662, y=180)

        check50 = Checkbutton(self,variable = pulso5)
        check50["command"] = partial (liga,5) # reescreve uma função
        check50.place(x=662, y=140)

        check40 = Checkbutton(self,variable = pulso4)
        check40["command"] = partial (liga,4) # reescreve uma função
        check40.place(x=662, y=105)                  

        self.protocol("WM_DELETE_WINDOW", on_closing)
        self.mainloop()

        print("A self foi fechada")


        self.mainloop()


class ThirdWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da self principal
        self.title('Terceira self')
        self.configure(background='yellow')
        self.geometry('480x240')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        self.master.title('self Inicio')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='white')

        menubar = Menu(self)
        self.master.config(menu=menubar)

        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)

        menubar.add_cascade(label='Arquivo', menu=filemenu)
        menubar.add_cascade(label='CMM', menu=filemenu2)
        menubar.add_cascade(label='Ajuda', menu=filemenu3)

        def Config():
            
            print("Abrindo Configurações")
            window = congig()
            
        def Save():
            print("Menu Save")
            
        def Quit():
            self.destroy()
        
        def ColorBlue():
            Text(background='blue').pack()
            
        def ColorRed():
            Text(background='red').pack()
            return
            
        def ColorBlack():
            Text(background='black').pack()
            return
            
        def Help():
            text = Text()
            text.pack();
            text.insert('insert', 'Ao clicar no botão da\n'
                                  'respectiva cor, o fundo da tela\n'
                                  'aparecerá na cor escolhida.')

        filemenu.add_command(label='Abrir...', command=Help)
        filemenu.add_command(label='Salvar como...', command=Save)
        filemenu.add_separator()

        filemenu.add_command(label='Sair', command=Quit)

        filemenu2.add_command(label='Monitoramento', command=Monitoramento)
        filemenu2.add_command(label='Configurações', command=Setup)
        filemenu2.add_command(label='Preto', command=ColorBlack)

        filemenu3.add_command(label='Ajuda', command=Help)

        for name in ("button1", "button2", "button3"):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('1'):
            window = Monitoramento()
        if btn_name.endswith('2'):
            window = SecondWindow()
        if btn_name.endswith('3'):
            window = ThirdWindow()

        window.mainloop()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop() 
