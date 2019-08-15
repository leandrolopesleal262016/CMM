#!/usr/bin/env python
# coding=UTF-8

# Formato valido

##{
## "clientId":"cdd0b16d-8973-4d8e-88c7-a8fb2919e8ef",
##  "qrCodeOriginal":"55785777",
##  "codigoIntegracaoCondominio":"0001"
##}

import requests

class Notifica:

    def __init__(self):

        self = self

    def qr_utilizado(self,cliente,id_qr):

        url = 'https://www.condfy.com.br/web/api/v1/qrCodes/utilizado'        
        data = {
          "clientId": "cdd0b16d-8973-4d8e-88c7-a8fb2919e8ef",
          "qrCodeOriginal": "id_qr","codigoIntegracaoCondominio":"cliente"
        }
        data["codigoIntegracaoCondominio"] = cliente
        data["qrCodeOriginal"] = id_qr
                
        r = requests.post(url,json=data)
        
        if r.status_code == 400:

            print("Resposta do Condfy: Não autorizado")

        elif r.status_code == 401:

            print("Resposta do Condfy: Alguns campos não foram informados")

        elif r.status_code == 404:

            print("Resposta do Condfy: QR Code não encontrado")

        elif r.status_code == 200:

            print("Resposta do Condfy: QR Code liberado")

        else:

            print("Resposta Condfy",r.status_code)
        






