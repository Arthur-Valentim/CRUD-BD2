# Trabalho de Banco de dados - Empresa de flores

**Desenvolvedores:** Arthur Valentim, Diego Rangel e Murilo Dias

## Motivação e Visão Geral
Este projeto acadêmico foi desenvolvido para demonstrar a aplicação prática da modelagem de dados relacional e a sua integração com a linguagem Python. O sistema simula o ambiente de back-end de uma prestadora de serviços de paisagismo, a Empresa Flora, resolvendo o problema de persistência e gerenciamento de informações críticas do negócio. A estruturação do banco segue rigorosamente normas de padronização de atributos e nomenclatura baseadas em domínios e qualificadores, garantindo um esquema de dados robusto e normalizado.

## Como o Sistema Funciona
A aplicação opera através de uma interface de linha de comando iterativa baseada em um controlador principal em Python que se comunica ativamente com um servidor MySQL. A arquitetura foi dividida em dois módulos independentes para separar as responsabilidades do código, onde um setor lida estritamente com as credenciais de acesso e a materialização das tabelas estruturais, enquanto o setor do aplicativo gerencia o fluxo de entrada de dados do usuário, executa o tratamento de exceções e envia as instruções de inserção de forma segura para a persistência no disco.

## Funcionalidades
O sistema oferece ferramentas de cadastro direcionadas para todas as entidades fundamentais do escopo da floricultura. O usuário consegue registrar perfis completos de clientes e funcionários com o detalhamento exigido de endereços residenciais subdivididos em logradouro, bairro, CEP e cidade. Além disso, a aplicação permite a inserção do catálogo de materiais disponíveis especificando valores unitários e regras de desconto, o cadastro de fornecedores com descrições em texto de seus catálogos de suprimentos e o registro do quadro de especialidades profissionais contendo o custo-hora de cada serviço prestado.

## Pré-requisitos
Para que o ambiente de execução funcione corretamente na sua máquina local, é obrigatório possuir a linguagem de programação Python previamente instalada, acompanhada da biblioteca de comunicação mysql-connector-python baixada através do gerenciador de pacotes nativo do seu terminal. É fundamental também ter o MySQL Community Server ativo e rodando com a senha de administrador devidamente configurada, além do MySQL Workbench instalado para facilitar o acompanhamento visual do banco de dados.

## Como Executar
O processo de inicialização ocorre em duas fases distintas executadas diretamente pelo terminal do seu editor de código. Primeiramente, você deve navegar até o script de criação localizado na pasta do banco e executá-lo para que o Python acesse o seu servidor local e crie o banco de dados vazio juntamente com todas as tabelas e suas respectivas chaves. Após o terminal retornar a mensagem de criação bem-sucedida, você deve executar o arquivo principal contido na pasta do aplicativo, o que fará com que o sistema inicie imediatamente a solicitação das ações de cadastro na sua tela.

## Como Testar
A validação do funcionamento do software é feita simulando a rotina de um operador do sistema de ponta a ponta. Com o aplicativo principal em execução no terminal, escolha uma das opções de registro oferecidas na tela e digite informações fictícias sempre que o console solicitar um novo campo numérico ou de texto. Após pressionar Enter na última variável e visualizar a mensagem de confirmação de cadastro no terminal, encerre o aplicativo e abra o seu MySQL Workbench. No gerenciador visual, basta abrir uma janela de consulta, executar uma instrução de seleção completa na tabela que você acabou de alimentar e comprovar que a linha de informações apareceu corretamente armazenada na grade de resultados.