import time
import os

class Tarefa:
    def __init__(self, descricao, status = "pendente"):
        self.descricao = descricao
        self.status = status
    def marcar_como_concluido(self):
        self.status = "concluido"
    def __str__(self):
        return f"[{self.status}] - {self.descricao}"
    
tarefas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_tarefas():
    arquivo = 'tarefas.txt'

    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            infos = f.read().splitlines()
            lista_objetos = []
            
            for linha_atual in infos:
                descricao, status = linha_atual.split(';')
                tarefa1 = Tarefa(descricao, status)
                lista_objetos.append(tarefa1)
            return lista_objetos

    else:
        print("Nenhum arquivo encontrado.")
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.txt', 'w') as f:
        for item in tarefas:
            descricao = item.descricao
            status = item.status
            f.write(f"{descricao};{status}\n")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefas cadastrada")
        time.sleep(1)
    else:
        for indice, item in enumerate(tarefas):
            print(f"{indice + 1}, {item}")
        time.sleep(2)

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        time.sleep(1)
        concluir_num = int(input("Qual o número da tarefa que deseja concluir?\n>>> "))
        indice = concluir_num - 1
        objeto_tarefa = tarefas[indice]
        objeto_tarefa.marcar_como_concluido()
        print("Tarefa concluida com sucesso!")
        time.sleep(1)
    except ValueError:
        print("Erro: Entrada inválida! Por favor, digite um número.")
        time.sleep(1)
    except IndexError:
        print("Erro: Essa tarefa não existe.")
        time.sleep(1)

def adicionar_tarefa(tarefas):
    descricao = input("Informe a nova tarefa:\n>>> ")
    nova_tarefa = Tarefa(descricao)
    tarefas.append(nova_tarefa)
    time.sleep(1) 

info = carregar_tarefas()

while True:
    limpar_tela()
    print("***** To do List *****")
    print("[1] Adicionar Tarefa")
    print("[2] Listar Tarefas")
    print("[3] Concluir Tarefas")
    print("[4] Sair")

    escolha = input("Digite sua opção:\n>> ")

    if escolha == "1":
        print("Opção escolhida: Adicionar nova Tarefa.")
        adicionar_tarefa(info)
        salvar_tarefas(info)
    elif escolha == "2":
        print("Opção escolhida: Listar tarefas existentes.")
        listar_tarefas(info)
    elif escolha == "3":
        print("Opção escolhida: Concluir tarefa.")
        concluir_tarefa(info)
        salvar_tarefas(info)
    elif escolha == "4":
        print("Saindo do programa...")
        time.sleep(1)
        break
    else: 
        print("Opção inválida! Tente novamente")
