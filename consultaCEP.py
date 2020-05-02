# Este é meu primeiro projeto de integração de Python com API
# O script lê o input, verifica se tem a quantidade de dígitos adequada e solicita a consulta pela API viacep.
import requests

def consultaCEP():
    print("\nConsulta de CEP\n")

    cep = input("Digite o CEP a ser consultado(apenas números): ")

    while len(cep) != 8:
        if len(cep) != 8:
            print("Ops, parece que você digitou alguma coisa errada. Vamos tentar de novo?\n")
            cep = input("Digite o CEP a ser consultado(apenas números): ")

    consulta = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

    resultado = consulta.json()

    if "erro" not in resultado:
        print("\nEncontramos os dados do CEP {}".format(resultado["cep"]))
        print("\nLogradouro: {}".format(resultado["logradouro"]))
        print("Bairro: {}".format(resultado["bairro"]))
        print("Cidade: {}".format(resultado["localidade"]))
        print("UF: {}".format(resultado["uf"]))

        restart = int(input("Deseja realizar uma nova consulta? \n1 - Sim\n2 - Não\nEscolho: "))

        if restart == 1:
            consultaCEP()

        if restart == 2:
            print("\nMuito obrigado por utilizar minha função. Foi um prazer te ajudar, até a próxima!")
            exit()

    else:
        print("O CEP {} é inválido, gostaria de tentar novamente?".format(cep))
        consultaCEP()

consultaCEP()