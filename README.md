# Gestão de RH

Projeto em Django para Gestão de Recursos Humanos.
Aplicacao rodando em: http://3.141.127.37:8000/

## Visão Geral

Este projeto é uma aplicação web desenvolvida com Django, focada na gestão de recursos humanos. Ele inclui funcionalidades como gerenciamento de funcionários, administração de departamentos e controle de documentos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `apps/`: Contém os aplicativos Django da aplicação.
- `gestao_rh/`: Contém as configurações principais do projeto Django.
- `media/`: Armazena documentos e outros arquivos enviados pelos usuários.
- `static/`: Arquivos estáticos utilizados no front-end, como CSS e JavaScript.
- `templates/`: Arquivos de templates HTML.
- `manage.py`: Script de gerenciamento do Django.
- `requirements.txt`: Lista de dependências do projeto.

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS (Bootstrap)
- JavaScript

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

### Passos para Executar

1. Clone o repositório:
    ```sh
    git clone https://github.com/dnsouzadev/gestao_rh.git
    cd gestao_rh
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Execute o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

6. Acesse o aplicativo no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para mais informações, entre em contato pelo email [workdndsza@gmail.com](mailto:workdndsza@gmail.com).
