Aviso: O Contexto a seguir, é completamente fictício, a empresa, o contexto, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um projeto:

# Contexto de Negócio
[![image](https://dgq0rlkor3ukz.cloudfront.net/wp-content/uploads/2019/06/seguro-auto-86.jpg)]

A Insurance All é uma empresa que oferece seguro saúde para seus clientes e a equipe de produtos está analisando a possibilidade de oferecer aos segurados um novo produto: o seguro de automóveis.

Tal como acontece com o seguro saúde, os clientes deste novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor segurado pela empresa, destinado a custear um eventual sinistro ou dano ao veículo.

A Insurance All conduziu uma pesquisa com cerca de 380.000 clientes sobre seu interesse em ingressar em um novo produto de seguro de automóveis no ano passado. Todos os clientes manifestaram interesse ou não em adquirir seguro de automóveis e essas respostas foram salvas em um banco de dados junto com outros atributos do cliente.

A equipe de produtos selecionou 127 mil novos clientes que não responderam à pesquisa para participar de uma campanha, na qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pela equipe de vendas por meio de ligações telefônicas.

Porém, a equipe de vendas tem capacidade para realizar 20 mil ligações no período da campanha.

# Problema de Negócio

Nesse contexto, você foi contratado como consultor de Data Science para construir um modelo que prevê se o cliente estaria ou não interessado em seguro de automóveis.

Com a solução, a equipe de vendas espera poder priorizar as pessoas com maior interesse no novo produto e, assim, otimizar a campanha fazendo apenas contatos com os clientes mais propensos a realizar a compra.

Como resultado de sua consultoria, você precisará entregar um relatório contendo algumas análises e respostas para as seguintes perguntas:

- Principais insights sobre os atributos mais relevantes dos clientes interessados em adquirir seguro de automóveis.
- Que porcentagem de clientes interessados em comprar seguro de automóveis a equipe de vendas poderá atingir com 20.000 ligações?
- E se a capacidade da equipe de vendas aumentar para 40.000 chamadas, que porcentagem de clientes interessados em adquirir seguro de automóveis a equipe de vendas poderá entrar em contato?
- Quantas ligações a equipe de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir seguro de automóveis?

Os Dados do conjunto estão disponível em um banco de dados Postgresql e cada linha representa um cliente e cada coluna contém alguns atributos que descrevem aquele cliente, além de sua resposta à pesquisa, na qual ela mencionou interesse ou não no novo produto de seguro.

# Dados

O conjunto de dados está disponível na plataforma do Kaggle, através desse link: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction 

 - **Id**: identificador único do cliente.
 - **Gender**: gênero do cliente.
 - **Age**: idade do cliente.
 - **Driving License**: 0, o cliente não tem permissão para dirigir e 1, o cliente tem para dirigir ( CNH – Carteira Nacional de Habilitação )
 - **Region Code**: código da região do cliente.
 - **Previously Insured**: 0, o cliente não tem seguro de automóvel e 1, o cliente já tem seguro de automóvel.
 - **Vehicle Age**: idade do veículo.
 - **Vehicle Damage**: 0, cliente nunca teve seu veículo danificado no passado e 1, cliente já teve seu veículo danificado no passado.
 - **Anual Premium**: quantidade que o cliente pagou à empresa pelo seguro de saúde anual.
 - **Policy sales channel**: código anônimo para o canal de contato com o cliente.
 - **Vintage**: número de dias que o cliente se associou à empresa através da compra do seguro de saúde.
 - **Response**: 0, o cliente não tem interesse e 1, o cliente tem interesse.

# Planejamento da Solução 
**1. Entendimento do negócio** - Buscar entender quais são os problemas a serem solucionados e como solucioná-los, entender os motivos por trás da necessidade de rankeamento dos clientes, quais aspectos serão considerados na hora da predição e quão melhor a solução proposta pode ser considerando os modelos de predição utilizados atualmente na empresa.

**2. Coleta de Dados** - Coletar os dados na plataforma do Kaggle.

**3. Limpeza dos Dados** - Verificar possíveis dados faltantes e como tratá-los de acordo com a circunstância, analisar existências de outliers e como agir de acordo, verificar outras possíveis inconsistências nos dados.

**4. Exploração dos Dados** - Buscar o melhor entendimento do negócio através da geração de insights, confrontar e validar hipóteses de negócios, verificar possíveis correlações de atributos e como isso ajudará na etapa de ML.

**5. Preparação dos Dados** - Transformar e balancear o que for necessário dos dados para que atenda as premissas da etapa de ML, é necessário deixar os dados bem preparados para que se tenha o melhor resultado possível na etapa de Machine Learning.

**6. Seleção das Features** - Após fazer a preparação e exploração dos dados e entender como cada feature se comporta, iremos selecionar as melhores features para compor o rankeamento através do machine learning.

**7. Aplicação dos Modelos de Machine Learning** - Nesta etapa foram escolhidos os algoritmos de machine learning que seriam usados e então os mesmos foram treinados com os dados já preparados e prontos, cada algoritmo foi testado usando seus devidos parâmetros e posteriormente estratégias de cross validation foram usadas para verificar o real resultado do medelo, bem como tecnicas de hyperparameter fine tunning para encontrar os melhores parâmetros para o modelo escolhido.

**8. Avaliação do Algoritmo** - O algoritmo é avaliado com base em algumas métricas e nesse ponto verifica-se ou não a necessidade de realizar mais um ciclo para melhorar o desempenho final.

**9. Tradução do Erro em Métricas de Negócio** - Com o melhor modelo escolhido, treinado e otimizado a taxa de erro encontrada é trasnformada em mátricas de negócio para que se saiba concretamente quanto de retorno financeiro aquela solução trouxe para a empresa.

**10. Deploy do Modelo em Produção** - O modelo foi colocado em produção no ambiente cloud Heroku para que as predições possam ser acessados através de requisições a uma API.

# Melhores Insights
