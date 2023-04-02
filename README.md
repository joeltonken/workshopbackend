# workshopbackend

# API DE CRUD SIMPLES COM DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) é um kit de ferramentas poderosas e flexíveis para criar APIs da Web.

## Exigências
- Python 3.11
- Django REST Framework 3.14
- PostgreSQL Database

## Estrutura

A API tem como princípio adicionar filmes, além do usuário poder acessar dados do aplicativo usando os métodos HTTP - GET, POST, PUT, DELETE. 
Essa etapa de criação somente poderá ser feita por um user.

Nesse caso, como há um único recurso, utiliza-se o seguinte URL - http://127.0.0.1:8000/:

Endpoint |Método HTTP | Método CRUD | Resultado
-- | -- |-- |--
`` | GET | LER | Obter todos os filmes
`/id_gerado/` | GET | LER | Obter um único filme
``| POST | CRIAR | Criar um novo filme
`/id_gerado/` | PUT | ATUALIZAR | Atualizar um filme
`/id_gerado/` | DELETE | EXCLUIR | Excluir um filme

e a URL - http://127.0.0.1:8000/admin/ para logar com o superuser (ou criar um com o python manage.py createsuperuser):

-LOGIN: fabrica

-PASSWORD: 12345

Além disso, também há a funcionalidade de Filtro e Ordenação para ver e organizar os filmes cadastrados.

## Instrução

### Clonar o repositório do projeto:
```
git clone https://github.com/joeltonken/workshopbackend/tree/desafio
```
### Criar o ambiente virtual
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
-   Solicitações não autenticadas não devem ter acesso e receberão o aviso "As credenciais de autenticação não foram fornecidas."

API realizada inteiramente em python com django-rest-framework.
