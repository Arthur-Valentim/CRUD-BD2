# Trabalho de Banco de Dados - Empresa Flora

**Desenvolvedores:** Arthur Valentim, Diego Rangel e Murilo Dias

## Motivação e Visão Geral

Este projeto acadêmico foi concebido para demonstrar a aplicação prática e o contraste entre a modelagem de dados relacional e a flexibilidade dos repositórios não relacionais. O sistema atua como o alicerce de gerenciamento da Empresa Flora, uma prestadora de serviços de paisagismo. 

A empresa necessita de um controle rigoroso sobre os registros de clientes, funcionários, fornecedores, estoque de materiais e quadro de especialidades profissionais. Para atender a essa demanda, a arquitetura da aplicação foi dividida em dois ecossistemas independentes. Essa separação isola as operações do MySQL e do MongoDB em diretórios específicos, facilitando a avaliação técnica de cada exigência do estudo de caso corporativo.

## O Ambiente Relacional (MySQL)

A primeira vertente do software explora o paradigma relacional utilizando o servidor MySQL através de uma interface de linha de comando. Nesta etapa, estruturada na pasta interna do projeto, o controlador principal desenvolvido em Python comunica-se com o banco de dados. O objetivo é garantir a integridade referencial e o preenchimento de dados padronizados no terminal. 

Este ambiente relacional exige a execução prévia do script de materialização das tabelas. Isso configura o esquema vazio antes que o aplicativo iterativo seja iniciado. Com a estrutura pronta, o usuário pode inserir informações simuladas e comprovar a gravação consultando o gerenciador gráfico do banco.

## O Ambiente Não Relacional (MongoDB)

A segunda vertente eleva o projeto ao paradigma orientado a documentos utilizando o MongoDB. Esta fase é integrada a uma interface gráfica web intuitiva, desenvolvida com o microframework Flask. Localizada na sua respectiva pasta, a aplicação web substitui as interações de terminal por um painel de controle interativo acessado diretamente pelo navegador. 

A interface foi desenhada para lidar perfeitamente com a natureza flexível do NoSQL. O sistema realiza o ciclo completo de operações de criação, leitura, atualização e deleção para todas as cinco entidades de negócio. Dados complexos, como endereços completos e catálogos de fornecimento, são embutidos diretamente dentro de documentos JSON. Isso elimina a necessidade de fragmentação ou junções complexas durante a navegação.

## Consultas e Operações Avançadas

Para atestar o domínio de operações avançadas exigidas pela disciplina, o diretório do MongoDB abriga também um script de execução autônoma. Este arquivo é dedicado exclusivamente à manipulação de coleções via código estrito. 

O script realiza atualizações em massa utilizando operadores de modificação de arrays e cálculos automáticos de incremento. Além disso, o código constrói pipelines de agregação complexos. A demonstração técnica culmina em uma junção relacional programada entre fornecedores e seus respectivos materiais. O sistema calcula quais itens estão órfãos para a execução de uma limpeza condicional automatizada diretamente no motor do banco de dados.

## Pré-requisitos e Execução do Sistema

O funcionamento pleno deste ecossistema exige a preparação do ambiente de execução local. É necessária a instalação da linguagem Python e o download das bibliotecas mysql-connector-python, pymongo e flask através do terminal do editor de código. 

É obrigatório manter o serviço do MySQL Community Server operando paralelamente ao MongoDB Compass, com as portas padrão devidamente liberadas para conexões locais. A inicialização da interface web requer a execução do servidor Python que hospedará as rotas no endereço local da máquina. Por fim, a verificação das lógicas de agregação deve ser conferida rodando o arquivo de operações avançadas e inspecionando os resultados físicos diretamente no console do desenvolvedor.