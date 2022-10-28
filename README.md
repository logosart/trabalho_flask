<h1 align="center"> 𝓣𝓻𝓪𝓫𝓪𝓵𝓱𝓸 𝓕𝓵𝓪𝓼𝓴 </h1>

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)

# **Descrição do Projeto**
Iremos realizar um portal acadêmico com implementações de gameficação. A gamificação trata de utilizar de processos e ferramentas como avatares, progressos, pontuação, rankings e prêmios dentro do ambiente estudantil.

Vamos progamar utilizando o pycharm como editor de código, utilizaremos o Flask para framework web, HTML e CSS para a construção da página web, Firebase para a hospedagem do site e por final será utilizado o GitHub para continuarmos a atualizar o projeto por meio de postagens.

<details>
  <summary> <b> <h2> Tecnologias utilizadas <h2> <b> </summary>
  <p>O PyCharm é o melhor IDE, você pode acessar a linha de comando, conectar-se a um banco de dados, criar um ambiente virtual e gerenciar seu sistema de controle de versão em um só lugar, economizando tempo por não precisar alternar constantemente entre janelas. 

O GitHub é um serviço baseado em nuvem que hospeda um sistema de controle de versão (VCS) chamado Git. Ele permite que os desenvolvedores colaborem e façam mudanças em projetos compartilhados enquanto mantêm um registro detalhado do seu progresso.

Flask é um framework de aplicação web WSGI leve. Ele foi projetado para tornar a introdução rápida e fácil, com a capacidade de escalar para aplicativos complexos.

O HTML e CSS são importantes para o desenvolvimento, HTML É uma linguagem baseada em marcação, onde marcamos os elementos para definir quais informações a página vai exibir. CSS é uma linguagem de folha de estilo composta por “camadas”, criado com o propósito de estilizar as páginas HTML, ou seja, definir a aparência das páginas, para deixá-las visualmente mais bonitas e agradáveis. 

O Firebase é uma plataforma de desenvolvimento de aplicativos com ferramentas para ajudar você a criar, expandir e monetizar seu aplicativo. </p>
</details>

<details>
  <summary><b> <h2>Funcionalidades <h2> <b></summary>
  <p>Um sistema de ranking serve para identificar os melhores colocados na atividade, destacando aqueles que mais tem o dominio da matéria. Ajuda no sistema de competição e etimula interesse por parte dos participantes em se esforçar para alcançar melhores colocações.

O desbloqueio de novas fases e conquistas é mais uma funcionalidade que pode trazer alto engajamento dos alunos. Ao cumprir uma determinada atividade , trabalho ou prova, os alunos podem receber recompensas e consequentemente ele continua prosseguindo no mapa de atividades.

Uma estratégia muito presente nos jogos são as recompensas, ela é realizada de acordo com as atividades feitas. Este também é um recurso para estimular o interesse do participante, por isso precisa ser implementado de maneira totalmente estratégica para cumprir com o papel. 

Os pontos são considerados um sistema de recompensa que evidenciam aos alunos seu progresso na dinâmica e aumenta sua motivação com as práticas. Vamos utilizar o método de medalhas, tendo em cada atividade uma colocação de 3 lugares e medalhas de quem realizou ou nao as atividades.
</p>
</details>

 <details>
  <summary><b> <h2>Primeiros Passos<h2> <b></summary>
  <p>Criamos algumas páginas em .html como a "homepage", "notas", "users", "login", "cadastro", que serão nossas prioridades iniciais.

