# Perguntas Estratégicas para Construção do TCC - Phablo Tavares

Este documento contém perguntas direcionadas e desenhadas especificamente para preencher as lacunas entre os dados brutos da sua atuação (issues, PRs, commits da `base_de_conhecimento_phablo_sipros`) e as exigências do documento oficial do TCC (baseado em `UFG_INF_BES_TCC_Modelo`).

O modelo de TCC do INF-UFG foca intensamente no **porquê**, **como**, **contexto organizacional** e **lições aprendidas**, indo além do simples "o que foi feito".

Por favor, responda cada pergunta abaixo. Suas respostas serão o insumo principal para a redação dos capítulos do seu TCC.

---

## Bloco 1: Definição de Foco e Fundamentação (Capítulos 1 e 2)

_O modelo de TCC sugere que, embora a atuação possa ser em várias áreas, o trabalho deve ter um "Tópico Específico" bem definido (ex: Segurança e Autenticação, Qualidade e Testes, Evolução Full-Stack)._

### 1.1 Qual será o tema central/foco principal do seu TCC?

_(Exemplo: "Implementação de Mecanismos de Autenticação e Segurança com Keycloak", "Evolução e Refatoração Full-Stack do Sistema SIPROS", ou "Práticas de V&V e Qualidade de Software")._
**Sua Resposta:**

> O tema central será a **Evolução e Refatoração Full-Stack do Sistema SIPROS**, com foco principal na implementação de **mecanismos de autenticação e segurança com Keycloak** (incluindo autenticação via Google e fluxo com PKCE). Complementarmente, o trabalho abordará:
>
> - **Qualidade e Testes:** Práticas de Verificação e Validação (V&V) e implementação de testes automatizados.
> - **Evolução de Interface:** Melhorias no Front-end, refatoração de fluxos legados e novas regras de negócio na UI.

### 1.2 Por que a resolução dos problemas que você trabalhou no SIPROS (ex: retirar credenciais hardcoded, unificar login) foi crucial para as partes interessadas (usuários, coordenação)?

**Sua Resposta:**

> A resolução foi crucial porque elevou o sistema a um novo nível de maturidade e funcionalidade. Embora o SIPROS tivesse uma arquitetura consolidada, ainda apresentava lacunas críticas, como rotas de _back-end_ sem telas correspondentes, fluxos de _front-end_ sem conexão real e o uso intensivo de dados _mockados_. Meu trabalho focou em remover esses _mocks_, conectar as pontas do sistema (front e back) e torná-lo realidade. O principal exemplo foi a autenticação com Google, que antes era uma funcionalidade vazia e passou a ser um fluxo de login real e persistente. Em suma, essas contribuições foram fundamentais para transformar um projeto estático em um sistema muito mais próximo de estar pronto para uso em produção (_production-ready_).

### 1.3 Avaliação das Ferramentas: Quais foram os pontos fortes e as _limitações_ das principais ferramentas adotadas (Keycloak, Angular, Docker, GitHub)?

_(O Capítulo 2 exige justificar a escolha e também as limitações das ferramentas utilizadas)._
**Sua Resposta:**

> A principal justificativa para o uso dessas ferramentas foi a aderência à arquitetura já estabelecida no projeto; optamos por manter o padrão do repositório em vez de adicionar novas tecnologias.
> **Pontos Fortes:** São tecnologias amplamente consolidadas e completas. O Keycloak oferece segurança robusta; o Angular viabiliza um _design_ bastante fiel às prototipações no Figma; a conteinerização pelo Docker facilita a padronização e o GitHub garante um excelente fluxo de versionamento.
> **Limitações:**
>
> - **Keycloak:** Possui uma curva de aprendizado inicial mais complexa, sobretudo para as configurações iniciais e criação de scripts para novos usuários.
> - **Angular:** Sua arquitetura rígida e a exigência de TypeScript impõem uma curva de aprendizado íngreme. Como eu não tinha experiência prévia, isso representou um desafio inicial até me adaptar.
> - **Docker:** Traz um forte custo computacional (_overhead_). Subir todos os contêineres do projeto exige uma máquina com hardware razoável, caso contrário, ocorrem travamentos.

