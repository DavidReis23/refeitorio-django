# Sistema de Gerenciamento do Refeitório

Este projeto foi desenvolvido como parte da disciplina de Implementação de Projeto com Framework e Estratégia de Deploy. Trata-se de um sistema web desenvolvido com Django para gerenciar o funcionamento de um refeitório universitário, permitindo o agendamento de refeições, visualização de horários e cardápios semanais.

## 📊 Dependências do Projeto

- Python 3.10 ou superior
- Django 4.x

### Instalação das dependências:

```bash
pip install django
```

## ⚖️ Instalação e Execução Local

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/refeitorio_project.git
```

2. Acesse o diretório do projeto:
```bash
cd refeitorio_project
```

3. Crie um ambiente virtual e ative:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

4. Instale o Django:
```bash
pip install django
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Inicie o servidor local:
```bash
python manage.py runserver
```

7. Acesse no navegador:
```
http://127.0.0.1:8000
```

## 🚀 Procedimento de Deploy

Para publicação do sistema em produção (exemplo no Render.com ou Railway):

1. Suba o projeto no GitHub com `.gitignore` e `requirements.txt`
2. Gere o `requirements.txt` com:
```bash
pip freeze > requirements.txt
```
3. Crie o arquivo `Procfile` com o seguinte conteúdo:
```
web: gunicorn refeitorio_project.wsgi
```
4. Configure as variáveis de ambiente de produção (SECRET_KEY, DEBUG=False, ALLOWED_HOSTS)
5. Execute as migrações e colete os arquivos estáticos:
```bash
python manage.py migrate
python manage.py collectstatic
```
6. O deploy será feito automaticamente após o push para a branch principal.

## 🧰 Estrutura do Projeto

```
refeitorio_project/
├── agendamento_refeitorio/
│   ├── templates/
│   │   ├── index.html
│   │   ├── cardapio_semanal.html
│   │   ├── horario_semanal.html
│   │   └── agendamento.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── views.py
│   └── urls.py
├── refeitorio_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## ✍️ Engenharia de Software Aplicada

- Arquitetura MVC com Django
- Modularização por aplicação (separação entre frontend, backend e regras de negócio)
- Uso de templates para reaproveitamento de código
- Versionamento via Git e GitHub
- Separando estáticos (CSS) e templates (HTML)

---

A gente usou *Django* porque ele é um *framework completo* para desenvolvimento de aplicações web em Python. Aqui vão alguns motivos específicos do porque usamos ele no nosso projeto:

---

*1. Rápida criação de sites funcionais**
Django já vem com muitas funcionalidades prontas: sistema de URLs, templates HTML, integração com banco de dados e muito mais. Isso acelera o desenvolvimento.

---

*2. Organização e boas práticas**
Ele incentiva o uso do padrão **MVC (Model-View-Controller)** (no Django chamado de **MTV: Model-Template-View**), o que ajuda a manter o projeto bem organizado, modular e fácil de manter.

---

*3. Admin automático**
Com poucos comandos, você já tem um painel de administração pronto para gerenciar os dados da aplicação.

---

*4. Segurança**
Django vem com recursos de segurança integrados: proteção contra injeção SQL, CSRF, XSS e outros ataques comuns.

---

*5. Comunidade ativa**
Por ser amplamente usado, você encontra fácil documentação, tutoriais e ajuda em fóruns e grupos.

---