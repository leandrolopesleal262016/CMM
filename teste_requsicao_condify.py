#!/usr/bin/env python
# coding=UTF-8

import requests # Funciona muito melhor :)

url = 'https://condfy.com.br/test/api/v1/qrCodes/utilizado'
data = {
  "clientId": "cdd0b16d-8973-4d8e-88c7-a8fb2919e8ef",
  "codigoIntegracaoCondominio": "2019",
  "qrCodeOriginal": "83587161"
}
r = requests.post(url,json=data)
print(r.status_code)






