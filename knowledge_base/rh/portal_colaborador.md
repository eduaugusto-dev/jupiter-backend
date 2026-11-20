
---
id: rh_012
titulo: Portal do Colaborador - Acesso e Funcionalidades
categoria: RH
tags:
  - portal do colaborador
  - portal interno
  - acesso
  - login
  - perfil
  - informações pessoais
  - serviços de RH
  - autoatendimento
  - RH
versao: 2.0
ultima_atualizacao: 2026-11-20
autor: SeguraOz
---

# Portal do Colaborador - Acesso e Funcionalidades

## 1. Visão geral

O Portal do Colaborador é o ambiente digital destinado a facilitar o acesso dos funcionários da SeguraOz às informações e aos serviços relacionados à sua vida profissional.

Por meio desse ambiente, os colaboradores poderão consultar informações, acompanhar solicitações e acessar funcionalidades disponibilizadas pela empresa.

O portal tem como objetivo centralizar serviços de Recursos Humanos, reduzindo a necessidade de consultas manuais e facilitando o acesso às informações internas.

O Júpiter atua como agente inteligente de atendimento de RH, complementando essa experiência ao permitir que os colaboradores obtenham orientações por meio de uma interface conversacional.

## 2. Objetivo

Este documento tem como objetivo apresentar orientações gerais sobre o Portal do Colaborador.

O conteúdo busca esclarecer:

- A finalidade do portal;
- Como realizar o acesso;
- Como consultar informações pessoais;
- Quais serviços podem estar disponíveis;
- Como utilizar os recursos de autoatendimento;
- Como proceder diante de dificuldades de acesso;
- Qual é a relação entre o portal e o Júpiter.

## 3. Acesso ao portal

O acesso ao Portal do Colaborador deverá ser realizado por meio dos canais oficiais disponibilizados pela SeguraOz.

O colaborador deverá utilizar suas credenciais individuais de autenticação.

O acesso poderá envolver:

- Identificação do usuário;
- E-mail ou identificador cadastrado;
- Senha individual;
- Mecanismos adicionais de segurança, quando disponíveis.

As credenciais são pessoais e não devem ser compartilhadas com outras pessoas.

## 4. Autenticação e segurança

A autenticação é responsável por identificar o colaborador e permitir o acesso às funcionalidades autorizadas.

Após a autenticação, o sistema deverá reconhecer a identidade do usuário e aplicar as permissões correspondentes ao seu perfil.

O acesso às informações deverá respeitar:

- A identidade do usuário autenticado;
- O perfil de acesso;
- As permissões atribuídas;
- A confidencialidade dos dados;
- As políticas de segurança da SeguraOz.

O Júpiter deverá utilizar a identidade autenticada para identificar o colaborador durante o atendimento.

O agente não deverá solicitar senhas, tokens ou outras credenciais diretamente na conversa.

## 5. Perfil do colaborador

O perfil reúne informações relacionadas à identificação e à atuação profissional do funcionário na SeguraOz.

As informações disponíveis poderão incluir:

- Nome completo;
- E-mail corporativo;
- Cargo;
- Departamento;
- Identificador do colaborador;
- Outras informações cadastrais autorizadas.

O colaborador poderá consultar seus próprios dados por meio das funcionalidades disponibilizadas.

O Júpiter poderá utilizar informações do perfil autenticado para contextualizar suas respostas, desde que tenha autorização para acessar esses dados.

## 6. Serviços de Recursos Humanos

O Portal do Colaborador poderá centralizar funcionalidades relacionadas aos principais processos de RH.

### 6.1. Informações salariais

Permite consultar informações relacionadas à remuneração, conforme as funcionalidades e permissões disponíveis.

Exemplos:
- Consulta de salário;
- Consulta de demonstrativos de pagamento;
- Informações sobre remuneração.

As informações individuais deverão ser obtidas de fontes oficiais e protegidas por controle de acesso.

### 6.2. Férias

