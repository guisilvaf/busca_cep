import requests

question = input("você sabe o seu CEP? S/N ")

if question.upper() == 'S':
    cep = input("Digite o seu CEP: ")

    api = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(api)

    dict_requisicao = requisicao.json()
    logradouro = dict_requisicao["logradouro"]
    complemento = dict_requisicao["complemento"]
    bairro = dict_requisicao["bairro"]
    localidade = dict_requisicao["localidade"]
    uf = dict_requisicao["uf"]

    print(f'O endereço para o CEP: {cep} é: {logradouro}{complemento} {bairro} {localidade} {uf}')

else:
    uf = input("Digite o seu UF: ")
    cidade = input("Digite a sua cidade: ")
    logradouro = input("Digite o seu logradouro: ")

    api = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'

    requisicao = requests.get(api)

    dict_requisicao = requisicao.json()

    print(dict_requisicao)
