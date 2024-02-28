#/*******************************************************************************
#Autor: João Ruan Araujo de Jesus Silva
#Componente Curricular: Mi algoritmos
#Concluido em: 18/02/2024
#Linguagem de progamação: Python 3.11.5
#Sistema operacional usado na criação do código: Windows 11
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

import classes
import bancodedados
bancodedados.banco_de_dados()
import funcoes


clinica1 = classes.clinica('Bem vindo')
categoria = (int(input('Selecione sua categoria.\nDigite 1 - Recepcionista\nDigite 2 - Dentista\n ---> ')))
voltarmenu = 1

if categoria == 1:
    while voltarmenu != 2:

            clinica1 = classes.clinica('Clínica')
            menurecepcionista = int(input('\n MENU\n Digite 1 - Adicionar nova sessão clínica\n Digite 2 - Para visualizar lista sessões clínicas\n Digite 3 - Buscar sessão clínica\n Digite 4 - Iniciar sessão clínica \n Digite 5 - Adicionar novo paciente\n Digite 6 - Marcar horário para paciente\n Digite 7 - Listar horários marcados do paciente\n Digite 8 - Confirmar se paciente está marcado para sessão atual\n Digite 9 - Colocar paciente na fila de atendimento\n Digite 10 - Listar próximo paciente da fila de atendimento\n Digite 11 - Listar consultas realizadas numa sessão clínica\n ---> '))
            
            if menurecepcionista == 1:
                novocadastro = 1
                while novocadastro == 1:
                    dia = input('Digite o dia: ')
                    mes = input('Digite o mês: ')
                    ano = input('Digite o ano: ')
                    horario = input('Horário da sessão: ')
                    tempo = input('Tempo de atendimento: ')
                    identificasessao = 1
                    for id in classes.sessoes_data:
                        if id["Id"] == identificasessao:
                            identificasessao += 1
                    clinica1.cadastrar_datas(identificasessao, f'{dia}/{mes}/{ano}', horario, tempo)
                    print(f'Cadastrado: Sessão do dia {dia}/{mes}/{ano} com {tempo} para atendimento.')
                    novocadastro = int(input('Deseja cadastrar outra sessão?\n 1- Para sim\n 2- Para não\n ---> '))

            if menurecepcionista == 2:
                clinica1.lista_sessoes()

            if menurecepcionista == 3:
                outra = 1
                while outra == 1:
                    tipoprocura = int(input('Deseja procurar sessões pela data ou pelo horário?\n 1 - Data\n 2 - Horario\n---> '))
                    clinica1.buscar_sessao(tipoprocura)
                    outra = int(input('\nDeseja fazer outra consulta?\n 1 - Sim\n 2 - Não\n--->  '))

            if menurecepcionista == 4:
                print('Selecione sessão para ser iniciada')
                for datas in classes.sessoes_data:
                    print(f'Id: {datas["Id"]} data: {datas["Data"]}')
                id_dasessao = int(input('Digite o Id da data que você quer selecionar: '))
                clinica1.iniciar_sessao(id_dasessao)
                classes.paciente_atendido = {}

            if menurecepcionista == 5:
                novopaciente = 1
                while novopaciente == 1:
                    nome = input('Qual o nome do paciente? ')
                    identidade = input(f'Qual o número de identidade do {nome}? ')
                    cpf = input(f'Qual o número de CPF do {nome}? ')
                    email = input(f'Qual o email do {nome}? ')
                    identificapaciente = 1
                    for id in classes.lista_pacientes:
                        if id["Id"] == identificapaciente:
                            identificapaciente += 1
                    print('Paciente cadastrado')
                    classes.paciente(identificapaciente, nome, identidade, cpf, email)
                    novopaciente = int(
                        input('Deseja cadastrar outro paciente?\n 1- Para sim\n 2- Para não\n ---> '))

            if menurecepcionista == 6:
                outra = 1
                while outra == 1:
                    print('Selecione o paciente')
                    for pacientesdaclinica in classes.lista_pacientes:
                        print(f'Id paciente: {pacientesdaclinica["Id"]} Nome: {pacientesdaclinica["Nome"]}')
                    idescolhido1 = int(input('Digite o Id do paciente que você quer selecionar: '))
                    for id in classes.lista_pacientes:
                        if id['Id'] == idescolhido1:
                            idpaciente = id['Id']
                            nome = id['Nome']
                            print('\nSelecione a sessão ')
                            for datas in classes.sessoes_data:
                                print(f'Id sessão: {datas["Id"]} nome: {datas["Data"]}')
                            idescolhido2 = int(input('Digite o Id da data que você quer selecionar: '))
                            for id in classes.sessoes_data:
                                if id['Id'] == idescolhido2:
                                    idsessao = id['Id']
                                    data = id['Data']
                    clinica1.marcar_sessao(idpaciente, nome, idsessao, data)

                    outra = int(input('Deseja marcar um novo horário para um paciente?\n 1- Para sim\n 2- Para não\n ---> '))

            if menurecepcionista == 7:
                clinica1.sessoes_do_paciente()

            if menurecepcionista == 8:
                outro = 1
                while outro == 1:
                    print(f'A sessão iniciada:\nSessão da data: {classes.sessao_iniciada_agora["Data"]}')
                    print('Pacientes:')
                    for listarpaciente in classes.lista_pacientes:
                        print(f'Id: {listarpaciente["Id"]} , Nome: {listarpaciente["Nome"]}')
                    selecionepaciente_verificar = int(input('\nDigite o Id do paciente que você quer verificar\n---> '))
                    clinica1.confirmar_sessao(selecionepaciente_verificar, classes.sessao_iniciada_agora)

                    outro = int(input('Deseja conferir outro paciente?\n 1 - Sim\n 2 - Não\n---> '))

            if menurecepcionista == 9:
                outro = 1
                while outro == 1:
                    tem_paciente = False
                    for procurarnas_marcadas in classes.sessoes_marcadas:
                        for id in procurarnas_marcadas['Id da sessão']:
                            if id == classes.sessao_iniciada_agora['Id']:
                                print(f'Id do paciente: {procurarnas_marcadas["Id do paciente"]} , Nome: {procurarnas_marcadas["Nome"]}')
                                tem_paciente = True

                    if tem_paciente == True:
                        paciente_para_fila = int(input('Digite o Id do paciente que vai para a fila de espera\n---> '))
                        clinica1.colocar_paciente_na_fila(classes.sessao_iniciada_agora, paciente_para_fila)
                        outro = int(input('Deseja adicionar outro paciente na fila?\n 1 - Sim\n 2 - Não\n---> '))
                    if tem_paciente == False:
                        print('Não tem pacientes marcados para a sessão atual.\nLogo não é possível selecionar ninguém para a fila de atendimento. ')
                        outro = int(input('Deseja adicionar outro paciente na fila?\n 1 - Sim\n 2 - Não\n---> '))

            if menurecepcionista == 10:
                clinica1.listar_proximo_paciente(classes.sessao_iniciada_agora)

            if menurecepcionista == 11:
                clinica1.listar_consultas(classes.sessao_iniciada_agora, classes.consultas_realizadas)
            
            funcoes.formatar('Deseja voltar para o menu principal?\n 1 - Desejo voltar\n 2 - Quero encerrar o programa', 36)
            voltarmenu = int(input('---> '))


