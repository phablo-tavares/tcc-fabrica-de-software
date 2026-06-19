# Perguntas Estratégicas para Construção do TCC - Phablo Tavares

Este documento contém perguntas direcionadas e desenhadas especificamente para preencher as lacunas entre os dados brutos da sua atuação (issues, PRs, commits da `base_de_conhecimento_phablo_sipros`) e as exigências do documento oficial do TCC (baseado em `UFG_INF_BES_TCC_Modelo`).

O modelo de TCC do INF-UFG foca intensamente no **porquê**, **como**, **contexto organizacional** e **lições aprendidas**, indo além do simples "o que foi feito". 

Por favor, responda cada pergunta abaixo. Suas respostas serão o insumo principal para a redação dos capítulos do seu TCC.

---

## Bloco 1: Definição de Foco e Fundamentação (Capítulos 1 e 2)
*O modelo de TCC sugere que, embora a atuação possa ser em várias áreas, o trabalho deve ter um "Tópico Específico" bem definido (ex: Segurança e Autenticação, Qualidade e Testes, Evolução Full-Stack).*

### 1.1 Qual será o tema central/foco principal do seu TCC?
*(Exemplo: "Implementação de Mecanismos de Autenticação e Segurança com Keycloak", "Evolução e Refatoração Full-Stack do Sistema SIPROS", ou "Práticas de V&V e Qualidade de Software").*
**Sua Resposta:**
> O tema central será a **Evolução e Refatoração Full-Stack do Sistema SIPROS**, com foco principal na implementação de **mecanismos de autenticação e segurança com Keycloak** (incluindo autenticação via Google e fluxo com PKCE). Complementarmente, o trabalho abordará:
> - **Qualidade e Testes:** Práticas de Verificação e Validação (V&V) e implementação de testes automatizados.
> - **Evolução de Interface:** Melhorias no Front-end, refatoração de fluxos legados e novas regras de negócio na UI.

### 1.2 Por que a resolução dos problemas que você trabalhou no SIPROS (ex: retirar credenciais hardcoded, unificar login) foi crucial para as partes interessadas (usuários, coordenação)?
**Sua Resposta:**
> A resolução foi crucial porque elevou o sistema a um novo nível de maturidade e funcionalidade. Embora o SIPROS tivesse uma arquitetura consolidada, ainda apresentava lacunas críticas, como rotas de *back-end* sem telas correspondentes, fluxos de *front-end* sem conexão real e o uso intensivo de dados *mockados*. Meu trabalho focou em remover esses *mocks*, conectar as pontas do sistema (front e back) e torná-lo realidade. O principal exemplo foi a autenticação com Google, que antes era uma funcionalidade vazia e passou a ser um fluxo de login real e persistente. Em suma, essas contribuições foram fundamentais para transformar um projeto estático em um sistema muito mais próximo de estar pronto para uso em produção (*production-ready*).

### 1.3 Avaliação das Ferramentas: Quais foram os pontos fortes e as *limitações* das principais ferramentas adotadas (Keycloak, Angular, Docker, GitHub)?
*(O Capítulo 2 exige justificar a escolha e também as limitações das ferramentas utilizadas).*
**Sua Resposta:**
> A principal justificativa para o uso dessas ferramentas foi a aderência à arquitetura já estabelecida no projeto; optamos por manter o padrão do repositório em vez de adicionar novas tecnologias.
> **Pontos Fortes:** São tecnologias amplamente consolidadas e completas. O Keycloak oferece segurança robusta; o Angular viabiliza um *design* bastante fiel às prototipações no Figma; a conteinerização pelo Docker facilita a padronização e o GitHub garante um excelente fluxo de versionamento.
> **Limitações:**
> - **Keycloak:** Possui uma curva de aprendizado inicial mais complexa, sobretudo para as configurações iniciais e criação de scripts para novos usuários.
> - **Angular:** Sua arquitetura rígida e a exigência de TypeScript impõem uma curva de aprendizado íngreme. Como eu não tinha experiência prévia, isso representou um desafio inicial até me adaptar.
> - **Docker:** Traz um forte custo computacional (*overhead*). Subir todos os contêineres do projeto exige uma máquina com hardware razoável, caso contrário, ocorrem travamentos.

