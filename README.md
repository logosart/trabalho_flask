<h1 align="center"> 𝓣𝓻𝓪𝓫𝓪𝓵𝓱𝓸 𝓕𝓵𝓪𝓼𝓴 </h1>

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)

# **Descrição do Projeto**
<p align="center"> Iremos realizar um portal acadêmico com implementações de gameficação. A gamificação trata de utilizar de processos e ferramentas como avatares, progressos, pontuação, rankings e prêmios dentro do ambiente estudantil.
</p>

Vamos progamar utilizando o pycharm como editor de código, utilizaremos o Flask para framework web, HTML e CSS para a construção da página web, Firebase para a hospedagem do site e por final será utilizado o GitHub para continuarmos a atualizar o projeto por meio de postagens.

## **Tecnologias utilizadas**

O PyCharm é o melhor IDE, você pode acessar a linha de comando, conectar-se a um banco de dados, criar um ambiente virtual e gerenciar seu sistema de controle de versão em um só lugar, economizando tempo por não precisar alternar constantemente entre janelas. 

O GitHub é um serviço baseado em nuvem que hospeda um sistema de controle de versão (VCS) chamado Git. Ele permite que os desenvolvedores colaborem e façam mudanças em projetos compartilhados enquanto mantêm um registro detalhado do seu progresso.

Flask é um framework de aplicação web WSGI leve. Ele foi projetado para tornar a introdução rápida e fácil, com a capacidade de escalar para aplicativos complexos.

O HTML e CSS são importantes para o desenvolvimento, HTML É uma linguagem baseada em marcação, onde marcamos os elementos para definir quais informações a página vai exibir. CSS é uma linguagem de folha de estilo composta por “camadas”, criado com o propósito de estilizar as páginas HTML, ou seja, definir a aparência das páginas, para deixá-las visualmente mais bonitas e agradáveis. 

O Firebase é uma plataforma de desenvolvimento de aplicativos com ferramentas para ajudar você a criar, expandir e monetizar seu aplicativo. 
## **Funcionalidades**

Um sistema de ranking serve para identificar os melhores colocados na atividade, destacando aqueles que mais tem o dominio da matéria. Ajuda no sistema de competição e etimula interesse por parte dos participantes em se esforçar para alcançar melhores colocações.

O desbloqueio de novas fases e conquistas é mais uma funcionalidade que pode trazer alto engajamento dos alunos. Ao cumprir uma determinada atividade , trabalho ou prova, os alunos podem receber recompensas e consequentemente ele continua prosseguindo no mapa de atividades.

Uma estratégia muito presente nos jogos são as recompensas, ela é realizada de acordo com as atividades feitas. Este também é um recurso para estimular o interesse do participante, por isso precisa ser implementado de maneira totalmente estratégica para cumprir com o papel. 

Os pontos são considerados um sistema de recompensa que evidenciam aos alunos seu progresso na dinâmica e aumenta sua motivação com as práticas. Vamos utilizar o método de medalhas, tendo em cada atividade uma colocação de 3 lugares e medalhas de quem realizou ou nao as atividades.
 
 ## **Primeiros Passos**

Criamos algumas páginas em .html como a "homepage", "notas", "users", "login", "cadastro", que serão nossas prioridades iniciais.

