import numbers
from random import random
from time import time
from tkinter import N
from tkinter.ttk import Separator
import pandas as pd
import null as nulo
from twilio.rest import Client
from random import randint


account_sid = "Axxx"
auth_token  = "axxxxxx"
client = Client(account_sid, auth_token)

especial = []
agenda = []
idmedico = []
esp = []
guardar_medico = []
guardar_consultorio = []
guardar_especialidade = []
guardar_data = []
guardar_hora = []
guardar_id = []
_cpf = []
_cpf_ = []

especialidades = ("Odontologia, Clínico geral, Radiologista, Dermatologista, Cardiologista")
lista_odontologia = pd.read_excel('1.xlsx')
lista_clínico = pd.read_excel('2.xlsx')
lista_radiologista = pd.read_excel('3.xlsx')
lista_dermatologista = pd.read_excel('4.xlsx')
lista_cardiologista = pd.read_excel('5.xlsx')

def pede_nome():
    while True:
        name = input("\nNome: ")
        if all(c.isalpha() or c.isspace() for c in name):
            return name
        else:
            print("Por favor digite um nome válido (somente letras e espaços)")

def pede_Cpf():
    global _cpf
    inputCPF = str(input("\nDigite seu CPF (somente números): "))
    _cpf = inputCPF
    if(pede_nome_arquivo(_cpf)):
        print('''\nPaciente cadastrado com sucesso! \nSiga para a opção 2 do MENU.''')
    else:
        print("\033[0;31mOPS! CPF inválido, retorne a etapa.\033[m")

def pede_medico():
    global idmedico
    idmedico = int(input('\nDigite o ID do médico desejado: '))
    ehNumero = False
    while (ehNumero == False):

        try:
            int(idmedico)
            ehNumero = True
            return idmedico

        except ValueError:
            try:
                int(idmedico)
                ehNumero = True
                return idmedico

            except ValueError:
                print("Digite apenas números.")

def pede_especialidade():
    global especial
    ehNumero = False
    while (ehNumero == False):
        especial = input('''\n
Digite 1 para Odontologia\n
Digite 2 para Clínico geral\n
Digite 3 para Radiologista\n
Digite 4 para Dermatologista\n
Digite 5 para Cardiologista\n\n
Digite a especialidade desejada: \n''')


        try:
            int(especial)
            ehNumero = True 
            
        except ValueError:
            try:
                float(especial)
                ehNumero = True
                return especial

            except ValueError:
                print("Digite apenas números.")

def pede_telefone():
    ehNumero = False
    while (ehNumero == False):
        tel = input("\nDigite o seu telefone: ")

        try:
            int(tel)
            ehNumero = True
            return tel
        except ValueError:
            try:
                float(tel)
                ehNumero = True
            except ValueError:
                print("Digite apenas números ou siga o exemplo a seguir: 1198******52")

def pede_idade():
    ehNumero = False
    while (ehNumero == False):
        ida = input("\nDigite sua idade: ")

        try:
            int(ida)
            ehNumero = True
            return ida
        except ValueError:
            try:
                int(ida)
                ehNumero = True
                return ida

            except ValueError:
                print("Digite apenas números.")

def pede_genero():
    while True:
        gen = input("\nGênero: ")
        if all(c.isalpha() or c.isspace() for c in gen):
            return gen
        else:
            print("Por favor digite somente letras.")

def mostra_dados(nome, telefone, idade, genero, _cpf):
    print(f"Nome: {nome}, Telefone: {telefone}, Idade: {idade}, Genero: {genero}, CPF:{_cpf}")

