import requests
import json
import codecs
import numpy as np
import os
from php import Php

from requests.api import request
from requests.sessions import PreparedRequest

while True:
    esr = input("Введите EСR без последней цифры: ")


    response = requests.get(f'https://dzv.rzdsupport.ru/public/stations/api/v1/online_table/{esr}?lang=ru',verify=True)
    response.encoding = 'utf-8'

    s = (json.dumps(response.json(), sort_keys=True, indent=4))
    text_en = codecs.decode (s, 'unicode_escape')
    print(text_en)

    choice = input("Для продолжения нажмите любую клавишу. Для выхода введите 'exit'): ")
    if choice == 'exit':
        break