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