def pede_nome_arquivo(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def novo():
    global agenda
    global _cpf_
    nome = pede_nome()
    telefone = pede_telefone()
    idade = pede_idade()
    genero = pede_genero()
    CPF = pede_Cpf()
    _cpf_ = CPF
    if _cpf_ == CPF:
        agenda.append([nome, telefone, idade, genero, _cpf])
    else:
        print('''Paciente cadastrado com sucesso! \nSiga para a opção 2 do MENU.\n''')

def especialidade():
    global especial
    print("\nEscolha uma especialidade: ")
    especialidadee = pede_especialidade()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    if especial == "1":
        print(lista_odontologia)

    elif especial == "2":
        print(lista_clínico)

    elif especial == "3":
        print(lista_radiologista)

    elif especial == "4":
        print(lista_dermatologista)

    elif especial == "5":
        print(lista_cardiologista)
    return medicos()

def medicos():
        global esp
        global guardar_consultorio
        global guardar_medico
        global guardar_especialidade
        global guardar_data
        global guardar_hora
        global guardar_id
        lista_especialidades = ['1', '2', '3', '4', '5']
        pedemedico = pede_medico()
        esp = []
         #print('fora for') modificar para while true 
        for especialidades in especial:
            tabela_especialidades = pd.read_excel(f'{especial}.xlsx')

            if(tabela_especialidades['ID'] == int(idmedico)).any():
                MEDICO = tabela_especialidades.loc[tabela_especialidades['ID'] == int(idmedico) , 'MÉDICOS'].values[0]
                CONSULTORIO = tabela_especialidades.loc[tabela_especialidades['ID'] == int(idmedico), 'CONSULTÓRIO'].values[0]
                DATA = tabela_especialidades.loc[tabela_especialidades['ID'] == int(idmedico), 'DATA'].values[0]
                HORA = tabela_especialidades.loc[tabela_especialidades['ID'] == int(idmedico), 'HORA'].values[0]
                ESPECIALIDADE = tabela_especialidades.loc[tabela_especialidades['ID'] == int(idmedico), 'ESPECIALIDADE'].values[0]
                guardar_medico = MEDICO
                guardar_consultorio = CONSULTORIO
                guardar_data = DATA
                guardar_hora = HORA
                guardar_especialidade = ESPECIALIDADE
                print(f'\nDeseja agendar uma consulta de especialidade {guardar_especialidade} com o médico(a) {MEDICO}, localizado em {CONSULTORIO}\nDATA: {guardar_data:.10} Hora: {guardar_hora} \n\nDigite 3 para confirmar os dados! ')
                esp.append(f'Especialidade: {guardar_especialidade}, Médico: {guardar_medico}, Consultório: {guardar_consultorio}, DATA: {guardar_data:.10}, HORA: {guardar_hora}')
                global teste
                teste = esp
            else:
                print("ID não encontrado, retorne a etapa.")

def lista():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("DADOS DO AGENDAMENTO\n" )
    dados = []
    for e in agenda:
        dados = e
    print(f"Nome: {dados[0]}\nTelefone: {dados[1]}\nIdade: {dados[2]}\nGênero: {dados[3]}\nCPF: {dados[4]}")
        # mostra_dados(dados[0],dados[1], dados[2], dados[3], dados[4])
    consulta = []
    for i in teste:
        consulta = i
    print(f"{consulta} ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('''
Digite 4 para alterar dados do paciente. 
Digite 5 para confirmar o agendamento.''')
    


print("=" * 80)
Mensagem = print('''
                                  BEM VINDO AO PROJETO xD
                        
                        
                        PARA REALIZAR UMA MARCAÇÃO DE CONSULTA ONLINE 
                                SIGA OS PASSO A PASSO ABAIXO:

PARA INCIAR O PROGRAMA > DIGITE 1. \n 
PARA VISUALIZAR AS ESPECIALIDADES E ESCOLHER UM MÉDICO > DIGITE 2º.\n 
PARA CONFIRMAR OS DADOS DA CONSULTA > DIGITE 3º\n
PARA ALTERAR OS DADOS DA CONSULTA > DIGITE 4º\n
PARA CONFIRMAR O AGENDAMENTO > DIGITE 5º

''')
def grava():
    global _cpf
    with open(_cpf, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                arquivo.write(f"Nome: {e[0]}\nTelefone: {e[1]}\nIdade: {e[2]}\nGênero{e[3]}\nCPF:{e[4]}\n")
                for i in esp:
                    arquivo.write(f"Especialidade: {guardar_especialidade}\nMédico: {guardar_medico}\nConsultório: {guardar_consultorio}\nData: {guardar_data:.10}\n Hora: {guardar_hora} ")
                    arquivo.close()
                    print('Agendamento confirmado, gerado o Token:')
    #RECEBER SMS
                    message = client.messages.create(
                        to = "+xxxxx", 
                        from_= "+xxxxx",
                        body = f'Consulta marcada com o Médico {guardar_medico} da especialidade {guardar_especialidade}, localizado em {guardar_consultorio}!\nData: {guardar_data:.10} Hora: {guardar_hora}\nPara maiores informações, entre em contato com nossa central de atendimento (11)98971-3252')
                    print(message.sid)
                    exit()

def pesquisa(nome2):
    mcpf = nome2.lower()
    for p,e in enumerate(agenda):
        if e[4].lower() == mcpf:
            return p
        else:
            print("CPF não encontrado")
    return None

def altera():
    global _cpf
    global guardar_consultorio
    global guardar_data
    global guardar_especialidade
    global guardar_hora
    global guardar_medico
    global agenda
    p = pesquisa(_cpf)
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        idade = agenda[p][2]
        genero = agenda[p][3]
        _cpf = agenda[p][4]
        print('''\n Usuário Encontrado! 
       Faça à alteração necessaria.''')
        mostra_dados (nome, telefone, idade, genero, _cpf)
        nome = pede_nome()
        telefone = pede_telefone()
        idade = pede_idade()
        genero = pede_genero()
        especiali = especialidade()
        agenda[p] = [nome, telefone, idade, genero, _cpf]
        return [especiali]
    else:
        print("Nome não encontrado.")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor= int(input (pergunta))
            if inicio <= valor <=fim:
                return valor
            else:
                print("Valor inválido, digite entre 0 a 5.")
        except ValueError:
            print(f"Valor inválido, favor digitar entre (inicio) e (fim)")

def valida(pergunta, inicio, fim):
    while True:
        try:
            valor= int(input (pergunta))
            if inicio <= valor <=fim:
                return valor
            else:
                print("Valor inválido, digite entre 1 a 5.")
        except ValueError:
            print(f"Valor inválido, favor digitar entre (inicio) e (fim)")

def menu():
    print("=" * 80)
    print("""

1 - CADASTRAR PACIENTE.
2 - ESPECIALIDADES E MÉDICOS.
3 - CONFIRMAR DADOS DO PACIENTE E DO AGENDAMENTO.
4 - ALTERAR DADOS DO PACIENTE E DA CONSULTA.
5 - CONFIRMAR AGENDAMENTO.
0 - SAIR

""")
    print("=" * 80)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

def sair():
    print("\033[0;31mObrigado por utilizar o nosso programa.\033[m")
    exit()

while True:
    opção = menu()
    if opção == 0:
        sair()
    elif opção == 1:
        novo()
    elif opção == 2:
        especialidade()
    elif opção == 3:
        lista()
    elif opção == 4:
        altera()
    elif opção == 5:
        grava()
    

    #TRHEAD <<<<< LOOPING POR VEZ