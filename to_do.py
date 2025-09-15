import time
import os

tarefas = []

def verificação():

    arquivo = 'tarefas.txt'

    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            infos = f.read().splitlines()

        print("Tarefas carregadas com sucesso!")
        time.sleep(1)
        return infos
    else:
        print("Nenhuma tarefa para ser carregada!")
        time.sleep(1)
        return []
 
def adicionar_tarefa(tarefas):
    nova_tarefa = input("Informe a nova tarefa:\n>>> ")
    tarefas.append(nova_tarefa)
    print("Nova tarefa adicionada com sucesso")
    time.sleep(1)

def listar_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        time.sleep(1)
    else:
        print("----- Tarefas -----")
        for indice, item in enumerate(tarefas):
            print(f"{indice + 1}. {item}")
        time.sleep(2)

def remover_tarefa(tarefas):
    listar_tarefa(tarefas)
    if not tarefas:
        return
    
    try: 
        time.sleep(1)
        remover_num = int(input("Qual o número da tarefa que deseja remover?\n>>> "))
        remover = remover_num - 1
        tarefas.pop(remover)
        print("Tarefa removida com sucesso!")
        time.sleep(1)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")
        time.sleep(1)
    except IndexError:
        print("Erro: Essa tarefa não existe.")
        time.sleep(1)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def salvar_tarefas(tarefas):
    with open('tarefas.txt', 'w') as f:
        for item in tarefas:
            f.write(item + '\n')
info = verificação()
while True:
    limpar_tela()
    print("***** To do List *****")
    print("[1] Adicionar Tarefa")
    print("[2] Listar Tarefas")
    print("[3] Remover Tarefas")
    print("[4] Sair")

    escolha = input("Digite sua opção:\n>> ")

    if escolha == "1":
        print("Opção escolhida: Adicionar nova Tarefa.")
        adicionar_tarefa(info)
        salvar_tarefas(info)
    elif escolha == "2":
        print("Opção escolhida: Listar tarefas existentes.")
        listar_tarefa(info)
    elif escolha == "3":
        print("Opção escolhida: Remover tarefa.")
        remover_tarefa(info)
        salvar_tarefas(info)
    elif escolha == "4":
        print("Saindo do programa...")
        time.sleep(1)
        break
    else: 
        print("Opção inválida! Tente novamente")