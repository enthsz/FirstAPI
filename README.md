# CRUD API com Django REST Framework e SimpleJWT

## Descrição do Projeto

Este projeto é uma API de CRUD (Create, Read, Update, Delete) desenvolvida com Django REST Framework, que utiliza JWT (JSON Web Token) para autenticação através do SimpleJWT. O objetivo deste projeto é fornecer uma API básica que permita a criação, leitura, atualização e exclusão de registros, garantindo a segurança dos endpoints com autenticação baseada em token.

## Funcionalidades

- **Autenticação JWT**: Implementação de autenticação usando JSON Web Tokens para proteger os endpoints.
- **CRUD Completo**: Endpoints para criar, ler, atualizar e excluir registros.
- **Filtros e Paginação**: Suporte para filtros de busca e paginação dos resultados.

## Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento rápido e seguro.
- **Django REST Framework**: Ferramenta poderosa e flexível para construção de APIs.
- **SimpleJWT**: Biblioteca para implementação de autenticação baseada em JWT.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- virtualenv (opcional, mas recomendado)

### Passo a Passo para Configuração

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-projeto.git
    cd seu-projeto
    ```

2. **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências do Django e do Django REST Framework:**
    ```bash
    pip install django djangorestframework
    ```

4. **Instale o SimpleJWT:**
    ```bash
    pip install djangorestframework_simplejwt
    ```

5. **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário (opcional, mas recomendado para acessar o admin do Django):**
    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

## Endpoints Principais

### Autenticação

- **Obter Token:**
    - URL: `/api/token/`
    - Método: `POST`
    - Corpo da Requisição:
      ```json
      {
          "username": "seu_username",
          "password": "sua_senha"
      }
      ```
    - Resposta:
      ```json
      {
          "refresh": "token_de_refresh",
          "access": "token_de_acesso"
      }
      ```

- **Renovar Token:**
    - URL: `/api/token/refresh/`
    - Método: `POST`
    - Corpo da Requisição:
      ```json
      {
          "refresh": "token_de_refresh"
      }
      ```
    - Resposta:
      ```json
      {
          "access": "novo_token_de_acesso"
      }
      ```

### Operações CRUD

- **Criar um Registro:**
    - URL: `/create-task/`
    - Método: `POST`
    - Cabeçalho: `Authorization: Bearer <token_de_acesso>`
    - Corpo da Requisição:
      ```json
      {
          "campo1": "valor1",
          "campo2": "valor2"
      }
      ```
    - Resposta:
      ```json
      {
          "id": 1,
          "campo1": "valor1",
          "campo2": "valor2"
      }
      ```

- **Listar Registros:**
    - URL: `http://127.0.0.1:8000/
    - Método: `GET`
    - Cabeçalho: `Authorization: Bearer <token_de_acesso>`
    - Resposta:
      ```json
      [
          {
              "id": 1,
              "campo1": "valor1",
              "campo2": "valor2"
          },
          {
              "id": 2,
              "campo1": "valor1",
              "campo2": "valor2"
          }
      ]
      ```

- **Detalhar um Registro:**
    - URL: `/task-delete/(Nome certo da tarefa)`
    - Método: `GET`
    - Cabeçalho: `Authorization: Bearer <token_de_acesso>`
    - Resposta:
      ```json
      {
          "id": 1,
          "campo1": "valor1",
          "campo2": "valor2"
      }
      ```

- **Atualizar um Registro:**
    - URL: `/task-delete/items/(Nome certo da tarefa)`
    - Método: `PUT`
    - Cabeçalho: `Authorization: Bearer <token_de_acesso>`
    - Corpo da Requisição:
      ```json
      {
          "campo1": "novo_valor1",
          "campo2": "novo_valor2"
      }
      ```
    - Resposta:
      ```json
      {
          "id": 1,
          "campo1": "novo_valor1",
          "campo2": "novo_valor2"
      }
      ```

- **Excluir um Registro:**
    - URL: `/task-delete/(Nome certo da tarefa/)`
    - Método: `DELETE`
    - Cabeçalho: `Authorization: Bearer <token_de_acesso>`
    - Resposta:
      ```json
      {
          "detail": "Registro excluído com sucesso."
      }
      ```

## Considerações Finais

Este projeto foi desenvolvido para demonstrar a integração entre Django REST Framework e SimpleJWT para a construção de uma API segura e funcional. Sinta-se à vontade para contribuir com melhorias ou relatar problemas através das issues no repositório.

