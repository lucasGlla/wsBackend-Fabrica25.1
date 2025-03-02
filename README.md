# Django Rest API - Dicebear Avatar Integration

Este projeto implementa uma API utilizando Django Rest Framework para integrar com a API Dicebear Avatar, permitindo que usuários e seus avatares sejam gerenciados. Ele oferece endpoints para criar usuários, associar avatares a esses usuários e obter o URL do avatar.

## Requisitos

- Python 3.11
- Django 3.11 ou superior
- Django Rest Framework
- Dicebear Avatar API para geração de avatares

## Instalação

1. Clone este repositório:

git clone https://github.com/lucasGlla/wsBackend-Fabrica25.1

2. Instale as dependências:

pip install -r requirements.txt

3. Execute as migrações para criar as tabelas no banco de dados:

python manage.py makemigrations
python manage.py migrate


4. Inicie o servidor de desenvolvimento:

python manage.py runserver

O projeto estará disponível em http://localhost:8000/api/

