# Importa as ferramentas do Flask necessárias para criar o servidor, renderizar o HTML e capturar dados de formulários
from flask import Flask, render_template, request, redirect, url_for
import pymongo

# Inicializa a aplicação web
app = Flask(__name__)

# Estabelece a conexão com o servidor local do MongoDB e seleciona o banco de dados da Empresa Flora
cliente_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
banco_dados = cliente_mongo["empresa_flores_nosql"]

# Mapeia as coleções do banco de dados para facilitar o acesso nas funções abaixo
col_clientes = banco_dados["clientes"]
col_funcionarios = banco_dados["funcionarios"]
col_fornecedores = banco_dados["fornecedores"]
col_materiais = banco_dados["materiais"]
col_especialidades = banco_dados["especialidades"]

# Rota principal que carrega a tela inicial do sistema
@app.route('/')
def index():
    # Busca todos os documentos de cada coleção no banco de dados e converte em listas do Python
    clientes = list(col_clientes.find())
    funcionarios = list(col_funcionarios.find())
    fornecedores = list(col_fornecedores.find())
    materiais = list(col_materiais.find())
    especialidades = list(col_especialidades.find())
    
    # Envia as listas capturadas para o arquivo index.html desenhar as tabelas na tela
    return render_template('index.html', clientes=clientes, funcionarios=funcionarios, 
                           fornecedores=fornecedores, materiais=materiais, especialidades=especialidades)

# --- CLIENTES ---

# Rota ativada quando o usuário clica no botão de cadastrar cliente
@app.route('/adicionar_cliente', methods=['POST'])
def adicionar_cliente():
    # Monta um dicionário capturando os dados preenchidos no formulário usando request.form
    novo_cliente = {
        "cnpj": request.form['cnpj'],
        "razao_social": request.form['razao_social'],
        "nome_fantasia": request.form['nome_fantasia'],
        "telefone": request.form['telefone'],
        # Estrutura aninhada para salvar os detalhes do endereço em um sub-documento
        "endereco": {
            "logradouro": request.form['logradouro'], "numero": request.form['numero'],
            "complemento": request.form['complemento'], "bairro": request.form['bairro'],
            "cep": request.form['cep'], "cidade": request.form['cidade'], "estado": request.form['estado']
        }
    }
    # Grava o novo registro no banco de dados e recarrega a página principal
    col_clientes.insert_one(novo_cliente)
    return redirect(url_for('index'))

# Rota ativada quando o usuário clica em editar um cliente específico, utilizando path: para aceitar a barra do CNPJ
@app.route('/editar_cliente/<path:cnpj>', methods=['GET', 'POST'])
def editar_cliente(cnpj):
    # Se o método for POST, significa que o usuário enviou o formulário de edição preenchido
    if request.method == 'POST':
        dados_atualizados = {
            "razao_social": request.form['razao_social'], "nome_fantasia": request.form['nome_fantasia'],
            "telefone": request.form['telefone'],
            "endereco": {
                "logradouro": request.form['logradouro'], "numero": request.form['numero'],
                "complemento": request.form['complemento'], "bairro": request.form['bairro'],
                "cep": request.form['cep'], "cidade": request.form['cidade'], "estado": request.form['estado']
            }
        }
        # Utiliza o operador $set para substituir apenas os dados alterados, mantendo o CNPJ intacto
        col_clientes.update_one({"cnpj": cnpj}, {"$set": dados_atualizados})
        return redirect(url_for('index'))
    
    # Se o método for GET, busca o cliente no banco e carrega a tela de edição preenchida com os dados atuais
    item = col_clientes.find_one({"cnpj": cnpj})
    return render_template('editar.html', item=item, tipo='cliente')

# Rota ativada pelo botão de exclusão, utilizando path: para aceitar a barra do CNPJ
@app.route('/deletar_cliente/<path:cnpj>')
def deletar_cliente(cnpj):
    # Apaga o documento que possui o CNPJ correspondente ao clicado na tabela
    col_clientes.delete_one({"cnpj": cnpj})
    return redirect(url_for('index'))

# --- FUNCIONÁRIOS ---

@app.route('/adicionar_funcionario', methods=['POST'])
def adicionar_funcionario():
    novo_funcionario = {
        "matricula": request.form['matricula'], "cpf": request.form['cpf'],
        "nome": request.form['nome'], "telefone": request.form['telefone'], "turno": request.form['turno'],
        "endereco": {
            "logradouro": request.form['logradouro'], "numero": request.form['numero'],
            "complemento": request.form['complemento'], "bairro": request.form['bairro'],
            "cep": request.form['cep'], "cidade": request.form['cidade'], "estado": request.form['estado']
        }
    }
    col_funcionarios.insert_one(novo_funcionario)
    return redirect(url_for('index'))

@app.route('/editar_funcionario/<matricula>', methods=['GET', 'POST'])
def editar_funcionario(matricula):
    if request.method == 'POST':
        dados_atualizados = {
            "cpf": request.form['cpf'], "nome": request.form['nome'],
            "telefone": request.form['telefone'], "turno": request.form['turno'],
            "endereco": {
                "logradouro": request.form['logradouro'], "numero": request.form['numero'],
                "complemento": request.form['complemento'], "bairro": request.form['bairro'],
                "cep": request.form['cep'], "cidade": request.form['cidade'], "estado": request.form['estado']
            }
        }
        col_funcionarios.update_one({"matricula": matricula}, {"$set": dados_atualizados})
        return redirect(url_for('index'))
    item = col_funcionarios.find_one({"matricula": matricula})
    return render_template('editar.html', item=item, tipo='funcionario')

