from biblioteca_CMM_oficial import Rele,Narrador,Temperatura,Email,Clima,Evento
from cmm_io import Entradas, Saidas # Classes para leituras das entradas e acionamento das saidas definidas no arq. config.txt
from banco import Banco # Classe para inserções, consulta e atualização no banco de dados CMM
from condfy import Notifica # Bliblioteca para requisições do Condfy
from biblioteca_QRCODE import Qrcode # Classe para conexão com leitor de QR Code (3SR Automação)
import start_leitores_qr # Conecta todos os leitores configurados na interface gráfica
from expansores import Leitor, Expansor 
