from biblioteca_CMM_oficial import Rele,Narrador,Temperatura,Email,Clima,Evento
from cmm_io import Entradas, Saidas # Classes para leituras das entradas e acionamento das saidas definidas no arq. config.txt
from expansor_modbus import Expansor # Acionamento de saidas dos expansores
from leitor_modbus import Leitor  # Leitura das entradas dos expansores
from IHM_Sociais import IHM # Interface gráfica local
from banco import Banco # Classe para inserções, consulta e atualização no banco de dados CMM
from condfy import Notifica # Bliblioteca para requisições do Condfy
from biblioteca_QRCODE import Qrcode # Classe para conexão com leitor de QR Code (3SR Automação)
from atualiza_monitor import Monitor # Atualiza o Banco de dados comforme a entrada e saidas da CLP
