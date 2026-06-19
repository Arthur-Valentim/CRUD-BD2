from MySql.db_config import get_connection

def inserir_cliente():
    # Solicita os dados do cliente via terminal e realiza a inserção na tabela Clien
    print("Cadastro de Novo Cliente")
    cnpj = input("CNPJ: ")
    razao_social = input("Razão Social: ")
    nome_fantasia = input("Nome Fantasia: ")
    telefone = input("Telefone: ")
    tipo_logradouro = input("Tipo de Logradouro (Rua, Avenida, etc): ")
    nome_logradouro = input("Nome do Logradouro: ")
    numero = input("Número: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado (UF): ")

    conn = None
    try:
        # Estabelece conexão com o banco e prepara o comando SQL de inserção
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO Clien (numCNPJClien, dscRzSocClien, dscNomFanClien, numTelefClien, dscTipLogClien, 
                           dscNomLogClien, numLograClien, dscComplClien, dscBairroClien, numCEPClien, 
                           dscCidadClien, dscEstadClien)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (cnpj, razao_social, nome_fantasia, telefone, tipo_logradouro, nome_logradouro, 
                   numero, complemento, bairro, cep, cidade, estado)
        # Executa a query passando as variáveis recebidas do usuário e confirma a transação
        cursor.execute(sql, valores)
        conn.commit()
        print("Cliente inserido com sucesso no banco de dados!")
    except Exception as e:
        # Captura e exibe qualquer erro que ocorra durante o processo de banco de dados
        print(f"Ocorreu um erro ao inserir o cliente: {e}")
    finally:
        # Garante que a conexão seja encerrada de forma segura ao final da operação
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def inserir_funcionario():
    # Coleta os dados de um novo funcionário e os insere na tabela Funci padronizada
    print("Cadastro de Novo Funcionario")
    matricula = input("Matricula: ")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    turno = input("Turno (manha, tarde, noite): ")
    tipo_logradouro = input("Tipo de Logradouro (Rua, Avenida, etc): ")
    nome_logradouro = input("Nome do Logradouro: ")
    numero = input("Número: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado (UF): ")

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO Funci (numMatriFunci, numCPFFunci, nomPessoFunci, numTelefFunci, dscTurnoFunci, 
                           dscTipLogFunci, dscNomLogFunci, numLograFunci, dscComplFunci, dscBairroFunci, 
                           numCEPFunci, dscCidadFunci, dscEstadFunci)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (matricula, cpf, nome, telefone, turno, tipo_logradouro, nome_logradouro, 
                   numero, complemento, bairro, cep, cidade, estado)
        cursor.execute(sql, valores)
        conn.commit()
        print("Funcionario inserido com sucesso no banco de dados!")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir o funcionario: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def inserir_fornecedor():
    # Recebe os dados do fornecedor, incluindo a lista de materiais, e insere na tabela Forne
    print("Cadastro de Novo Fornecedor")
    cnpj = input("CNPJ: ")
    razao_social = input("Razão Social: ")
    nome_fantasia = input("Nome Fantasia: ")
    telefone = input("Telefone: ")
    tipo_logradouro = input("Tipo de Logradouro (Rua, Avenida, etc): ")
    nome_logradouro = input("Nome do Logradouro: ")
    numero = input("Número: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado (UF): ")
    lista_materiais = input("Descricao dos tipos de materiais fornecidos: ")

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO Forne (numCNPJForne, dscRzSocForne, dscNomFanForne, numTelefForne, dscTipLogForne, 
                           dscNomLogForne, numLograForne, dscComplForne, dscBairroForne, numCEPForne, 
                           dscCidadForne, dscEstadForne, dscListaForne)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (cnpj, razao_social, nome_fantasia, telefone, tipo_logradouro, nome_logradouro, 
                   numero, complemento, bairro, cep, cidade, estado, lista_materiais)
        cursor.execute(sql, valores)
        conn.commit()
        print("Fornecedor inserido com sucesso no banco de dados!")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir o fornecedor: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def inserir_material():
    # Captura as propriedades numéricas e textuais de um material e salva na tabela Mater
    print("Cadastro de Novo Material")
    codigo = input("Codigo do material: ")
    nome = input("Nome do material: ")
    preco_unitario = float(input("Preco unitario (ex: 10.50): "))
    unidade = input("Unidade (ex: KG, UN): ")
    preco_desconto = float(input("Preco com desconto (ex: 9.00): "))
    qtd_minima = int(input("Quantidade minima para obter desconto: "))

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO Mater (codIdentMater, nomPessoMater, valUnitMater, dscUnidaMater, valDescMater, qtdMinimMater)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (codigo, nome, preco_unitario, unidade, preco_desconto, qtd_minima)
        cursor.execute(sql, valores)
        conn.commit()
        print("Material inserido com sucesso no banco de dados!")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir o material: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def inserir_especialidade():
    # Registra um novo tipo de especialista com seu respectivo custo-hora na tabela Espec
    print("Cadastro de Nova Especialidade")
    codigo = input("Codigo da especialidade: ")
    nome = input("Nome da especialidade: ")
    valor_hora = float(input("Custo-hora (ex: 150.00): "))

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO Espec (codIdentEspec, nomPessoEspec, valHoraEspec)
        VALUES (%s, %s, %s)
        """
        valores = (codigo, nome, valor_hora)
        cursor.execute(sql, valores)
        conn.commit()
        print("Especialidade inserida com sucesso no banco de dados!")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir a especialidade: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def iniciar_sistema():
    # Controla o fluxo principal do programa mantendo um loop para escolha de ações pelo usuário
    while True:
        opcao = input("Digite a opcao (1-Cliente, 2-Funcionario, 3-Fornecedor, 4-Material, 5-Especialidade, 0-Sair): ")
        if opcao == '1':
            inserir_cliente()
        elif opcao == '2':
            inserir_funcionario()
        elif opcao == '3':
            inserir_fornecedor()
        elif opcao == '4':
            inserir_material()
        elif opcao == '5':
            inserir_especialidade()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opcao invalida, tente novamente.")
        print()

# Ponto de entrada da aplicação, executa o menu principal ao rodar o script
if __name__ == "__main__":
    iniciar_sistema()