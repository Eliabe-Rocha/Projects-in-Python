from time import sleep

def show_list(lista_tarefas):
    print('Sua lista de tarefas é:\n')
    print(lista_tarefas)
    print('\n', '#'*80, '\n')

def desfazer_func(lista_tarefas, desfazer):
    if not lista_tarefas:
        print('Nenhum ação a ser desfeita')
        return

    last_action = lista_tarefas.pop()
    desfazer.append(last_action)


def refazer_func(lista_tarefas, desfazer):
    if not desfazer:
        print('Nenhuma ação a ser refeita')
        return

    last_action = desfazer.pop()
    lista_tarefas.append(last_action)


if __name__ == '__main__':
    lista_tarefas = []
    desfazer = []

    while True:
        print("Por gentileza, escolha uma das opções abaixo ou digite a tarefa que deseja adiconar a lista:")
        print("1 - Exibir lista de tarefas. \n2 - Desfazer tarefas. \n3 - Refazer tarefas"
              "\n4 - Sair do programa \n")
        option = input("Digite uma opção: ")

        if option == '1':
            show_list(lista_tarefas)
            continue

        elif option == '2':
            desfazer_func(lista_tarefas, desfazer)
            continue

        elif option == '3':
            refazer_func(lista_tarefas, desfazer)
            continue

        elif option == '4':
            print('Encerrando o programa', sep='')
            for i in range(3):
                print('.', end='')
                sleep(0.8)
            print('\nAté mais!')
            break

        lista_tarefas.append(option)