---

## Bloco 2: Contexto e Dinâmica Organizacional (Capítulos 1 e 3)
*O TCC exige que se relate o ambiente em que o projeto foi desenvolvido e como a equipe se organizava.*

### 2.1 Como era a dinâmica de trabalho e as metodologias da equipe da Fábrica de Software?
*(Havia cerimônias Scrum/Kanban? Como as tarefas eram priorizadas e distribuídas? Havia papéis bem definidos como Scrum Master, Tech Lead? Como a comunicação ocorria?)*
**Sua Resposta:**
> A dinâmica de trabalho era inspirada na metodologia Scrum (com o uso de quadros Kanban), embora não a seguíssemos de forma estrita. Nossa organização funcionava da seguinte maneira:
> - **Levantamento e Planejamento:** Nós, discentes, analisávamos as demandas, dividíamos em épicos e criávamos as *issues* no GitHub. A coordenação da Fábrica de Software atuava como *Product Owner*, selecionando e priorizando quais *issues* entrariam em cada *Sprint*. As *Sprints* tinham duração de duas semanas.
> - **Autogerenciamento e Desenvolvimento:** Com as tarefas definidas, a equipe possuía total liberdade para se organizar, dividir sub-tarefas e distribuí-las conforme a familiaridade técnica de cada um. Estabelecíamos prazos internos e, ao final da *Sprint*, reservávamos os últimos 1 a 2 dias para alinhar o código e abrir os *Pull Requests* necessários para a *branch* principal, sempre em comunicação com a Fábrica de Software para garantir o alinhamento esperado.
> - **Reunião de Revisão (*Sprint Review*):** Ao término das duas semanas da *Sprint*, fazíamos uma reunião no período da tarde com a Fábrica e os docentes. Apresentávamos nossas entregas e recebíamos os *feedbacks* (elogios pelo que funcionou bem ou cobranças de melhoria). Com base no que foi entregue ou no que ficou pendente, a Fábrica nos direcionava novas *tasks*, reiniciando o ciclo de desenvolvimento desde o zero.
> - **Comunicação e Liderança:** A comunicação interna era constante para garantir a qualidade e a entrega no prazo. Havia também papéis de liderança estabelecidos: a Ester e o Lucas atuavam como a interface direta ("ponte") entre a Fábrica de Software, os docentes e nós, discentes.

### 2.2 Como foi o seu processo de ambientação (Onboarding)?
*(Como você estudou e se familiarizou com a base de código do SIPROS antes de conseguir entregar a primeira funcionalidade?)*
**Sua Resposta:**
> O processo de *onboarding* foi muito bem estruturado pela Fábrica de Software. O foco inicial foi nivelar o conhecimento da equipe sobre as tecnologias do SIPROS e as ferramentas essenciais (como Git e Docker) para conseguirmos rodar o projeto localmente (tanto o *back-end* quanto o *front-end*). Esse treinamento foi detalhado e crucial para equilibrar o nível técnico de todos, especialmente para quem não tinha experiência prévia em desenvolvimento num ambiente de metodologias ágeis. Após essa base sólida fornecida pela Fábrica, tornou-se responsabilidade de cada discente identificar suas próprias lacunas de conhecimento e buscar o aprendizado necessário para conseguir realizar as entregas.

