import requests
import unittest


# Passo 1
def get_username(username: str):
    requisicao = requests.get(f'https://api.github.com/users/{username}')
    if requisicao.status_code == 200:
        data = requisicao.json()
        print(data)
        return data
    else:
        print(f'Erro: {requisicao.status_code}')


# Passo 2
class User:
    def __init__(self, username):
        self._username = username

    def get_parameter(self, parameters: list):
        requisicao = requests.get(f'https://api.github.com/users/{self._username}')
        if requisicao.status_code == 200:
            data = requisicao.json()
        else:
            print(f'Erro: {requisicao.status_code}')
            type(requisicao.status_code)
            return requisicao.status_code

        if type(parameters) == str:
            parameters = [parameters]

        response_dict = {}
        for parameter in parameters:
            response_dict[parameter] = data[parameter]

        print(response_dict)
        return response_dict


class TestMethods(unittest.TestCase):
    """Classe de testes unitários. Crie seus testes aqui."""

    def test_this_test_words(self):
        self.assertTrue(True)

    def test_username_parameters(self):
        parameters = ['login', 'id', 'avatar_url', 'html_url']
        response = get_username('githubuser')
        for param in parameters:
            self.assertTrue(param in response.keys())

    def test_user_object(self):
        user_test = User("githubuser")
        parameters = ['login', 'id', 'avatar_url', 'html_url']
        self.assertFalse(user_test.get_parameter(parameters) == 404)

if __name__ == "__main__":
    unittest.main()
