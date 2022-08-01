# Passo 1:

import requests


def get_username(username: str):
    requisicao = requests.get(f'https://api.github.com/users/{username}')
    if requisicao.status_code == 200:
        data = requisicao.json()
        print(data)
        return data
    else:
        print(f'Erro: {requisicao.status_code}')