### 2.3 Como foi a comunicação e integração do seu trabalho com os outros membros da Equipe Dourada?
*(A Equipe Dourada era composta por Phablo Tavares, Thiago Vicente de Aquino, Hugo Moreno Veiga Jardim, Ester Adaiane Oliveira Ferreira, Lucas Gabriel Nunes Alves, Felipe Duarte da Rocha Paço e José Alves de Oliveira Neto. Cite exemplos de como foi colaborar com eles, conflitos de código ou tomada de decisões em conjunto).*
**Sua Resposta:**
> A comunicação com a Equipe Dourada ocorreu de forma constante e alinhada, apoiada em dois canais principais:
> - **Canal Oficial (Discord):** Utilizado para contato direto com a Fábrica de Software. Por lá, enviávamos avisos de *Pull Requests*, comunicávamos nossas entregas e fazíamos pedidos de ajuda, garantindo que a coordenação estivesse sempre ciente do nosso progresso.
> - **Canal Interno (WhatsApp):** Um grupo próprio para comunicações mais pontuais e rápidas entre os discentes, sem a necessidade de expor todas as discussões no canal oficial.
> 
> Nossa metodologia de comunicação valorizava muito a expressividade e a transparência. Constantemente eu e outros colegas perguntávamos sobre o andamento das tarefas, e qualquer membro com dificuldades ou impedimentos reportava imediatamente ao grupo para nos organizarmos. Além disso, realizávamos reuniões síncronas frequentes nos canais de voz do Discord para dividir tarefas, debater soluções e discutir pendências urgentes.
> 
> **Resolução de Conflitos de Código:** A comunicação sobre código seguia a mesma dinâmica e prezava pela autonomia. Se eu me deparasse com um conflito de código, eu mesmo tentava resolvê-lo. Apenas acionávamos outro membro caso fosse algo muito crítico. Havia uma autoavaliação constante: *"Preciso comunicar esse problema ou posso apenas resolvê-lo? Se eu resolvê-lo sozinho, isso vai gerar um efeito colateral para o meu colega quando ele fizer o pull da branch?"*. Sempre que a análise indicava a possibilidade de impacto no trabalho de outro membro, nós conversávamos e definíamos uma estratégia em conjunto para garantir o alinhamento.

---

## Bloco 3: Desafios, Decisões Técnicas e Soluções (Capítulo 3)
*A base de dados cita as PRs aprovadas, mas o relato de experiência (Capítulo 3) quer entender a "dor" do processo técnico.*

### 3.1 Ao remover o mock de autenticação e integrar o login com Google/Keycloak, quais foram os maiores desafios técnicos enfrentados?
*(Quais foram os bugs mais difíceis, problemas de arquitetura prévia ou dificuldades no aprendizado do Keycloak e OAuth2/PKCE?)*
**Sua Resposta:**
> Os desafios técnicos se dividiram em duas frentes principais:
> 
> 1. **Curva de Aprendizado e Configuração (GCP):** O primeiro obstáculo foi aprender a realizar a configuração do OAuth no *Google Cloud Platform* (GCP Console). O processo exigiu o mapeamento cuidadoso de credenciais, URLs de *callback* e variáveis de ambiente, ferramentas com as quais eu não tinha familiaridade prévia.
> 
> 2. **Implementação e Estabilidade (*Bugs*):** O segundo desafio foi integrar isso ao código base sem causar efeitos colaterais ou quebrar testes existentes. Durante a implementação, enfrentei problemas complexos de estado da aplicação. Por exemplo, o login funcionava, mas se o usuário navegasse de volta para uma tela específica, o fluxo quebrava ou a sessão com o Keycloak não era validada corretamente. Superei isso rastreando e testando exaustivamente todos os fluxos e casos de uso possíveis até que tudo ficasse perfeitamente estável.
> 
> **Pendência para Produção:** Como a aplicação não foi colocada em produção durante o meu ciclo, ficou o direcionamento técnico para a Fábrica de Software: será preciso gerar uma nova credencial no GCP ou migrar as variáveis de ambiente que eu criei para o servidor de produção, garantindo a segurança do *client secret*.