![primeirospassos](https://user-images.githubusercontent.com/114426524/195723442-dde8dd20-4e24-4994-b256-ab20b8f2b637.png)</p>
</details>

<details>
  <summary><b> <h2>HTML<h2> <b></summary>
  <p>Após definir as páginas começamos a dar uma "cara" a elas, através do html definimos cores, moldes, tabelas, dentro da página web.

![WhatsApp Image 2022-10-28 at 19 36 13](https://user-images.githubusercontent.com/114426524/198746055-54d75cd9-07fa-48af-9e4a-01eecf20c9ac.jpeg)

Como por exemplo o cadastro, que após algum tempo de trabalho conseguimos chegar a algo que todos concordaram que está bom.</p>
</details>

<details>
  <summary><b> <h2>Banco de Dados<h2> <b></summary>
  <p>Estrutura do banco de dados:
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
<details>
  <summary> <b> <h3>Modelo-Lógico-BD<h3> <b> </summary>
  <p>Para que nosso banco de dados fosse bem estruturado, antes realizamos a criação do Modelo lógico através do Draw.io, onde ajudou posteriormente para que o banco seja conectado de forma eficaz.

![WhatsApp Image 2022-10-10 at 20 53 45](https://user-images.githubusercontent.com/114426524/195723727-70dd7160-a849-4130-9449-52b6d05616fa.jpeg)

</p>
</details></p>
</details>

<details>
  <summary><b> <h2>Pré requisitos<h2> <b></summary>
  <p>asgiref==3.5.2
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

Localizada também na pasta requeriments que vem junto ao clone.</p>
</details>

<details>
  <summary><b> <h2>Como rodar a aplicação<h2> <b></summary>
  <p>No terminal, clone o projeto:
git clone https://github.com/logosart/trabalho_flask
Após isso verifique se todos os pré_requisitos foram instalados, abra a pasta main.py e de Run, após isso pegue o link gerado no terminal e entre.</p>
</details>

<details>
  <summary><b> <h2>Padronização e Permissão de rotas<h2> <b></summary>
  <p>

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

http://127.0.0.1:5000/users/%3Cnome_usuario%3E</p>
</details>

<details>
  <summary><b> <h2>Histórias de usuário<h2> <b></summary>
  <p>
  
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
Então o sistema o redirecionará para a página de notas</p>
</details>

<details>
  <summary><b> <h2>Regras de negócio<h2> <b></summary>
  <p>
  
  1.	Para realizar o cadastro no site, o usuário deve inserir todas as informações corretas, caso contrário receberá uma mensagem de erro de cadastro na tela.
2.	No login, o usuário deve inserir o email e a senha cadastrado, caso informe as informações erradas, receberá uma mensagem de erro de login na tela
3.	Se o usuário esquecer da senha, deverá clicar no botão "Esqueceu a senha" para recupera-la.
4.	O sistema de gamificação apresentará um ranking com todos os colocados, com direito de escolha se o usuário quer que apareceça seu nome ou seja anônimo.
5.	Para avançar para a proxima fase da atividade o usuário deve ter realizado a atividade anterior, caso contrário ela ficará bloqueada até que ele conclua a atividade passada.
6.	Os pontos por serem considerados um sistema de recompensas, os alunos que ficarem em 1º, 2º e 3º receberão medalhas como forma de premiação.
7.	O usuário terá acesso as atividades corrigidas com relatórios realizados pelos professores para que ele veja em quais pontos ele deve melhorar.
8.	O usuário terá uma área de acesso para ver suas notas, onde apresentarão suas notas e médias na disciplina, caso o usuário estiver com uma nota baixa na disciplina a nota terá uma cor vermelha sinalizando assim o usuário.
9.	No perfil do usuário terá todas as informações dele, medalhas e quantas atividades ele já realizou, o usuário também pode alterar as informações pessoais dele.

<details>
  <summary><b> <h3>Regras de cálculo<h3> <b></summary>
  <p>Com os dados fornecidos e aprovados pelo titular, validaremos a performance de todos os usuários a partir das notas e desempenho nas 
atividades da plataforma, assim, criaremos um ranking a partir disso, sendo necessário obviamente, os dados de cada usuário
</p>
</details>

<details>
  <summary><b> <h3>Regras de manipulação de dados<h3> <b></summary>
  <p>Usuário– Proprietário dos dados pessoais que serão tratados ao longo de todo o processo.
Administrador– Pessoa física ou jurídica responsável por estipular como os dados pessoais serão tratados.

Para que os dados possam ser manipulados deve haver o consentimento do usuário ao aceitar as regras de uso da plataforma, e deve sempre 
ser explicado para que fim esses dados serão usados. </p>
</details>

<details>
  <summary><b> <h3>Mapeamento de regras e respostas<h3> <b></summary>
  <p>
  
  ![WhatsApp Image 2022-10-28 at 14 11 17](https://user-images.githubusercontent.com/114426524/198731685-8b8a5b61-701e-418d-b38f-5d08a6a5799e.jpeg)
  </p>
</details>
</details>

<details>
  <summary><b> <h2>Termos de uso<h2> <b></summary>
  <p>Antes de acessar ou utilizar o Site, o que inclui acessar o site pelar internet e desfrutar do ensino por gamificação, você deve concordar com os Termos de Uso e a Política de Privacidade. É necessário também que você registre uma conta no site. Ao registrar uma conta, você declara ter 16 anos de idade ou mais, se for menor de 18 anos, você deve declarar que seu responsável legal analisou e está de acordo com estes termos.

### **AO ACESSAR O SITE E UTILIZA-LO, VOCÊ ESTARÁ DE ACORDO COM ESTES TERMOS DE USO. SE NÃO ESTIVER DE ACORDO COM ESTES TERMOS DE USO, NÃO ACESSE E USE ESSE SITE.**

Estamos sempre desenvolvendo novos recursos e tecnologias para melhorar nossos serviços, como parte dessa melhoria, às vezes adicionamos ou removemos recursos e funcionalidades, aumentamos ou diminuímos limites para nosso site e começamos a oferecer novos serviços ou deixamos de oferecer os antigos. Se fizermos mudanças que impactem negativamente seu uso dos nossos serviços ou se paramos de oferecer um serviço, vamos receber as críticas e vamos reunir com a equipe e discutir sobre a melhoria de nosso serviço.

<details>
  <summary><b> <h3>Limitações de Licença<h3> <b></summary>
  <p>Qualquer uso do Serviço em descumprimento a estas Limitações de Licença é estritamente proibido e poderá resultar na revogação imediata de sua licença limitada e responsabilizá-lo por violações da lei.

Fazer uso ou participar (direta ou indiretamente) de trapaças, explorar erros, usar softwares de automação, bots, hacks, modificações ou qualquer software de terceiros não autorizado projetado para modificar o Serviço ou interferir no Serviço, quebrando a dinâmica de outros estudantes.

Alterar ou causar a alteração de arquivos que fazem parte do site sem o consentimento expresso, por escrito.

Interromper, interferir ou, de outro modo, afetar adversamente o fluxo normal do site ou, ainda, agir de maneira que possa afetar negativamente experiência de outros usuários ao utiliza-lo. Isso inclui a comercialização de vitórias e qualquer outro tipo de manipulação de rankings, aproveitando-se de erros para obter vantagem injusta sobre outros jogadores, bem como qualquer outro ato que intencionalmente viole ou não esteja de acordo com a proposta de nosso Site.

Instituir, ajudar, ou se envolver em qualquer tipo de ataque, incluindo, mas não limitado à distribuição de vírus, ataques de negação de serviço ou outras tentativas de interromper o andamento do site, uso ou desfruto do mesmo por parte de outra pessoa.

Publicar qualquer informação que seja ofensiva, ameaçadora, obscena, difamatória, caluniosa, ou, ainda de teor questionável ou ofensivo, seja de forma racial, sexual, religiosa, questionável ou ofensiva, ou, ainda, envolver-se em comportamento negativo em curso, tais como, por exemplo, publicando repetidamente informações de forma não solicitada.

Assediar, ofender, insultar ou ferir terceiros, incluindo funcionários e representantes do serviço de suporte ao cliente, ou tentar praticar tais atos, ou, ainda, defender ou incitar a prática de tais atos.

Fazer engenharia reversa, descompilar, desmontar, decifrar ou tentar obter o Código-fonte de softwares subjacentes ou outras propriedades intelectuais usadas para prestar o site, ou obter informações do serviço ou de jogos usando métodos que não sejam expressamente permitidos.

Solicitar ou tentar solicitar Informações de Login ou quaisquer outras credenciais de login, ou informações pessoais de outros usuários do Serviço.
Coletar ou publicar informações privadas de alguém, incluindo dados de identificação pessoal (seja em forma de texto, imagem ou vídeo), documentos de identificação ou informações financeiras por meio do Serviço.

Podemos se reserva o direito de determinar quais condutas considera violar as regras de uso ou que, de outra forma, não estejam de acordo ou do espírito destes Termos de Uso ou do próprio Serviço. e reserva o direito de tomar medidas, como resultado de tais condutas, o que pode incluir o encerramento de sua Conta e a proibição do seu uso do Serviço, no todo ou em parte.</p>
</details>

<details>
  <summary><b> <h3>Concessão de Licença Limitada para Uso do Site<h3> <b></summary>
  <p>Condicionadas à sua concordância com os presentes Termos de Uso, bem como com outras políticas aplicáveis e sua conformidade continuada das mesmas, nosso serviço concede a você uma licença não exclusiva, intransferível, não sublicenciável, revogável e limitada para o acesso e uso do Serviço para seus próprios fins de entretenimento e aprendizagem. Você concorda em não usar o Serviço para nenhuma outra finalidade. 
Aplicam-se as seguintes restrições ao uso do Site: 
Você não poderá (e nem tentará) comprar, vender, alugar ou dar sua Conta, criar uma Conta usando identidade ou dados falsos, ou em nome de outrem; você não poderá usar o Serviço caso já tenha sido removido ou banido. 
Você deve usar sua Conta apenas para fins não comerciais; você não poderá usar o Serviço para fazer propaganda ou solicitar ou transmitir propagandas comerciais, inclusive correntes, mala direta, spam ou mensagens repetitivas ou enganosas a ninguém.
</p>
</details>

<details>
  <summary><b> <h3>Dados de Acesso a sua Conta<h3> <b></summary>
  <p>Para utilizar qualquer de nossos Serviços você precisa criar uma Conta através de cadastro de conta na plataforma, será solicitado que você escolha uma senha para sua conta e informar entre outros dados, como o endereço de e-mail e o número de matricula. O USUÁRIO é o único responsável, para todos os fins, pelas operações efetuadas em sua conta. Para proteger sua Conta, o usuário deve manter a senha em sigilo ou logout. A atividade realizada na Conta ou por seu intermédio é de responsabilidade do usuário. Não recomendamos que a senha da Conta seja reutilizada em aplicativos de terceiros ou computadores públicos. Caso tome conhecimento ou suspeite de violações de segurança, incluindo, mas não limitado à perda, roubo ou divulgação não autorizada dos Dados de Acesso, você deve notificar imediatamente o nosso suporte ao cliente e modificar seus Dados de Acesso. Você é o único responsável pela manutenção da confidencialidade dos Dados de Acesso e será responsável por todos os usos dos Dados de Acesso autorizados ou não por você. Você é responsável por tudo o que acontecer por meio da sua Conta. </p>
</details>

<details>
  <summary><b> <h3>Suspensão e Cessação da Conta e do Serviço<h3> <b></summary>
  <p>Podemos limitar, suspender, encerrar, modificar ou excluir contas ou o acesso aos serviços ou a partes do serviço em caso de descumprimento destes termos de uso ou caso suspeitamos que você deixou de cumpri-los, ou, ainda, por uso ilegal ou inadequado do serviço, ou pela suspeita de tal uso, sem aviso prévio. Você poderá perder sua conta, bem como benefícios, privilégios itens adquiridos e itens comprados relacionados ao seu uso do serviço, ficando a com a nossa equipe para indenizá-lo por tais perdas ou resultados. 

Podemos se reserva no direito de parar de oferecer e/ou de manter o Serviço específico ou parte do Serviço a qualquer momento de contas que estejam inativas por 180 dias, sem aviso prévio, o qual resultará no cancelamento automático da sua licença para usar o serviço ou parte dele. Nesse caso, não teremos a obrigação de fornecer restituições, benefícios ou outras indenizações para os usuários em relação a tais serviços interrompidos.
</p>
</details>

<details>
  <summary><b> <h3>Privacidade da Informação<h3> <b></summary>
  <p>Nosso serviço tomará todas as medidas possíveis para manter a confidencialidade e a segurança da plataforma, porém, não se responderá por prejuízo que possa ser derivado da violação dessas medidas por parte de terceiros que utilizem as redes públicas ou a internet, subvertendo os sistemas de segurança para acessar as informações de Usuários.

O endereço de e-mail fornecido pelo Usuário poderá ser utilizado para informá-lo sobre os conteúdos do Laboratório de Dados Educacionais, assim como para aviso sobre mudanças ou melhorias. </p>
</details>

<details>
  <summary><b> <h3>Conteúdo, dados submetidos e propriedade intelectual<h3> <b></summary>
  <p>Não mineração. É vedada a utilização de softwares de mineração de dados (softwares que identificam um padrão ou uma sequência lógica de dados de um grande banco de dados) em nosso Site, de qualquer tipo ou espécie, além de outro aqui não tipificado, que atue de modo similar.
Integridade do Site. Você se compromete a não acessar áreas de programação dos nosso Site, seu banco de dados, códigos fonte ou qualquer outro conjunto de dados disponíveis nestes ambientes, bem como não realizar ou permitir engenharia reversa, nem traduzir, decompilar, copiar, modificar, reproduzir, alugar, sublicenciar, publicar, divulgar, transmitir, emprestar, distribuir ou, de outra maneira, dispor inapropriadamente das funcionalidades destes.
</p>
</details>

</p>
</details>

<details>
  <summary><b> <h2>LGPD<h2> <b></summary>
  <p>Somente quem controla o site terá acesso e será responsável pela segurança das informações disponibilizadas pelos usuários.

O site armazenará, organizará e conservará os dados do usuário e só será compartilhado sob a autorização do dono da conta.

O site só utilizará de suas informações para funções que nele exijam o uso para confirmação de alguma tarefa no site, caso contrário os dados do usuário estarão guardados com as devidas seguranças de privacidade.

O site responsabiliza-se pela manutenção de medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito.

Nosso site se responsabiliza e se compromete em informar o usuário caso algo venha acontecer na conta que não seja do consentimento do usuário. Nosso site se compromete em prestar ajuda imediatamente ao usuário caso ocorra algo de anormal e que comprometa a sua conta e seus dados pessoais.</p>
</details>

## Contribuintes
Mikaell de Godoy Vitorio(Pygodoy)
Lucas Souza Araújo(logosart)
Isaac Pereira Mota(IsaacMota)
Paulo César Alves Cabral(Psyllo)