Permite consultar informações relacionadas ao planejamento e ao acompanhamento de férias.

Exemplos:
- Consulta de saldo disponível;
- Visualização de períodos;
- Acompanhamento de solicitações;
- Consulta de registros.

### 6.3. Banco de horas

Permite acompanhar informações relacionadas à jornada e aos saldos de horas, quando disponíveis.

Exemplos:
- Consulta de saldo;
- Visualização de registros;
- Orientações sobre compensação.

### 6.4. Benefícios

Permite consultar orientações e informações relacionadas aos benefícios disponibilizados pela empresa.

A disponibilidade das informações individuais dependerá dos registros e das permissões aplicáveis.

### 6.5. Documentos

Permite acessar orientações sobre documentos relacionados ao vínculo empregatício.

Exemplos:
- Holerites;
- Comprovantes;
- Registros administrativos;
- Documentos disponibilizados pela empresa.

### 6.6. Solicitações e atendimento

O portal poderá disponibilizar mecanismos para acompanhar solicitações e entrar em contato com o Departamento de Recursos Humanos.

As funcionalidades efetivamente disponíveis deverão ser confirmadas nos canais oficiais.

## 7. Integração com o Júpiter

O Júpiter é o agente inteligente de atendimento interno de RH da SeguraOz.

Sua função é facilitar o acesso às informações e aos procedimentos da empresa por meio de uma interface conversacional.

O agente utiliza duas fontes principais de informação:

### 7.1. Base de conhecimento (RAG)

A base de conhecimento reúne documentos institucionais e procedimentos de RH.

Ela permite que o Júpiter responda perguntas relacionadas a:

- Políticas internas;
- Procedimentos de férias;
- Folha de pagamento;
- Benefícios;
- Banco de horas;
- Ponto eletrônico;
- Admissão;
- Desligamento;
- Licenças e afastamentos;
- Documentos do colaborador;
- Portal do Colaborador.

### 7.2. Banco de dados estruturado (Supabase)

O Supabase armazena informações estruturadas utilizadas pelo sistema.

Quando autorizado, o Júpiter poderá consultar informações individuais, como:

- Dados do perfil;
- Salário;
- Registros de férias;
- Saldo de férias;
- Informações de folha de pagamento;
- Outros dados disponibilizados pelas integrações.

A consulta deverá respeitar a identidade e as permissões do usuário autenticado.

### 7.3. Funcionamento conjunto

A base de conhecimento e o banco de dados possuem funções complementares.

A base RAG responde perguntas sobre regras e procedimentos.

O Supabase fornece informações individuais registradas no sistema.

Exemplo:

Pergunta: "Como funciona a solicitação de férias?"

Fonte: Base de conhecimento RAG.

Pergunta: "Quantos dias de férias eu tenho disponíveis?"

Fonte: Supabase, por meio de consulta autorizada.

Essa separação permite que o Júpiter apresente orientações gerais e informações individuais sem confundir políticas internas com dados pessoais.

## 8. Dificuldades de acesso

Caso o colaborador encontre dificuldades para acessar o portal, deverá utilizar os canais oficiais de suporte da SeguraOz.

Exemplos de dificuldades:

- Credenciais não reconhecidas;
- Problemas de autenticação;
- Esquecimento de senha;
- Perfil não identificado;
- Falha no carregamento;
- Indisponibilidade de funcionalidades.

O Júpiter poderá orientar o colaborador sobre os procedimentos documentados, mas não deverá solicitar credenciais ou prometer a recuperação de acesso sem uma funcionalidade autorizada.

## 9. Responsabilidades

### 9.1. Colaborador

- Utilizar suas credenciais individuais;
- Manter suas informações atualizadas;
- Não compartilhar dados de autenticação;
- Consultar informações pelos canais autorizados;
- Comunicar dificuldades de acesso;
- Utilizar os serviços conforme as orientações internas.

### 9.2. Departamento de Recursos Humanos

