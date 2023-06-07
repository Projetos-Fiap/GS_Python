#Turma ESPW - Global Solution - Controle de Excedentes e Agendamento de Coleta
## Grupo 2 - Unicórnio
<li>Alessandra Vaiano (RM551497)</li>  
<li>André Lambert (RM99148)</li>  
<li>Bryan Willian (RM551305)</li>
<li>Lucas Feijó (RM99727)</li>
<li>Vitor Maia (RM99658)</li>

## Introdução
Repo destinado à entrega de COMPUTATIONAL THINKING USING PYTHON para a Global Solution do primeiro semestre de 2023. O tema proposto nessa GS foi a fome e a insegurança alimentar.
## A Ideia
A ideia escolhida pela squad foi atacar o desperdício de alimentos produzidos por estabelecimentos como restaurantes, self-services e afins. Isso será feito através de um site que intermediará os estabelecimentos citados e ONGs que distribuam alimentos. Assim evitando o desperdício de alimentos por parte do estabelecimento, facilitando a obtenção de alimentos por parte da ONG e impulsionando ações que levam comida a pessoas em stuação de insegurança alimentar.

## O Projeto
Nesse projeto em python foi desenvolvido o que seria o sistema de controle de Excedentes e Agendamento de Coleta, assim como o controle de usuários (Estabelecimento ou ONG).

### Dependêcias
python 3.10.0

### Como iniciar o projeto
Para iniciar o projeto basta clonar o repositório e rodar python gs.py na linha de comando.

### Login (Estabelecimento/ONG)
Para logar basta selecionar a opção de login. Há 3 usuários pré-criados: (user: pfTio@gmail.com senha: 123 tipo: Estabelecimento), (user: sorveteTia@gmail.com senha: 123 tipo: Estabelecimento) e (user: pratoCheio@gmail.com senha: 123 tipo: ONG)

### Cadastro de Usuários (Estabelecimento/ONG)
Para cadastrar-se basta selecionar a opção de cadastro como Estabelecimento ou ONG

### Alteração de Senha (Estabelecimento/ONG)
Para alterar a senha de um usuário é necessário estar logado, a senha atual será pedida e então uma nova senha poderá ser definida.

### Edição de Informações do Usuário (Estabelecimento/ONG)
Uma vez logado, tanto como Estabelecimento ou ONG é possível editar informações do usuário como nome, endereço, etc.

### Listar Agendamentos (Estabelecimento/ONG)
Uma vez logado, é possível listar todos os seus agendamentos marcados.

### Cancelar Agendamento (Estabelecimento/ONG)
Uma vez logado, é possível cancelar um agendamento marcado.

### Cadastar Excedente (Estabelecimento)
Uma vez logado como Estabelecimento, é possível cadastrar um Excedente. Para isso será necessário informar nome, descrição, quantidade em gramas de comida, data de vencimento do alimento, e uma datas e horas iniciais e finais indicando intervalo de tempo em que o excedente estará disponível para coleta.

### Listar Excedentes (Estabelecimento)
Uma vez logado como Estabelecimento, é possível listar todos os Excedentes criados que ainda estejam disponíveis ou que já tenham uma coleta agendada.

### Listar Doações Efetuadas (Estalecimento)
Uma logado como Estabelecimento, é possível visualizar todos as doações feitas, indicadas pelos agendamentos cujo status = efetuado.

### Listar Excedentes Coletados (ONG)
Uma logado como ONG, é possível visualizar todos os excedentes coletados, indicadas pelos agendamentos cujo status = efetuado.

### Buscar Excedentes (ONG)
Esta é a função principal do projeto, uma vez logado como ONG, você pode buscar por excedentes que estejam disponíveis serem coletados e criar um agendamento para a coleta.


