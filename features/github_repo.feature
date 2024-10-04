#language:pt

Funcionalidade: Testa se é possivel acessar a página de um repositório buscando seu nome no github.

  Contexto: Busca repositórios no github
    Dado que eu esteja com o browser aberto

  Esquema do Cenario: Cenário de busca por <texto>
    Quando acesso o https://github.com/
    E faço o login com as credenciais do arquivo de configuração
    E clico na busca do github
    E busco o seguinte texto <texto>
    E clico no primeiro resultado
    Então devo ser redirecionado para a página <url>

  Exemplos:
    | url                                       | texto       |
    | https://github.com/Douglas019BR/COWDOL    | Douglas019BR/COWDOL |
    | https://github.com/Douglas019BR/bdd-study | Douglas019BR/bdd-study | 
    | https://github.com/torvalds/linux         | Linux |

