# workshopbackend

# API DE CRUD SIMPLES COM DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) é um kit de ferramentas poderosas e flexíveis para criar APIs da Web.

## Exigências
- Python 
- Django REST Framework

## Instalação
```
	pip install django
	pip install djangorestframework
	pip install django-filter
	pip install pillow
  	pip install psycopg2
```

## Estrutura

A API tem como princípio adicionar filmes, assim como os usuários podem acessar dados do aplicativo usando os métodos HTTP - GET, POST, PUT, DELETE. 
Essa etapa de criação somente poderá ser feita por um user.

Nesse caso, como há um único recurso, utiliza-se o seguinte URL - http://127.0.0.1:8000/:

Endpoint |Método HTTP | Método CRUD | Resultado
-- | -- |-- |--
`` | GET | LER | Obter todos os filmes
`` | GET | LER | Obter um único filme
``| POST | CRIAR | Criar um novo filme
`` | PUT | ATUALIZAR | Atualizar um filme
`` | DELETE | EXCLUIR | Excluir um filme

## Instrução

### Crie o ambiente virtual
```
python -m venv venv
```
### Ative o venv
```bash
# linux: 

source venv/bin/activate

```

```bash
# windows: 

.\vevn\Scripts\activate

```

### Instale as dependências 
```
pip install -r requirements.txt
```
### Execute as migrações
```
./manage.py migrate
```
### Rode a aplicação
```
./manage.py runserver
```

A API tem algumas restrições:
-   Somente usuário cadastrado(superuser) pode criar e ver filmes.
-   Somente o criador de um filme pode atualizá-lo ou excluí-lo.
-   Solicitações não autenticadas não devem ter acesso.

API realizada interamente em python com django-rest-framework.
