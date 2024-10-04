#language:pt

Funcionalidade: Testa se é possivel acessar uma página pesquisando o nome na busca do google e clicando no botão 'estou com sorte'

  Contexto: Busca google estou com sorte
    Dado que eu esteja com o browser aberto

  Esquema do Cenario: Cenário de busca por <texto>
    Quando acesso o https://www.google.com
    E preencho o campo de busca com o texto <texto>
    E clico em estou com sorte
    Então devo ser redirecionado para a página <url>

  Exemplos:
    | url                                          | texto       |
    | https://www.python.org/downloads/release/python-3110/ | python 3.11 |
    | https://github.com/                          | github      | 

