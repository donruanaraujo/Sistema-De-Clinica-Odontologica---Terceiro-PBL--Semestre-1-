# Listas fundamentais para o funcionamento do programa.
lista_pacientes = []
sessoes_data = []
sessoes_marcadas = []
consultas_realizadas = []

import funcoes

class paciente:
    def __init__(self, identificapaciente, nome, identidade, cpf, email):
        self.nome = nome
        self.identidade = identidade
        self.cpf = cpf
        self.email = email
        self.identificapaciente = identificapaciente
        novopacientecadastrado = {'Id': identificapaciente, 'Nome': nome,'RG': identidade, 'CPF': cpf, 'Email': email, 'Anotações': []}
        lista_pacientes.append(novopacientecadastrado)
        # Essa classe é usada para aplicar competência 5, e é executada pela recepcionista.

class clinica:
    def __init__(self, clinica):
        self.clinica = clinica
    # Os métodos estão organizados na ordem numérica das opções(ou competência) pedidas no documento do PBL. Também está mencionado para quem é destinado cada opção.

    # 1 Método para a recepcionista.
    def cadastrar_datas(self, iddata, novadata, horario, novotempo):
        self.novadata = novadata
        self.horario = horario
        self.novotempo = novotempo
        self.iddata = iddata
        novasessao = {'Id': iddata, 'Data': novadata,'Horário da sessão': horario, 'Tempo de atendimento': novotempo}
        sessoes_data.append(novasessao)

    # 2 Método para a recepcionista.
    def lista_sessoes(self):
        funcoes.formatar('Lista de sessões clínicas', 25)
        for e in sessoes_data:
            print(f'Id:{e["Id"]}\nData: {e["Data"]}')
            print()

    # 3 Método para a recepcionista e o dentista (Competência 3 e 11 do PBL).
    def buscar_sessao(self, tipoprocura):
        nao_existe = True
        if tipoprocura == 1:
            data = input('Digite a data ')
            funcoes.formatar('Aqui estão as sessões na data informada', 39)
            for valores in sessoes_data:
                if data == valores["Data"]:
                    for chave, valores in valores.items():
                        print(f'{chave}: {valores}')
                        nao_existe = False
            if nao_existe == True:
                print("Desculpe! Não existe sessão na data informada.")

        if tipoprocura == 2:
            horario = input('Digite o horário de início de consulta: ')
            funcoes.formatar('Aqui estão as sessões no horário informado', 42)
            for valores in sessoes_data:
                if horario == valores["Horário da sessão"]:
                    for chave, valores in valores.items():
                        print(f'{chave}: {valores}')
                        nao_existe = False

            if nao_existe == True:
                print("Desculpe! Não existe sessão no horário informado.")

        if tipoprocura < 1 or tipoprocura> 2:
            print('Carácter errado!')

    # 4 Opção para recepcionista e o dentista (Competência 4 e 12 do PBL).
    def iniciar_sessao(self, id_dasessao):
        for id in sessoes_data:
            if id['Id'] == id_dasessao:
                id['Pacientes na fila'] = []
                global sessao_iniciada_agora
                sessao_iniciada_agora = id
                sessoes_data.remove(id)
                print('A sessão selecionada foi iniciada!')

    # 5 A competência 5 está pela classe paciente.

    # 6 Método para a recepcionista.
    def marcar_sessao(self, idpaciente, nome, idsessao, data):
        novamarcacao = {'Id do paciente': idpaciente, 'Nome': nome,
                        'Id da sessão': [idsessao], 'Data da sessão': [data]}
        paravelhopaciente = False
        for velha_sessao in sessoes_marcadas:
            if velha_sessao['Id do paciente'] == novamarcacao['Id do paciente']:
                for idnovo in novamarcacao['Id da sessão']:
                    velha_sessao['Id da sessão'].append(idnovo)
                for datanova in novamarcacao['Data da sessão']:
                    velha_sessao['Data da sessão'].append(datanova)
                    paravelhopaciente = True
        if paravelhopaciente == False:
            sessoes_marcadas.append(novamarcacao)

    # 7 Método para a recepcionista.
    def sessoes_do_paciente(self): 
        outro = 1
        while outro == 1:
            temsessao = False
            print('Selecione o paciente')
            for listarpaciente in lista_pacientes:
                print(f'Paciente Id: {listarpaciente["Id"]} Nome: {listarpaciente["Nome"]}')
            selecionesessao_verificar = int(input('Digite o Id do paciente que você quer selecionar: '))
            for id in sessoes_marcadas:
                if id["Id do paciente"] == selecionesessao_verificar:
                    print(f'Esses são os horários de {id["Nome"]}:')
                    for sessoes in id["Data da sessão"]:
                        print(sessoes)
                        temsessao = True
            if temsessao == False:
                print('Esse paciente não tem horário marcado')
            outro = int(input('\nDeseja pesquisar a sessão de outro paciente?\n 1 - Sim\n 2 - Não\n---> '))

    # 8 Método para a recepcionista.
    def confirmar_sessao(self, selecionepaciente_verificar, selecionesessao_verificar):
        confirma_paciente = False
        for sessoes_da_lista in sessoes_marcadas:
            if sessoes_da_lista['Id do paciente'] == selecionepaciente_verificar:
                for procurar in selecionesessao_verificar['Pacientes na fila']:
                    if selecionepaciente_verificar == procurar['Id']:
                        print('Esse paciente tem sessão marcada na data informada')
                        confirma_paciente = True
        if confirma_paciente == False:
            print('Esse paciente não está marcado para a atual sessão')
            # Se um paciente foi agendado para a sessão atual e já recebeu atendimento do dentista, sua marcação é considerada concluída e ele é removido do grupo dos pacientes que ainda estão marcados para a sessão atual. Ex: O paciente "Ruan Araujo", no banco de dados ele teve sua sessão marcada e já entrou para atendimento.

    # 9 Método para a recepcionista.
    def colocar_paciente_na_fila(self, sessoes_atualiniciada, paciente_para_fila):
        for paciente_escolhido in lista_pacientes:
            if paciente_escolhido['Id'] == paciente_para_fila:
                paciente_para_fila = paciente_escolhido
        sessoes_atualiniciada['Pacientes na fila'].append(paciente_para_fila)

    # 10 Método para a recepcionista.
    def listar_proximo_paciente(self, sessoes_atualiniciada):
        if sessoes_atualiniciada['Pacientes na fila'] != []:
            for paciente_da_lista in reversed(sessoes_atualiniciada['Pacientes na fila']):
                proximo = paciente_da_lista
            print(f'O próximo da lista é o {proximo["Nome"]} ')
        else:
            print('Não existe um próximo paciente para ser atendido.')

    # 13 Método para o dentista.
    def atender_proximo(self, sessoes_atualiniciada):
            atender = sessoes_atualiniciada['Pacientes na fila'].pop(0)
            global paciente_atendido
            paciente_atendido = atender
            consultas_realizadas.append(paciente_atendido)

    # 14 Método para o dentista.
    def Ler_prontuário(self, ler_paciente):
        print(f'Id: {ler_paciente["Id"]}\nNome: {ler_paciente["Nome"]}\nRG: {ler_paciente["RG"]}\nCPF: {ler_paciente["CPF"]}\nEmail: {ler_paciente["Email"]}\n' )
        if ler_paciente["Anotações"] != []:
            contador = 1
            for i in ler_paciente["Anotações"]:
                print(f'Anotação {contador} - {i["Anotação registrada"]}')
                contador += 1
        else:
            print('O paciente atual não tem anotações')
                    
    # 15 Método para o dentista.
    def ler_primeira_anotação(self, ler_paciente_anot1):
            if ler_paciente_anot1['Anotações'] != []:
                primeira_anotacao = ler_paciente_anot1['Anotações']
                primeira_anotacao = primeira_anotacao[0]
                primeira_anotacao = primeira_anotacao['Anotação registrada']
                print(f'Primeira anotação:\n{primeira_anotacao}')

            else:
                print('O paciente não tem anotações anteriores.')

    # 16 Método para o dentista.
    def ler_ultima_anotação(self, ler_paciente_anot2):
            if ler_paciente_anot2['Anotações'] != []:
                ultima_anotacao = ler_paciente_anot2['Anotações']
                ultima_anotacao = ultima_anotacao[-1]
                ultima_anotacao = ultima_anotacao['Anotação registrada']
                print(f'A última anotação\n{ultima_anotacao}')

            else:
                print('O paciente não tem anotações anteriores')

    # 17 Método para o dentista.
    def anotar_prontuario(self, sessao_iniciada_agora, anotacao):
        nova_anotacao = {'Data Id': sessao_iniciada_agora['Id'], 'Data': sessao_iniciada_agora['Data'],'Horário da sessão': sessao_iniciada_agora['Horário da sessão'], 'Anotação registrada': anotacao}
        paciente_atendido['Anotações'].append(nova_anotacao)
        
    # 18 Método para a recepcionista.
    def listar_consultas(self, sessao_iniciada_agora, consultas_realizadas):
        data = sessao_iniciada_agora["Data"]
        horario = sessao_iniciada_agora["Horário da sessão"]
        print(f'As consultas da data: {data} - horário: {horario}\n')
        for cada_consulta in consultas_realizadas:
            print(f'Id: {cada_consulta["Id"]} - Paciente: {cada_consulta["Nome"]}')
 