![primeirospassos](https://user-images.githubusercontent.com/114426524/195723442-dde8dd20-4e24-4994-b256-ab20b8f2b637.png)

## **HTML**
 
 Após definir as páginas começamos a dar uma "cara" a elas, através do html definimos cores, moldes, tabelas, dentro da página web.
![Html](https://user-images.githubusercontent.com/114426524/195723554-b307b936-5c95-4633-88e7-b7034c463ce4.png)

Como por exemplo o cadastro, que após algum tempo de trabalho conseguimos chegar a algo que todos concordaram que está bom.

## **Banco de dados**
Estrutura do banco de dados:
{
  "Alunos": {
    "AlMatricula": 0, /Int/
    "IdCurso": 0,  /Int/
    "IdPessoa": 0 /Int/
  },
  
  "Avaliações": {
    "AlMatricula": 0, /Int/
    "IdAvaliação": 0, /Int/
    "IdCurso": 0, /Int/
    "IdDisciplina": 0, /Int/
    "Nota": 0  /Int/
  },
  
  "Curso": {
    "IdCurso": 0, /Int/
    "Nome": "", /string/
    "Semestre": 0 /Int/
  },
  
  "Disciplina": {
    "Curso": "", /string/
    "IdCurso": 0, /Int/
    "IdDiscplina": 0, /Int/
    "Nome": "", /string/
    "ProfMatricula": 0 /Int/
  },
  
  "Matricula": {
    "AlMatricula": 0, /Int/
    "IdCurso": 0, /Int/
    "IdMatricula": 0 /Int/
  },
  
  "Pessoa": {
    "CPF": 0, /Int/
    "DtNasc": "", /Int/
    "IdPessoa": 0, /Int/ 
    "Nome": "", /string/
    "Sexo": "" /string/
  },
  
  "Professor": {
    "Graduação": 0, /Int/
    "IdPessoa": 0, /Int/
    "ProfMatricula": 0 /Int/
  }
}

### **Modelo-Lógico-BD**

Para que nosso banco de dados fosse bem estruturado, antes realizamos a criação do Modelo lógico através do Draw.io, onde ajudou posteriormente para que o banco seja conectado de forma eficaz.
![WhatsApp Image 2022-10-10 at 20 53 45](https://user-images.githubusercontent.com/114426524/195723727-70dd7160-a849-4130-9449-52b6d05616fa.jpeg)


### **Pré requisitos**
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

### **Como rodar a aplicação**
No terminal, clone o projeto:
git clone https://github.com/logosart/trabalho_flask
Após isso verifique se todos os pré_requisitos foram instalados, abra a pasta main.py e de Run, após isso pegue o link gerado no terminal e entre.

## **Padronização e Permissão de rotas**

**Rota de acesso para página inicial**

http://127.0.0.1:5000/

**Rota de acesso dos usuários para realizarem seu login**

http://127.0.0.1:5000/login

**Rota de acesso dos usuários para realizarem o cadastro**

http://127.0.0.1:5000/cadastro

**Rota de acesso para cadastro do professor**

http://127.0.0.1:5000/cadastro_professor

**Rota de acesso do usuário onde só ele poderá ver suas notas e médias**

http://127.0.0.1:5000/notas

**Rota de acesso do usuário para entrar no seu perfil**

http://127.0.0.1:5000/users/%3Cnome_usuario%3E

## **Histórias de usuário**

### **História 1: Cadastro**

Eu como usuário desejo me cadastrar no site para que eu possa utilizá-lo

**Cenário 1: Cadastrar**

Dado que o usuário deseja se cadastrar
E ele seleciona para se cadastrar
E preenche todos os dados obrigatórios
Então o sistema Irá cadastrar os dados do usuário
E ele será levado para a Homepage 

**Cenário 2: Senha fraca**

Dado que o usuário tenha preenchido todos os dados de cadastro
E a senha possuir poucos caracteres
Então o sistema apresenta a mensagem "Senha fraca"
E retorna para o usuário escrever novamente 

### **História 2: Login**

Eu como usuário desejo realizar o login no site para que eu possa utiliza-lo

**Cenário 1: Login**

Dado que o usuário já possua uma conta
E seleciona para realizar o login 
E preencha todos os campos obrigatórios corretamente
Então o sistema mandará o usuário para a Homepage

**Cenário 2: Senha incorreta**

Dado que o usuário tenha preenchido todos os campos de login
E a senha tenha sido digitada incorretamente
Então o sistema apresentará a seguinte mensagem "Senha incorreta"
E retorna para o usuário escrever novamente 

**Cenário 3: Email incorreto**

Dado que o usuário tenha preenchido todos os campos de login
E o email tenha sido digitado incorretamente
Então o sistema apresentará a seguinte mensagem "Email incorreto"
E retorna para o usuário escrever novamente 

**Cenário 4: Esqueci a senha**

Dado que o usuário não se lembre de sua senha
E tenha clicado na mensagem "esqueci minha senha"
Então o sistema irá mandar um Email para o usuário
Quando o usuário preencher a mudança de email
Então sua senha de acesso será trocada

### **História 3: Perfil**

Eu como usuário desejo visualizar meu perfil para ver minhas informações

**Cenário 1: Visualizar perfil**

Dado que o usuário já tenha se cadastrado
E deseja visualizar seu perfil
E tenha clicado para isso
Então o sistema apresentará o perfil do usuário com suas informações

**Cenário 2: Mudar email**

Dado que o usuário deseja mudar seu email
E tenha clicado para isso
Então o sistema apresentará um campo de mudança de email
Quando o usuário preencher com seu antigo email e com o novo email 
E confirmar
Então o email de acesso será mudado

**Cenário 3: Mudar senha**

Dado que o usuário deseja mudar sua senha
E tenha clicado para isso
Então o sistema apresentará um campo de mudança de senha
Quando o usuário preencher com sua antiga senha e com a que deseja para a mudança
E confirmar
Então a senha de acesso será mudado

### **História 4: Atividades**

Eu como usuário desejo realizar atividades para ganhar pontos

**Cenário1: Enviar Atividade**

Dado que o usuário tenha entrado no campo de atividades
E tenha alguma atividade para ser realizada
E o usuário tenha enviado a atividade 
Então o sistema apresentará a seguinte mensagem "Atividade enviada"
E retorna o usuário para a pagina de atividades

**Cenário 2: Distribuição de pontos de atividade**

Dado que o usuário tenha realizado uma atividade
E tenha recebido um nota para ela
Então o sistema através de um calculo, distribuirá os pontos para esse aluno

**Cenário 3: Medalhas**

Dado que o usuário tenha realizado as atividades 
Então baseado nos pontos dos outros alunos os 3 primeiros colocados receberão uma medalha
E ficará salva no perfil do aluno

### **História 5: Notas**

Eu como usuário desejo visualizar minhas notas para saber se atingi a média

**Cenário 1: Ver notas**

Dado que o usuário queira ver suas notas
E tenha clicado para isso
Então o sistema o redirecionará para a página de notas

## **Regras de negócio**

1.	Para realizar o cadastro no site, o usuário deve inserir todas as informações corretas, caso contrário receberá uma mensagem de erro de cadastro na tela.
2.	No login, o usuário deve inserir o email e a senha cadastrado, caso informe as informações erradas, receberá uma mensagem de erro de login na tela
3.	Se o usuário esquecer da senha, deverá clicar no botão "Esqueceu a senha" para recupera-la.
4.	O sistema de gamificação apresentará um ranking com todos os colocados, com direito de escolha se o usuário quer que apareceça seu nome ou seja anônimo.
5.	Para avançar para a proxima fase da atividade o usuário deve ter realizado a atividade anterior, caso contrário ela ficará bloqueada até que ele conclua a atividade passada.
6.	Os pontos por serem considerados um sistema de recompensas, os alunos que ficarem em 1º, 2º e 3º receberão medalhas como forma de premiação.
7.	O usuário terá acesso as atividades corrigidas com relatórios realizados pelos professores para que ele veja em quais pontos ele deve melhorar.
8.	O usuário terá uma área de acesso para ver suas notas, onde apresentarão suas notas e médias na disciplina, caso o usuário estiver com uma nota baixa na disciplina a nota terá uma cor vermelha sinalizando assim o usuário.
9.	No perfil do usuário terá todas as informações dele, medalhas e quantas atividades ele já realizou, o usuário também pode alterar as informações pessoais dele.

### **Mapeamento de regras e respostas**

![WhatsApp Image 2022-10-28 at 14 11 17](https://user-images.githubusercontent.com/114426524/198731685-8b8a5b61-701e-418d-b38f-5d08a6a5799e.jpeg)

### **Regras de manipulação de dados**

Usuário– Proprietário dos dados pessoais que serão tratados ao longo de todo o processo.
Administrador– Pessoa física ou jurídica responsável por estipular como os dados pessoais serão tratados.

Para que os dados possam ser manipulados deve haver o consentimento do usuário ao aceitar as regras de uso da plataforma, e deve sempre 
ser explicado para que fim esses dados serão usados. 

### **Regras de cálculo**

Com os dados fornecidos e aprovados pelo titular, validaremos a performance de todos os usuários a partir das notas e desempenho nas 
atividades da plataforma, assim, criaremos um ranking a partir disso, sendo necessário obviamente, os dados de cada usuário

## **Termos de uso**

### **Concessão de Licença Limitada para Uso do Serviço**

Condicionadas à sua concordância com os presentes Termos de Uso, bem como com outras políticas aplicáveis e sua conformidade continuada das mesmas, nosso serviço concede a você uma licença não exclusiva, intransferível, não sublicenciável, revogável e limitada para o acesso e uso do Serviço para seus próprios fins de entretenimento e aprendizagem. Você concorda em não usar o Serviço para nenhuma outra finalidade. 
Aplicam-se as seguintes restrições ao uso do Serviço: 
Você não poderá (e nem tentará) comprar, vender, alugar ou dar sua Conta, criar uma Conta usando identidade ou dados falsos, ou em nome de outrem; você não poderá usar o Serviço caso já tenha sido removido ou banido. 
Você deve usar sua Conta apenas para fins não comerciais; você não poderá usar o Serviço para fazer propaganda ou solicitar ou transmitir propagandas comerciais, inclusive correntes, mala direta, spam ou mensagens repetitivas ou enganosas a ninguém.

### **Dados de Acesso a sua Conta**

Para utilizar qualquer de nossos Serviços você precisa criar uma Conta através de cadastro de conta na plataforma, será solicitado que você escolha uma senha para sua conta e informar entre outros dados, como o endereço de e-mail e o número de matricula.
O USUÁRIO é o único responsável, para todos os fins, pelas operações efetuadas em sua conta. Para proteger sua Conta, o usuário deve manter a senha em sigilo ou logout. A atividade realizada na Conta ou por seu intermédio é de responsabilidade do usuário. Não recomendamos que a senha da Conta seja reutilizada em aplicativos de terceiros ou computadores públicos. Caso tome conhecimento ou suspeite de violações de segurança, incluindo, mas não limitado à perda, roubo ou divulgação não autorizada dos Dados de Acesso, você deve notificar imediatamente o nosso suporte ao cliente e modificar seus Dados de Acesso. Você é o único responsável pela manutenção da confidencialidade dos Dados de Acesso e será responsável por todos os usos dos Dados de Acesso autorizados ou não por você. Você é responsável por tudo o que acontecer por meio da sua Conta. 

### **Desenvolvimento, melhorias e atualizações**

Estamos sempre desenvolvendo novos recursos e tecnologias para melhorar nossos serviços, como parte dessa melhoria, às vezes adicionamos ou removemos recursos e funcionalidades, aumentamos ou diminuímos limites para nossos serviços e começamos a oferecer novos serviços ou deixamos de oferecer os antigos.
Se fizermos mudanças que impactem negativamente seu uso dos nossos serviços ou se paramos de oferecer um serviço, vamos receber a críticas de vocês e logo vamos se reunir com a nossa equipe e discutir sobre a melhoria de nosso serviço.

### **Privacidade da Informação**

Nosso serviço tomará todas as medidas possíveis para manter a confidencialidade e a segurança da plataforma, porém, não se responderá por prejuízo que possa ser derivado da violação dessas medidas por parte de terceiros que utilizem as redes públicas ou a internet, subvertendo os sistemas de segurança para acessar as informações de Usuários.
O endereço de e-mail fornecido pelo Usuário poderá ser utilizado para informá-lo sobre os conteúdos do Laboratório de Dados Educacionais, assim como para aviso sobre mudanças ou melhorias. 

### **Conteúdo, dados submetidos e propriedade intelectual**

Não mineração. É vedada a utilização de softwares de mineração de dados (softwares que identificam um padrão ou uma sequência lógica de dados de um grande banco de dados) em nosso Site, de qualquer tipo ou espécie, além de outro aqui não tipificado, que atue de modo similar.
Integridade do Site. Você se compromete a não acessar áreas de programação dos nosso Site, seu banco de dados, códigos fonte ou qualquer outro conjunto de dados disponíveis nestes ambientes, bem como não realizar ou permitir engenharia reversa, nem traduzir, decompilar, copiar, modificar, reproduzir, alugar, sublicenciar, publicar, divulgar, transmitir, emprestar, distribuir ou, de outra maneira, dispor inapropriadamente das funcionalidades destes.

## **LGPD**

Somente quem controla o site terá acesso e será responsável pela segurança das informações disponibilizadas pelos usuários.

O site armazenará, organizará e conservará os dados do usuário e só será compartilhado sob a autorização do dono da conta.

O site só utilizará de suas informações para funções que nele exijam o uso para confirmação de alguma tarefa no site, caso contrário os dados do usuário estarão guardados com as devidas seguranças de privacidade.

O site responsabiliza-se pela manutenção de medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito.

Nosso site se responsabiliza e se compromete em informar o usuário caso algo venha acontecer na conta que não seja do consentimento do usuário. Nosso site se compromete em prestar ajuda imediatamente ao usuário caso ocorra algo de anormal e que comprometa a sua conta e seus dados pessoais.

## Contribuintes
Mikaell de Godoy Vitorio(Pygodoy)
Lucas Souza Araújo(logosart)
Isaac Pereira Mota(IsaacMota)
Paulo César Alves Cabral(Psyllo)