### 3.2 Por que foi decidido usar a extensão PKCE (Proof Key for Code Exchange) no fluxo de login? Houve alguma outra alternativa discutida ou descartada?
**Sua Resposta:**
> A decisão de utilizar a extensão PKCE (*Proof Key for Code Exchange*) acoplada ao *Authorization Code Flow* foi essencialmente técnica e voltada para a segurança. Como o SIPROS utiliza Angular, que é uma *Single Page Application* (SPA) executada no navegador do usuário, é impossível armazenar um *client secret* de forma segura no *front-end* (já que o código fica visível ao cliente). 
> 
> As alternativas avaliadas foram:
> 1. **Authorization Code Flow Tradicional:** Descartado porque exigiria a exposição do *client secret* no navegador.
> 2. **Implicit Flow:** Era o padrão antigo para SPAs, mas foi sumariamente descartado por ser considerado obsoleto e vulnerável pelas atuais recomendações de segurança do OAuth 2.0, já que expõe o *token* diretamente na URL e no histórico do navegador.
> 
> Sendo assim, o PKCE foi a solução viável e segura adotada. Ele substitui a necessidade do *client secret* estático por um verificador dinâmico (`code_challenge` e `code_verifier`) gerado a cada tentativa de login. Isso mitiga ataques de interceptação (como injeção de código ou CSRF) e garante uma autenticação robusta sem comprometer credenciais sensíveis no lado do cliente.

### 3.3 No trabalho de V&V (Issue #139) comparando o Figma com os Casos de Uso, quais inconsistências chamaram mais a sua atenção? Como isso gerou impacto real na correção do sistema?
**Sua Resposta:**
> O que mais me chamou atenção foi o alto grau de inconsistência e a dificuldade em determinar a "fonte da verdade" do sistema. Existiam diversas divergências críticas:
> - **Incompatibilidade Front x Documentação:** Havia regras de negócio descritas nos Casos de Uso que não existiam no protótipo, bem como telas ou campos no protótipo que não estavam mapeados na documentação.
> - **Contradições Internas:** Os próprios documentos de Casos de Uso divergiam entre si e continham descrições que entravam em conflito, além de imagens (*prints*) completamente desatualizadas.
> - **Desorganização do Figma:** Era difícil identificar qual *design* correspondia à versão final oficial e quais eram apenas rascunhos.
> 
> **Impacto Real:** Diante dessa confusão, a equipe precisou tomar uma decisão gerencial para destravar o projeto. Optamos por definir que os **Casos de Uso** seriam a fonte oficial da verdade. Com essa premissa estabelecida, mapeamos as divergências e geramos dezenas de novas *issues* focadas em corrigir, higienizar e organizar o protótipo no Figma para que ele refletisse corretamente a documentação, além de ajustar o sistema de acordo.

---

## Bloco 4: Avaliação de Qualidade de Software (Capítulo 3)
*Existe uma seção obrigatória sobre como a qualidade foi assegurada no seu trabalho.*