---

## Bloco 2: Contexto e Dinâmica Organizacional (Capítulos 1 e 3)

_O TCC exige que se relate o ambiente em que o projeto foi desenvolvido e como a equipe se organizava._

### 2.1 Como era a dinâmica de trabalho e as metodologias da equipe da Fábrica de Software?

_(Havia cerimônias Scrum/Kanban? Como as tarefas eram priorizadas e distribuídas? Havia papéis bem definidos como Scrum Master, Tech Lead? Como a comunicação ocorria?)_
**Sua Resposta:**

> A dinâmica de trabalho era inspirada na metodologia Scrum (com o uso de quadros Kanban), embora não a seguíssemos de forma estrita. Nossa organização funcionava da seguinte maneira:
>
> - **Levantamento e Planejamento:** Nós, discentes, analisávamos as demandas, dividíamos em épicos e criávamos as _issues_ no GitHub. A coordenação da Fábrica de Software atuava como _Product Owner_, selecionando e priorizando quais _issues_ entrariam em cada _Sprint_. As _Sprints_ tinham duração de duas semanas.
> - **Autogerenciamento e Desenvolvimento:** Com as tarefas definidas, a equipe possuía total liberdade para se organizar, dividir sub-tarefas e distribuí-las conforme a familiaridade técnica de cada um. Estabelecíamos prazos internos e, ao final da _Sprint_, reservávamos os últimos 1 a 2 dias para alinhar o código e abrir os _Pull Requests_ necessários para a _branch_ principal, sempre em comunicação com a Fábrica de Software para garantir o alinhamento esperado.
> - **Reunião de Revisão (_Sprint Review_):** Ao término das duas semanas da _Sprint_, fazíamos uma reunião no período da tarde com a Fábrica e os docentes. Apresentávamos nossas entregas e recebíamos os _feedbacks_ (elogios pelo que funcionou bem ou cobranças de melhoria). Com base no que foi entregue ou no que ficou pendente, a Fábrica nos direcionava novas _tasks_, reiniciando o ciclo de desenvolvimento desde o zero.
> - **Comunicação e Liderança:** A comunicação interna era constante para garantir a qualidade e a entrega no prazo. Havia também papéis de liderança estabelecidos: a Ester e o Lucas atuavam como a interface direta ("ponte") entre a Fábrica de Software, os docentes e nós, discentes.

### 2.2 Como foi o seu processo de ambientação (Onboarding)?

_(Como você estudou e se familiarizou com a base de código do SIPROS antes de conseguir entregar a primeira funcionalidade?)_
**Sua Resposta:**

> O processo de _onboarding_ foi muito bem estruturado pela Fábrica de Software. O foco inicial foi nivelar o conhecimento da equipe sobre as tecnologias do SIPROS e as ferramentas essenciais (como Git e Docker) para conseguirmos rodar o projeto localmente (tanto o _back-end_ quanto o _front-end_). Esse treinamento foi detalhado e crucial para equilibrar o nível técnico de todos, especialmente para quem não tinha experiência prévia em desenvolvimento num ambiente de metodologias ágeis. Após essa base sólida fornecida pela Fábrica, tornou-se responsabilidade de cada discente identificar suas próprias lacunas de conhecimento e buscar o aprendizado necessário para conseguir realizar as entregas.

### 2.3 Como foi a comunicação e integração do seu trabalho com os outros membros da Equipe Dourada?

_(A Equipe Dourada era composta por Phablo Tavares, Thiago Vicente de Aquino, Hugo Moreno Veiga Jardim, Ester Adaiane Oliveira Ferreira, Lucas Gabriel Nunes Alves, Felipe Duarte da Rocha Paço e José Alves de Oliveira Neto. Cite exemplos de como foi colaborar com eles, conflitos de código ou tomada de decisões em conjunto)._
**Sua Resposta:**