@app.route('/deletar_funcionario/<matricula>')
def deletar_funcionario(matricula):
    col_funcionarios.delete_one({"matricula": matricula})
    return redirect(url_for('index'))

# --- FORNECEDORES ---

@app.route('/adicionar_fornecedor', methods=['POST'])
def adicionar_fornecedor():
    novo_fornecedor = {
        "cnpj": request.form['cnpj'], "razao_social": request.form['razao_social'],
        "nome_fantasia": request.form['nome_fantasia'], "telefone": request.form['telefone'],
        "lista_materiais": request.form['lista_materiais'], "descricao_materiais": request.form['descricao_materiais'],
        "endereco": {
            "logradouro": request.form['logradouro'], "numero": request.form['numero'],
            "complemento": request.form['complemento'], "bairro": request.form['bairro'],
            "cep": request.form['cep'], "cidade": request.form['cidade'], "estado": request.form['estado']
        }
    }
    col_fornecedores.insert_one(novo_fornecedor)
    return redirect(url_for('index'))

# Rota ativada quando o usuário clica em editar um fornecedor específico, utilizando path: para aceitar a barra do CNPJ
@app.route('/editar_fornecedor/<path:cnpj>', methods=['GET', 'POST'])
def editar_fornecedor(cnpj):
    if request.method == 'POST':
        dados_atualizados = {
            "razao_social": request.form['razao_social'], "nome_fantasia": request.form['nome_fantasia'],
            "telefone": request.form['telefone'], "lista_materiais": request.form['lista_materiais'], 
            "descricao_materiais": request.form['descricao_materiais'],
            "endereco": {
                "logradouro": request.form['logradouro'], "numero": request.form['numero'],
                "complemento": request.form['complemento'], "bairro": request.form['bairro'],
                "cep": request.form['cep'], "cidade": request.form['cidade'], "estado": request.form['estado']
            }
        }
        col_fornecedores.update_one({"cnpj": cnpj}, {"$set": dados_atualizados})
        return redirect(url_for('index'))
    item = col_fornecedores.find_one({"cnpj": cnpj})
    return render_template('editar.html', item=item, tipo='fornecedor')

# Rota ativada pelo botão de exclusão, utilizando path: para aceitar a barra do CNPJ
@app.route('/deletar_fornecedor/<path:cnpj>')
def deletar_fornecedor(cnpj):
    col_fornecedores.delete_one({"cnpj": cnpj})
    return redirect(url_for('index'))

# --- MATERIAIS ---

@app.route('/adicionar_material', methods=['POST'])
def adicionar_material():
    # As funções float() e int() garantem que os valores numéricos sejam salvos corretamente no banco, e não como texto
    novo_material = {
        "codigo": request.form['codigo'], "nome": request.form['nome'],
        "preco_unitario": float(request.form['preco_unitario']), "unidade": request.form['unidade'],
        "preco_desconto": float(request.form['preco_desconto']), "qtd_minima": int(request.form['qtd_minima'])
    }
    col_materiais.insert_one(novo_material)
    return redirect(url_for('index'))

@app.route('/editar_material/<codigo>', methods=['GET', 'POST'])
def editar_material(codigo):
    if request.method == 'POST':
        dados_atualizados = {
            "nome": request.form['nome'], "preco_unitario": float(request.form['preco_unitario']),
            "unidade": request.form['unidade'], "preco_desconto": float(request.form['preco_desconto']),
            "qtd_minima": int(request.form['qtd_minima'])
        }
        col_materiais.update_one({"codigo": codigo}, {"$set": dados_atualizados})
        return redirect(url_for('index'))
    item = col_materiais.find_one({"codigo": codigo})
    return render_template('editar.html', item=item, tipo='material')

@app.route('/deletar_material/<codigo>')
def deletar_material(codigo):
    col_materiais.delete_one({"codigo": codigo})
    return redirect(url_for('index'))

# --- ESPECIALIDADES ---

@app.route('/adicionar_especialidade', methods=['POST'])
def adicionar_especialidade():
    nova_especialidade = {
        "codigo": request.form['codigo'], "nome": request.form['nome'], "custo_hora": float(request.form['custo_hora'])
    }
    col_especialidades.insert_one(nova_especialidade)
    return redirect(url_for('index'))

@app.route('/editar_especialidade/<codigo>', methods=['GET', 'POST'])
def editar_especialidade(codigo):
    if request.method == 'POST':
        dados_atualizados = {
            "nome": request.form['nome'], "custo_hora": float(request.form['custo_hora'])
        }
        col_especialidades.update_one({"codigo": codigo}, {"$set": dados_atualizados})
        return redirect(url_for('index'))
    item = col_especialidades.find_one({"codigo": codigo})
    return render_template('editar.html', item=item, tipo='especialidade')

@app.route('/deletar_especialidade/<codigo>')
def deletar_especialidade(codigo):
    col_especialidades.delete_one({"codigo": codigo})
    return redirect(url_for('index'))

# Comandos de inicialização que mantêm o servidor rodando e acompanhando alterações
if __name__ == '__main__':
    app.run(debug=True)