import pymongo

# Estabelece a conexão com o servidor local do MongoDB na porta padrão
cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleciona o banco de dados da Empresa Flora (ele é criado automaticamente se não existir)
banco_dados = cliente_mongo["empresa_flores_nosql"]

# Mapeia cada uma das coleções (equivalentes às tabelas no relacional) para variáveis do Python
col_clientes = banco_dados["clientes"]
col_funcionarios = banco_dados["funcionarios"]
col_fornecedores = banco_dados["fornecedores"]
col_materiais = banco_dados["materiais"]
col_especialidades = banco_dados["especialidades"]

def executar_crud_completo():
    print("Limpando banco de dados para nova execução...")
    # O comando delete_many com um filtro vazio {} apaga todos os documentos da coleção
    # Isso garante que cada vez que o script rodar, os dados não fiquem duplicados
    col_clientes.delete_many({})
    col_funcionarios.delete_many({})
    col_fornecedores.delete_many({})
    col_materiais.delete_many({})
    col_especialidades.delete_many({})

    print("Inserindo dados em todas as categorias (insertMany)...")
    # O insert_many recebe uma lista de dicionários Python e os insere como documentos JSON no banco
    col_clientes.insert_many([
        {"cnpj": "11.111.111/0001-11", "razao_social": "Jardins e Cia", "nome_fantasia": "Jardins", "telefone": "27999999999", "endereco": {"logradouro": "Rua A", "numero": "10", "complemento": "", "bairro": "Centro", "cep": "29000-000", "cidade": "Vitória", "estado": "ES"}},
        {"cnpj": "22.222.222/0001-22", "razao_social": "Verde Vida Paisagismo", "nome_fantasia": "Verde Vida", "telefone": "27888888888", "endereco": {"logradouro": "Rua B", "numero": "20", "complemento": "Loja 2", "bairro": "Jardim da Penha", "cep": "29060-000", "cidade": "Vitória", "estado": "ES"}}
    ])

    col_funcionarios.insert_many([
        {"matricula": "F001", "cpf": "123.456.789-00", "nome": "Carlos Silva", "telefone": "27777777777", "turno": "Manhã - 08h às 12h", "endereco": {"logradouro": "Rua C", "numero": "30", "complemento": "", "bairro": "Laranjeiras", "cep": "29165-000", "cidade": "Serra", "estado": "ES"}},
        {"matricula": "F002", "cpf": "987.654.321-11", "nome": "Ana Souza", "telefone": "27666666666", "turno": "Tarde - 12h às 16h", "endereco": {"logradouro": "Rua D", "numero": "40", "complemento": "Apt 101", "bairro": "Centro", "cep": "29160-000", "cidade": "Serra", "estado": "ES"}}
    ])

    col_fornecedores.insert_many([
        {"cnpj": "33.333.333/0001-33", "razao_social": "Agro Flores Insumos", "nome_fantasia": "Agro Flores", "telefone": "11999999999", "lista_materiais": ["Adubo", "Terra Preta"], "descricao_materiais": "Insumos básicos de plantio", "endereco": {"logradouro": "Av Central", "numero": "100", "complemento": "", "bairro": "Sé", "cep": "01000-000", "cidade": "São Paulo", "estado": "SP"}},
        {"cnpj": "44.444.444/0001-44", "razao_social": "Cia das Mudas Botanicas", "nome_fantasia": "Cia Mudas", "telefone": "31999999999", "lista_materiais": ["Muda de Rosa", "Muda de Girassol"], "descricao_materiais": "Mudas florais e ornamentais variadas", "endereco": {"logradouro": "Av Sul", "numero": "200", "complemento": "Galpão", "bairro": "Savassi", "cep": "30000-000", "cidade": "Belo Horizonte", "estado": "MG"}}
    ])

    col_materiais.insert_many([
        {"codigo": "MAT01", "nome": "Adubo Orgânico", "preco_unitario": 20.0, "unidade": "KG", "preco_desconto": 18.0, "qtd_minima": 10, "cnpj_fornecedor": "33.333.333/0001-33"},
        {"codigo": "MAT02", "nome": "Terra Preta", "preco_unitario": 10.0, "unidade": "KG", "preco_desconto": 9.0, "qtd_minima": 20, "cnpj_fornecedor": "33.333.333/0001-33"},
        {"codigo": "MAT03", "nome": "Muda de Rosa", "preco_unitario": 15.0, "unidade": "UN", "preco_desconto": 12.0, "qtd_minima": 5, "cnpj_fornecedor": "44.444.444/0001-44"}
    ])

    col_especialidades.insert_many([
        {"codigo": "ESP01", "nome": "Paisagista Pleno", "custo_hora": 150.0},
        {"codigo": "ESP02", "nome": "Jardineiro", "custo_hora": 80.0}
    ])

    print("\nDemonstrando o uso do FIND...")
    # O comando find busca documentos que atendam a um critério. Aqui, acessamos um campo aninhado usando a notação de ponto
    busca_es = col_funcionarios.find({"endereco.estado": "ES"})
    for func in busca_es:
        print(f"Funcionário Capixaba encontrado: {func['nome']} (Turno: {func['turno']})")

    print("\nDemonstrando as ATUALIZAÇÕES estudadas na disciplina...")
    # update_one: Atualiza o primeiro documento que bater com o filtro ("codigo": "MAT01")
    # $set altera o valor de um campo existente. $inc soma o valor informado (5.0) ao valor atual do campo
    col_materiais.update_one({"codigo": "MAT01"}, {"$set": {"nome": "Adubo Orgânico Premium"}, "$inc": {"preco_unitario": 5.0}})
    
    # update_many: Atualiza TODOS os documentos que atenderem ao filtro composto
    col_clientes.update_many({"endereco.cidade": "Vitória", "endereco.estado": "ES"}, {"$set": {"status_atendimento": "Prioritário"}})
    
    # $push adiciona um novo elemento ao final do array "lista_materiais" sem verificar se ele já existe
    col_fornecedores.update_one({"cnpj": "33.333.333/0001-33"}, {"$push": {"lista_materiais": "Fertilizante Químico"}})
    
    # $pull remove do array "lista_materiais" todas as ocorrências que forem iguais ao valor especificado
    col_fornecedores.update_one({"cnpj": "33.333.333/0001-33"}, {"$pull": {"lista_materiais": "Terra Preta"}})
    
    # $addToSet combinado com $each adiciona múltiplos itens a um array, mas apenas se eles ainda não existirem nele (evita duplicatas)
    col_fornecedores.update_one({"cnpj": "44.444.444/0001-44"}, {"$addToSet": {"lista_materiais": {"$each": ["Vaso de Cerâmica", "Semente", "Muda de Rosa"]}}})

    print("\nDemonstrando AGGREGATE e funções agregadas...")
    # O aggregate recebe uma lista (pipeline) de operações
    # $group agrupa documentos. Ao usar _id: None, ele agrupa todos os documentos em um só resultado
    # $avg calcula a média do custo_hora. $sum: 1 funciona como um contador para saber quantas especialidades existem
    pipeline_media = [{"$group": {"_id": None, "media_custo": {"$avg": "$custo_hora"}, "total_especialidades": {"$sum": 1}}}]
    resultado_media = list(col_especialidades.aggregate(pipeline_media))
    if resultado_media:
        print(f"Média de custo-hora das {resultado_media[0]['total_especialidades']} especialidades ativas: R$ {resultado_media[0]['media_custo']:.2f}")

    # Este pipeline de agregação é mais complexo, com 3 estágios:
    # 1. $lookup: Faz a junção (join) da coleção atual (fornecedores) com a coleção "materiais", cruzando cnpj com cnpj_fornecedor
    # 2. $match: Filtra o resultado da junção para manter apenas os fornecedores do estado de SP
    # 3. $project: Define o que será exibido na saída, calculando o tamanho ($size) do array de materiais cruzados gerado no lookup
    pipeline_lookup = [
        {"$lookup": {"from": "materiais", "localField": "cnpj", "foreignField": "cnpj_fornecedor", "as": "materiais_oferecidos"}},
        {"$match": {"endereco.estado": "SP"}},
        {"$project": {"razao_social": 1, "total_materiais_cadastrados": {"$size": "$materiais_oferecidos"}}}
    ]
    resultado_lookup = col_fornecedores.aggregate(pipeline_lookup)
    for forn in resultado_lookup:
        print(f"O fornecedor {forn['razao_social']} possui {forn.get('total_materiais_cadastrados', 0)} materiais fisicamente vinculados ao seu CNPJ no banco.")

    print("\nDemonstrando DELETIONS...")
    print("As funções de deleção estão inativadas no código para preservar os dados e permitir a visualização gráfica no MongoDB Compass.")
    
    # ATENÇÃO: PARA EXCLUIR REGISTROS, APAGUE A CERQUILHA (#) DO INÍCIO DAS LINHAS ABAIXO
    # delete_one: Apaga um único documento que atenda ao filtro
    # col_especialidades.delete_one({"codigo": "ESP02"})
    
    # delete_many com $in: Apaga todos os documentos cujo cnpj esteja dentro da lista informada na variável
    # var_cnpjs_para_excluir = ["44.444.444/0001-44"]
    # col_fornecedores.delete_many({"cnpj": {"$in": var_cnpjs_para_excluir}})

# Ponto de entrada do script Python que chama a função principal ao executar o arquivo
if __name__ == "__main__":
    executar_crud_completo()