> A comunicação com a Equipe Dourada ocorreu de forma constante e alinhada, apoiada em dois canais principais:
>
> - **Canal Oficial (Discord):** Utilizado para contato direto com a Fábrica de Software. Por lá, enviávamos avisos de _Pull Requests_, comunicávamos nossas entregas e fazíamos pedidos de ajuda, garantindo que a coordenação estivesse sempre ciente do nosso progresso.
> - **Canal Interno (WhatsApp):** Um grupo próprio para comunicações mais pontuais e rápidas entre os discentes, sem a necessidade de expor todas as discussões no canal oficial.
>
> Nossa metodologia de comunicação valorizava muito a expressividade e a transparência. Constantemente eu e outros colegas perguntávamos sobre o andamento das tarefas, e qualquer membro com dificuldades ou impedimentos reportava imediatamente ao grupo para nos organizarmos. Além disso, realizávamos reuniões síncronas frequentes nos canais de voz do Discord para dividir tarefas, debater soluções e discutir pendências urgentes.
>
> **Resolução de Conflitos de Código:** A comunicação sobre código seguia a mesma dinâmica e prezava pela autonomia. Se eu me deparasse com um conflito de código, eu mesmo tentava resolvê-lo. Apenas acionávamos outro membro caso fosse algo muito crítico. Havia uma autoavaliação constante: _"Preciso comunicar esse problema ou posso apenas resolvê-lo? Se eu resolvê-lo sozinho, isso vai gerar um efeito colateral para o meu colega quando ele fizer o pull da branch?"_. Sempre que a análise indicava a possibilidade de impacto no trabalho de outro membro, nós conversávamos e definíamos uma estratégia em conjunto para garantir o alinhamento.

---

## Bloco 3: Desafios, Decisões Técnicas e Soluções (Capítulo 3)

_A base de dados cita as PRs aprovadas, mas o relato de experiência (Capítulo 3) quer entender a "dor" do processo técnico._

### 3.1 Ao remover o mock de autenticação e integrar o login com Google/Keycloak, quais foram os maiores desafios técnicos enfrentados?

_(Quais foram os bugs mais difíceis, problemas de arquitetura prévia ou dificuldades no aprendizado do Keycloak e OAuth2/PKCE?)_
**Sua Resposta:**

> Os desafios técnicos se dividiram em duas frentes principais:
>
> 1. **Curva de Aprendizado e Configuração (GCP):** O primeiro obstáculo foi aprender a realizar a configuração do OAuth no _Google Cloud Platform_ (GCP Console). O processo exigiu o mapeamento cuidadoso de credenciais, URLs de _callback_ e variáveis de ambiente, ferramentas com as quais eu não tinha familiaridade prévia.
> 2. **Implementação e Estabilidade (_Bugs_):** O segundo desafio foi integrar isso ao código base sem causar efeitos colaterais ou quebrar testes existentes. Durante a implementação, enfrentei problemas complexos de estado da aplicação. Por exemplo, o login funcionava, mas se o usuário navegasse de volta para uma tela específica, o fluxo quebrava ou a sessão com o Keycloak não era validada corretamente. Superei isso rastreando e testando exaustivamente todos os fluxos e casos de uso possíveis até que tudo ficasse perfeitamente estável.
>
> **Pendência para Produção:** Como a aplicação não foi colocada em produção durante o meu ciclo, ficou o direcionamento técnico para a Fábrica de Software: será preciso gerar uma nova credencial no GCP ou migrar as variáveis de ambiente que eu criei para o servidor de produção, garantindo a segurança do _client secret_.

### 3.2 Por que foi decidido usar a extensão PKCE (Proof Key for Code Exchange) no fluxo de login? Houve alguma outra alternativa discutida ou descartada?

**Sua Resposta:**

