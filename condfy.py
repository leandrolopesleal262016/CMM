#!/usr/bin/env python
# coding=UTF-8

import requests

class Notifica:

    def __init__(self):

        self = self

    def qr_utilizado(self,cliente,id_qr):

        url = 'https://condfy.com.br/test/api/v1/qrCodes/utilizado'
        data = {
          "clientId": "cdd0b16d-8973-4d8e-88c7-a8fb2919e8ef",
          "codigoIntegracaoCondominio": "cliente",
          "qrCodeOriginal": "id_qr"
        }

        data["cliente"] = cliente
        data["id_qr"] = id_qr
        
        r = requests.post(url,json=data)

        if r.status_code == 400:

            print("Resposta do Condfy: Não autorizado")

        if r.status_code == 401:

            print("Resposta do Condfy: Alguns campos não foram informados")

        if r.status_code == 404:

            print("Resposta do Condfy: QR Code não encontrado")

        if r.status_code == 200:

            print("Resposta do Condfy: QR Code liberado")
        






