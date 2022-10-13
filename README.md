<h1 align="center"> 𝓣𝓻𝓪𝓫𝓪𝓵𝓱𝓸 𝓕𝓵𝓪𝓼𝓴 </h1>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## Descrição do Projeto
<p align="center"> Iremos realizar um portal acadêmico com implementações de gameficação. A gamificação trata de utilizar de processos e ferramentas como avatares, progressos, pontuação, rankings e prêmios dentro do ambiente estudantil.
</p>

Vamos progamar utilizando o pycharm como editor de código, utilizaremos o Flask para framework web, HTML e CSS para a construção da página web, Firebase para a hospedagem do site e por final será utilizado o GitHub para continuarmos a atualizar o projeto por meio de postagens.
<!--ts-->
* [Ferramentas](#Ferramentas)
<!--te-->
O PyCharm é o melhor IDE, você pode acessar a linha de comando, conectar-se a um banco de dados, criar um ambiente virtual e gerenciar seu sistema de controle de versão em um só lugar, economizando tempo por não precisar alternar constantemente entre janelas. 

O GitHub é um serviço baseado em nuvem que hospeda um sistema de controle de versão (VCS) chamado Git. Ele permite que os desenvolvedores colaborem e façam mudanças em projetos compartilhados enquanto mantêm um registro detalhado do seu progresso.

Flask é um framework de aplicação web WSGI leve. Ele foi projetado para tornar a introdução rápida e fácil, com a capacidade de escalar para aplicativos complexos.

O HTML e CSS são importantes para o desenvolvimento, HTML É uma linguagem baseada em marcação, onde marcamos os elementos para definir quais informações a página vai exibir. CSS é uma linguagem de folha de estilo composta por “camadas”, criado com o propósito de estilizar as páginas HTML, ou seja, definir a aparência das páginas, para deixá-las visualmente mais bonitas e agradáveis. 

O Firebase é uma plataforma de desenvolvimento de aplicativos com ferramentas para ajudar você a criar, expandir e monetizar seu aplicativo. 
* [Funcionalidades](#Funcionalidades)

Um sistema de ranking serve para identificar os melhores colocados na atividade, destacando aqueles que mais tem o dominio da matéria. Ajuda no sistema de competição e etimula interesse por parte dos participantes em se esforçar para alcançar melhores colocações.

O desbloqueio de novas fases e conquistas é mais uma funcionalidade que pode trazer alto engajamento dos alunos. Ao cumprir uma determinada atividade , trabalho ou prova, os alunos podem receber recompensas e consequentemente ele continua prosseguindo no mapa de atividades.

Uma estratégia muito presente nos jogos são as recompensas, ela é realizada de acordo com as atividades feitas. Este também é um recurso para estimular o interesse do participante, por isso precisa ser implementado de maneira totalmente estratégica para cumprir com o papel. 

Os pontos são considerados um sistema de recompensa que evidenciam aos alunos seu progresso na dinâmica e aumenta sua motivação com as práticas. Vamos utilizar o método de medalhas, tendo em cada atividade uma colocação de 3 lugares e medalhas de quem realizou ou nao as atividades.
 
 * [Primeiros passos](#Primeiros-passos)

Criamos algumas páginas em .html como a "homepage", "notas", "users", "login", "cadastro", que serão nossas prioridades iniciais.

![primeirospassos](https://user-images.githubusercontent.com/114426524/195723442-dde8dd20-4e24-4994-b256-ab20b8f2b637.png)

* [HTML](#HTML)
 
 Após definir as páginas começamos a dar uma "cara" a elas, através do html definimos cores, moldes, tabelas, dentro da página web.
![Html](https://user-images.githubusercontent.com/114426524/195723554-b307b936-5c95-4633-88e7-b7034c463ce4.png)
Como por exemplo o cadastro, que após algum tempo de trabalho conseguimos chegar a algo que todos concordaram que está bom.

* [Modelo Lógico BD](#Modelo-Lógico-BD)

Para que nosso banco de dados fosse bem estruturado, antes realizamos a criação do Modelo lógico através do Draw.io, onde ajudou posteriormente para que o banco seja conectado de forma eficaz.
![WhatsApp Image 2022-10-10 at 20 53 45](https://user-images.githubusercontent.com/114426524/195723727-70dd7160-a849-4130-9449-52b6d05616fa.jpeg)

* [Pré-requisitos](#Pré-requisitos)
asgiref==3.5.2
certifi==2022.6.15
click==8.1.3
colorama==0.4.5
distlib==0.3.5
Django==4.1
filelock==3.8.0
Flask==2.2.2
gunicorn==20.1.0
install==1.3.5
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
pipenv==2022.8.15
pippip==0.0.10
platformdirs==2.5.2
pygame==2.1.2
sqlparse==0.4.2
tzdata==2022.2
virtualenv==20.16.3
virtualenv-clone==0.5.7
Werkzeug==2.2.2
pip==22.2.2
pandas~=1.5.0
numpy~=1.23.3
SQLAlchemy
flask_sqlalchemy
mysql-connector-python==8.0.31

Localizada também na pasta requeriments que vem junto ao clone.

* [Como rodar a aplicação](#Como-rodar-a-aplicação)
No terminal, clone o projeto:
git clone https://github.com/logosart/trabalho_flask
Após isso verifique se todos os pré_requisitos foram instalados, abra a pasta main.py e de Run, após isso pegue o link gerado no terminal e entre.