> A decisão de utilizar a extensão PKCE (_Proof Key for Code Exchange_) acoplada ao _Authorization Code Flow_ foi essencialmente técnica e voltada para a segurança. Como o SIPROS utiliza Angular, que é uma _Single Page Application_ (SPA) executada no navegador do usuário, é impossível armazenar um _client secret_ de forma segura no _front-end_ (já que o código fica visível ao cliente).
>
> As alternativas avaliadas foram:
>
> 1. **Authorization Code Flow Tradicional:** Descartado porque exigiria a exposição do _client secret_ no navegador.
> 2. **Implicit Flow:** Era o padrão antigo para SPAs, mas foi sumariamente descartado por ser considerado obsoleto e vulnerável pelas atuais recomendações de segurança do OAuth 2.0, já que expõe o _token_ diretamente na URL e no histórico do navegador.
>
> Sendo assim, o PKCE foi a solução viável e segura adotada. Ele substitui a necessidade do _client secret_ estático por um verificador dinâmico (`code_challenge` e `code_verifier`) gerado a cada tentativa de login. Isso mitiga ataques de interceptação (como injeção de código ou CSRF) e garante uma autenticação robusta sem comprometer credenciais sensíveis no lado do cliente.

### 3.3 No trabalho de V&V (Issue #139) comparando o Figma com os Casos de Uso, quais inconsistências chamaram mais a sua atenção? Como isso gerou impacto real na correção do sistema?

**Sua Resposta:**

> O que mais me chamou atenção foi o alto grau de inconsistência e a dificuldade em determinar a "fonte da verdade" do sistema. Existiam diversas divergências críticas:
>
> - **Incompatibilidade Front x Documentação:** Havia regras de negócio descritas nos Casos de Uso que não existiam no protótipo, bem como telas ou campos no protótipo que não estavam mapeados na documentação.
> - **Contradições Internas:** Os próprios documentos de Casos de Uso divergiam entre si e continham descrições que entravam em conflito, além de imagens (_prints_) completamente desatualizadas.
> - **Desorganização do Figma:** Era difícil identificar qual _design_ correspondia à versão final oficial e quais eram apenas rascunhos.
>
> **Impacto Real:** Diante dessa confusão, a equipe precisou tomar uma decisão gerencial para destravar o projeto. Optamos por definir que os **Casos de Uso** seriam a fonte oficial da verdade. Com essa premissa estabelecida, mapeamos as divergências e geramos dezenas de novas _issues_ focadas em corrigir, higienizar e organizar o protótipo no Figma para que ele refletisse corretamente a documentação, além de ajustar o sistema de acordo.

---

## Bloco 4: Avaliação de Qualidade de Software (Capítulo 3)

_Existe uma seção obrigatória sobre como a qualidade foi assegurada no seu trabalho._

### 4.1 Como a qualidade do código foi garantida durante as suas entregas?

