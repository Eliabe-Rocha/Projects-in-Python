import re


def remover_char(cnpj):
    return re.sub(r'\D', '', cnpj)


def calculo(cnpj, digito):
    digito_1 = []

    if digito == 1:
        list_num = remover_char(cnpj)[:12]
    elif digito == 2:
        list_num = cnpj
    else:
        return None

    contador = len(list_num) - 7
    for x in list_num:
        if contador < 2:
            contador = 9
            list_dig = int(x) * contador
            digito_1.append(list_dig)
            contador -= 1
        else:
            list_dig = int(x) * contador
            digito_1.append(list_dig)
            contador -= 1

    digito_verificador = 11 - (sum(digito_1) % 11)
    if digito_verificador > 9:
        list_num += '0'
        return list_num
    else:
        list_num += str(digito_verificador)
        return list_num


def validador():
    while True:
        cnpj = input('Por gentileza, digite o CNPJ que deseja validar: ')

        novo_cnpj = remover_char(cnpj)
        if len(cnpj) != 18 or (novo_cnpj[0] * 14) == novo_cnpj:
            print("Por gentileza, digite um CNPJ válido!")
        else:
            digito_1 = calculo(cnpj, 1)
            resultado = calculo(digito_1, 2)

            if remover_char(cnpj) == resultado:
                return 'CNPJ validado!!!'
            else:
                return 'CNPJ inválido!!!'

print(validador())
# 04.252.011/0001-10
# 11.111.111/1111-11