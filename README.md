### Olar, 

Esté é um sistema de contas a pagar, para o Gersonzinho, controlar o que as filiais dele estão fazendo.

Para instalar o sistema e rodar, é necessário seguir as instruções abaixo:

* 1º Baixar o projeto e ter um ambiente que rode Python!

* 2º Assim que baixar o projeto, é necessário baixar suas dependências:

	* 2.1. Entre na pasta do sistema baixado

`$ cd ConPag/`

	* 2.2. Instalar e Ativar o ambiente virtualenv

`$ python3 -m venv .venv`

`$ source .venv/bin/activate`

	* 2.3. Após ativado o ambiente virtualenv, é necessário baixar as dependências do sistema

`$ .venv/bin/pip3 install -r requiriments.txt`

* 3º Instalando as dependências, é necessário instalar a BASE DE DADOS e criar um "SUPER USUÁRIO (ADMIN)"

`$ .venv/bin/python3 manage.py makemigrations`

`$ .venv/bin/python3 manage.py migrate`

`$ .venv/bin/python3 manage.py createsuperuser`

* 4º Após fazer os passos acimas, que śão de extrema necessidade, vamos iniciar o sistema e ver como funciona

`$ .venv/bin/python3 manage.py runserver`

* 5º Assim que o sistema "subir", ele irá informar em qual "DOMINIO" ele foi inciado

`(acesse a URI 126.0.1:8000)`

Vooooooooooooooia lá! O sistema já está rodando! 

Agora... vamos configurar?

Assim que abrir a página, ele vai abrir com um formulário de LOGIN, esse formulário é para etrar no sistema. Porém, precisamos
acessar a area administrativa para configurar os usuários que teram acesso ao sistema, cadastras as filiais e suas contas.
Para fazer tudo isso, vamos adicionar do lado da URI o /admin/ 

`127.0.0.1:8000/admin/`

Assim que acessar, o sistema irá abrir um fomulário da área administrativa. Vamos colocar o nosso usuário ADMIN que criamos no passo acima.
Realizando o LOGIN, podemos visualizar uma listagem com várias tabelas.


Vamos primeiramente adicionar um ESTABELECIMENTO, clique no botão adicionar do lado, preencha o formulário e salve.
Após criar um ESTABELECIMENTO, vamos criar uma CONTA para ele, vamos fazer o mesmo procedimento que fizemos com o ESTABELECIMENTO.
Assim que criar uma CONTA, vamos criar USUARIO para acessar o sistema.
O USUARIO é responsṕavel por fazer os lançamentos de contas a pagar dentro da FILIAL.
Agora vamos fazer exatamente a mesma coisa, só que em USUÁRIOS no CORE. Vamos ligar nosso usuário ao nosso estabelecimento.

Cadastrou o usário e adicionou um Estabelecimento para ele? Sim? Certo!!!
Vamos sair da área administrativa e vamos voltar para a URI 127.0.0.1:8000/.

Após preencher o formulário de login do sistema, vamos encontrar a primeira página do sistema.


Agora nosso sistema está rodando e você já possui um usuário para fazer os lançamentos de contas a pagar necessários.

=)