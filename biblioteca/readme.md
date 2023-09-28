![Alt text](https://th.bing.com/th/id/OIP.sXcc0k0bH1Zy9R22hm8p8AHaEO?w=284&h=180&c=7&r=0&o=5&pid=1.7 "a title")

# Passo a passo para rodar o aplicativo:

## Comandos
- digitar códigos somente no Prompt de Comando, evitar PowerShell

## Desenvolvimento virtual
- Criar ambiente virtual de desenvolvimento: ````python -m venv .env````
- Ativar desenvolvimento virtual: ````.env/Scripts/activate>````

## Dependencias
- Digitar: ````cd ../..````
- Instalar dependencias: ````pip install django psycopg2````

## Iniciar projeto django
Digitar: ````py -m django startapp app````
Digitar: ````py -m django startproject config .````

## Alterações de configuração
- Alterar settings.py (INSTALLED_APPS, lang, UTC e configurações do banco de dados)

## Tabelas
- Criar tabelas no models.py
- Importar tabelas no arquivo admin.py: ````from .models import *```` ````admin.site.register(NOME_DA_MODEL)````
- Criar banco de dados no pgAdmin: clicar com o botao direito em databases > create > database > inserir nome do bd

## Banco de dados
- Digitar: ````python manage.py migrate````
- Digitar: ````python manage.py migrate````
- Digitar: ````python manage.py makemigrations````

## Usuário administrador
- Digitar: ````python manage.py createsuperuser````

## Iniciar servidor
- Digitar: ````python manage.py runserver````