- Orientar os colaboradores sobre os serviços disponíveis;
- Manter as informações e os procedimentos de RH atualizados;
- Apoiar solicitações relacionadas aos serviços internos;
- Encaminhar dificuldades que dependam de análise administrativa.

### 9.3. Setor de Tecnologia da Informação

Quando aplicável, deverá acompanhar os aspectos técnicos do portal, incluindo disponibilidade, autenticação, integrações e segurança dos sistemas.

### 9.4. Júpiter

- Orientar sobre o uso dos serviços de RH;
- Responder dúvidas utilizando a base de conhecimento;
- Consultar informações individuais quando autorizado;
- Reconhecer o contexto do usuário autenticado;
- Respeitar as permissões de acesso;
- Encaminhar dificuldades que dependam de atendimento humano.

## 10. Segurança e confidencialidade

O Portal do Colaborador poderá disponibilizar informações pessoais, profissionais e financeiras.

Por esse motivo, o acesso deverá respeitar os controles de segurança estabelecidos pela SeguraOz.

O Júpiter deverá:

- Responder com base na identidade autenticada;
- Consultar somente informações autorizadas;
- Não revelar dados de outros colaboradores;
- Não solicitar senhas ou tokens;
- Não compartilhar informações confidenciais;
- Não afirmar que uma operação foi realizada sem confirmação;
- Respeitar os mecanismos de autorização do sistema.

## 11. Perguntas frequentes

**O que é o Portal do Colaborador?**

É o ambiente digital destinado a centralizar informações e serviços relacionados aos funcionários da SeguraOz.

**Como posso acessar o portal?**

O acesso deverá ser realizado pelos canais oficiais da empresa, utilizando as credenciais individuais disponibilizadas ao colaborador.

**Posso consultar meu salário pelo portal?**

A consulta dependerá da disponibilidade da funcionalidade e das permissões de acesso estabelecidas pela SeguraOz.

**Qual é a relação entre o portal e o Júpiter?**

O portal centraliza serviços e informações, enquanto o Júpiter oferece atendimento conversacional para orientar os colaboradores sobre procedimentos e consultar dados autorizados.

**O Júpiter consegue consultar minhas férias?**

Sim, quando a integração com o Supabase estiver disponível e o usuário possuir autorização para consultar seus próprios registros.

**O que devo fazer se não conseguir acessar minha conta?**

O colaborador deverá seguir os procedimentos oficiais de recuperação de acesso ou procurar o suporte responsável.

## 12. Diretrizes para respostas do Júpiter

Ao responder perguntas relacionadas ao Portal do Colaborador, o agente deverá:

1. Identificar a dúvida apresentada.
2. Utilizar este documento para explicar as funcionalidades e os procedimentos gerais.
3. Consultar a documentação oficial quando forem solicitadas orientações específicas.
4. Consultar o Supabase quando forem necessárias informações individuais autorizadas.
5. Respeitar a identidade e as permissões do usuário autenticado.
6. Não afirmar que funcionalidades estão disponíveis sem confirmação.
7. Não solicitar credenciais de acesso.
8. Encaminhar dificuldades técnicas ou administrativas aos setores responsáveis.

## 13. Limites de atuação

O Júpiter não deverá:

- Criar ou alterar credenciais por conta própria;
- Recuperar senhas sem funcionalidade autorizada;
- Conceder permissões de acesso;
- Consultar dados de outros colaboradores sem autorização;
- Realizar operações não implementadas;
- Garantir a disponibilidade de funcionalidades não confirmadas;
- Substituir os canais oficiais de suporte.

## 14. Considerações finais

O Portal do Colaborador representa um importante canal de acesso aos serviços e às informações internas da SeguraOz.

A centralização dos recursos contribui para uma experiência mais organizada e facilita o relacionamento entre os funcionários e o Departamento de Recursos Humanos.

Integrado a esse ambiente, o Júpiter complementa o autoatendimento ao oferecer orientações rápidas, consultas contextualizadas e acesso facilitado à base de conhecimento institucional.