### 4.1 Como a qualidade do código foi garantida durante as suas entregas?
*(Descreva a cultura de testes, a sua iniciativa na estruturação da suíte de testes de unidade - Issue #304 - e como eram as políticas para aprovação de um Code Review).*
**Sua Resposta:**
> 

### 4.2 Quais indicadores ou percepções provam que as suas contribuições melhoraram o sistema?
*(Tivemos redução de bugs? Códigos mais limpos? Melhor feedback dos usuários sobre o botão do Google?)*
**Sua Resposta:**
> 

---

## Bloco 5: Reflexões, Aprendizados e Trabalhos Futuros (Capítulo 4)
*Para a conclusão, é preciso abstrair o código e focar no profissional Phablo.*

### 5.1 Quais foram as principais evoluções em suas *Soft Skills* (comunicação, organização, liderança técnica) e *Hard Skills* (Angular, arquitetura, testes)?
**Sua Resposta:**
> **Evolução em Soft Skills:**
> - **Autogerenciamento:** Foi um ponto crucial. O ambiente exigia que a equipe se organizasse e garantisse as entregas por conta própria; tínhamos que "nos virar" para fazer o projeto dar certo.
> - **Comunicação:** Entendi na prática que a comunicação é indispensável. Nada chegava "de mão beijada", então ser expressivo, relatar impedimentos e manter o alinhamento constante com os colegas foi vital para que o trabalho fluísse.
> - **Liderança Técnica (Autonomia):** Embora eu não tenha ocupado um cargo formal de gestão, exerci liderança sobre os artefatos que produzi. Como as *issues* tinham escopos amplos, assumi a responsabilidade de tomar decisões técnicas e arquiteturais, fundamentando-as de forma clara.
> 
> **Evolução em Hard Skills:**
> - **Angular:** Superei a barreira inicial da minha falta de experiência prévia com *front-end* e consegui realizar entregas consistentes.
> - **Testes:** Tive que pesquisar e me aprofundar bastante para entender a estruturação de testes e como escrevê-los da maneira ideal.
> - **Infraestrutura (GCP e Docker):** Evoluí muito no entendimento do Google Cloud Platform (GCP Console) e na conteinerização. Complementarmente, aprimorei até o meu gerenciamento de recursos de *hardware*, pois precisei otimizar a forma como subia a aplicação para conseguir rodar um ambiente pesado num computador pessoal mais modesto.

### 5.2 Quais foram as suas impressões gerais sobre trabalhar num projeto real (legado/em andamento) de uma Fábrica de Software em comparação com projetos puramente acadêmicos/teóricos?
**Sua Resposta:**
> As impressões foram majoritariamente positivas. A grande diferença de um projeto real para projetos puramente acadêmicos é o peso da responsabilidade: a aplicação era "de verdade" e não estávamos apenas simulando. Uma decisão técnica errada ou a falta de comprometimento impactaria diretamente o cronograma, outras equipes e o futuro do sistema. A dinâmica foi muito fiel a um ambiente de mercado de trabalho, onde havia forte demanda e a necessidade concreta de entregar valor.
> 
> Embora projetos teóricos sejam fundamentais para construir a base conceitual, meu perfil de aprendizado se consolida colocando a "mão na massa". Foi lidando com problemas reais — como entender por que um requisito de negócio estava mal escrito ou refatorar uma classe para aderir a princípios de código limpo (*Clean Code*) — que eu mais evoluí. Em suma, a Fábrica de Software proporcionou uma experiência profissional autêntica, agregando uma bagagem prática inestimável, especialmente para discentes que ainda não tinham vivenciado o mercado de trabalho durante o curso.

### 5.3 Quais limitações ainda restaram no SIPROS e quais sugestões de melhoria arquitetural ou de processo você deixaria para as próximas turmas (Trabalhos Futuros)?
**Sua Resposta:**
> 

### 5.4 Você tem em mente artigos, literaturas ou relatos de experiência na literatura que se assemelham aos problemas que você resolveu? (Trabalhos Relacionados)
**Sua Resposta:**
> **Relatos de Experiência Prática:** Do ponto de vista profissional, os desafios que enfrentei no SIPROS são idênticos aos que já vivenciei em empresas reais no mercado de tecnologia. O uso de metodologias ágeis e a resolução de problemas arquiteturais complexos refletem a rotina da indústria. O diferencial que torna o SIPROS único é a sua natureza como um software acadêmico, onde a curva de aprendizado da equipe precisa ser gerida de perto pela coordenação.
> 
> **Literatura e Trabalhos Relacionados:** Para o TCC, podemos citar literaturas focadas em dois eixos que resolvemos neste projeto:
> 1. **Fábricas de Software Acadêmicas e Metodologias Ágeis:** Existem diversos trabalhos e artigos acadêmicos que relatam como a aplicação de *Scrum* e *Kanban* em projetos universitários (Aprendizagem Baseada em Projetos - PBL) aproxima os alunos da realidade do mercado, ilustrando bem os benefícios do autogerenciamento e as dores do nivelamento técnico que vivenciamos.
> 2. **Evolução de Segurança em SPAs (PKCE / OAuth 2.0):** Em relação à implementação de autenticação, a literatura atual de cibersegurança e os padrões mais recentes (como o OAuth 2.1) documentam exatamente a mudança que promovi: o abandono do *Implicit Flow* (considerado vulnerável para SPAs como Angular) pela adoção obrigatória do *Authorization Code Flow* com PKCE, que mitiga ataques de interceptação sem expor credenciais sensíveis no *front-end*.