_(Descreva a cultura de testes, a sua iniciativa na estruturação da suíte de testes de unidade - Issue #304 - e como eram as políticas para aprovação de um Code Review)._
**Sua Resposta:**

> A qualidade do código foi assegurada através de duas frentes principais: consolidação de testes automatizados e revisões por pares (_Code Review_).
>
> - **Cultura de Testes (Issue #304):** Inicialmente, a equipe tinha certa dificuldade com a padronização e estruturação dos testes automatizados. Assumi a responsabilidade de criar a **Issue #304**, cujo escopo foi definir e estruturar a suíte oficial de testes de unidade para o projeto. Pesquisei as melhores abordagens e escrevi a documentação e a base para que a equipe pudesse desenvolver testes confiáveis, garantindo que nossas refatorações (especialmente no _back-end_) não causassem regressões.
> - **Políticas de Code Review:** Para que uma tarefa fosse fundida nas ramificações principais (como a `dev`), era obrigatório que o código passasse pela revisão rigorosa de, no mínimo, outro colega. Atuei ativamente não só abrindo _Pull Requests_, mas também como **Revisor**. Conforme os registros do projeto, revisei entregas críticas de outros colegas, desde a geração de relatórios e _endpoints_ de _back-end_ até fluxos complexos de UI/UX e validações de rotas no Angular. Nossa cultura de revisão exigia o alinhamento das lógicas implementadas com a "fonte da verdade" documentada, além de garantir que a arquitetura do Keycloak estivesse coesa.

### 4.2 Quais indicadores ou percepções provam que as suas contribuições melhoraram o sistema?

_(Tivemos redução de bugs? Códigos mais limpos? Melhor feedback dos usuários sobre o botão do Google?)_
**Sua Resposta:**

> A melhora no sistema pode ser comprovada por métricas de redução de débito técnico, estabilidade de fluxos e experiência do usuário:
>
> - **Redução de Débito Técnico e Segurança (Issue #214):** Uma das provas mais claras de código mais limpo foi a remoção completa dos serviços paralelos de autenticação que rodavam no _front-end_ (como o serviço _mockado_ e o arquivo `mock-users.json`). Além de enxugar o código centralizando tudo no `AutenticacaoService`, externalizei credenciais (como o `CLIENT_ID` do Keycloak) para variáveis de ambiente, mitigando falhas graves de segurança.
> - **Melhoria de UI/UX e Acessibilidade (Issue #253):** A ativação do botão "Entrar com Google" revolucionou a experiência de ponta a ponta. O _feedback_ prático foi super positivo, pois permitiu o acesso imediato sem a necessidade de criação manual de contas longas, delegando a fricção e a segurança para a plataforma do Google.
> - **Estabilidade e Prevenção de Bugs (Issues #139 e #179):** Através do detalhado processo de V&V, identifiquei inconsistências críticas (telas divergindo dos Casos de Uso) que evitaram inúmeros _bugs_ comportamentais antes mesmo da homologação final. Paralelamente, o tratamento de sessão do Keycloak (evitando que o usuário caísse numa tela vazia sem renderização após logar) garantiu um comportamento previsível e à prova de falhas na navegação.

---

## Bloco 5: Reflexões, Aprendizados e Trabalhos Futuros (Capítulo 4)

_Para a conclusão, é preciso abstrair o código e focar no profissional Phablo._

### 5.1 Quais foram as principais evoluções em suas _Soft Skills_ (comunicação, organização, liderança técnica) e _Hard Skills_ (Angular, arquitetura, testes)?

**Sua Resposta:**

> **Evolução em Soft Skills:**
>
> - **Autogerenciamento:** Foi um ponto crucial. O ambiente exigia que a equipe se organizasse e garantisse as entregas por conta própria; tínhamos que "nos virar" para fazer o projeto dar certo.
> - **Comunicação:** Entendi na prática que a comunicação é indispensável. Nada chegava "de mão beijada", então ser expressivo, relatar impedimentos e manter o alinhamento constante com os colegas foi vital para que o trabalho fluísse.
> - **Liderança Técnica (Autonomia):** Embora eu não tenha ocupado um cargo formal de gestão, exerci liderança sobre os artefatos que produzi. Como as _issues_ tinham escopos amplos, assumi a responsabilidade de tomar decisões técnicas e arquiteturais, fundamentando-as de forma clara.
>
> **Evolução em Hard Skills:**
>
> - **Angular:** Superei a barreira inicial da minha falta de experiência prévia com _front-end_ e consegui realizar entregas consistentes.
> - **Testes:** Tive que pesquisar e me aprofundar bastante para entender a estruturação de testes e como escrevê-los da maneira ideal.
> - **Infraestrutura (GCP e Docker):** Evoluí muito no entendimento do Google Cloud Platform (GCP Console) e na conteinerização. Complementarmente, aprimorei até o meu gerenciamento de recursos de _hardware_, pois precisei otimizar a forma como subia a aplicação para conseguir rodar um ambiente pesado num computador pessoal mais modesto.

### 5.2 Quais foram as suas impressões gerais sobre trabalhar num projeto real (legado/em andamento) de uma Fábrica de Software em comparação com projetos puramente acadêmicos/teóricos?

**Sua Resposta:**

> As impressões foram majoritariamente positivas. A grande diferença de um projeto real para projetos puramente acadêmicos é o peso da responsabilidade: a aplicação era "de verdade" e não estávamos apenas simulando. Uma decisão técnica errada ou a falta de comprometimento impactaria diretamente o cronograma, outras equipes e o futuro do sistema. A dinâmica foi muito fiel a um ambiente de mercado de trabalho, onde havia forte demanda e a necessidade concreta de entregar valor.
>
> Embora projetos teóricos sejam fundamentais para construir a base conceitual, meu perfil de aprendizado se consolida colocando a "mão na massa". Foi lidando com problemas reais — como entender por que um requisito de negócio estava mal escrito ou refatorar uma classe para aderir a princípios de código limpo (_Clean Code_) — que eu mais evoluí. Em suma, a Fábrica de Software proporcionou uma experiência profissional autêntica, agregando uma bagagem prática inestimável, especialmente para discentes que ainda não tinham vivenciado o mercado de trabalho durante o curso.

### 5.3 Quais limitações ainda restaram no SIPROS e quais sugestões de melhoria arquitetural ou de processo você deixaria para as próximas turmas (Trabalhos Futuros)?

**Sua Resposta:**

> Analisando o estado final das entregas, identifiquei algumas limitações e débitos técnicos que configuram ótimas oportunidades de Trabalhos Futuros para as próximas turmas da Fábrica de Software:
>
> 1. **Gestão Administrativa Pendente:** Os _endpoints_ de retaguarda para alteração de _status_ das inscrições e geração de relatórios oficiais ainda são "stubs" (retornam `HTTP 501 Not Implemented`). Implementar a máquina de estados e a lógica de negócio no _back-end_ é vital para que a coordenação possa gerenciar os candidatos.
> 2. **Login com Gov.BR e Produção:** O botão "Entrar com Gov.BR" ainda é apenas visual e exige a integração completa do _Identity Provider_ no Keycloak. Adicionalmente, as credenciais OAuth do Google precisam ser migradas para contas institucionais definitivas.
> 3. **Melhoria Arquitetural (Assincronismo):** Atualmente, o envio de e-mails com comprovantes PDF ocorre de forma síncrona junto à transação do banco de dados (`@Transactional`). Refatorar esse envio para um modelo assíncrono (orientado a eventos do Spring) é crucial para evitar latência e travamentos em momentos de pico de inscrições.
> 4. **Integração Visual (MinIO):** Os _cards_ dos processos seletivos utilizam ícones genéricos. Expandir o uso da infraestrutura do _MinIO_ para armazenamento dinâmico das logos e anexos deixaria o sistema visualmente mais rico e profissional.
> 5. **Ciclo Completo do Candidato:** O botão de "Cancelar Inscrição" no _dashboard_ age apenas de forma visual e local. É necessário fechar esse ciclo conectando-o ao _back-end_ para a persistência correta do cancelamento.

### 5.4 Você tem em mente artigos, literaturas ou relatos de experiência na literatura que se assemelham aos problemas que você resolveu? (Trabalhos Relacionados)

**Sua Resposta:**

> **Relatos de Experiência Prática:** Do ponto de vista profissional, os desafios que enfrentei no SIPROS são idênticos aos que já vivenciei em empresas reais no mercado de tecnologia. O uso de metodologias ágeis e a resolução de problemas arquiteturais complexos refletem a rotina da indústria. O diferencial que torna o SIPROS único é a sua natureza como um software acadêmico, onde a curva de aprendizado da equipe precisa ser gerida de perto pela coordenação.
>
> **Literatura e Trabalhos Relacionados:** Para o TCC, podemos citar literaturas focadas em dois eixos que resolvemos neste projeto:
>
> 1. **Fábricas de Software Acadêmicas e Metodologias Ágeis:** Existem diversos trabalhos e artigos acadêmicos que relatam como a aplicação de _Scrum_ e _Kanban_ em projetos universitários (Aprendizagem Baseada em Projetos - PBL) aproxima os alunos da realidade do mercado, ilustrando bem os benefícios do autogerenciamento e as dores do nivelamento técnico que vivenciamos.
> 2. **Evolução de Segurança em SPAs (PKCE / OAuth 2.0):** Em relação à implementação de autenticação, a literatura atual de cibersegurança e os padrões mais recentes (como o OAuth 2.1) documentam exatamente a mudança que promovi: o abandono do _Implicit Flow_ (considerado vulnerável para SPAs como Angular) pela adoção obrigatória do _Authorization Code Flow_ com PKCE, que mitiga ataques de interceptação sem expor credenciais sensíveis no _front-end_.

---

## Bloco 6: Formalidades Acadêmicas e Contexto de Negócio (Capítulos 1, 2 e 3)

_Perguntas adicionadas com base na estrutura obrigatória do documento `UFG_INF_BES_TCC_Modelo`._

### 6.1 Propósito e Público-Alvo do SIPROS (Contextualização)

_(O que é o sistema SIPROS sob a ótica de negócio? Qual problema real ele resolve? Quem é o público-alvo e qual o nível de criticidade desse sistema para a UFG?)_
**Sua Resposta:**

> O Sistema Integrado de Processos Seletivos (SIPROS) é uma plataforma institucional concebida para ser genérica, modular e extensível, voltada à configuração e gestão de processos seletivos de diferentes naturezas (ingresso em cursos de pós-graduação, monitoria, bolsas, extensão, participação em eventos, entre outros).
>
> **Problema que resolve:** Em vez de a instituição criar formulários descentralizados, custosos e descartáveis para cada seleção, o SIPROS oferece uma arquitetura centralizada que permite configurar processos de forma flexível e reutilizável, garantindo a padronização e o reaproveitamento de dados.
>
> **Público-alvo:** Atende a dois perfis principais: os gestores/coordenadores acadêmicos (que configuram os editais e gerenciam as etapas do processo) e os candidatos (alunos internos e pessoas externas que acessam o portal para realizar as inscrições).
>
> **Criticidade:** O sistema possui altíssima criticidade, pois lida com dados pessoais e acadêmicos sensíveis e será a principal porta de entrada institucional para esses editais. Por envolver uma vasta base de usuários, eventuais falhas de segurança (como roubo de credenciais ou vazamento de dados) causariam impactos legais e de reputação imensos para a UFG, o que justifica totalmente o forte rigor aplicado na autenticação com Keycloak e na implantação do PKCE para evitar interceptações no front-end.

### 6.2 Objetivos Geral e Específicos do TCC

_(Declare qual é o Objetivo Geral da escrita deste seu documento de TCC e cite de 4 a 5 Objetivos Específicos que serão os marcos para atingir o objetivo geral)._
**Sua Resposta:**

> **Objetivo Geral:**
> Descrever e analisar a experiência prática de evolução e refatoração full-stack do sistema SIPROS no contexto da Fábrica de Software acadêmica, com ênfase na implementação de mecanismos robustos de segurança, autenticação e na adoção de práticas para elevação da qualidade do software.
>
> **Objetivos Específicos:**
>
> 1. Descrever o ambiente organizacional, a metodologia ágil adotada e a divisão de papéis dentro do projeto SIPROS.
> 2. Relatar as implementações técnicas voltadas à segurança, especialmente a integração com o Google e o tratamento do fluxo de gerenciamento de sessão via Keycloak.
> 3. Descrever a execução de processos de Verificação e Validação (V&V) aplicados para garantir a conformidade da interface (front-end) com os Casos de Uso estabelecidos.
> 4. Apresentar as práticas de garantia de qualidade (QA) adotadas, como a estruturação da suíte de testes automatizados e o rigor das revisões por pares (_Code Review_).
> 5. Refletir criticamente sobre os desafios vivenciados e analisar a contribuição desta vivência prática de mercado na evolução das _hard skills_ e _soft skills_ como Engenheiro de Software.

### 6.3 Metodologia do Trabalho Acadêmico

_(A sua pesquisa e redação deste TCC se classifica como um **Estudo de Caso** - onde você apenas analisou o trabalho de terceiros - ou uma **Pesquisa-Ação** - onde você atuou ativamente no código para resolver os problemas? Justifique brevemente)._
**Sua Resposta:**

> O trabalho é classificado fundamentalmente como uma **Pesquisa-Ação**.
>
> Diferentemente de um Estudo de Caso — no qual eu seria apenas um observador analisando um fenômeno passivamente —, neste TCC eu me engajei ativamente no ambiente e no problema. Integrei a Equipe Dourada de desenvolvimento da Fábrica de Software, analisei o sistema legado, estruturei _issues_, tomei decisões arquiteturais e, de forma direta, alterei o código-fonte (seja na integração com o GCP/Keycloak, nas rotas do Angular ou na escrita de testes no back-end) para propor soluções reais aos problemas existentes. O documento, portanto, relata o ciclo iterativo de identificar problemas, planejar ações técnicas, executá-las no código e avaliar os seus resultados concretos em conjunto com a equipe e a coordenação.

### 6.4 Fundamentação Teórica dos Processos de Software

_(Antes de relatar o que você fez na prática, como a literatura/livros clássicos definem a teoria das áreas em que você atuou? Como a teoria define "Verificação e Validação de Software"? Como a teoria define "Segurança e Controle de Acesso em Aplicações Web"?)_
**Sua Resposta:**

> A fundamentação das atividades realizadas apoia-se em padrões clássicos da Engenharia de Software.
> - **Verificação e Validação (V&V):** Segundo o *SWEBOK V3* (Software Engineering Body of Knowledge) e a norma IEEE 1012, a Validação visa garantir que o software atende às necessidades operacionais do usuário ("estamos construindo o produto certo?"), enquanto a Verificação foca em garantir que o sistema está em conformidade com as suas especificações e requisitos documentados ("estamos construindo o produto da maneira certa?"). Na minha atuação, aplicar V&V significou confrontar a documentação (Casos de Uso) com a interface (Figma), eliminando inconsistências precocemente.
> - **Qualidade de Software:** O modelo de qualidade ISO/IEC 25010 (SQuaRE) estabelece a manutenibilidade, adequação funcional e segurança como atributos críticos do produto de software. A minha inserção na estruturação da suíte de testes automatizados visou diretamente garantir a confiabilidade e manutenibilidade do código.
> - **Segurança (Autenticação e Autorização):** A literatura técnica de cibersegurança e os padrões da IETF (como as RFCs 6749 e 7636) fundamentam a transição para protocolos modernos de delegação de autorização. O uso do OAuth 2.0 associado à extensão PKCE é atualmente o padrão exigido na literatura para mitigar ataques de interceptação em aplicações *Single Page Application* (SPA), preenchendo as lacunas de segurança do sistema original.

### 6.5 Motivação Ampla e Social

_(Por que a resolução de problemas reais de autenticação e a vivência prática numa Fábrica de Software acadêmica são essenciais para a formação do Engenheiro de Software hoje? Como o seu relato pode ajudar estudantes de turmas futuras?)_
**Sua Resposta:**

> A vivência em uma Fábrica de Software acadêmica preenche uma lacuna fundamental na formação do Engenheiro de Software: a transição entre a teoria de sala de aula e a realidade ambígua e complexa do mercado de trabalho.
> 
> Ao atuar na evolução de um sistema real e de grande escopo como o SIPROS, deparei-me com desafios que raramente surgem em projetos acadêmicos isolados. O trabalho exigiu lidar com código legado, identificar a ausência de uma "fonte da verdade" unificada (divergências entre Casos de Uso e Protótipos), implementar boas práticas de qualidade (testes automatizados e *Code Review*) e colaborar continuamente dentro de uma equipe utilizando métodos ágeis.
> 
> O relato dessa experiência serve não apenas para validar os conhecimentos técnicos aplicados para evoluir o sistema, mas também como um guia prático para estudantes de turmas futuras. Ele demonstra a importância vital das *soft skills* — como autogerenciamento, comunicação ativa e capacidade investigativa — para atuar de forma profissional na resolução de problemas sistêmicos, comprovando que a Engenharia de Software vai muito além da simples escrita de código.