if categoria == 2:
    while voltarmenu != 2:
# Dada a natureza da opção 3 e o pré-requisito do PBL, a dita opção só pode ser executada com eficiência se uma sessão foi marcada, iniciada e os pacientes foram colocados na fila de atendimento. Por isso o banco_de_dados já inicia esses parâmetros. Assim facilitando o teste do programa.
# Já a opção 4,5,6 e 7 necessita que um paciente esteja na sala de atendimento como "Paciente atual". Por isso o banco_de_dados já inicia o atendimento de um paciente para que o prontuário do "paciente atual" seja visualizado e as anotações do "paciente atual" sejam manipuladas. 
            menudentista = int(input('\n MENU\n Digite 1 - Buscar sessão clínica\n Digite 2 - Iniciar sessão clínica\n Digite 3 - Atender próximo paciente\n Digite 4 - Ler prontuário completo do paciente atual\n Digite 5 - Ler primeira anotação do paciente atual\n Digite 6 - Ler última anotação do paciente atual\n Digite 7 - Anotar no prontuário do paciente atual\n Digite 8 - Encerrar sessão atual\n --->  '))
            if menudentista == 1:
                outra = 1
                while outra == 1:
                    tipoprocura = int(input('Deseja procurar sessões pela data ou pelo horário?\n 1 - Data\n 2 - Horario\n---> '))
                    clinica1.buscar_sessao(tipoprocura)
                    outra = int(input('\nDeseja fazer outra consulta?\n 1 - Sim\n 2 - Não\n--->  '))

            if menudentista == 2:
                print('Selecione sessão para ser iniciada')
                for datas in classes.sessoes_data:
                    print(f'Id: {datas["Id"]} data: {datas["Data"]}')
                id_dasessao = int(input('Digite o Id da data que você quer selecionar: '))
                clinica1.iniciar_sessao(id_dasessao)
                classes.paciente_atendido = {}

            if menudentista == 3:
                if classes.sessao_iniciada_agora['Pacientes na fila'] != []:
                    clinica1.atender_proximo(classes.sessao_iniciada_agora)
                    print(f'O Próximo é {classes.paciente_atendido["Nome"]}')
                else:
                    print('Não há próximo paciente')
                    classes.paciente_atendido = {}
                
            if menudentista == 4:
                if classes.paciente_atendido != {}:
                    clinica1.Ler_prontuário(classes.paciente_atendido)
                else:
                    print('Não há paciente atual para se ler o prontuário.')

            if menudentista == 5:
                if classes.paciente_atendido != {}:
                    clinica1.ler_primeira_anotação(classes.paciente_atendido)
                else:
                    print('Não há um paciente em atendimento no momento para a leitura de anotações.')

            if menudentista == 6:
                if classes.paciente_atendido != {}:
                    clinica1.ler_ultima_anotação(classes.paciente_atendido)
                else:
                    print('Não há um paciente em atendimento no momento para a leitura de anotações.')

            if menudentista == 7:
                if classes.paciente_atendido != {}:
                    anotacao = input('Anotação do paciente:\n')
                    clinica1.anotar_prontuario(classes.sessao_iniciada_agora, anotacao)
                    print('Anotação salva!')
                else:
                    print('Não há um paciente em atendimento no momento para fazer anotações.')
            
            if menudentista == 8:
                sessao_iniciada_agora = {}
                paciente_atendido = {}
                classes.paciente_atendido = {}
                print('A sessão atual foi encerrada')
                # Se a sessão atual foi encerrada, logo não existirá um “paciente atual” originário da dita sessão. Logo não será possível ler o prontuário do paciente atual, ler primeira anotação do paciente atual, ler a última anotação do paciente atual e nem fazer anotação no prontuário do paciente atual, contudo, o programa não irá quebrar caso tais opções sejam selecionadas, uma mensagem será exibida informando o usuário sobre o fato de não existir o “paciente atual”. Todavia, caso uma nova sessão seja iniciada, e um novo paciente seja chamado, as ditas opções de prontuário e anotações voltará a funcionar normalmente, já que agora existe um paciente “atual novamente”. 

            funcoes.formatar('Deseja voltar para o menu principal?\n 1 - Desejo voltar\n 2 - Quero encerrar o programa', 36)
            voltarmenu = int(input('---> '))

print('Programa encerrado')