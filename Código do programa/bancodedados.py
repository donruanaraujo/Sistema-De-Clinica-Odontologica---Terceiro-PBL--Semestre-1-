import classes
def banco_de_dados():
    clinica1 = classes.clinica('Clínica')
    # DADOS ARMAZENADOS PARA TESTES

    # Pacientes cadastrados 
    classes.paciente(1, 'Ruan Araujo', '29.965.687-1', '245.888.447-41', 'ruanaraujo99@marktechbr.com.br')
    classes.paciente(2, 'Lucas Freitas', '154.789.632-98', '876.543.210-12', 'Lucasfreitas88@foz.com.br')
    classes.paciente(3, 'Guilherme Silva', '987.654.321-54', '456.789.012-34', 'guilherme@email.com')
    classes.paciente(4, 'Isabela Oliveira', '369.258.147-25', '123.456.789-01', 'isabela@email.com')
    classes.paciente(5, 'Felipe Santos', '741.852.963-89', '654.321.098-76', 'felipe@email.com')
    classes.paciente(6, 'Larissa Lima', '852.147.963-25', '789.012.345-67', 'larissa@email.com')
    classes.paciente(7, 'Thiago Costa', '236.951.487-20', '159.357.482-63', 'thiago@email.com')
    classes.paciente(8, 'Gabriela Rocha', '410.753.926-84', '632.574.819-05', 'gabriela@email.com')
    classes.paciente(9, 'Pedro Pereira', '573.816.294-08', '948.260.371-57', 'pedro@email.com')
    classes.paciente(10, 'Manuela Souza', '195.637.402-68', '820.194.753-26', 'manuela@email.com')
    classes.paciente(11, 'Rafael Oliveira', '308.426.915-73', '467.139.582-31', 'rafael@email.com')
    classes.paciente(12, 'Marina Martins', '631.972.548-09', '294.753.816-40', 'marina@email.com')

    # Sessões clínica adicionadas
    clinica1.cadastrar_datas(1, '01/03/2024', '13h', '1h')
    clinica1.cadastrar_datas(2, '02/03/2024', '13h', '2h')
    clinica1.cadastrar_datas(3, '03/03/2024', '13h', '3h')
    clinica1.cadastrar_datas(4, '04/03/2024', '15h', '4h')
    clinica1.cadastrar_datas(5, '05/03/2024', '15h', '5h')
    clinica1.cadastrar_datas(6, '06/03/2024', '15h', '6h')
    clinica1.cadastrar_datas(7, '07/03/2024', '15h', '7h')



    # Marcar sessão/horário para pacientes
    clinica1.marcar_sessao(1, 'Ruan Araujo', 7, '07/03/2024')
    clinica1.marcar_sessao(2, 'Lucas Freitas', 7, '07/03/2024')
    clinica1.marcar_sessao(3, 'Guilherme Silva', 7, '07/03/2024')

    # Sessão iniciada
    clinica1.iniciar_sessao(7)
    # Quando a sessão é iniciada, ela sai da lista de sessões marcadas(sessões_data)
    

    # Pacientes que chegaram, e já foram colocados na fila de espera.
    clinica1.colocar_paciente_na_fila(classes.sessao_iniciada_agora, 1)
    clinica1.colocar_paciente_na_fila(classes.sessao_iniciada_agora, 2)
    clinica1.colocar_paciente_na_fila(classes.sessao_iniciada_agora, 3)

    # Para visualizar o prontuário do "paciente atual" ou suas anotações, durante os testes do programa, naturalmente é necessário chamar um paciente para que ele se torne o "paciente atual" no consultório do dentista.
    clinica1.atender_proximo(classes.sessao_iniciada_agora)
        # Aqui o primeiro paciente da fila foi chamado para atendimento.

    # Armazenamento de anotações "paciente atual"(O primeiro da fila que foi chamado para atendimento, e agora está no consultório). Para que a opção 5 e 6 do menu do dentista seja visualizada com melhor clareza (Opção 5 - Ler primeira anotação do paciente atual e opção 6 - Ler última anotação do paciente atual)
    clinica1.anotar_prontuario(classes.sessao_iniciada_agora, 'O paciente está com Cáries Dentárias.')
    clinica1.anotar_prontuario(classes.sessao_iniciada_agora, 'O paciente está com Doença Periodontal.')
   